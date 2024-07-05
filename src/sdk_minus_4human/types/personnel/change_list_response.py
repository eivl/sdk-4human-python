# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ChangeListResponse", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    company_employees: List[int] = FieldInfo(alias="companyEmployees")
    """
    Internal ID list of changed company-employees (field called `id` in
    company-employee object)
    """

    employments: List[int]
    """
    Internal ID list of changed employments (field called `id` in employment object)
    """

    users: List[str]
    """ID list of changed users (field called `id` in user object)"""

    employments_with_end_date_in_period: Optional[List[int]] = FieldInfo(
        alias="employmentsWithEndDateInPeriod", default=None
    )
    """
    External ID list of employments with end date in a specified period (field
    called `id` in employment object)
    """

    employments_with_start_date_in_period: Optional[List[int]] = FieldInfo(
        alias="employmentsWithStartDateInPeriod", default=None
    )
    """
    External ID list of employments with start date in a specified period (field
    called `id` in employment object)
    """


class UnionMember1(BaseModel):
    company_employees: List[str] = FieldInfo(alias="companyEmployees")
    """
    External ID list of changed company-employees (field called `employeeId` in
    company-employee object)
    """

    employments: List[str]
    """
    External ID list of changed employments (field called `number` in employment
    object)
    """

    users: List[str]
    """ID list of changed users (field called `id` in user object)"""

    employments_with_end_date_in_period: Optional[List[str]] = FieldInfo(
        alias="employmentsWithEndDateInPeriod", default=None
    )
    """
    External ID list of employments with end date in a specified period (field
    called `number` in employment object)
    """

    employments_with_start_date_in_period: Optional[List[str]] = FieldInfo(
        alias="employmentsWithStartDateInPeriod", default=None
    )
    """
    External ID list of employments with start date in a specified period (field
    called `number` in employment object)
    """


ChangeListResponse = Union[UnionMember0, UnionMember1]
