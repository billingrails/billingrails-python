"""This file is auto-generated. Do not edit manually."""

from typing import Dict, Any

from ..types import (
    PlanCreate,
    PlanListResponse,
    PlanResponse,
    PlanUpdate,
)


class PlansResource:
    """Plans resource"""

    def __init__(self, client):
        self.client = client

    def list(self, **params) -> PlanListResponse:
        """List plans
        
        Retrieves a list of plans."""
        return self.client.request("GET", f"/plans", params=params)

    def create(self, data: PlanCreate) -> PlanResponse:
        """Create a plan
        
        Creates a plan."""
        return self.client.request("POST", f"/plans", json=data)

    def retrieve(self, id: str, **params) -> PlanResponse:
        """Retrieve a plan
        
        Retrieves a plan by ID."""
        return self.client.request("GET", f"/plans/{id}", params=params)

    def update(self, id: str, data: PlanUpdate) -> PlanResponse:
        """Update a plan
        
        Updates a plan."""
        return self.client.request("PUT", f"/plans/{id}", json=data)

    def delete(self, id: str) -> Dict[str, Any]:
        """Delete a plan
        
        Deletes a plan."""
        return self.client.request("DELETE", f"/plans/{id}")

    def archive(self, id: str) -> PlanResponse:
        """Archive a plan
        
        Archives a plan."""
        return self.client.request("POST", f"/plans/{id}/archive", json={})

    def unarchive(self, id: str) -> PlanResponse:
        """Unarchive a plan
        
        Restores an archived plan."""
        return self.client.request("POST", f"/plans/{id}/unarchive", json={})

    def duplicate(self, id: str) -> PlanResponse:
        """Duplicate a plan
        
        Creates a new plan with the same attributes and items. The new plan's origin_id is set to the source plan."""
        return self.client.request("POST", f"/plans/{id}/duplicate", json={})
