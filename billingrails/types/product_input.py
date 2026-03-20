"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .price_input import PriceInput


"""Input for creating or updating a product. Accepts either `price` or `prices` array (prices takes precedence)."""
class ProductInput(TypedDict, total=False):
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
