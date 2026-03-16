"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional

from .price import Price


class PriceResponse(TypedDict, total=False):
    price: Optional[Price]
