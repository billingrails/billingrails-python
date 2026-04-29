"""This file is auto-generated. Do not edit manually."""

from typing import List, Literal, Optional, TypedDict


class CreditGrantCreate(TypedDict, total=False):
    """Type of credit grant."""
    type: Literal["paid", "promotional"]
    """Account ID associated with the credit grant."""
    account_id: str
    """Asset code of the credit grant. Required when `currency` is not set."""
    asset_code: Optional[str]
    """Currency of the credit grant. Required when `asset_code` is not set."""
    currency: Optional[str]
    """Granted amount in currency subunits or quantity of credit assets."""
    grant_amount: int
    """Whether to create an invoice after payment. Defaults to `true`."""
    invoice_after_payment: Optional[bool]
    """Name of the credit grant."""
    name: Optional[str]
    """Description of the credit grant."""
    description: Optional[str]
    """Date when the credit grant expires."""
    expires_at: Optional[str]
    """Initialize payment for the credit grant and return the providers payment URL."""
    initiate_payment: Optional[bool]
    """Integration ID for payment processing."""
    integration_id: Optional[str]
    """Payment methods to show on the payment link."""
    allowed_payment_methods: Optional[List[str]]
    """URL to redirect after payment."""
    return_url: Optional[str]
    """Key-value pairs that can be used to store additional information."""
    metadata: Optional[dict]
