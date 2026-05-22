"""This file is auto-generated. Do not edit manually."""

from ..types import (
    DeleteResponse,
    MeterCreate,
    MeterListResponse,
    MeterResponse,
    MeterUpdate,
)


class MetersResource:
    """Meters resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> MeterListResponse:
        """List meters
        
        Retrieves a list of meters."""
        return self.client.request("GET", f"/meters", params=params)

    def create(self, data: MeterCreate) -> MeterResponse:
        """Create a meter
        
        Creates a meter."""
        return self.client.request("POST", f"/meters", json=data)

    def retrieve(self, id: str, **params) -> MeterResponse:
        """Retrieve a meter
        
        Retrieves meter by ID."""
        return self.client.request("GET", f"/meters/{id}", params=params)

    def update(self, id: str, data: MeterUpdate) -> MeterResponse:
        """Update a meter
        
        Updates a meter."""
        return self.client.request("PATCH", f"/meters/{id}", json=data)

    def delete(self, id: str) -> DeleteResponse:
        """Delete a meter
        
        Deletes a meter. Allowed only when no price, benefit or subscription is associated with it."""
        return self.client.request("DELETE", f"/meters/{id}")

    def archive(self, id: str) -> MeterResponse:
        """Archive a meter
        
        Archives a meter."""
        return self.client.request("POST", f"/meters/{id}/archive", json={})

    def unarchive(self, id: str) -> MeterResponse:
        """Unarchive a meter
        
        Restores an archived meter."""
        return self.client.request("POST", f"/meters/{id}/unarchive", json={})
