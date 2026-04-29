"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class TaxRateUpdate(TypedDict, total=False):
    """Name of the tax rate."""
    name: Optional[str]
    """Description of the tax rate."""
    description: Optional[str]
    """Type of tax rate."""
    type: Optional[Literal["sales", "vat", "gst", "custom"]]
    """Tax percentage (0–100)."""
    percentage: Optional[int]
    """Whether the tax is included in the price."""
    inclusive: Optional[bool]
    """Country code for the tax rate."""
    country: Optional[str]
    """Label shown on invoices."""
    invoice_name: Optional[str]
