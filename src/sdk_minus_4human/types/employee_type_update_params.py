# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployeeTypeUpdateParams"]


class EmployeeTypeUpdateParams(TypedDict, total=False):
    employee_type: Annotated[str, PropertyInfo(alias="employeeType")]

    employment_type_id: Annotated[str, PropertyInfo(alias="employmentTypeId")]

    reason: bool

    status: Literal["active", "archived"]

    substitute: bool

    type_id: Annotated[str, PropertyInfo(alias="typeId")]
