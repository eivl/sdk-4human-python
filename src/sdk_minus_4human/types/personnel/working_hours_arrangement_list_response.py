# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WorkingHoursArrangementListResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    description: Optional[str] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    internal_id: Optional[str] = FieldInfo(alias="internalId", default=None)

    name: Optional[str] = None

    status: Optional[str] = None

    working_hours_per_week: Optional[float] = FieldInfo(alias="workingHoursPerWeek", default=None)


class WorkingHoursArrangementListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
