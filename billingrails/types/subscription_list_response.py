"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .subscription import Subscription


class SubscriptionListResponse(TypedDict, total=False):
    subscriptions: Optional[List[Subscription]]
    meta: Optional[dict]
