"""
Billingrails API errors.
"""

from __future__ import annotations

import json
from typing import Any, Optional, Tuple

import requests

RETRYABLE_HTTP_STATUSES = frozenset((429, 500, 502, 503, 504))


class BillingrailsError(Exception):
    """Base class for all SDK errors."""


class BillingrailsConnectionError(BillingrailsError):
    """Network or transport failure."""


class BillingrailsApiError(BillingrailsError):
    """Structured API error.

    Distinct from the OpenAPI ``ApiError`` TypedDict in ``types``.
    """

    def __init__(
        self,
        message: str,
        *,
        status: Optional[int] = None,
        code: Optional[str] = None,
        error_type: Optional[str] = None,
        details: Any = None,
    ):
        super().__init__(message)
        self.status = status
        self.code = code
        self.type = error_type
        self.details = details


class BillingrailsInvalidRequestError(BillingrailsApiError):
    """HTTP 400."""


class BillingrailsAuthenticationError(BillingrailsApiError):
    """HTTP 401."""


class BillingrailsNotFoundError(BillingrailsApiError):
    """HTTP 404."""


class BillingrailsRateLimitError(BillingrailsApiError):
    """HTTP 429."""


class BillingrailsServerError(BillingrailsApiError):
    """HTTP 5xx."""


def parse_error_payload(data: Any) -> Tuple[str, Optional[str], Optional[str], Any]:
    """Parse error JSON; supports flat fields or a nested ``error`` object."""
    if not isinstance(data, dict):
        return "Unknown error", None, None, None

    message = str(data.get("message") or "Unknown error")
    nested = data.get("error")
    if isinstance(nested, dict):
        code = nested.get("code")
        typ = nested.get("type")
        details = nested.get("details", data.get("details"))
        return (
            message,
            str(code) if code is not None else (str(data["code"]) if "code" in data else None),
            str(typ) if typ is not None else (str(data["type"]) if "type" in data else None),
            details,
        )

    code = data.get("code")
    typ = data.get("type")
    return (
        message,
        str(code) if code is not None else None,
        str(typ) if typ is not None else None,
        data.get("details"),
    )


def error_from_response(response: requests.Response) -> BillingrailsApiError:
    """Build a ``BillingrailsApiError`` subclass from the response status and body."""
    status = response.status_code
    try:
        data = response.json() if response.content else {}
    except (ValueError, json.JSONDecodeError):
        data = {}

    msg, code, typ, details = parse_error_payload(data)
    opts = {"status": status, "code": code, "error_type": typ, "details": details}

    if status == 400:
        return BillingrailsInvalidRequestError(msg, **opts)
    if status == 401:
        return BillingrailsAuthenticationError(msg, **opts)
    if status == 404:
        return BillingrailsNotFoundError(msg, **opts)
    if status == 429:
        return BillingrailsRateLimitError(msg, **opts)
    if 500 <= status <= 599:
        return BillingrailsServerError(msg, **opts)
    return BillingrailsApiError(msg, **opts)


def handle_api_error(exc: BaseException) -> BillingrailsError:
    """Map ``requests`` failures to SDK errors (used after retries are exhausted)."""
    if isinstance(exc, BillingrailsApiError):
        return exc

    if isinstance(exc, requests.exceptions.RequestException):
        response = getattr(exc, "response", None)
        if response is not None:
            return error_from_response(response)
        return BillingrailsConnectionError(
            str(exc) or "Failed to connect to the Billingrails API"
        )

    return BillingrailsError(str(exc))


def should_retry_status(status_code: int) -> bool:
    """Return True if this HTTP status is in `RETRYABLE_HTTP_STATUSES`."""
    return status_code in RETRYABLE_HTTP_STATUSES
