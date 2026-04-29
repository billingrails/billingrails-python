"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .plan import Plan


class PlanResponse(TypedDict, total=False):
    plan: Optional[Plan]
    meta: Optional[dict]
