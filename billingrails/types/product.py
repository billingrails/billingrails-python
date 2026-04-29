"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict

from .interval import Interval
from .price import Price


class Product(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["product"]]
    """ID of the object."""
    id: Optional[str]
    """Name of the product."""
    name: Optional[str]
    """Internal identifier of the product."""
    code: Optional[str]
    """Status of the product."""
    status: Optional[Literal["draft", "active", "archived"]]
    """Description of the product."""
    description: Optional[str]
    """Name that appears on invoices for this product."""
    invoice_name: Optional[str]
    """Timestamp indicating when the object was created."""
    created_at: Optional[str]
    """Billing interval for the product (derived from default price)."""
    interval: Optional[Interval]
    """Default price for the product."""
    price: Optional[Price]
