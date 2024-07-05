# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["EmploymentTypeListResponse", "Item"]


class Item(BaseModel):
    id: str

    title: str


class EmploymentTypeListResponse(BaseModel):
    items: Optional[List[Item]] = None
