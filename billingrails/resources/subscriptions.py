"""This file is auto-generated. Do not edit manually."""

from typing import Dict, Any

from ..types import (
    CheckoutSessionResponse,
    SubscriptionCreate,
    SubscriptionListResponse,
    SubscriptionResponse,
)


class SubscriptionsResource:
    """Subscriptions resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> SubscriptionListResponse:
        """List subscriptions
        
        Retrieves a list of subscriptions."""
        return self.client.request("GET", f"/subscriptions", params=params)

    def create(self, data: SubscriptionCreate) -> SubscriptionResponse:
        """Create a subscription
        
        Creates a subscription."""
        return self.client.request("POST", f"/subscriptions", json=data)

    def retrieve(self, id: str, **params) -> SubscriptionResponse:
        """Retrieve subscription
        
        Retrieves a subscription by ID."""
        return self.client.request("GET", f"/subscriptions/{id}", params=params)

    def update(self, id: str, data: SubscriptionCreate) -> SubscriptionResponse:
        """Update a subscription
        
        Updates a subscription."""
        return self.client.request("PUT", f"/subscriptions/{id}", json=data)

    def resume(self, id: str, data: Dict[str, Any]) -> CheckoutSessionResponse:
        """Resume a paused subscription
        
        Creates a subscription resumption checkout session, triggers payment, and returns the payment link. The subscription must be paused. Requires an active payment integration (site payment routes or an active integration). The customer is redirected to the payment link to pay the resumption invoice; after payment the subscription becomes active again."""
        return self.client.request("POST", f"/subscriptions/{id}/resume", json=data)
