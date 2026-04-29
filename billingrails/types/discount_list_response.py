"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .discount import Discount


class DiscountListResponse(TypedDict, total=False):
    discounts: Optional[List[Discount]]
    meta: Optional[dict]
