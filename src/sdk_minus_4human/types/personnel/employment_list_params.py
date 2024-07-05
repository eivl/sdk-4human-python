# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmploymentListParams"]


class EmploymentListParams(TypedDict, total=False):
    employee_id: Annotated[str, PropertyInfo(alias="employeeId")]
    """
    This is an external identifier of a company employee ("employeeId" field in
    company employee object)
    """

    employment_id: Annotated[str, PropertyInfo(alias="employmentId")]
    """
    Employment ID which may be interpreted as internal ID (if external=false) or
    "number" field (if external=true)
    """

    external: bool
    """
    Param determines if "employmentId" is external (field called "number") or
    internal (field called "id")
    """

    limit: int
    """Number of records returned in one request"""

    organisation_number: Annotated[str, PropertyInfo(alias="organisationNumber")]
    """
    ID of the company fetched from [brreg.no](https://www.brreg.no) for norway or
    custom one for other countries
    """

    page: int
    """Number of returned page"""
