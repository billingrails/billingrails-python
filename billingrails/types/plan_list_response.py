"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .plan import Plan


class PlanListResponse(TypedDict, total=False):
    plans: Optional[List[Plan]]
    meta: Optional[dict]
