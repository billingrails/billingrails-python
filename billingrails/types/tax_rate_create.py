"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, Literal


class TaxRateCreate(TypedDict, total=False):
    """Unique code for the tax rate."""
    code: str
    """Name of the tax rate."""
    name: str
    """Description of the tax rate."""
    description: Optional[str]
    """Type of tax rate."""
    type: Optional[Literal["sales", "vat", "gst", "custom"]]
    """Tax percentage (0–100)."""
    percentage: int
    """Whether the tax is included in the price."""
    inclusive: bool
    """Country code for the tax rate."""
    country: Optional[str]
    """Label shown on invoices."""
    invoice_name: Optional[str]
