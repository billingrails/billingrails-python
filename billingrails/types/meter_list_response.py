"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .meter import Meter


class MeterListResponse(TypedDict, total=False):
    meters: Optional[List[Meter]]
    meta: Optional[dict]
