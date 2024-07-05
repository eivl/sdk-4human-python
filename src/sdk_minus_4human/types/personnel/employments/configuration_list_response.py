# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ConfigurationListResponse", "Item"]


class Item(BaseModel):
    key: Optional[str] = None

    value: Optional[object] = None


class ConfigurationListResponse(BaseModel):
    items: Optional[List[Item]] = None
