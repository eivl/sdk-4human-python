# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkplanListResponse", "Item"]


class Item(BaseModel):
    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)
    """Identifier for company (id field)"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """
    The date this entry was created on, the format is `Y-m-d\\TTH:i:sP` for example
    `2024-01-04T19:30:00+00:00`
    """

    date: Optional[str] = None
    """
    The date of the work plan day, the format is `Y-m-d\\TTH:i:sP` for example
    `2024-01-05T00:00:00+00:00`
    """

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """Identifier for employee (employee_id field)"""

    employment_id: Optional[int] = FieldInfo(alias="employmentId", default=None)
    """Identifier for employment (id field)"""

    number_of_hours: Optional[float] = FieldInfo(alias="numberOfHours", default=None)
    """Number of work hours for given day"""

    origin: Optional[str] = None
    """Origin, how the work plan day was added"""

    source_system: Optional[str] = FieldInfo(alias="sourceSystem", default=None)
    """Phrase identifying the system which is the source of the work plan"""


class WorkplanListResponse(BaseModel):
    items: Optional[List[Item]] = None
