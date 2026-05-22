"""This file is auto-generated. Do not edit manually."""

from typing import Dict, Optional, TypedDict

from .entitlement_aggregate import EntitlementAggregate


class EntitlementsResponse(TypedDict, total=False):
    entitlements: Optional[Dict[str, EntitlementAggregate]]
    meta: Optional[dict]
