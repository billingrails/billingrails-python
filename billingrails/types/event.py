"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class Event(TypedDict, total=False):
    """ID of the object."""
    id: Optional[str]
    """The name of the event."""
    event_name: Optional[str]
    """Unique identifier for this event."""
    idempotency_key: Optional[str]
    """Represents the object's type."""
    object: Optional[Literal["event"]]
    """Properties associated with the event."""
    properties: Optional[dict]
    """Timestamp indicating the occurrence of the event."""
    timestamp: Optional[str]
