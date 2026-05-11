"""This file is auto-generated. Do not edit manually."""

from typing import List, Optional, TypedDict

from .credit_asset import CreditAsset


class CreditAssetListResponse(TypedDict, total=False):
    credit_assets: Optional[List[CreditAsset]]
    meta: Optional[dict]
