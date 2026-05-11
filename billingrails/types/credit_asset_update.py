"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict


class CreditAssetUpdate(TypedDict, total=False):
    name: Optional[str]
    """Unique code for this asset within the site."""
    code: Optional[str]
    description: Optional[str]
    metadata: Optional[dict]
    price: Optional[Any]
