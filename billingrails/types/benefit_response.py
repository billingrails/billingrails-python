"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .benefit import Benefit


class BenefitResponse(TypedDict, total=False):
    benefit: Optional[Benefit]
    meta: Optional[dict]
