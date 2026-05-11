"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .charge import Charge


class ChargeResponse(TypedDict, total=False):
    charge: Optional[Charge]
    meta: Optional[dict]
