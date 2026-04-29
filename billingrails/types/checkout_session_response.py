"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .checkout_session import CheckoutSession


class CheckoutSessionResponse(TypedDict, total=False):
    """Provider payment URL. Only present when `initiate_payment` is `true`."""
    payment_url: Optional[str]
    checkout_session: Optional[CheckoutSession]
    meta: Optional[dict]
