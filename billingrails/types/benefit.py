"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class Benefit(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["benefit"]]
    """ID of the benefit."""
    id: Optional[str]
    """Timestamp when the benefit was created."""
    created_at: Optional[str]
    """Display name."""
    name: Optional[str]
    """Unique code for this benefit."""
    code: Optional[str]
    """Optional description."""
    description: Optional[str]
    """Status of the benefit."""
    status: Optional[Literal["active", "archived"]]
    """Benefit type."""
    type: Optional[Literal["feature_access", "feature_quota", "credit"]]
    """Meter ID for feature quota benefits."""
    meter_id: Optional[str]
    """Meter profile ID for feature quota benefits."""
    meter_profile_id: Optional[str]
