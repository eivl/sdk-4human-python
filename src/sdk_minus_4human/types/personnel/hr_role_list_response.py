# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HrRoleListResponse", "Item", "ItemAccessLevel", "ItemExternalMapping"]


class ItemAccessLevel(BaseModel):
    id: str

    levels: Optional[List[str]] = None


class ItemExternalMapping(BaseModel):
    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    system_name: Optional[str] = FieldInfo(alias="systemName", default=None)


class Item(BaseModel):
    id: Optional[str] = None

    access_group: Optional[List[str]] = FieldInfo(alias="accessGroup", default=None)

    access_level: Optional[ItemAccessLevel] = FieldInfo(alias="accessLevel", default=None)

    evolution_role_codes: Optional[List[str]] = FieldInfo(alias="evolutionRoleCodes", default=None)

    external_mappings: Optional[List[ItemExternalMapping]] = FieldInfo(alias="externalMappings", default=None)

    internal: Optional[bool] = None

    mapping_enabled: Optional[bool] = FieldInfo(alias="mappingEnabled", default=None)

    title: Optional[str] = None


class HrRoleListResponse(BaseModel):
    items: Optional[List[Item]] = None
