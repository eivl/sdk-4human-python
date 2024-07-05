# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SkillRetrieveResponse",
    "Employment",
    "Fields",
    "FieldsDocument",
    "SkillType",
    "SkillTypeCategory",
    "SkillTypeCategoryIcon",
    "Source",
    "MetaFields",
]


class Employment(BaseModel):
    id: int

    job_title: str = FieldInfo(alias="jobTitle")


class FieldsDocument(BaseModel):
    id: str

    original_name: str = FieldInfo(alias="originalName")


class Fields(BaseModel):
    comment: Optional[str] = None

    completed_date: Optional[str] = FieldInfo(alias="completedDate", default=None)

    country_of_provider: Optional[str] = FieldInfo(alias="countryOfProvider", default=None)

    current_score: Optional[int] = FieldInfo(alias="currentScore", default=None)

    custom_url: Optional[str] = FieldInfo(alias="customUrl", default=None)

    documents: Optional[List[FieldsDocument]] = None

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


class SkillTypeCategoryIcon(BaseModel):
    icon_name: str = FieldInfo(alias="iconName")

    prefix: Literal["fas", "fab", "far", "fal", "fad"]


class SkillTypeCategory(BaseModel):
    id: str

    color: Optional[str] = None

    icon: Optional[SkillTypeCategoryIcon] = None

    name: str

    number: str


class SkillType(BaseModel):
    id: str

    approval: bool

    categories: List[SkillTypeCategory]

    description: Optional[str] = None

    name: str

    number: str

    privacy: str


class Source(BaseModel):
    additional_data: Optional[str] = FieldInfo(alias="additionalData", default=None)

    name: Optional[str] = None

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    type: Optional[str] = None


class MetaFields(BaseModel):
    administrator: Optional[str] = None

    fixed_url: Optional[str] = FieldInfo(alias="fixedUrl", default=None)

    hours_of_duration: Optional[int] = FieldInfo(alias="hoursOfDuration", default=None)

    tags: Optional[List[str]] = None


class SkillRetrieveResponse(BaseModel):
    id: str

    created_at: str = FieldInfo(alias="createdAt")

    created_by: str = FieldInfo(alias="createdBy")

    employment: Optional[Employment] = None

    fields: Fields

    lesson_version_id: Optional[int] = FieldInfo(alias="lessonVersionId", default=None)

    privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"]

    program_template_version_id: Optional[int] = FieldInfo(alias="programTemplateVersionId", default=None)

    skill_type: SkillType = FieldInfo(alias="skillType")

    source: Source

    status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved", "notApplicable"]

    updated_at: str = FieldInfo(alias="updatedAt")

    meta_fields: Optional[MetaFields] = FieldInfo(alias="metaFields", default=None)
