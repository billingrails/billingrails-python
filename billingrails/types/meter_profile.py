"""This file is auto-generated. Do not edit manually."""

from typing import List, Literal, Optional, TypedDict


class MeterProfile(TypedDict, total=False):
    """ID of the profile."""
    id: Optional[str]
    """Name of the meter profile."""
    name: str
    """Unique identifier for the meter profile."""
    code: Optional[str]
    """When `true`, usage is counted across billing periods; when `false`, usage resets each period."""
    recurring: bool
    """Specifies the method for aggregating matching events."""
    aggregation_method: Literal["sum", "count", "count_unique", "min", "max", "latest"]
    """A key that specifies which event property is used to aggregate data. Not required for `count` aggregation method."""
    aggregation_property: Optional[str]
    """Time window for aggregation."""
    aggregation_time_window: Optional[Literal["hour", "day"]]
    """Filters to apply to events for this profile."""
    filters: Optional[List[dict]]
