"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .meter_profile import MeterProfile


class MeterCreate(TypedDict, total=False):
    """Name of the meter."""
    name: str
    """The name of the event to track usage for."""
    event_name: str
    """Internal description of the meter."""
    description: Optional[str]
    """Defines the connection between event data and Billingrails accounts."""
    account_mapping: dict
    """Meter profiles define aggregation behaviors for a meter."""
    profiles: List[MeterProfile]
