"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class PaymentRequest(TypedDict, total=False):
    """Type of payment request."""
    type: Optional[str]
    """Currency of the payment request."""
    currency: Optional[str]
    """Amount due in the payment request."""
    due_amount: Optional[int]
    """Date the payment request is due."""
    due_at: Optional[str]
    """Number of days until the payment request is due."""
    due_in_days: Optional[int]
    """ID of the payment request."""
    id: Optional[str]
    """Represents the object's type."""
    object: Optional[Literal["payment_request"]]
    """Sequence order (position) of this payment request."""
    ordinal: Optional[int]
    """Status of the payment request."""
    status: Optional[str]
