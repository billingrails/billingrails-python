"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List, Literal

from .price import Price
from .interval import Interval
from .fee import Fee


class Plan(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["plan"]]
    """ID of the object."""
    id: Optional[str]
    """Name of the plan."""
    name: Optional[str]
    """Internal identifier of the plan."""
    code: Optional[str]
    """Status of the plan."""
    status: Optional[Literal["draft", "active", "archived"]]
    """Description of the plan."""
    description: Optional[str]
    """Name that appears on invoices for this plan."""
    invoice_name: Optional[str]
    """Trial period of the plan in days."""
    trial_period_days: Optional[int]
    """Timestamp indicating when the object was created."""
    created_at: Optional[str]
    """Billing interval for the plan (derived from default price)."""
    interval: Optional[Interval]
    """Default price for the plan."""
    price: Optional[Price]
    """Fees associated with the plan."""
    fees: Optional[List[Fee]]
