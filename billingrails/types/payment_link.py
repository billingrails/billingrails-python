"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, Literal


class PaymentLink(TypedDict, total=False):
    """Type of payment link."""
    type: Optional[Literal["subscription"]]
    """Represents the object's type."""
    object: Optional[Literal["payment_page"]]
    """ID of the payment link."""
    id: Optional[str]
    """Name of the payment link."""
    name: Optional[str]
    """Status of the payment link."""
    status: Optional[Literal["published", "unpublished", "archived"]]
    """Description of the payment link."""
    description: Optional[str]
    """URL-friendly identifier for the payment link."""
    slug: Optional[str]
    """Public URL that can be shared with customers."""
    url: Optional[str]
    """URL to redirect to after payment completion."""
    return_url: Optional[str]
    """Timestamp indicating when the object was created."""
    created_at: Optional[str]
