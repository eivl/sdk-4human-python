# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LocationListResponse", "Item", "ItemPostAddress", "ItemVisitAddress"]


class ItemPostAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class ItemVisitAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class Item(BaseModel):
    id: Optional[int] = None

    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    name: Optional[str] = None

    post_address: Optional[ItemPostAddress] = FieldInfo(alias="postAddress", default=None)

    visit_address: Optional[ItemVisitAddress] = FieldInfo(alias="visitAddress", default=None)


class LocationListResponse(BaseModel):
    items: Optional[List[Item]] = None

    selected_company_number: Optional[str] = FieldInfo(alias="selectedCompanyNumber", default=None)
