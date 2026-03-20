"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, Literal

from .price import Price
from .product import Product
from .fee import Fee


class PlanItem(TypedDict, total=False):
    object: Optional[Literal["plan_item"]]
    id: Optional[str]
    created_at: Optional[str]
    product_id: Optional[str]
    fee_id: Optional[str]
    price_id: Optional[str]
    price: Optional[Price]
    product: Optional[Product]
    fee: Optional[Fee]
