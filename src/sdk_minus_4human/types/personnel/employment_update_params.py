# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "EmploymentUpdateParams",
    "CustomField",
    "EffectiveDates",
    "AdditionalSalary",
    "Benefit",
    "Deduction",
    "MainSalary",
    "SubstituteForEmployment",
]


class EmploymentUpdateParams(TypedDict, total=False):
    comment: Required[Optional[str]]

    cost_place: Required[Annotated[Optional[str], PropertyInfo(alias="costPlace")]]

    custom_fields: Required[Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]]

    effective_dates: Required[Annotated[EffectiveDates, PropertyInfo(alias="effectiveDates")]]

    employee_type_id: Required[Annotated[Optional[str], PropertyInfo(alias="employeeTypeId")]]

    end_date: Required[Annotated[Optional[str], PropertyInfo(alias="endDate")]]

    external_id: Required[Annotated[Optional[str], PropertyInfo(alias="externalId")]]

    first_working_day: Required[
        Annotated[Union[str, datetime, None], PropertyInfo(alias="firstWorkingDay", format="iso8601")]
    ]

    fte_factor: Required[Annotated[Optional[float], PropertyInfo(alias="fteFactor")]]
    """Decimal precision 0.00001"""

    hr_role_id: Required[Annotated[str, PropertyInfo(alias="hrRoleId")]]

    job_id: Required[Annotated[int, PropertyInfo(alias="jobId")]]
    """database internal id of job."""

    last_working_day: Required[
        Annotated[Union[str, datetime, None], PropertyInfo(alias="lastWorkingDay", format="iso8601")]
    ]

    main_workplace_id: Required[Annotated[Optional[str], PropertyInfo(alias="mainWorkplaceId")]]

    manager_id: Required[Annotated[Optional[int], PropertyInfo(alias="managerId")]]
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    notice_period: Required[Annotated[Optional[str], PropertyInfo(alias="noticePeriod")]]
    """
    concatenation of value + measurement unit units are first letter of time range
    (d - days, w -weeks, m - months, y - years) example value `2w` - two weeks
    """

    number: Required[str]
    """
    The employment number serves as an external ID for employment (flag
    isExternal=true) and is used for lookups.
    """

    occupational_code: Required[Annotated[Optional[str], PropertyInfo(alias="occupationalCode")]]
    """Use code only without name"""

    org_unit_id: Required[Annotated[int, PropertyInfo(alias="orgUnitId")]]
    """database id of employment organisation unit."""

    personal_job_description: Required[Annotated[Optional[str], PropertyInfo(alias="personalJobDescription")]]

    position_title: Required[Annotated[Optional[str], PropertyInfo(alias="positionTitle")]]

    present_fte_factor: Required[Annotated[Optional[float], PropertyInfo(alias="presentFteFactor")]]
    """Decimal precision 0.00001"""

    probation_period: Required[Annotated[Optional[str], PropertyInfo(alias="probationPeriod")]]
    """
    concatenation of value + measurement unit units are first letter of time range
    (d - days, w -weeks, m - months, y - years) example value `2w` - two weeks
    """

    salary_seniority_date: Required[
        Annotated[Union[str, datetime, None], PropertyInfo(alias="salarySeniorityDate", format="iso8601")]
    ]

    salary_type: Required[Annotated[Optional[str], PropertyInfo(alias="salaryType")]]

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]

    working_hours_arrangement: Required[Annotated[Optional[str], PropertyInfo(alias="workingHoursArrangement")]]

    working_hours_per_week: Required[Annotated[Optional[float], PropertyInfo(alias="workingHoursPerWeek")]]

    work_relation_type: Required[Annotated[Optional[str], PropertyInfo(alias="workRelationType")]]

    external: bool
    """
    Param determines if "employmentId" is external (field called "number") or
    internal (field called "id")
    """

    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    additional_salaries: Annotated[Iterable[AdditionalSalary], PropertyInfo(alias="additionalSalaries")]

    benefits: Iterable[Benefit]

    deductions: Iterable[Deduction]

    main_salary: Annotated[MainSalary, PropertyInfo(alias="mainSalary")]

    overtime_allowance: Annotated[
        Optional[Literal["FIELD_OVERTIME_ALLOWANCE_YES", "FIELD_OVERTIME_ALLOWANCE_NO"]],
        PropertyInfo(alias="overtimeAllowance"),
    ]

    reason_for_employment: Annotated[Optional[str], PropertyInfo(alias="reasonForEmployment")]

    substitute_for_employment: Annotated[
        Optional[Iterable[SubstituteForEmployment]], PropertyInfo(alias="substituteForEmployment")
    ]


class CustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]
    """UUID of a given custom field"""

    value_id: Required[Annotated[Optional[str], PropertyInfo(alias="valueId")]]
    """UUID of a given value of a custom field"""

    value: Optional[str]
    """
    This value will be set only if "valueId" is not provided, contains free text
    value.
    """


class EffectiveDates(TypedDict, total=False):
    comment: Required[Optional[str]]

    end_validity_date: Required[Annotated[Optional[str], PropertyInfo(alias="endValidityDate")]]

    immediate: Required[Optional[bool]]

    start_validity_date: Required[Annotated[Optional[str], PropertyInfo(alias="startValidityDate")]]


class AdditionalSalary(TypedDict, total=False):
    id: Required[float]

    amount: Required[str]

    currency: Required[Optional[str]]

    details: Required[Optional[str]]


class Benefit(TypedDict, total=False):
    id: Required[float]

    amount: Required[str]

    currency: Required[Optional[str]]

    details: Required[Optional[str]]


class Deduction(TypedDict, total=False):
    id: Required[float]

    amount: Required[str]

    currency: Required[Optional[str]]

    details: Required[Optional[str]]


class MainSalary(TypedDict, total=False):
    id: Optional[int]

    amount: Optional[str]

    currency: Optional[str]

    regulation_id: Annotated[Optional[int], PropertyInfo(alias="regulationId")]
    """
    Internal 4human's reference ID that defines a group of versions of one salary
    regulation
    """

    step_id: Annotated[Optional[int], PropertyInfo(alias="stepId")]
    """
    Internal 4human's reference ID that defines a group of versions of one salary
    regulation step
    """

    type: Optional[Literal["MAIN_SALARY_TYPE_INDIVIDUAL", "MAIN_SALARY_TYPE_REGULATION"]]


class SubstituteForEmployment(TypedDict, total=False):
    id: int

    value: str
