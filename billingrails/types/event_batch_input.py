"""This file is auto-generated. Do not edit manually."""

from typing import List, TypedDict

from .event_input import EventInput


class EventBatchInput(TypedDict):
    events: List[EventInput]
