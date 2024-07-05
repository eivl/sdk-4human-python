# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    filter: Literal["all", "offboarding", "invited", "uninvited", "expired", "inactive"]
    """filter users by given status"""

    limit: int
    """Number of records returned in one request"""

    org_units: Annotated[str, PropertyInfo(alias="orgUnits")]
    """comma separated list of orgUnits"""

    page: int
    """Number of returned page"""

    query: str
    """filter users by name, work email, job type"""
