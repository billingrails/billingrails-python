"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List


class AccountDebitResponse(TypedDict, total=False):
    """The account ID."""
    account_id: Optional[str]
    """Updated balances."""
    balances: Optional[List[dict]]
    meta: Optional[dict]
