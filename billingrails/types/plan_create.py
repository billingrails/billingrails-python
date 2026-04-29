"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict


class PlanCreate(TypedDict, total=False):
    name: str
    description: Optional[str]
    currency: str
    trial_period_days: Optional[int]
    items: Optional[List[dict]]
    code: str
    account_id: Optional[str]
