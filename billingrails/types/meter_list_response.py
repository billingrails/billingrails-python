"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .meter import Meter


class MeterListResponse(TypedDict, total=False):
    meters: Optional[List[Meter]]
    meta: Optional[dict]
