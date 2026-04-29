"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .discount import Discount


class DiscountResponse(TypedDict, total=False):
    discount: Optional[Discount]
    meta: Optional[dict]
