"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List, Literal

from .checkout_session_line_item import CheckoutSessionLineItem


class CheckoutSession(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["checkout_session"]]
    """ID of the checkout session."""
    id: Optional[str]
    """Type of checkout session."""
    type: Optional[Literal["one_time", "subscription"]]
    """Status of the checkout session."""
    status: Optional[Literal["pending", "succeeded", "failed", "expired", "canceled", "abandoned"]]
    """Currency of the checkout session."""
    currency: Optional[str]
    """Subtotal amount before discounts and taxes."""
    subtotal_amount: Optional[int]
    """Total discount amount applied."""
    discount_amount: Optional[int]
    """Total tax amount."""
    tax_amount: Optional[int]
    """Total amount to be charged."""
    total_amount: Optional[int]
    """ID of the account associated with the checkout session."""
    account_id: Optional[str]
    """ID of the plan for subscription checkout sessions."""
    plan_id: Optional[str]
    """ID of the payment integration."""
    integration_id: Optional[str]
    """ID of the payment link if created from one."""
    payment_page_id: Optional[str]
    """URL to redirect after payment completion."""
    return_url: Optional[str]
    """URL to the hosted checkout page."""
    url: Optional[str]
    """Allowed payment methods."""
    allowed_payment_methods: Optional[List[str]]
    """Start of the billing period."""
    billing_start: Optional[str]
    """End of the billing period."""
    billing_end: Optional[str]
    """Date when the checkout session expires."""
    expires_at: Optional[str]
    """Timestamp indicating when the object was created."""
    created_at: Optional[str]
    """Key-value pairs that can be used to store additional information."""
    metadata: Optional[dict]
    """Line items in the checkout session."""
    line_items: Optional[List[CheckoutSessionLineItem]]
