"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict


class CheckoutSessionUpdate(TypedDict, total=False):
    """ID of the payment integration to use."""
    integration_id: Optional[str]
    """Discounts to apply to the checkout session. Replaces existing discounts."""
    discounts: Optional[List[dict]]
    """Key-value pairs that can be used to store additional information."""
    metadata: Optional[dict]
