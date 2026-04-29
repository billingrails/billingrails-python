"""This file is auto-generated. Do not edit manually."""

from typing import List, Literal, Optional, TypedDict


class InvoiceInput(TypedDict, total=False):
    """Payment collection method for the invoice."""
    collection_method: Optional[Literal["automatic", "manual"]]
    """Payment method ID to charge (required if collection_method is automatic)."""
    payment_method_id: Optional[str]
    """Date the invoice is due."""
    due_at: Optional[str]
    """Items in the invoice."""
    line_items: Optional[List[dict]]
