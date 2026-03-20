"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .price_input import PriceInput


class FeeCreate(TypedDict, total=False):
    """Name of the fee."""
    name: str
    """Unique code for the fee."""
    code: str
    """Product ID or code associated with the fee."""
    product_id: str
    """Description of the fee."""
    description: Optional[str]
    """Name that appears on invoices for this fee."""
    invoice_name: Optional[str]
    """Default price configuration for the fee. If both price and prices are provided, prices takes precedence."""
    price: PriceInput
    """Additional prices for this fee. Takes precedence over the price field if both are provided."""
    prices: Optional[List[PriceInput]]
