"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class Charge(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["charge"]]
    """ID of the charge."""
    id: Optional[str]
    """Lifecycle status of the charge."""
    status: Optional[Literal["ready", "settled", "invoiced", "discarded"]]
    """Account that owns the charge."""
    account_id: Optional[str]
    """Subscription ID when the charge line item is a subscription item."""
    subscription_id: Optional[str]
    """Associated meter event, when applicable."""
    event_id: Optional[str]
    """Display name for the charge line."""
    name: Optional[str]
    """Optional description."""
    description: Optional[str]
    """Price ID for the line."""
    price_id: Optional[str]
    """Pricing model key."""
    price_model: Optional[str]
    """Quantity billed."""
    quantity: Optional[int]
    """Unit amount before tax/discount."""
    unit_amount: Optional[int]
    """Subtotal in minor units."""
    subtotal_amount: Optional[int]
    """Discount amount in minor units."""
    discount_amount: Optional[int]
    """Tax amount in minor units."""
    tax_amount: Optional[int]
    """Total amount in minor units."""
    total_amount: Optional[int]
    billing_start: Optional[str]
    billing_end: Optional[str]
    proration: Optional[dict]
    amount_details: Optional[dict]
    created_at: Optional[str]
