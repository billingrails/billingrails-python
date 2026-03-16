"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional

from .checkout_session import CheckoutSession


class CheckoutSessionResponse(TypedDict, total=False):
    """URL to complete the payment. Only present when `with_payment_link` is true."""
    payment_link: Optional[str]
    checkout_session: Optional[CheckoutSession]
    meta: Optional[dict]
