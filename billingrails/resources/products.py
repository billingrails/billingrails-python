"""This file is auto-generated. Do not edit manually."""

from typing import Dict, Any

from ..types import (
    ProductCreate,
    ProductListResponse,
    ProductResponse,
    ProductUpdate,
)


class ProductsResource:
    """Products resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> ProductListResponse:
        """List products
        
        Retrieves a list of products."""
        return self.client.request("GET", f"/products", params=params)

    def create(self, data: ProductCreate) -> ProductResponse:
        """Create a product
        
        Creates a product."""
        return self.client.request("POST", f"/products", json=data)

    def retrieve(self, id: str, **params) -> ProductResponse:
        """Retrieve a product
        
        Retrieves product by ID."""
        return self.client.request("GET", f"/products/{id}", params=params)

    def update(self, id: str, data: ProductUpdate) -> ProductResponse:
        """Update a product
        
        Updates a product."""
        return self.client.request("PATCH", f"/products/{id}", json=data)

    def delete(self, id: str) -> Dict[str, Any]:
        """Delete a product
        
        Deletes a product when it is not used in any subscription and not referenced on invoices."""
        return self.client.request("DELETE", f"/products/{id}")

    def archive(self, id: str) -> ProductResponse:
        """Archive a product
        
        Archives a product."""
        return self.client.request("POST", f"/products/{id}/archive", json={})

    def unarchive(self, id: str) -> ProductResponse:
        """Unarchive a product
        
        Restores an archived product."""
        return self.client.request("POST", f"/products/{id}/unarchive", json={})
