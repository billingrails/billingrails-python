"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List


class AccountBalancesResponse(TypedDict, total=False):
    """The account ID."""
    account_id: Optional[str]
    """Balances by currency."""
    balances: Optional[List[dict]]
    meta: Optional[dict]
