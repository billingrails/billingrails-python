"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List, Literal

from .plan_item import PlanItem


class Plan(TypedDict, total=False):
    object: Optional[Literal["plan"]]
    id: Optional[str]
    created_at: Optional[str]
    code: Optional[str]
    name: Optional[str]
    description: Optional[str]
    currency: Optional[str]
    status: Optional[Literal["active", "archived"]]
    trial_period_days: Optional[int]
    account_id: Optional[str]
    items: Optional[List[PlanItem]]
