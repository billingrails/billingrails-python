"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class PaymentLinkCreate(TypedDict, total=False):
    """Unique code for the payment link."""
    code: str
    """Name of the payment link."""
    name: str
    """Type of payment link."""
    type: Literal["subscription"]
    """Status of the payment link."""
    status: Optional[Literal["draft", "active", "archived"]]
    """Description of the payment link."""
    description: Optional[str]
    """ID of the plan for subscription payment links. Required when type is `subscription`."""
    plan_id: Optional[str]
    """URL-friendly identifier for the payment link."""
    slug: Optional[str]
