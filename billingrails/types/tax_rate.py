"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, Literal


class TaxRate(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["tax_rate"]]
    """ID of the tax rate."""
    id: Optional[str]
    """When the tax rate was created."""
    created_at: Optional[str]
    """Name of the tax rate."""
    name: Optional[str]
    """Unique code for the tax rate."""
    code: Optional[str]
    """Description of the tax rate."""
    description: Optional[str]
    """Type of tax rate."""
    type: Optional[Literal["sales", "vat", "gst", "custom"]]
    """Status of the tax rate."""
    status: Optional[Literal["active", "archived"]]
    """Tax percentage (0–100)."""
    percentage: Optional[int]
    """Whether the tax is included in the price."""
    inclusive: Optional[bool]
    """Country code for the tax rate."""
    country: Optional[str]
    """Key-value pairs for additional information."""
    metadata: Optional[dict]
