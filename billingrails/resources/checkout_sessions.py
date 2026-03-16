"""This file is auto-generated. Do not edit manually."""

from ..types import (
    CheckoutSessionCreate,
    CheckoutSessionResponse,
    CheckoutSessionUpdate,
)


class CheckoutSessionsResource:
    """Checkout sessions resource"""

    def __init__(self, client):
        self.client = client

    def create(self, data: CheckoutSessionCreate) -> CheckoutSessionResponse:
        """Create a checkout session
        
        Creates a checkout session for processing payments."""
        return self.client.request("POST", f"/checkout_sessions", json=data)

    def retrieve(self, id: str, **params) -> CheckoutSessionResponse:
        """Retrieve a checkout session
        
        Retrieves a checkout session by ID."""
        return self.client.request("GET", f"/checkout_sessions/{id}", params=params)

    def update(self, id: str, data: CheckoutSessionUpdate) -> CheckoutSessionResponse:
        """Update a checkout session
        
        Updates a checkout session."""
        return self.client.request("PUT", f"/checkout_sessions/{id}", json=data)
