"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class EntitlementBenefit(TypedDict, total=False):
    """Benefit ID."""
    id: Optional[str]
    """Display name."""
    name: Optional[str]
    """Benefit code."""
    code: Optional[str]
    """Benefit type."""
    type: Optional[Literal["feature_access", "feature_quota", "credit"]]
