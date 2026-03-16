"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, Literal


class PaymentLinkUpdate(TypedDict, total=False):
    """Name of the payment link."""
    name: Optional[str]
    """Type of payment link."""
    type: Optional[Literal["subscription"]]
    """Status of the payment link."""
    status: Optional[Literal["draft", "active", "archived"]]
    """Description of the payment link."""
    description: Optional[str]
    """ID of the plan associated with the payment link. Required if type is `subscription`."""
    plan_id: Optional[str]
    """URL-friendly identifier for the payment link."""
    slug: Optional[str]
