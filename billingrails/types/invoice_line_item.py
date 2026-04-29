"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class InvoiceLineItem(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["invoice_line_item"]]
    """ID of the invoice item."""
    id: Optional[str]
    """ID of the usage event associated with this line item, if any."""
    event_id: Optional[str]
    """Name of the invoice item."""
    name: Optional[str]
    """Description of the invoice item."""
    description: Optional[str]
    """Quantity of the invoice item."""
    quantity: Optional[int]
    """Unit amount of the invoice item (smallest currency unit; may be fractional)."""
    unit_amount: Optional[int]
    """Subtotal amount of the invoice item."""
    subtotal_amount: Optional[int]
    """Total amount of the invoice item."""
    total_amount: Optional[int]
    """Start date for the billing period."""
    billing_start: Optional[str]
    """End date for the billing period."""
    billing_end: Optional[str]
