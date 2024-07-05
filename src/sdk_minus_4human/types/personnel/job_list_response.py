# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JobListResponse", "Item", "ItemOccupationalCode"]


class ItemOccupationalCode(BaseModel):
    code: str
    """Occupational numerical code, usually 7-digits long"""

    country: str
    """Country code, usually "NOR" for Norwegian occupational code"""

    name: Optional[str] = None
    """Occupational code name"""


class Item(BaseModel):
    id: int
    """Not editable, unique internal 4human's ID, not visible in system interface"""

    category_name: Optional[str] = FieldInfo(alias="categoryName", default=None)
    """Name of the job category to which the job is assigned"""

    created_at: str = FieldInfo(alias="createdAt")
    """Date of job creation"""

    description: Optional[str] = None
    """Additional job description"""

    number: str
    """Editable, unique external ID, allowing to store the ID of the client's system"""

    occupational_codes: List[ItemOccupationalCode] = FieldInfo(alias="occupationalCodes")
    """The list of occupational codes.

    Occupational code consists of country code, numerical code and name
    """

    status: Literal["active", "inactive"]
    """Job status"""

    title: str
    """Job name"""


class JobListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
