"""This file is auto-generated. Do not edit manually."""

from typing import TypedDict, Optional, List

from .tax_rate import TaxRate


class TaxRateListResponse(TypedDict, total=False):
    tax_rates: Optional[List[TaxRate]]
    meta: Optional[dict]
