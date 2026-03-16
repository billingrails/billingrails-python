"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional

from .fee import Fee


class FeeResponse(TypedDict, total=False):
    fee: Optional[Fee]
    meta: Optional[dict]
