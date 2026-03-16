"""This file is auto-generated. Do not edit manually."""

from typing import Dict, Any

from ..types import (
    PaymentInput,
    PaymentListResponse,
    PaymentResponse,
)


class PaymentsResource:
    """Payments resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> PaymentListResponse:
        """List payments
        
        Retrieves a list of payments."""
        return self.client.request("GET", f"/payments", params=params)

    def create(self, data: PaymentInput) -> Dict[str, Any]:
        """Create a payment
        
        Create an online or offline payment for an invoice, payment request, or credit grant."""
        return self.client.request("POST", f"/payments", json=data)

    def retrieve(self, id: str, **params) -> PaymentResponse:
        """Retrieve payment
        
        Retrieves a payment by ID."""
        return self.client.request("GET", f"/payments/{id}", params=params)
