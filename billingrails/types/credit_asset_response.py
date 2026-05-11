"""This file is auto-generated. Do not edit manually."""

from typing import Optional, TypedDict

from .credit_asset import CreditAsset


class CreditAssetResponse(TypedDict, total=False):
    credit_asset: Optional[CreditAsset]
    meta: Optional[dict]
