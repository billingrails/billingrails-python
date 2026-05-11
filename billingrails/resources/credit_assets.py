"""This file is auto-generated. Do not edit manually."""

from ..types import (
    CreditAssetCreate,
    CreditAssetListResponse,
    CreditAssetResponse,
    CreditAssetUpdate,
)


class CreditAssetsResource:
    """Credit assets resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> CreditAssetListResponse:
        """List credit assets
        
        Retrieves a list of credit assets."""
        return self.client.request("GET", f"/credit_assets", params=params)

    def create(self, data: CreditAssetCreate) -> CreditAssetResponse:
        """Create a credit asset
        
        Creates a credit asset."""
        return self.client.request("POST", f"/credit_assets", json=data)

    def retrieve(self, id: str, **params) -> CreditAssetResponse:
        """Retrieve a credit asset
        
        Retrieves a credit asset by ID or code."""
        return self.client.request("GET", f"/credit_assets/{id}", params=params)

    def update(self, id: str, data: CreditAssetUpdate) -> CreditAssetResponse:
        """Update a credit asset
        
        Updates a credit asset."""
        return self.client.request("PATCH", f"/credit_assets/{id}", json=data)
