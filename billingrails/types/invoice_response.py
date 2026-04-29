"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .invoice import Invoice


class InvoiceResponse(TypedDict, total=False):
    invoice: Optional[Invoice]
    meta: Optional[dict]
