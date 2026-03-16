"""This file is auto-generated. Do not edit manually."""

from ..types import (
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
        return self.client.request("PUT", f"/meters/{id}", json=data)
