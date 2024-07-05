# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AbsenceListResponse",
    "Item",
    "ItemAbsenceCode",
    "ItemAbsenceUser",
    "ItemComment",
    "ItemCommentCreatedBy",
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
    """The UUID of the absence user."""

    company_employee_id: Optional[int] = FieldInfo(alias="companyEmployeeId", default=None)
    """The internal id of the absence user."""

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """The external id of the absence user."""


class ItemCommentCreatedBy(BaseModel):
    id: Optional[str] = None
    """The ID of the user who created the item."""


class ItemComment(BaseModel):
    comment: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The timestamp when the item was created."""

    created_by: Optional[ItemCommentCreatedBy] = FieldInfo(alias="createdBy", default=None)


class ItemCompany(BaseModel):
    id: Optional[int] = None
    """The ID of the company."""

    unit_id: Optional[str] = FieldInfo(alias="unitId", default=None)
    """The unit id of the company."""


class ItemCreatedBy(BaseModel):
    id: Optional[str] = None
    """The ID of the user who created the item."""


class ItemUpdatedBy(BaseModel):
    id: Optional[str] = None
    """The ID of the user who last updated the item."""


class Item(BaseModel):
    id: Optional[int] = None
    """The ID of the item."""

    absence_calculation: Optional[Literal["percentage", "hours"]] = FieldInfo(alias="absenceCalculation", default=None)
    """
    Discriminator that determines the unit in which the absenceCalculationValue
    field is measured.
    """

    absence_calculation_value: Optional[float] = FieldInfo(alias="absenceCalculationValue", default=None)
    """
    Number value for part time absence measured in % or hours, depending on the
    absenceCalculation field.
    """

    absence_code: Optional[ItemAbsenceCode] = FieldInfo(alias="absenceCode", default=None)

    absence_user: Optional[ItemAbsenceUser] = FieldInfo(alias="absenceUser", default=None)

    comments: Optional[List[ItemComment]] = None

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

    external_absence_id: Optional[str] = FieldInfo(alias="externalAbsenceId", default=None)
    """The external id of the absence."""

    instance_id: Optional[str] = FieldInfo(alias="instanceId", default=None)
    """The ID of the instance."""

    origin: Optional[
        Literal["ABSENCE_REGISTERED_BY_API", "ABSENCE_REGISTERED_MANUALLY", "ABSENCE_REGISTERED_FROM_SICK_NOTE"]
    ] = None
    """The way the absence was registered in the system (e.g.

    ABSENCE_REGISTERED_MANUALLY)
    """

    source_system: Optional[str] = FieldInfo(alias="sourceSystem", default=None)
    """Name of the system that is responsible for the absence creation."""

    status: Optional[Literal["for_approval", "approved", "rejected"]] = None
    """The status of the absence."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The timestamp when the item was last updated."""

    updated_by: Optional[ItemUpdatedBy] = FieldInfo(alias="updatedBy", default=None)


class AbsenceListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
