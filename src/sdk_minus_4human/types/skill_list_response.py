# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SkillListResponse",
    "Item",
    "ItemEmployment",
    "ItemFields",
    "ItemFieldsDocument",
    "ItemMetaFields",
    "ItemSkillType",
    "ItemSkillTypeCategory",
    "ItemSkillTypeCategoryIcon",
    "ItemSource",
]


class ItemEmployment(BaseModel):
    id: int

    job_title: str = FieldInfo(alias="jobTitle")


class ItemFieldsDocument(BaseModel):
    id: str

    original_name: str = FieldInfo(alias="originalName")


class ItemFields(BaseModel):
    comment: Optional[str] = None

    completed_date: Optional[str] = FieldInfo(alias="completedDate", default=None)

    country_of_provider: Optional[str] = FieldInfo(alias="countryOfProvider", default=None)

    current_score: Optional[int] = FieldInfo(alias="currentScore", default=None)

    custom_url: Optional[str] = FieldInfo(alias="customUrl", default=None)

    documents: Optional[List[ItemFieldsDocument]] = None

    educational_level: Optional[int] = FieldInfo(alias="educationalLevel", default=None)

    expiry_date: Optional[str] = FieldInfo(alias="expiryDate", default=None)

    internal_external: Optional[int] = FieldInfo(alias="internalExternal", default=None)

    length_of_experience: Optional[str] = FieldInfo(alias="lengthOfExperience", default=None)

    name_of_provider: Optional[str] = FieldInfo(alias="nameOfProvider", default=None)

    oral_language_skill_level: Optional[int] = FieldInfo(alias="oralLanguageSkillLevel", default=None)

    planned_completed_date: Optional[str] = FieldInfo(alias="plannedCompletedDate", default=None)

    provider_place: Optional[str] = FieldInfo(alias="providerPlace", default=None)

    requirement: Optional[int] = None

    skill_title: Optional[str] = FieldInfo(alias="skillTitle", default=None)

    started_date: Optional[str] = FieldInfo(alias="startedDate", default=None)

    target_score: Optional[int] = FieldInfo(alias="targetScore", default=None)

    user_defined_notification_date: Optional[str] = FieldInfo(alias="userDefinedNotificationDate", default=None)

    written_language_skill_level: Optional[int] = FieldInfo(alias="writtenLanguageSkillLevel", default=None)


class ItemMetaFields(BaseModel):
    administrator: Optional[str] = None

    fixed_url: Optional[str] = FieldInfo(alias="fixedUrl", default=None)

    hours_of_duration: Optional[int] = FieldInfo(alias="hoursOfDuration", default=None)

    tags: Optional[List[str]] = None


class ItemSkillTypeCategoryIcon(BaseModel):
    icon_name: str = FieldInfo(alias="iconName")

    prefix: Literal["fas", "fab", "far", "fal", "fad"]


class ItemSkillTypeCategory(BaseModel):
    id: str

    color: Optional[str] = None

    icon: Optional[ItemSkillTypeCategoryIcon] = None

    name: str

    number: str


class ItemSkillType(BaseModel):
    id: str

    approval: bool

    categories: List[ItemSkillTypeCategory]

    description: Optional[str] = None

    name: str

    number: str

    privacy: str


class ItemSource(BaseModel):
    additional_data: Optional[str] = FieldInfo(alias="additionalData", default=None)

    name: Optional[str] = None

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    type: Optional[str] = None


class Item(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")

    created_by: str = FieldInfo(alias="createdBy")

    employment: Optional[ItemEmployment] = None

    fields: ItemFields

    lesson_version_id: Optional[int] = FieldInfo(alias="lessonVersionId", default=None)

    meta_fields: ItemMetaFields = FieldInfo(alias="metaFields")

    privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"]

    program_template_version_id: Optional[int] = FieldInfo(alias="programTemplateVersionId", default=None)

    skill_type: ItemSkillType = FieldInfo(alias="skillType")

    source: ItemSource

    status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved", "notApplicable"]

    updated_at: str = FieldInfo(alias="updatedAt")


class SkillListResponse(BaseModel):
    items: List[Item]

    limit: int

    page: int

    pages: int

    total: int
