"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .subscription import Subscription


class SubscriptionResponse(TypedDict, total=False):
    subscription: Optional[Subscription]
    meta: Optional[dict]
