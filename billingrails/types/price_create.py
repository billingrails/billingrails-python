"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List, Literal

from .interval import Interval


"""Price create payload. One of plan_id or fee_id is required."""
class PriceCreate(TypedDict, total=False):
    """Amount in currency subunits (for flat, package, or tiered pricing)."""
    amount: Optional[int]
    """Currency code."""
    currency: str
    """Pricing model."""
    model: Literal["flat", "per_unit", "package", "volume", "graduated", "percentage"]
    """Flat amount added to percentage model."""
    flat_amount: Optional[int]
    """Package size (for package model)."""
    package_size: Optional[int]
    """Percentage rate (for percentage model)."""
    percentage_rate: Optional[int]
    """Pricing tiers (for volume and graduated models)."""
    tiers: Optional[List[dict]]
    """Billing interval for this price."""
    interval: Optional[Interval]
    """Number of billing cycles for this price."""
    billing_cycles: Optional[int]
    """When to bill for this price."""
    bill_timing: Optional[Literal["advance", "arrears"]]
    """Number of free units included per billing cycle."""
    free_units: Optional[int]
    """Number of free events included per billing cycle."""
    free_events: Optional[int]
    """Number of free units per event."""
    free_units_per_event: Optional[int]
    """Meter ID for usage-based billing."""
    meter_id: Optional[str]
    """Meter profile ID to use for this price."""
    meter_profile_id: Optional[str]
    """Feature entitlements associated with this price."""
    entitlements: Optional[List[dict]]
    """Plan ID to associate the price with."""
    plan_id: Optional[str]
    """Fee ID to associate the price with."""
    fee_id: Optional[str]
