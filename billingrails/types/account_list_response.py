"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .account import Account


class AccountListResponse(TypedDict, total=False):
    accounts: Optional[List[Account]]
    meta: Optional[dict]
