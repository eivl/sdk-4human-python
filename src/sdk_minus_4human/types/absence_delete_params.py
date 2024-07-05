# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AbsenceDeleteParams"]


class AbsenceDeleteParams(TypedDict, total=False):
    company_employee_id: Annotated[Optional[int], PropertyInfo(alias="companyEmployeeId")]
    """Database identifier for company-employee (id field)"""

    company_id: Annotated[Optional[int], PropertyInfo(alias="companyId")]
    """The ID of the company."""

    created_by: Annotated[Optional[str], PropertyInfo(alias="createdBy")]
    """UserId that created absence"""

    date_from: Annotated[Union[str, datetime, None], PropertyInfo(alias="dateFrom", format="iso8601")]
    """The start date of the absence. Format like 2023-06-05T00:00:00+00:00"""

    date_to: Annotated[Union[str, datetime, None], PropertyInfo(alias="dateTo", format="iso8601")]
    """The end date of the absence. Format like 2023-06-05T00:00:00+00:00"""

    employee_id: Annotated[Optional[str], PropertyInfo(alias="employeeId")]
    """Identifier for company-employee (employee id field)"""

    external_absence_code_ids: Annotated[List[str], PropertyInfo(alias="externalAbsenceCodeIds")]
    """External ID for absence code"""

    external_absence_id: Annotated[Iterable[int], PropertyInfo(alias="externalAbsenceId")]
    """Endpoint accepts both string and int.

    But the value is saved as a string. So if 1 provided it will be saved as '1'
    """

    internal_absence_id: Annotated[Iterable[int], PropertyInfo(alias="internalAbsenceId")]
    """Endpoint accepts both string and int.

    But the value is saved as a string. So if 1 provided it will be saved as '1'
    """

    origin: Optional[
        Literal["ABSENCE_REGISTERED_BY_API", "ABSENCE_REGISTERED_MANUALLY", "ABSENCE_REGISTERED_FROM_SICK_NOTE"]
    ]
    """The way absence was registered in the system (e.g. ABSENCE_REGISTERED_MANUALLY)"""

    source_system: Annotated[Optional[str], PropertyInfo(alias="sourceSystem")]
    """Name of the system that is responsible for the absence creation"""

    unit_id: Annotated[Optional[str], PropertyInfo(alias="unitId")]
    """Identifier for company by unit id field."""
