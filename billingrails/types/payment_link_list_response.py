"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .payment_link import PaymentLink


class PaymentLinkListResponse(TypedDict, total=False):
    payment_links: Optional[List[PaymentLink]]
    meta: Optional[dict]
