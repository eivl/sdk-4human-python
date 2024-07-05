# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SkillTypeStatusResponse", "Item", "ItemCategory", "ItemCategoryIcon"]


class ItemCategoryIcon(BaseModel):
    icon_name: str = FieldInfo(alias="iconName")

    prefix: Literal["fas", "fab", "far", "fal", "fad"]


class ItemCategory(BaseModel):
    id: str

    color: Optional[str] = None

    icon: Optional[ItemCategoryIcon] = None

    name: str

    number: str


class Item(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")

    default_skill_status: Literal[
        "toBePlanned", "planned", "started", "toBeApproved", "approved", "expired"
    ] = FieldInfo(alias="defaultSkillStatus")

    description: Optional[str] = None

    name: str

    number: str

    privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"]

    status: Literal["active", "draft", "archived"]

    tags: Optional[List[str]] = None

    updated_at: str = FieldInfo(alias="updatedAt")

    categories: Optional[List[ItemCategory]] = None

    cv_templates: Optional[List[str]] = FieldInfo(alias="CVTemplates", default=None)

    path_categories: Optional[List[List[str]]] = FieldInfo(alias="pathCategories", default=None)


class SkillTypeStatusResponse(BaseModel):
    items: List[Item]

    limit: int

    page: int

    pages: int

    total: int
