"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .product import Product


class ProductResponse(TypedDict, total=False):
    product: Optional[Product]
