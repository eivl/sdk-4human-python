# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LocationListResponse", "Item"]


class Item(BaseModel):
    id: Optional[int] = None

    company_country: Optional[str] = FieldInfo(alias="companyCountry", default=None)
    """ISO 3166-1 alpha-3 country code"""

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)
    """database id of company"""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """Name of company that location belongs to"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    name: Optional[str] = None
    """Location name"""

    number: Optional[str] = None
    """identifier of location (companyLocationId from UI)"""

    status: Optional[Literal["ACTIVE", "INACTIVE"]] = None


class LocationListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
