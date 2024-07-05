# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JobUpdateResponse", "ACL", "OccupationalCode"]


class ACL(BaseModel):
    setting: Literal["allow", "deny"]
    """Setting that says whether the permission is granted or rejected"""

    subject_id: str = FieldInfo(alias="subjectId")
    """Internal 4human's ID of the object to which the permission is set"""

    subject_type: Literal["org_unit"] = FieldInfo(alias="subjectType")
    """Subject type of the permission"""


class OccupationalCode(BaseModel):
    code: str
    """Occupational numerical code, usually 7-digits long"""

    country: str
    """Country code, usually "NOR" for Norwegian occupational code"""

    name: Optional[str] = None
    """
    This field is always `null` for this endpoint, use GET list endpoint to check
    the correct occupational code name
    """


class JobUpdateResponse(BaseModel):
    id: int
    """Not editable, unique internal 4human's ID, not visible in system interface"""

    acl: List[ACL]
    """Permissions definition"""

    category_name: Optional[str] = FieldInfo(alias="categoryName", default=None)
    """Name of the job category to which the job is assigned"""

    created_at: str = FieldInfo(alias="createdAt")
    """Date of job creation"""

    description: Optional[str] = None
    """Additional job description"""

    number: str
    """Editable, unique external ID, allowing to store the ID of the client's system"""

    occupational_codes: List[OccupationalCode] = FieldInfo(alias="occupationalCodes")
    """The list of occupational codes.

    Occupational code consists of country code, numerical code and name
    """

    status: Literal["active", "inactive"]
    """Job status"""

    title: str
    """Job name"""
