"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .price_input import PriceInput


class ProductUpdate(TypedDict, total=False):
    """Name of the product."""
    name: Optional[str]
    """Description of the product."""
    description: Optional[str]
    """Name that appears on invoices for this product."""
    invoice_name: Optional[str]
    """Default price configuration for the product. If both price and prices are provided, prices takes precedence."""
    price: Optional[PriceInput]
    """Additional prices for this product. Takes precedence over the price field if both are provided."""
    prices: Optional[List[PriceInput]]
