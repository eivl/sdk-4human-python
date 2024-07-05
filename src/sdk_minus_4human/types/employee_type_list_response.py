# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmployeeTypeListResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    employee_type: Optional[str] = FieldInfo(alias="employeeType", default=None)

    employment_type: Optional[str] = FieldInfo(alias="employmentType", default=None)

    employment_type_id: Optional[str] = FieldInfo(alias="employmentTypeId", default=None)

    reason: Optional[bool] = None

    status: Optional[Literal["active", "archived"]] = None

    substitute: Optional[bool] = None

    type_id: Optional[str] = FieldInfo(alias="typeId", default=None)


class EmployeeTypeListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
