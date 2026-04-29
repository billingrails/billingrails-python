"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict


class AccountDebit(TypedDict, total=False):
    """The amount to debit in the smallest currency unit."""
    amount: int
    """The asset code for the debit."""
    asset_code: Optional[str]
    """The currency code for the debit."""
    currency: Optional[str]
    """Optional reference ID for tracking the debit."""
    reference_id: Optional[str]
