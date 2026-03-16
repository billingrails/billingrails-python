"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional

from .payment import Payment


class PaymentResponse(TypedDict, total=False):
    payment: Optional[Payment]
    meta: Optional[dict]
