"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict


class EventInput(TypedDict, total=False):
    """The name of the event."""
    event_name: str
    """Properties associated with the event."""
    properties: dict
    """Unique identifier for this event."""
    idempotency_key: Optional[str]
    """Timestamp indicating the occurrence of the event."""
    timestamp: Optional[str]
