# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AbsenceCodeListResponse",
    "Item",
    "ItemAbsenceCode",
    "ItemAbsenceUser",
    "ItemCompany",
    "ItemCreatedBy",
    "ItemUpdatedBy",
]


class ItemAbsenceCode(BaseModel):
    category: Literal["leave_of_absence", "other", "sick_leave", "vacation"]

    id: Optional[int] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    internal_id: Optional[str] = FieldInfo(alias="internalId", default=None)

    name: Optional[str] = None

    type: Optional[Literal["self_certified", "documented", "paid", "not_paid", "sick_child", "no_types"]] = None


class ItemAbsenceUser(BaseModel):
    id: Optional[str] = None
    """The ID of the absence user."""


class ItemCompany(BaseModel):
    id: Optional[int] = None
    """The ID of the company."""


class ItemCreatedBy(BaseModel):
    id: Optional[str] = None
    """The ID of the user who created the item."""


class ItemUpdatedBy(BaseModel):
    id: Optional[str] = None
    """The ID of the user who last updated the item."""


class Item(BaseModel):
    id: Optional[int] = None
    """The ID of the item."""

    absence_code: Optional[ItemAbsenceCode] = FieldInfo(alias="absenceCode", default=None)

    absence_user: Optional[ItemAbsenceUser] = FieldInfo(alias="absenceUser", default=None)

    company: Optional[ItemCompany] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The timestamp when the item was created."""

    created_by: Optional[ItemCreatedBy] = FieldInfo(alias="createdBy", default=None)

    date_from: Optional[datetime] = FieldInfo(alias="dateFrom", default=None)
    """The start date of the absence."""

    date_to: Optional[datetime] = FieldInfo(alias="dateTo", default=None)
    """The end date of the absence."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The timestamp when the item was deleted."""

    employment_ids: Optional[List[float]] = FieldInfo(alias="employmentIds", default=None)
    """The IDs of employments associated with the absence."""

    instance_id: Optional[str] = FieldInfo(alias="instanceId", default=None)
    """The ID of the instance."""

    status: Optional[Literal["for_approval", "approved", "rejected"]] = None
    """The status of the absence."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The timestamp when the item was last updated."""

    updated_by: Optional[ItemUpdatedBy] = FieldInfo(alias="updatedBy", default=None)


class AbsenceCodeListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
