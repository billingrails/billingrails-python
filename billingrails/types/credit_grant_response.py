"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .credit_grant import CreditGrant


class CreditGrantResponse(TypedDict, total=False):
    credit_grant: Optional[CreditGrant]
    meta: Optional[dict]
