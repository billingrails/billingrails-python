"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .price_input import PriceInput
from .fee_input import FeeInput


class PlanCreate(TypedDict, total=False):
    """Internal identifier of the plan."""
    code: str
    """Name of the plan."""
    name: str
    """Description of the plan."""
    description: Optional[str]
    """Name that appears on invoices for this plan."""
    invoice_name: Optional[str]
    """Trial period of the plan in days."""
    trial_period_days: Optional[int]
    """Default price configuration for the plan. If both price and prices are provided, prices takes precedence."""
    price: PriceInput
    """Additional prices for this plan. Takes precedence over the price field if both are provided."""
    prices: Optional[List[PriceInput]]
    """Fees associated with the plan."""
    fees: Optional[List[FeeInput]]
