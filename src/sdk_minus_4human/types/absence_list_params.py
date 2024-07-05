# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AbsenceListParams"]


class AbsenceListParams(TypedDict, total=False):
    absence_code_category: Annotated[
        Literal["leave_of_absence", "other", "sick_leave", "vacation", "working"],
        PropertyInfo(alias="absenceCodeCategory"),
    ]
    """Filters absences by absence code category."""

    absence_code_external_id: Annotated[str, PropertyInfo(alias="absenceCodeExternalId")]
    """Filters absences by absence code external ID."""

    absence_code_ids: Annotated[str, PropertyInfo(alias="absenceCodeIds")]
    """Filters absences by absence codes.

    Multiple absence codes can be specified by comma-separated values.
    """

    absence_code_internal_id: Annotated[str, PropertyInfo(alias="absenceCodeInternalId")]
    """Filters absences by absence code internal ID."""

    absence_code_type: Annotated[
        Literal["self_certified", "documented", "paid", "not_paid", "sick_child", "no_types"],
        PropertyInfo(alias="absenceCodeType"),
    ]
    """Filters absences by absence code type."""

    company_employee_id: Annotated[str, PropertyInfo(alias="companyEmployeeId")]
    """Filters absences by company employee id.

    Company employee id refers to employee that absence is created for.
    """

    company_id: Annotated[int, PropertyInfo(alias="companyId")]
    """Filters absences by company ID."""

    created_at_from: Annotated[Union[str, date], PropertyInfo(alias="createdAtFrom", format="iso8601")]
    """Lists absences that were created after (or equal to) the specified date."""

    created_at_to: Annotated[Union[str, date], PropertyInfo(alias="createdAtTo", format="iso8601")]
    """Lists absences that were created before (or equal to) the specified date."""

    created_by: Annotated[str, PropertyInfo(alias="createdBy")]
    """Filters absences by user id (uuid) that created an absence."""

    date_from: Annotated[Union[str, date], PropertyInfo(alias="dateFrom", format="iso8601")]
    """Lists absences that have date_from after (or equal to) the specified date."""

    date_to: Annotated[Union[str, date], PropertyInfo(alias="dateTo", format="iso8601")]
    """Lists absences that have date_from before (or equal to) the specified date."""

    employee_id: Annotated[str, PropertyInfo(alias="employeeId")]
    """Filters absences by employee id.

    Employee id refers to employee that absence is created for.
    """

    external_absence_id: Annotated[str, PropertyInfo(alias="externalAbsenceId")]
    """Filters absences by absence external id."""

    instance_id: Annotated[str, PropertyInfo(alias="instanceId")]
    """Filters absences by instance ID (UUID)."""

    limit: int
    """Max returned results. Default 100."""

    origin: Literal["ABSENCE_REGISTERED_BY_API", "ABSENCE_REGISTERED_MANUALLY", "ABSENCE_REGISTERED_FROM_SICK_NOTE"]
    """Filters absences by the way the absence was registered in the system."""

    page: int
    """Results page. Default 1."""

    source_system: Annotated[str, PropertyInfo(alias="sourceSystem")]
    """
    Filters absences by name of the system that is responsible for the absence
    creation.
    """

    status: Literal["for_approval", "approved", "rejected"]
    """Filters absences by absence status."""

    updated_at_from: Annotated[Union[str, date], PropertyInfo(alias="updatedAtFrom", format="iso8601")]
    """Lists absences that were updated after (or equal to) the specified date."""

    updated_at_to: Annotated[Union[str, date], PropertyInfo(alias="updatedAtTo", format="iso8601")]
    """Lists absences that were updated before (or equal to) the specified date."""

    updated_by: Annotated[str, PropertyInfo(alias="updatedBy")]
    """Filters absences by employee ID (UUID) that updated the absence."""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """Filters absences by user id (uuid).

    User id refers to employee that absence is created for.
    """
