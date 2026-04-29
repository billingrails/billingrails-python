"""This file is auto-generated. Do not edit manually."""

from typing import List, Literal, Optional, TypedDict

from .meter_profile import MeterProfile


class Meter(TypedDict, total=False):
    """Represents the object's type."""
    object: Optional[Literal["meter"]]
    """ID of the object."""
    id: Optional[str]
    """Name of the meter."""
    name: Optional[str]
    """The name of the event to record usage for."""
    event_name: Optional[str]
    """Internal description of the meter."""
    description: Optional[str]
    """Status of the meter."""
    status: Optional[Literal["active", "inactive"]]
    """Defines the connection between event data and Billingrails accounts."""
    account_mapping: Optional[dict]
    """Timestamp indicating when the object was created."""
    created_at: Optional[str]
    """The default meter profile."""
    default_profile: Optional[MeterProfile]
    """Meter profiles define aggregation behaviors for a meter."""
    profiles: Optional[List[MeterProfile]]
