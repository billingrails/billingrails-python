"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .account import Account


class AccountListResponse(TypedDict, total=False):
    accounts: Optional[List[Account]]
    meta: Optional[dict]
