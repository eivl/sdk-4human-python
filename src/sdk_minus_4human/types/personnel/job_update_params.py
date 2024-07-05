# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobUpdateParams", "ACL", "OccupationalCode"]


class JobUpdateParams(TypedDict, total=False):
    acl: Required[Iterable[ACL]]
    """Permissions definition"""

    number: Required[str]
    """Editable, unique external ID, allowing to store the ID of the client's system"""

    title: Required[str]
    """Job name"""

    external: bool
    """
    Param determines if `jobId` parameter is provided as external ID (field called
    `number`) or internal 4human's ID (field called `id`)
    """

    category_id: Annotated[Optional[str], PropertyInfo(alias="categoryId")]
    """Internal 4human's ID of job category to which job will be assigned"""

    description: Optional[str]
    """Additional job description"""

    occupational_codes: Annotated[Iterable[OccupationalCode], PropertyInfo(alias="occupationalCodes")]
    """The list of occupational codes.

    Occupational code consists of country code, numerical code and name. In this
    field only country and code are necessary, the name will be automatically fetch
    from occupational code catalog available under this link
    <a href="https://data.ssb.no/api/klass/v1/versions/683" target="_blank">https://data.ssb.no/api/klass/v1/versions/683</a>
    """

    status: Literal["active", "inactive"]
    """Job status"""


class ACL(TypedDict, total=False):
    setting: Required[Literal["allow", "deny"]]
    """Setting that says whether the permission is granted or rejected"""

    subject_id: Required[Annotated[str, PropertyInfo(alias="subjectId")]]
    """Internal 4human's ID of the object to which the permission is set"""

    subject_type: Required[Annotated[Literal["org_unit"], PropertyInfo(alias="subjectType")]]
    """Subject type of the permission"""


class OccupationalCode(TypedDict, total=False):
    code: Required[str]
    """
    Occupational numerical code (usually 7-digits long) without the occupational
    code name
    """

    country: Required[str]
    """Country code, usually "NOR" for Norwegian occupational code"""
