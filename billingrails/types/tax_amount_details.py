"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict


class TaxAmountDetails(TypedDict, total=False):
    """Total inclusive tax amount."""
    inclusive_amount: Optional[int]
    """Total inclusive tax percentage."""
    inclusive_percentage: Optional[int]
    """Total exclusive tax amount."""
    exclusive_amount: Optional[int]
    """Total exclusive tax percentage."""
    exclusive_percentage: Optional[int]
