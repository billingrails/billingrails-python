"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .subscription import Subscription


class SubscriptionListResponse(TypedDict, total=False):
    subscriptions: Optional[List[Subscription]]
    meta: Optional[dict]
