"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, Literal


class DiscountCreate(TypedDict, total=False):
    """Unique code for the discount."""
    code: str
    """Name of the discount."""
    name: str
    """Type of discount."""
    type: Literal["percentage", "fixed_amount"]
    """Description of the discount."""
    description: Optional[str]
    """Percentage off. Required when type is `percentage`."""
    percent_off: Optional[int]
    """Currency. Required when type is `fixed_amount`."""
    currency: Optional[str]
    """Amount off in currency subunits. Required when type is `fixed_amount`."""
    amount_off: Optional[int]
    """Whether discount can be applied to multiple billing periods."""
    recurring: Optional[bool]
    """Maximum number of billing periods discount can recur (null = forever)."""
    max_recurring_intervals: Optional[int]
    """Maximum number of redemptions across all accounts."""
    max_redemptions: Optional[int]
    """Maximum number of redemptions per account."""
    max_redemptions_per_account: Optional[int]
    """Date when the discount becomes valid."""
    valid_from: Optional[str]
    """Date when the discount expires."""
    valid_until: Optional[str]
    """Key-value pairs that can be used to store additional information."""
    metadata: Optional[dict]
