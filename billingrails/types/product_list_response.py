"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .product import Product


class ProductListResponse(TypedDict, total=False):
    products: Optional[List[Product]]
    meta: Optional[dict]
