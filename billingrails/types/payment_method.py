"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class PaymentMethod(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["payment_method"]]
    """ID of the payment method."""
    id: Optional[str]
    """Status of the payment method."""
    status: Optional[str]
    """Type of the payment method."""
    type: Optional[str]
    """Payment provider for the payment method. ex. `stripe`, `paystack`."""
    provider: Optional[str]
    """ID of the account associated with the payment method."""
    account_id: Optional[str]
    """Name of the account associated with the payment method."""
    account_name: Optional[str]
    """Details of the payment method."""
    details: Optional[dict]
    """Date the payment method was created."""
    created_at: Optional[str]
