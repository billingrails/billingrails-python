"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .benefit import Benefit


class BenefitListResponse(TypedDict, total=False):
    benefits: Optional[List[Benefit]]
    meta: Optional[dict]
