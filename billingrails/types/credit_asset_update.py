"""This file is auto-generated. Do not edit manually."""

from typing import Any, Dict, Optional, TypedDict


class CreditAssetUpdate(TypedDict, total=False):
    name: Optional[str]
    """Unique code for this asset."""
    code: Optional[str]
    description: Optional[str]
    metadata: Optional[Dict[str, Any]]
    price: Optional[Any]
