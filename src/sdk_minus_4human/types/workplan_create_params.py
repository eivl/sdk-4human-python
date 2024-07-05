# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkplanCreateParams", "CalendarDay"]


class WorkplanCreateParams(TypedDict, total=False):
    calendar_days: Required[Annotated[Iterable[CalendarDay], PropertyInfo(alias="calendarDays")]]

    date_from: Required[Annotated[str, PropertyInfo(alias="dateFrom")]]
    """The start date of the work plan. Format like 2023-06-05T00:00:00+00:00"""

    date_to: Required[Annotated[str, PropertyInfo(alias="dateTo")]]
    """The end date of the work plan. Format like 2023-06-05T00:00:00+00:00"""

    company_employee_ids: Annotated[Iterable[float], PropertyInfo(alias="companyEmployeeIds")]

    company_id: Annotated[float, PropertyInfo(alias="companyId")]

    employee_ids: Annotated[List[str], PropertyInfo(alias="employeeIds")]

    employment_ids: Annotated[Iterable[float], PropertyInfo(alias="employmentIds")]

    source_system: Annotated[Optional[str], PropertyInfo(alias="sourceSystem")]
    """Name of the system that the work plan was originally created in"""

    unit_id: Annotated[str, PropertyInfo(alias="unitId")]


class CalendarDay(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    number_of_hours: Required[Annotated[float, PropertyInfo(alias="numberOfHours")]]
