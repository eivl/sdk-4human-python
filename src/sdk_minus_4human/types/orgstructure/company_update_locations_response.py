# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CompanyUpdateLocationsResponse", "Item"]


class Item(BaseModel):
    id: Optional[int] = None

    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)

    name: Optional[str] = None

    status: Optional[Literal["new", "updated", "removed"]] = None


class CompanyUpdateLocationsResponse(BaseModel):
    company_updated: Optional[bool] = FieldInfo(alias="companyUpdated", default=None)

    items: Optional[List[Item]] = None

    total: Optional[int] = None
