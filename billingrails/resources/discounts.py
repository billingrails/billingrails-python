"""This file is auto-generated. Do not edit manually."""

from ..types import (
    DiscountCreate,
    DiscountListResponse,
    DiscountResponse,
    DiscountUpdate,
)


class DiscountsResource:
    """Discounts resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> DiscountListResponse:
        """List discounts
        
        Retrieve a list of discounts."""
        return self.client.request("GET", f"/discounts", params=params)

    def create(self, data: DiscountCreate) -> DiscountResponse:
        """Create a discount
        
        Creates a discount."""
        return self.client.request("POST", f"/discounts", json=data)

    def retrieve(self, id: str, **params) -> DiscountResponse:
        """Retrieve discount
        
        Retrieves a discount by ID."""
        return self.client.request("GET", f"/discounts/{id}", params=params)

    def update(self, id: str, data: DiscountUpdate) -> DiscountResponse:
        """Update a discount
        
        Updates a discount."""
        return self.client.request("PATCH", f"/discounts/{id}", json=data)

    def archive(self, id: str) -> DiscountResponse:
        """Archive a discount
        
        Archives a discount."""
        return self.client.request("POST", f"/discounts/{id}/archive", json={})

    def unarchive(self, id: str) -> DiscountResponse:
        """Unarchive a discount
        
        Unarchives a discount."""
        return self.client.request("POST", f"/discounts/{id}/unarchive", json={})
