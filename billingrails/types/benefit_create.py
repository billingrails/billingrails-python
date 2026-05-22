"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class BenefitCreate(TypedDict, total=False):
    """Display name."""
    name: str
    """Unique code for this benefit."""
    code: str
    description: Optional[str]
    """Benefit type."""
    type: Literal["feature_access", "feature_quota", "credit"]
    """Meter ID. Required for feature quota benefits."""
    meter_id: Optional[str]
    """Meter profile ID for feature quota benefits."""
    meter_profile_id: Optional[str]
