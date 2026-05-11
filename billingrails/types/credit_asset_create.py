"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict


class CreditAssetCreate(TypedDict, total=False):
    """Display name."""
    name: str
    """Unique code for this asset."""
    code: str
    description: Optional[str]
    metadata: Optional[dict]
    """Price configuration for a paid asset. Omit for a promotional asset."""
    price: Optional[Any]
