# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AccessGroupListResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    title: Optional[str] = None


class AccessGroupListResponse(BaseModel):
    items: Optional[List[Item]] = None
