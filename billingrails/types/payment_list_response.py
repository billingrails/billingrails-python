"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .payment import Payment


class PaymentListResponse(TypedDict, total=False):
    payments: Optional[List[Payment]]
    meta: Optional[dict]
