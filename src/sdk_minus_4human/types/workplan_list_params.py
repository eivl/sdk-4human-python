# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkplanListParams"]


class WorkplanListParams(TypedDict, total=False):
    date_from: Required[Annotated[Union[str, date], PropertyInfo(alias="dateFrom", format="iso8601")]]
    """
    Lists work plan days that are equal or after this date using ATOM format
    Y-m-d\\TTH:i:sP
    """

    date_to: Required[Annotated[Union[str, date], PropertyInfo(alias="dateTo", format="iso8601")]]
    """
    Lists work plan days that are equal or before this date using ATOM format
    Y-m-d\\TTH:i:sP
    """

    company_employee_id: Annotated[str, PropertyInfo(alias="companyEmployeeId")]
    """Filters work plan days by company employee id"""

    company_id: Annotated[int, PropertyInfo(alias="companyId")]
    """Filters work plan days by company id"""

    created_at_from: Annotated[Union[str, date], PropertyInfo(alias="createdAtFrom", format="iso8601")]
    """
    Lists work plan days that are created on or after this date using ATOM format
    Y-m-d\\TTH:i:sP
    """

    created_at_to: Annotated[Union[str, date], PropertyInfo(alias="createdAtTo", format="iso8601")]
    """
    Lists work plan days that are created on or before this date using ATOM format
    Y-m-d\\TTH:i:sP
    """

    employee_id: Annotated[str, PropertyInfo(alias="employeeId")]
    """
    Filters work plan days by employee id, needs to be used with "companyId"
    parameter
    """

    employment_id: Annotated[int, PropertyInfo(alias="employmentId")]
    """Filters work plan days by employment id"""

    limit: int
    """Max returned results, default value is 100"""

    origin: Literal["registered_by_api", "generated_from_work_plan"]
    """Filters work plan days by it`s origin"""

    page: int
    """Results page, default value is 1"""

    source_system: Annotated[str, PropertyInfo(alias="sourceSystem")]
    """
    Filters work plan days by a phrase identifying the system which is the source of
    the work plan
    """
