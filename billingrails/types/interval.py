"""This file is auto-generated. Do not edit manually."""

from typing import Literal, TypedDict


class Interval(TypedDict):
    """Frequency of the interval."""
    frequency: int
    """Unit of the interval."""
    unit: Literal["day", "week", "month", "year"]
