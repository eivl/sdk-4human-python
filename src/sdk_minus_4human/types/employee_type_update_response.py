# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmployeeTypeUpdateResponse"]


class EmployeeTypeUpdateResponse(BaseModel):
    id: Optional[str] = None
    """UUID of employee type"""

    employee_type: Optional[str] = FieldInfo(alias="employeeType", default=None)
    """Name field from UI"""

    employment_type_id: Optional[str] = FieldInfo(alias="employmentTypeId", default=None)
    """UUID of employment type"""

    reason: Optional[bool] = None
    """determines if User requires reason for this type"""

    status: Optional[Literal["active", "archived"]] = None

    substitute: Optional[bool] = None
    """determines if User requires substitute for this type"""

    type_id: Optional[str] = FieldInfo(alias="typeId", default=None)
    """Id field from UI"""
