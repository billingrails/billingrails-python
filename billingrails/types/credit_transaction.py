"""This file is auto-generated. Do not edit manually."""

from typing import Literal, Optional, TypedDict


class CreditTransaction(TypedDict, total=False):
    object: Optional[Literal["credit_transaction"]]
    id: Optional[str]
    """Ledger line type."""
    type: Optional[Literal["inflow", "outflow", "reversal"]]
    status: Optional[Literal["pending", "settled", "failed", "ongoing", "reversed"]]
    """Signed amount (negative for outflows)."""
    amount: Optional[int]
    running_balance: Optional[int]
    currency: Optional[str]
    asset_code: Optional[str]
    description: Optional[str]
    reference_id: Optional[str]
    created_at: Optional[str]
    """Present when the transaction source is an invoice."""
    invoice_id: Optional[str]
    """Present when the transaction source is a charge."""
    charge_id: Optional[str]
