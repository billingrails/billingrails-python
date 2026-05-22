"""This file is auto-generated. Do not edit manually."""

from ..types import (
    PaymentLinkCreate,
    PaymentLinkListResponse,
    PaymentLinkResponse,
    PaymentLinkUpdate,
)


class PaymentLinksResource:
    """Payment links resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> PaymentLinkListResponse:
        """List payment links
        
        Retrieves a list of payment links."""
        return self.client.request("GET", f"/payment-links", params=params)

    def create(self, data: PaymentLinkCreate) -> PaymentLinkResponse:
        """Create payment link
        
        Creates a new payment link."""
        return self.client.request("POST", f"/payment-links", json=data)

    def retrieve(self, id: str, **params) -> PaymentLinkResponse:
        """Retrieve payment link
        
        Retrieves a payment link by ID."""
        return self.client.request("GET", f"/payment-links/{id}", params=params)

    def update(self, id: str, data: PaymentLinkUpdate) -> PaymentLinkResponse:
        """Update payment link
        
        Updates a payment link."""
        return self.client.request("PATCH", f"/payment-links/{id}", json=data)
