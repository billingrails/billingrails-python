"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .payment_link import PaymentLink


class PaymentLinkResponse(TypedDict, total=False):
    payment_page: Optional[PaymentLink]
    meta: Optional[dict]
