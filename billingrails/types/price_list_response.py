"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .price import Price


class PriceListResponse(TypedDict, total=False):
    plans: Optional[List[Price]]
    meta: Optional[dict]
