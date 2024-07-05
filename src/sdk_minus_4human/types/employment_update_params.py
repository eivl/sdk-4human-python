# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EmploymentUpdateParams",
    "AdditionalSalary",
    "Benefit",
    "CustomField",
    "Deduction",
    "EffectiveDates",
    "MainSalary",
    "SubstituteForEmployment",
]


class EmploymentUpdateParams(TypedDict, total=False):
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

    comment: Optional[str]

    cost_place: Annotated[Optional[str], PropertyInfo(alias="costPlace")]

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]

    deductions: Iterable[Deduction]

    effective_dates: Annotated[EffectiveDates, PropertyInfo(alias="effectiveDates")]
    """If effectiveDates are not provided, the changes will be immediate"""

    employee_type_id: Annotated[Optional[str], PropertyInfo(alias="employeeTypeId")]
    """database UUID for employee type"""

    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]
    """If endDate field is provided, the startDate field must also be provided"""

    external_id: Annotated[Optional[str], PropertyInfo(alias="externalId")]

    first_working_day: Annotated[Union[str, datetime, None], PropertyInfo(alias="firstWorkingDay", format="iso8601")]

    fte_factor: Annotated[Optional[float], PropertyInfo(alias="fteFactor")]
    """Decimal precision 0.00001"""

    hr_role_id: Annotated[str, PropertyInfo(alias="hrRoleId")]

    job_id: Annotated[int, PropertyInfo(alias="jobId")]

    last_working_day: Annotated[Union[str, datetime, None], PropertyInfo(alias="lastWorkingDay", format="iso8601")]

    location: Optional[str]

    main_salary: Annotated[MainSalary, PropertyInfo(alias="mainSalary")]

    main_workplace_id: Annotated[Optional[str], PropertyInfo(alias="mainWorkplaceId")]

    manager_id: Annotated[Optional[int], PropertyInfo(alias="managerId")]
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    notice_period: Annotated[Optional[str], PropertyInfo(alias="noticePeriod")]

    number: str

    occupational_code: Annotated[Optional[str], PropertyInfo(alias="occupationalCode")]
    """Use code only without name"""

    org_unit_id: Annotated[int, PropertyInfo(alias="orgUnitId")]
    """database id of employment organisation unit."""

    org_units_with_advanced_access: Annotated[Iterable[int], PropertyInfo(alias="orgUnitsWithAdvancedAccess")]

    overtime_allowance: Annotated[
        Optional[Literal["FIELD_OVERTIME_ALLOWANCE_YES", "FIELD_OVERTIME_ALLOWANCE_NO"]],
        PropertyInfo(alias="overtimeAllowance"),
    ]

    personal_job_description: Annotated[Optional[str], PropertyInfo(alias="personalJobDescription")]

    position_title: Annotated[Optional[str], PropertyInfo(alias="positionTitle")]

    present_fte_factor: Annotated[Optional[float], PropertyInfo(alias="presentFteFactor")]
    """Decimal precision 0.00001"""

    probation_period: Annotated[Optional[str], PropertyInfo(alias="probationPeriod")]

    reason_for_employment: Annotated[Optional[str], PropertyInfo(alias="reasonForEmployment")]

    salary_type: Annotated[Optional[str], PropertyInfo(alias="salaryType")]

    start_date: Annotated[str, PropertyInfo(alias="startDate")]

    substitute_for_employment: Annotated[
        Optional[Iterable[SubstituteForEmployment]], PropertyInfo(alias="substituteForEmployment")
    ]

    working_hours_arrangement: Annotated[Optional[str], PropertyInfo(alias="workingHoursArrangement")]

    working_hours_per_week: Annotated[Optional[float], PropertyInfo(alias="workingHoursPerWeek")]

    work_relation_type: Annotated[Optional[str], PropertyInfo(alias="workRelationType")]


class AdditionalSalary(TypedDict, total=False):
    id: Required[float]

    amount: Required[str]
    """Should be provided only if its individual"""

    currency: Required[Optional[str]]
    """Currency code in ISO 4217 format. Should be provided only if its individual"""

    details: Required[Optional[str]]


class Benefit(TypedDict, total=False):
    id: Required[float]

    amount: Required[str]
    """Should be provided only if its individual"""

    currency: Required[Optional[str]]
    """Currency code in ISO 4217 format. Should be provided only if its individual"""

    details: Required[Optional[str]]


class CustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]
    """UUID of a given custom field"""

    value: Optional[str]
    """
    Custom field value (name in case of structured fields, or free typed value in
    case of free text/date/numeric fields). Field may have various length depends on
    enabled validator up to 1000
    """

    value_id: Annotated[Optional[str], PropertyInfo(alias="valueId")]


class Deduction(TypedDict, total=False):
    id: Required[float]

    amount: Required[str]
    """Should be provided only if its individual."""

    currency: Required[Optional[str]]
    """Currency code in ISO 4217 format. Should be provided only if its individual."""

    details: Required[Optional[str]]


class EffectiveDates(TypedDict, total=False):
    comment: Required[Optional[str]]

    end_validity_date: Required[Annotated[Optional[str], PropertyInfo(alias="endValidityDate")]]

    immediate: Required[Optional[bool]]
    """
    If immediate is true, the changes will be immediate otherwise with planned
    validity date.
    """

    start_validity_date: Required[Annotated[Optional[str], PropertyInfo(alias="startValidityDate")]]


class MainSalary(TypedDict, total=False):
    id: Optional[int]

    amount: Optional[str]

    currency: Optional[str]

    regulation_id: Annotated[Optional[int], PropertyInfo(alias="regulationId")]
    """
    Internal 4human's reference ID that defines a group of versions of one salary
    regulation.
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
