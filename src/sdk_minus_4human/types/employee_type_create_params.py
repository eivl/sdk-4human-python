# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployeeTypeCreateParams"]


class EmployeeTypeCreateParams(TypedDict, total=False):
    employee_type: Required[Annotated[str, PropertyInfo(alias="employeeType")]]

    employment_type_id: Required[Annotated[str, PropertyInfo(alias="employmentTypeId")]]

    type_id: Required[Annotated[str, PropertyInfo(alias="typeId")]]

    reason: bool

    substitute: bool
