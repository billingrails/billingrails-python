"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .payment import Payment


class PaymentResponse(TypedDict, total=False):
    payment: Optional[Payment]
    meta: Optional[dict]
