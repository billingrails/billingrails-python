"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict


class BenefitUpdate(TypedDict, total=False):
    """Display name."""
    name: Optional[str]
    description: Optional[str]
    """Meter ID for feature quota benefits."""
    meter_id: Optional[str]
    """Meter profile ID for feature quota benefits."""
    meter_profile_id: Optional[str]
