# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AccessGroupAssignResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    title: Optional[str] = None


class AccessGroupAssignResponse(BaseModel):
    items: Optional[List[Item]] = None
