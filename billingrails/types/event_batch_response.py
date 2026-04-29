"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .event import Event


class EventBatchResponse(TypedDict, total=False):
    events: Optional[List[Event]]
    meta: Optional[dict]
