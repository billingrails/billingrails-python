"""Installed package version and HTTP User-Agent helpers for the SDK."""

from __future__ import annotations

from importlib import metadata


def get_version() -> str:
    """Return installed ``billingrails`` package version, or ``unknown`` if unavailable."""
    try:
        return metadata.version("billingrails")
    except metadata.PackageNotFoundError:
        return "unknown"


__version__ = get_version()


def user_agent() -> str:
    """Return the HTTP ``User-Agent`` string for this SDK."""
    return f"Billingrails Python SDK/{__version__}"
