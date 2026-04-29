"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict


class Address(TypedDict, total=False):
    """City."""
    city: Optional[str]
    """Country."""
    country: Optional[str]
    """Address line 1."""
    line1: Optional[str]
    """Address line 2."""
    line2: Optional[str]
    """Postal code."""
    postal_code: Optional[str]
    """Region."""
    region: Optional[str]
    """State."""
    state: Optional[str]
