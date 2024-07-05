# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkplanDeleteParams"]


class WorkplanDeleteParams(TypedDict, total=False):
    date_from: Required[Annotated[str, PropertyInfo(alias="dateFrom")]]
    """The start date of the absence. Format like 2023-06-05T00:00:00+00:00"""

    date_to: Required[Annotated[str, PropertyInfo(alias="dateTo")]]
    """The end date of the absence. Format like 2023-06-05T00:00:00+00:00"""

    company_employee_id: Annotated[Optional[int], PropertyInfo(alias="companyEmployeeId")]
    """Database identifier for company-employee (id field)"""

    company_id: Annotated[Optional[int], PropertyInfo(alias="companyId")]
    """Database identifier for company-employee (company field)"""

    employee_id: Annotated[Optional[str], PropertyInfo(alias="employeeId")]
    """Database identifier for company-employee (employee_id field)"""

    employment_id: Annotated[Optional[int], PropertyInfo(alias="employmentId")]
    """Database identifier for employment (id field)"""

    unit_id: Annotated[Optional[str], PropertyInfo(alias="unitId")]
    """Database identifier for organizational_unit (unit_id field)"""
