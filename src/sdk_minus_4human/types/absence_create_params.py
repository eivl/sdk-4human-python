# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AbsenceCreateParams", "Absence"]


class AbsenceCreateParams(TypedDict, total=False):
    absences: Iterable[Absence]


class Absence(TypedDict, total=False):
    absence_code_id: Annotated[Optional[int], PropertyInfo(alias="absenceCodeId")]
    """Database identifier for absence-code (id field)"""

    absence_code_id_external: Annotated[Optional[str], PropertyInfo(alias="absenceCodeIdExternal")]
    """External ID of absence-code, allowing to store the ID of the client's system"""

    comment: Optional[str]
    """Comment added to the absence"""

    company_employee_id: Annotated[Optional[int], PropertyInfo(alias="companyEmployeeId")]
    """Database identifier for company-employee (id field)"""

    company_id: Annotated[Optional[int], PropertyInfo(alias="companyId")]
    """Database identifier for company-employee (company field)"""

    date_from: Annotated[str, PropertyInfo(alias="dateFrom")]
    """The start date of the absence. Format like 2023-06-05T00:00:00+00:00"""

    date_to: Annotated[str, PropertyInfo(alias="dateTo")]
    """The end date of the absence. Format like 2023-06-05T00:00:00+00:00"""

    employee_id: Annotated[Optional[str], PropertyInfo(alias="employeeId")]
    """Database identifier for company-employee (employee_id field)"""

    employment_id: Annotated[Optional[Iterable[int]], PropertyInfo(alias="employmentId")]
    """Array of database identifier for employment (id field).

    Given employment must be assigned to the company-employee provided as employeeId
    or companyEmployeeId.

    To create an absence for a given employmentId it should have specified FTE
    value. Otherwise will be skipped.

    If employmentId is null/empty then absence is created for all employments having
    fte value assigned to a given company-employee. If none of provided employmentId
    has FTE value 400 is returned.
    """

    external_absence_id: Annotated[Union[str, int, None], PropertyInfo(alias="externalAbsenceId")]
    """Endpoint accepts both string and int.

    But the value is saved as a string. So if 1 provided it will be saved as '1'
    """

    hours: Optional[float]
    """Number value for part time absence measured in hours"""

    percentage: Optional[float]
    """Number value for part time absence measured in %.

    100% accepted as well, if absence-code allows it is transformed into full time
    absence
    """

    source_system: Annotated[Optional[str], PropertyInfo(alias="sourceSystem")]
    """Name of the system that is responsible for the absence creation"""

    status: Optional[Literal["approved", "for_approval"]]
    """Determines the absence status value that absences will be created with"""

    unit_id: Annotated[Optional[str], PropertyInfo(alias="unitId")]
    """Database identifier for organizational_unit (unit_id field)"""
