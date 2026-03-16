"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional

from .tax_rate import TaxRate


class TaxRateResponse(TypedDict, total=False):
    tax_rate: Optional[TaxRate]
    meta: Optional[dict]
