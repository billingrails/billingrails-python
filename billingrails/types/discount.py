"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, Literal


class Discount(TypedDict, total=False):
    """Type of discount."""
    type: Optional[Literal["percentage", "fixed_amount"]]
    """Represents the object's type."""
    object: Optional[Literal["discount"]]
    """ID of the discount."""
    id: Optional[str]
    """Account ID (if discount is account-specific)."""
    account_id: Optional[str]
    """Status of the discount."""
    status: Optional[Literal["pending", "active", "expired", "archived"]]
    """Name of the discount."""
    name: Optional[str]
    """Unique code for the discount."""
    code: Optional[str]
    """Description of the discount."""
    description: Optional[str]
    """Percentage off."""
    percent_off: Optional[int]
    """Currency for fixed amount discounts."""
    currency: Optional[str]
    """Amount off in currency subunits."""
    amount_off: Optional[int]
    """Whether discount can be applied to multiple billing periods."""
    recurring: Optional[bool]
    """Maximum number of billing periods discount can recur (null = forever)."""
    max_recurring_intervals: Optional[int]
    """Maximum number of redemptions across all accounts."""
    max_redemptions: Optional[int]
    """Maximum number of redemptions per account."""
    max_redemptions_per_account: Optional[int]
    """Total number of redemptions across all accounts."""
    redemptions: Optional[int]
    """Date when the discount becomes valid."""
    valid_from: Optional[str]
    """Date when the discount expires."""
    valid_until: Optional[str]
    """Date when the discount expired."""
    expired_at: Optional[str]
    """Timestamp indicating when the object was created."""
    created_at: Optional[str]
