# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AbsenceCreateResponse",
    "Failure",
    "FailureError",
    "FailurePayload",
    "Success",
    "SuccessCreatedAbsenceData",
    "SuccessPayload",
]


class FailureError(BaseModel):
    field: Optional[str] = None

    message: Optional[str] = None

    params: Optional[List[str]] = None


class FailurePayload(BaseModel):
    absence_code_id: Optional[int] = FieldInfo(alias="absenceCodeId", default=None)

    absence_code_id_external: Optional[str] = FieldInfo(alias="absenceCodeIdExternal", default=None)

    comment: Optional[str] = None

    company_employee_id: Optional[int] = FieldInfo(alias="companyEmployeeId", default=None)

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    date_from: Optional[str] = FieldInfo(alias="dateFrom", default=None)
    """The start date of the absence."""

    date_to: Optional[str] = FieldInfo(alias="dateTo", default=None)
    """The end date of the absence."""

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)

    employment_id: Optional[List[int]] = FieldInfo(alias="employmentId", default=None)

    external_absence_id: Optional[str] = FieldInfo(alias="externalAbsenceId", default=None)

    hours: Optional[float] = None

    percentage: Optional[float] = None

    source_system: Optional[str] = FieldInfo(alias="sourceSystem", default=None)

    status: Optional[Literal["approved", "for_approval"]] = None

    unit_id: Optional[str] = FieldInfo(alias="unitId", default=None)


class Failure(BaseModel):
    errors: Optional[List[FailureError]] = None

    payload: Optional[FailurePayload] = None


class SuccessCreatedAbsenceData(BaseModel):
    internal_absence_id: Optional[int] = FieldInfo(alias="internalAbsenceId", default=None)


class SuccessPayload(BaseModel):
    absence_code_id: Optional[int] = FieldInfo(alias="absenceCodeId", default=None)

    absence_code_id_external: Optional[str] = FieldInfo(alias="absenceCodeIdExternal", default=None)

    comment: Optional[str] = None

    company_employee_id: Optional[int] = FieldInfo(alias="companyEmployeeId", default=None)

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    date_from: Optional[str] = FieldInfo(alias="dateFrom", default=None)
    """The start date of the absence."""

    date_to: Optional[str] = FieldInfo(alias="dateTo", default=None)
    """The end date of the absence."""

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)

    employment_id: Optional[List[int]] = FieldInfo(alias="employmentId", default=None)

    external_absence_id: Optional[str] = FieldInfo(alias="externalAbsenceId", default=None)

    hours: Optional[float] = None

    percentage: Optional[float] = None

    source_system: Optional[str] = FieldInfo(alias="sourceSystem", default=None)

    status: Optional[Literal["approved", "for_approval"]] = None

    unit_id: Optional[str] = FieldInfo(alias="unitId", default=None)


class Success(BaseModel):
    created_absence_data: Optional[SuccessCreatedAbsenceData] = FieldInfo(alias="createdAbsenceData", default=None)

    payload: Optional[SuccessPayload] = None


class AbsenceCreateResponse(BaseModel):
    failures: Optional[List[Failure]] = None

    success: Optional[List[Success]] = None
