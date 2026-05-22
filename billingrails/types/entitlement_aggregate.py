"""This file is auto-generated. Do not edit manually."""

from typing import Any, List, Optional, TypedDict

from .entitlement_benefit import EntitlementBenefit
from .entitlement_duplicate import EntitlementDuplicate


class EntitlementAggregate(TypedDict, total=False):
    feature_value: Optional[Any]
    usage: Optional[int]
    benefit: Optional[EntitlementBenefit]
    duplicates: Optional[List[EntitlementDuplicate]]
