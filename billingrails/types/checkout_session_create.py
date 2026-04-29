"""This file is auto-generated. Do not edit manually."""

from typing import List, Literal, Optional, TypedDict


class CheckoutSessionCreate(TypedDict, total=False):
    """Type of checkout session."""
    type: Literal["one_time", "subscription"]
    """Currency of the checkout session."""
    currency: str
    """ID of the customer account associated with the checkout session."""
    account_id: Optional[str]
    """ID of the plan for subscription checkout sessions."""
    plan_id: Optional[str]
    """ID of the payment integration."""
    integration_id: Optional[str]
    """URL to redirect after payment completion."""
    return_url: Optional[str]
    """Directly initialize payment for the checkout and return the providers payment URL."""
    initiate_payment: Optional[bool]
    """Allowed payment methods."""
    allowed_payment_methods: Optional[List[str]]
    """If true, creates a preview checkout session for testing purposes."""
    preview: Optional[bool]
    """Line items for the checkout session."""
    line_items: List[dict]
    """Discounts to apply to the checkout session."""
    discounts: Optional[List[dict]]
    """Tax rates to apply to the checkout session."""
    taxes: Optional[List[dict]]
    """Key-value pairs that can be used to store additional information."""
    metadata: Optional[dict]
