"""This file is auto-generated. Do not edit manually."""

from typing import Any, Dict, Literal, Optional, TypedDict


class CreditAsset(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["credit_asset"]]
    """ID of the credit asset."""
    id: Optional[str]
    """Timestamp when the credit asset was created."""
    created_at: Optional[str]
    """Display name."""
    name: Optional[str]
    """Optional description."""
    description: Optional[str]
    """Unique code for this asset."""
    code: Optional[str]
    """Pricing for paid assets. Null when the asset is promotional  only."""
    price: Optional[Any]
    """Arbitrary metadata."""
    metadata: Optional[Dict[str, Any]]
