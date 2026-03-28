"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, Literal

from .price import Price


class Fee(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["fee"]]
    """ID of the object."""
    id: Optional[str]
    """Name of the fee."""
    name: Optional[str]
    """Unique code for this fee."""
    code: Optional[str]
    """Description of the fee."""
    description: Optional[str]
    """Status of the fee."""
    status: Optional[Literal["active", "archived"]]
    """Invoice name of the fee."""
    invoice_name: Optional[str]
    """Timestamp indicating when the object was created."""
    created_at: Optional[str]
    """Default price for the fee."""
    price: Optional[Price]
