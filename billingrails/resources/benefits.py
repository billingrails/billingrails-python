"""This file is auto-generated. Do not edit manually."""

from ..types import (
    BenefitCreate,
    BenefitListResponse,
    BenefitResponse,
    BenefitUpdate,
    DeleteResponse,
)


class BenefitsResource:
    """Benefits resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> BenefitListResponse:
        """List benefits
        
        Retrieves a list of benefits."""
        return self.client.request("GET", f"/benefits", params=params)

    def create(self, data: BenefitCreate) -> BenefitResponse:
        """Create a benefit
        
        Creates a benefit."""
        return self.client.request("POST", f"/benefits", json=data)

    def retrieve(self, id: str, **params) -> BenefitResponse:
        """Retrieve a benefit
        
        Retrieves a benefit by ID."""
        return self.client.request("GET", f"/benefits/{id}", params=params)

    def update(self, id: str, data: BenefitUpdate) -> BenefitResponse:
        """Update a benefit
        
        Updates a benefit."""
        return self.client.request("PATCH", f"/benefits/{id}", json=data)

    def delete(self, id: str) -> DeleteResponse:
        """Delete a benefit
        
        Deletes a benefit by ID. Allowed only when the benefit is not assigned to any product, price or entitlements."""
        return self.client.request("DELETE", f"/benefits/{id}")

    def archive(self, id: str) -> BenefitResponse:
        """Archive a benefit
        
        Archives a benefit."""
        return self.client.request("POST", f"/benefits/{id}/archive", json={})

    def unarchive(self, id: str) -> BenefitResponse:
        """Unarchive a benefit
        
        Unarchives a benefit."""
        return self.client.request("POST", f"/benefits/{id}/unarchive", json={})
