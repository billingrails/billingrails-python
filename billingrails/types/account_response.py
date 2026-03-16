"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional

from .account import Account


class AccountResponse(TypedDict, total=False):
    account: Optional[Account]
    meta: Optional[dict]
