"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .meter import Meter


class MeterResponse(TypedDict, total=False):
    meter: Optional[Meter]
    meta: Optional[dict]
