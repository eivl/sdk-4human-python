# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ConfigurationListResponse", "MetaField", "Category", "CategoryIcon", "Section", "SectionField"]


class MetaField(BaseModel):
    id: str

    description_translation: str = FieldInfo(alias="descriptionTranslation")

    name_translation: str = FieldInfo(alias="nameTranslation")

    visibility: Literal["none", "visible"]


class CategoryIcon(BaseModel):
    icon_name: str = FieldInfo(alias="iconName")

    prefix: Literal["fas", "fab", "far", "fal", "fad"]


class Category(BaseModel):
    id: str

    color: str

    icon: Optional[CategoryIcon] = None

    name: str

    number: str


class SectionField(BaseModel):
    id: str

    description_translation: str = FieldInfo(alias="descriptionTranslation")

    name_translation: str = FieldInfo(alias="nameTranslation")

    options: Optional[object] = None

    value: Optional[object] = None

    visibility: Literal["none", "visible", "mandatory"]


class Section(BaseModel):
    id: str

    description_translation: str = FieldInfo(alias="descriptionTranslation")

    fields: List[SectionField]

    name_translation: str = FieldInfo(alias="nameTranslation")


class ConfigurationListResponse(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")

    default_skill_status: Literal[
        "toBePlanned", "planned", "started", "toBeApproved", "approved", "expired"
    ] = FieldInfo(alias="defaultSkillStatus")

    description: Optional[str] = None

    meta_fields: List[MetaField] = FieldInfo(alias="metaFields")

    name: str

    number: str

    privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"]

    status: Literal["active", "draft", "archived"]

    categories: Optional[List[Category]] = None

    sections: Optional[List[Section]] = None

    uploaded_at: Optional[str] = FieldInfo(alias="uploadedAt", default=None)
