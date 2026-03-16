"""This file is auto-generated. Do not edit manually."""

from typing import Dict, Any

from ..types import (
    FeeCreate,
    FeeListResponse,
    FeeResponse,
    FeeUpdate,
)


class FeesResource:
    """Fees resource"""

    def __init__(self, client):
        self.client = client

    def list(self) -> FeeListResponse:
        """List fees
        
        Retrieve a list of fees."""
        return self.client.request("GET", f"/fees")

    def create(self, data: FeeCreate) -> FeeResponse:
        """Create a fee
        
        Creates a fee."""
        return self.client.request("POST", f"/fees", json=data)

    def retrieve(self, id: str, **params) -> FeeResponse:
        """Retrieve fee
        
        Retrieves a fee by ID."""
        return self.client.request("GET", f"/fees/{id}", params=params)

    def update(self, id: str, data: FeeUpdate) -> FeeResponse:
        """Update a fee
        
        Updates a fee."""
        return self.client.request("PUT", f"/fees/{id}", json=data)

    def delete(self, id: str) -> Dict[str, Any]:
        """Delete a fee
        
        Deletes a fee."""
        return self.client.request("DELETE", f"/fees/{id}")

    def archive(self, id: str) -> FeeResponse:
        """Archive a fee
        
        Archives a fee, making it inactive for new subscriptions."""
        return self.client.request("POST", f"/fees/{id}/archive", json={})

    def undo_archive(self, id: str) -> FeeResponse:
        """Unarchive a fee
        
        Restores an archived fee to active status."""
        return self.client.request("POST", f"/fees/{id}/unarchive", json={})
