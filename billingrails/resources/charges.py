"""This file is auto-generated. Do not edit manually."""

from ..types import (
    ChargeResponse,
)


class ChargesResource:
    """Charges resource"""

    def __init__(self, client):
        self.client = client

    def settle(self, id: str) -> ChargeResponse:
        """Settle a charge
        
        Marks a charge in `ready` status as settled. Typically used when confirming usage outside automatic credit settlement."""
        return self.client.request("POST", f"/charges/{id}/settle", json={})

    def discard(self, id: str) -> ChargeResponse:
        """Discard a charge
        
        Discards a `ready`charge."""
        return self.client.request("DELETE", f"/charges/{id}")
