"""This file is auto-generated. Do not edit manually."""

from ..types import (
    TaxRateCreate,
    TaxRateListResponse,
    TaxRateResponse,
    TaxRateUpdate,
)


class TaxRatesResource:
    """Tax rates resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> TaxRateListResponse:
        """List tax rates
        
        Retrieve a list of tax rates."""
        return self.client.request("GET", f"/tax-rates", params=params)

    def create(self, data: TaxRateCreate) -> TaxRateResponse:
        """Create a tax rate
        
        Creates a tax rate."""
        return self.client.request("POST", f"/tax-rates", json=data)

    def retrieve(self, id: str, **params) -> TaxRateResponse:
        """Retrieve tax rate
        
        Retrieves a tax rate by ID."""
        return self.client.request("GET", f"/tax-rates/{id}", params=params)

    def update(self, id: str, data: TaxRateUpdate) -> TaxRateResponse:
        """Update a tax rate
        
        Updates a tax rate."""
        return self.client.request("PATCH", f"/tax-rates/{id}", json=data)

    def delete(self, id: str) -> Dict[str, Any]:
        """Delete a tax rate
        
        Deletes a tax rate."""
        return self.client.request("DELETE", f"/tax-rates/{id}")

    def archive(self, id: str) -> TaxRateResponse:
        """Archive a tax rate
        
        Archives a tax rate."""
        return self.client.request("POST", f"/tax-rates/{id}/archive", json={})

    def unarchive(self, id: str) -> TaxRateResponse:
        """Unarchive a tax rate
        
        Unarchives a tax rate."""
        return self.client.request("POST", f"/tax-rates/{id}/unarchive", json={})
