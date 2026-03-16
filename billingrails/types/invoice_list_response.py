"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .invoice import Invoice


class InvoiceListResponse(TypedDict, total=False):
    invoices: Optional[List[Invoice]]
    meta: Optional[dict]
