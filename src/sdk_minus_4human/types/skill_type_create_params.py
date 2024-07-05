# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SkillTypeCreateParams", "MetaField", "Section", "SectionField"]


class SkillTypeCreateParams(TypedDict, total=False):
    categories: Required[List[str]]

    cv_categories: Required[Annotated[List[str], PropertyInfo(alias="cvCategories")]]

    default_skill_status: Required[
        Annotated[
            Literal["toBePlanned", "planned", "started", "toBeApproved", "approved"],
            PropertyInfo(alias="defaultSkillStatus"),
        ]
    ]

    description: Required[Optional[str]]

    meta_fields: Required[Annotated[Iterable[MetaField], PropertyInfo(alias="metaFields")]]

    name: Required[str]

    number: Required[str]

    privacy: Required[Literal["public", "myOrganization", "myManagers", "onlyMe"]]

    sections: Required[Iterable[Section]]


class MetaField(TypedDict, total=False):
    id: Required[Literal["administrator", "fixedUrl", "hoursOfDuration", "tags"]]

    value: Required[Union[int, str, List[str], None]]

    visibility: Required[Literal["none", "visible"]]


class SectionField(TypedDict, total=False):
    id: Required[
        Literal[
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
    ]

    visibility: Required[Literal["none", "visible", "mandatory"]]

    value: Union[int, str, Iterable[object], object, None]


class Section(TypedDict, total=False):
    id: Required[Literal["details", "skillProvider", "expiryPlanningAndScore", "attachmentsAndLinks"]]

    fields: Required[Iterable[SectionField]]
