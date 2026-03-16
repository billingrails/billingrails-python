"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .price_input import PriceInput


"""Input for creating or updating a plan. Accepts either `price` or `prices` array (prices takes precedence)."""
class PlanInput(TypedDict, total=False):
    """Name of the plan."""
    name: Optional[str]
    """Description of the plan."""
    description: Optional[str]
    """Name that appears on invoices for this plan."""
    invoice_name: Optional[str]
    """Trial period of the plan in days."""
    trial_period_days: Optional[int]
    """Default price configuration for the plan. If both price and prices are provided, prices takes precedence."""
    price: Optional[PriceInput]
    """Additional prices for this plan. Takes precedence over the price field if both are provided."""
    prices: Optional[List[PriceInput]]
