"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .invoice import Invoice


class InvoiceListResponse(TypedDict, total=False):
    invoices: Optional[List[Invoice]]
    meta: Optional[dict]
