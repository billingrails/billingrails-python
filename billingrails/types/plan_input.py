"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List


class PlanInput(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    currency: Optional[str]
    trial_period_days: Optional[int]
    items: Optional[List[dict]]
