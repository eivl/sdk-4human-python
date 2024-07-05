# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UserRetrieveResponse", "AccessGroup", "AccessGroupsFromHrRole"]


class AccessGroup(BaseModel):
    id: Optional[str] = None

    title: Optional[str] = None


class AccessGroupsFromHrRole(BaseModel):
    id: Optional[str] = None

    title: Optional[str] = None


class UserRetrieveResponse(BaseModel):
    access_groups: Optional[List[AccessGroup]] = FieldInfo(alias="accessGroups", default=None)

    access_groups_from_hr_roles: Optional[List[AccessGroupsFromHrRole]] = FieldInfo(
        alias="accessGroupsFromHrRoles", default=None
    )

    instance_owner: Optional[bool] = FieldInfo(alias="instanceOwner", default=None)
