# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SkillTypeRetrieveResponse",
    "Category",
    "CategoryIcon",
    "CvCategory",
    "CvCategoryIcon",
    "MetaField",
    "Section",
    "SectionField",
]


class CategoryIcon(BaseModel):
    icon_name: str = FieldInfo(alias="iconName")

    prefix: Literal["fas", "fab", "far", "fal", "fad"]


class Category(BaseModel):
    id: str

    color: Optional[str] = None

    icon: Optional[CategoryIcon] = None

    name: str

    number: str


class CvCategoryIcon(BaseModel):
    icon_name: str = FieldInfo(alias="iconName")

    prefix: Literal["fas", "fab", "far", "fal", "fad"]


class CvCategory(BaseModel):
    id: str

    color: Optional[str] = None

    icon: Optional[CvCategoryIcon] = None

    name: str


class MetaField(BaseModel):
    id: Literal["administrator", "fixedUrl", "hoursOfDuration", "tags"]

    description_translation: str = FieldInfo(alias="descriptionTranslation")

    name_translation: str = FieldInfo(alias="nameTranslation")

    options: Optional[object] = None

    value: Optional[object] = None

    visibility: Literal["none", "visible"]


class SectionField(BaseModel):
    id: Literal[
        "skillTitle",
        "startedDate",
        "completedDate",
        "comment",
        "lengthOfExperience",
        "educationalLevel",
        "writtenLanguageSkillLevel",
        "oralLanguageSkillLevel",
        "internalExternal",
        "nameOfProvider",
        "countryOfProvider",
        "providerPlace",
        "targetScore",
        "currentScore",
        "expiryDate",
        "plannedCompletedDate",
        "requirement",
        "criticality",
        "userDefinedNotificationDate",
        "documents",
        "customUrl",
    ]

    description_translation: str = FieldInfo(alias="descriptionTranslation")

    name_translation: str = FieldInfo(alias="nameTranslation")

    options: Optional[object] = None

    value: Optional[object] = None

    visibility: Literal["none", "visible", "mandatory"]


class Section(BaseModel):
    id: Literal["details", "skillProvider", "expiryPlanningAndScore", "attachmentsAndLinks"]

    description_translation: str = FieldInfo(alias="descriptionTranslation")

    fields: List[SectionField]

    name_translation: str = FieldInfo(alias="nameTranslation")


class SkillTypeRetrieveResponse(BaseModel):
    id: str

    categories: List[Category]

    created_at: str = FieldInfo(alias="createdAt")

    cv_categories: List[CvCategory] = FieldInfo(alias="cvCategories")

    default_skill_status: Literal[
        "toBePlanned", "planned", "started", "toBeApproved", "approved", "expired"
    ] = FieldInfo(alias="defaultSkillStatus")

    description: Optional[str] = None

    meta_fields: List[MetaField] = FieldInfo(alias="metaFields")

    name: str

    number: str

    privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"]

    sections: List[Section]

    status: Literal["active", "draft", "archived"]

    updated_at: str = FieldInfo(alias="updatedAt")
