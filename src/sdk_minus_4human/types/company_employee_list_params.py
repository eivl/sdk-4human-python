# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CompanyEmployeeListParams"]


class CompanyEmployeeListParams(TypedDict, total=False):
    company_id: Annotated[int, PropertyInfo(alias="companyId")]

    employee_id: Annotated[str, PropertyInfo(alias="employeeId")]

    employment_id: Annotated[str, PropertyInfo(alias="employmentId")]

    external: bool
    """
    Param determines if employmentId used in filter is external (number) or internal
    (id)
    """

    limit: int

    page: int

    user_id: Annotated[str, PropertyInfo(alias="userId")]
