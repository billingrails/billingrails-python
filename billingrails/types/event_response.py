"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional

from .event import Event


class EventResponse(TypedDict, total=False):
    event: Optional[Event]
    meta: Optional[dict]
