# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AbsenceUpdateResponse",
    "Failure",
    "FailureError",
    "FailurePayload",
    "Success",
    "SuccessPayload",
    "SuccessUpdatedAbsenceData",
]


class FailureError(BaseModel):
    field: Optional[str] = None

    message: Optional[str] = None

    params: Optional[List[str]] = None


class FailurePayload(BaseModel):
    id: Union[str, int, None] = None

    absence_code_id: Optional[int] = FieldInfo(alias="absenceCodeId", default=None)

    absence_code_id_external: Optional[str] = FieldInfo(alias="absenceCodeIdExternal", default=None)

    comment: Optional[str] = None

    date_from: Optional[str] = FieldInfo(alias="dateFrom", default=None)
    """The start date of the absence."""

    date_to: Optional[str] = FieldInfo(alias="dateTo", default=None)
    """The end date of the absence."""

    external_absence_id: Optional[str] = FieldInfo(alias="externalAbsenceId", default=None)

    hours: Optional[float] = None

    percentage: Optional[float] = None

    source_system: Optional[str] = FieldInfo(alias="sourceSystem", default=None)


class Failure(BaseModel):
    errors: Optional[List[FailureError]] = None

    payload: Optional[FailurePayload] = None


class SuccessPayload(BaseModel):
    id: Union[str, int, None] = None

    absence_code_id: Optional[int] = FieldInfo(alias="absenceCodeId", default=None)

    absence_code_id_external: Optional[str] = FieldInfo(alias="absenceCodeIdExternal", default=None)

    comment: Optional[str] = None

    date_from: Optional[str] = FieldInfo(alias="dateFrom", default=None)
    """The start date of the absence."""

    date_to: Optional[str] = FieldInfo(alias="dateTo", default=None)
    """The end date of the absence."""

    hours: Optional[float] = None

    percentage: Optional[float] = None

    source_system: Optional[str] = FieldInfo(alias="sourceSystem", default=None)


class SuccessUpdatedAbsenceData(BaseModel):
    id: Optional[int] = None


class Success(BaseModel):
    payload: Optional[SuccessPayload] = None

    updated_absence_data: Optional[SuccessUpdatedAbsenceData] = FieldInfo(alias="updatedAbsenceData", default=None)


class AbsenceUpdateResponse(BaseModel):
    failures: Optional[List[Failure]] = None

    success: Optional[List[Success]] = None
