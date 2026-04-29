"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict

from .address import Address


class AccountCreate(TypedDict, total=False):
    """Type of account."""
    type: Optional[Literal["individual", "organization"]]
    """Name of the account."""
    name: str
    """Email of the account."""
    email: str
    """External unique reference ID or identifier for this account."""
    external_id: Optional[str]
    """Shipping address of the account."""
    shipping_address: Optional[Address]
    """Billing address of the account."""
    billing_address: Optional[Address]
    """Invoice settings for the account."""
    invoice_settings: Optional[dict]
    """Key-value pairs that can be used to store additional information."""
    metadata: Optional[dict]
