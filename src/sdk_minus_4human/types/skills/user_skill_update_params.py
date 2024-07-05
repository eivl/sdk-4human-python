# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "UserSkillUpdateParams",
    "Company",
    "CompanyEmployee",
    "InstanceUser",
    "Skill",
    "SkillField",
    "SkillType",
    "SkillTypeCategory",
]


class UserSkillUpdateParams(TypedDict, total=False):
    mode: Literal["READ_ONLY", "EDIT", "CREATE"]
    """
    `CREATE` - create skill type if skill type not exists, otherwise update skill
    type name `EDIT` - update skill type name if skill type exists, otherwise do not
    create skill type `READ_ONLY` - do not create skill type and do not edit skill
    type name
    """

    company: Company

    company_employee: Annotated[CompanyEmployee, PropertyInfo(alias="companyEmployee")]

    instance_user: Annotated[InstanceUser, PropertyInfo(alias="instanceUser")]

    skill: Skill

    skill_type: Annotated[SkillType, PropertyInfo(alias="skillType")]

    skill_type_category: Annotated[SkillTypeCategory, PropertyInfo(alias="skillTypeCategory")]


class Company(TypedDict, total=False):
    organization_number: Annotated[Optional[str], PropertyInfo(alias="organizationNumber")]

    unit_id: Annotated[Optional[str], PropertyInfo(alias="unitId")]


class CompanyEmployee(TypedDict, total=False):
    employee_id: Annotated[Optional[str], PropertyInfo(alias="employeeId")]


class InstanceUser(TypedDict, total=False):
    email: Optional[str]


class SkillField(TypedDict, total=False):
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
            "documents",
            "customUrl",
            "internalExternal",
            "nameOfProvider",
            "countryOfProvider",
            "providerPlace",
            "targetScore",
            "currentScore",
            "expiryDate",
            "plannedCompletedDate",
            "userDefinedNotificationDate",
            "requirement",
            "criticality",
        ]
    ]

    data: Required[object]
    """
    - Allowed values depending on `id` field:
      - `lengthOfExperience`, available suffixes:
        - `y` for year(s)
        - `m` for month(s)
        - `w` for week(s)
        - `d` for day(s)
        - `h` for hour(s)
      - `educationalLevel`:
        - `1` for Primary school
        - `2` for High school
        - `3` for Certificate of apprenticeship
        - `4` for Technical College
        - `5` for Higher apprenticeship
        - `6` for Academic credit
        - `7` for Year study University/College
        - `8` for 2-year University/College
        - `9` for 3-year University/College
        - `10` for Bachelor's degree
        - `11` for Master's degree
        - `12` for Ph.D.
      - `writtenLanguageSkillLevel` and `oralLanguageSkillLevel`:
        - `1` for Elementary proficiency
        - `2` for Limited working proficiency
        - `3` for Professional working proficiency
        - `4` for Full professional proficiency
        - `5` for Native or bilingual proficiency
      - `internalExternal`:
        - `1` for Internal
        - `2` for External
      - `targetScore` and `currentScore`:
        - `1` for Some knowledge
        - `2` for Competent
        - `3` for Highly competent
        - `4` for Expert
      - `requirement`:
        - `1` for Legal requirement
        - `2` for ISO-requirement
        - `3` for Internal requirement
        - `4` for Other
        - `5` for Customer requirement
      - `criticality`:
        - `1` for Optional
        - `2` for Required
        - `3` for Recommended
        - `4` for Critical
    """


class Skill(TypedDict, total=False):
    fields: Iterable[SkillField]

    status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved"]


class SkillType(TypedDict, total=False):
    name: Required[str]

    number: Required[str]


class SkillTypeCategory(TypedDict, total=False):
    name: str
