"""This file is auto-generated. Do not edit manually."""

from typing import Dict, Any

from ..types import (
    PriceCreate,
    PriceResponse,
    PriceUpdate,
)


class PricesResource:
    """Prices resource"""

    def __init__(self, client):
        self.client = client

    def create(self, data: PriceCreate) -> PriceResponse:
        """Create a price
        
        Creates a price."""
        return self.client.request("POST", f"/prices", json=data)

    def retrieve(self, id: str, **params) -> PriceResponse:
        """Retrieve a price
        
        Retrieves a price by ID."""
        return self.client.request("GET", f"/prices/{id}", params=params)

    def update(self, id: str, data: PriceUpdate) -> PriceResponse:
        """Update a price
        
        Updates a price by ID."""
        return self.client.request("PUT", f"/prices/{id}", json=data)

    def delete(self, id: str) -> Dict[str, Any]:
        """Delete a price
        
        Deletes a price by ID."""
        return self.client.request("DELETE", f"/prices/{id}")

    def archive(self, id: str) -> PriceResponse:
        """Archive a price
        
        Archives a price, making it inactive for new subscriptions."""
        return self.client.request("POST", f"/prices/{id}/archive", json={})

    def undo_archive(self, id: str) -> PriceResponse:
        """Unarchive a price
        
        Restores an archived price to active status."""
        return self.client.request("POST", f"/prices/{id}/unarchive", json={})
