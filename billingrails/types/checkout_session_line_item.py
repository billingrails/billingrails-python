"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional


class CheckoutSessionLineItem(TypedDict, total=False):
    """ID of the line item."""
    id: Optional[str]
    """Name of the line item."""
    name: Optional[str]
    """Description of the line item."""
    description: Optional[str]
    """Quantity of the item."""
    quantity: Optional[int]
    """Unit amount in smallest currency unit (may be fractional)."""
    unit_amount: Optional[int]
    """Total amount for the line item."""
    total_amount: Optional[int]
    """Pricing model for the line item."""
    price_model: Optional[str]
    """Start of the billing period for this line item."""
    billing_start: Optional[str]
    """End of the billing period for this line item."""
    billing_end: Optional[str]
