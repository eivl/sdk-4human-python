# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "EmploymentCreateParams",
    "Employment",
    "EmploymentAdditionalSalary",
    "EmploymentBenefit",
    "EmploymentCustomField",
    "EmploymentDeduction",
    "EmploymentMainSalary",
    "PersonalIdentification",
    "User",
    "UserAddressInfo",
    "UserAddressInfoPostAddress",
    "UserAddressInfoVisitAddress",
    "CompanyEmployee",
    "CompanyEmployeeCustomField",
    "CompanyEmployeeFreeEmployer",
    "CompanyEmployeeResidencePermit",
    "CompanyEmployeeWorkPermit",
    "TaskTemplateChange",
]


class EmploymentCreateParams(TypedDict, total=False):
    employment: Required[Employment]

    personal_identification: Required[Annotated[PersonalIdentification, PropertyInfo(alias="personalIdentification")]]

    user: Required[User]

    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    send_invitation: Annotated[bool, PropertyInfo(alias="sendInvitation")]
    """Determines if invitation email should be sent."""

    company_employee: Annotated[Optional[CompanyEmployee], PropertyInfo(alias="companyEmployee")]

    personal_greetings: Annotated[str, PropertyInfo(alias="personalGreetings")]

    program_template_id: Annotated[Optional[int], PropertyInfo(alias="programTemplateId")]

    reference_date: Annotated[Optional[str], PropertyInfo(alias="referenceDate")]

    task_template_changes: Annotated[Optional[Iterable[TaskTemplateChange]], PropertyInfo(alias="taskTemplateChanges")]


class EmploymentAdditionalSalary(TypedDict, total=False):
    id: Required[int]

    amount: Optional[str]

    currency: Optional[str]
    """Currency code in ISO 4217 format.

    Should be provided only if deduction is individual
    """

    details: Optional[str]
    """Should be provided only if additional salary is individual"""


class EmploymentBenefit(TypedDict, total=False):
    id: Required[int]

    amount: Optional[str]
    """Should be provided only if deduction is individual"""

    currency: Optional[str]
    """Currency code in ISO 4217 format.

    Should be provided only if deduction is individual
    """

    details: Optional[str]
    """Should be provided only if deduction is individual"""


class EmploymentCustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]

    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]


class EmploymentDeduction(TypedDict, total=False):
    id: Required[int]

    amount: Optional[str]
    """Should be provided only if deduction is individual"""

    currency: Optional[str]
    """Currency code in ISO 4217 format.

    Should be provided only if deduction is individual
    """

    details: Optional[str]
    """Should be provided only if deduction is individual"""


class EmploymentMainSalary(TypedDict, total=False):
    id: Optional[int]
    """Internal 4human's ID of individual main salary which can be assigned"""

    amount: Optional[str]
    """The amount associated with the individual main salary."""

    currency: Optional[str]
    """The currency in which the individual main salary is disbursed"""

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
    """The type of the main salary that is assigned to the employment."""


class Employment(TypedDict, total=False):
    hr_role_id: Required[Annotated[str, PropertyInfo(alias="hrRoleId")]]

    job_id: Required[Annotated[int, PropertyInfo(alias="jobId")]]

    org_units_with_advanced_access: Required[
        Annotated[Optional[Iterable[int]], PropertyInfo(alias="orgUnitsWithAdvancedAccess")]
    ]

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]

    id: Optional[int]
    """Internal ID of an employment. If null, new employment will be created."""

    additional_salaries: Annotated[
        Optional[Iterable[EmploymentAdditionalSalary]], PropertyInfo(alias="additionalSalaries")
    ]

    benefits: Optional[Iterable[EmploymentBenefit]]

    comment: Optional[str]

    cost_place: Annotated[Optional[str], PropertyInfo(alias="costPlace")]

    custom_fields: Annotated[Iterable[EmploymentCustomField], PropertyInfo(alias="customFields")]

    deductions: Optional[Iterable[EmploymentDeduction]]

    email_work: Annotated[Optional[str], PropertyInfo(alias="emailWork")]

    employee_type: Annotated[Optional[str], PropertyInfo(alias="employeeType")]
    """EmployeeType ID"""

    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]

    external_id: Annotated[Optional[str], PropertyInfo(alias="externalId")]

    first_working_day: Annotated[Optional[str], PropertyInfo(alias="firstWorkingDay")]

    fte_factor: Annotated[Optional[float], PropertyInfo(alias="fteFactor")]
    """Decimal precision 0.00001"""

    last_working_day: Annotated[Optional[str], PropertyInfo(alias="lastWorkingDay")]

    location: Optional[str]

    main_salary: Annotated[EmploymentMainSalary, PropertyInfo(alias="mainSalary")]

    main_workplace: Annotated[Optional[str], PropertyInfo(alias="mainWorkplace")]

    manager_id: Annotated[Optional[int], PropertyInfo(alias="managerId")]
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    notice_period: Annotated[Optional[str], PropertyInfo(alias="noticePeriod")]

    number: Optional[str]
    """Company number of an employment.

    It's considered as an external ID of an employment.
    """

    occupational_code: Annotated[Optional[str], PropertyInfo(alias="occupationalCode")]
    """Use code only without name"""

    org_unit_id: Annotated[int, PropertyInfo(alias="orgUnitId")]

    overtime_allowance: Annotated[
        Optional[Literal["FIELD_OVERTIME_ALLOWANCE_YES", "FIELD_OVERTIME_ALLOWANCE_NO"]],
        PropertyInfo(alias="overtimeAllowance"),
    ]

    personal_job_description: Annotated[Optional[str], PropertyInfo(alias="personalJobDescription")]

    phone_number_work: Annotated[Optional[str], PropertyInfo(alias="phoneNumberWork")]

    position_title: Annotated[Optional[str], PropertyInfo(alias="positionTitle")]

    present_fte_factor: Annotated[Optional[float], PropertyInfo(alias="presentFteFactor")]
    """Decimal precision 0.00001"""

    probation_period: Annotated[Optional[str], PropertyInfo(alias="probationPeriod")]

    reason_for_employment: Annotated[Optional[str], PropertyInfo(alias="reasonForEmployment")]

    salary_seniority_date: Annotated[Optional[str], PropertyInfo(alias="salarySeniorityDate")]

    salary_type: Annotated[Optional[str], PropertyInfo(alias="salaryType")]

    seniority_date: Annotated[Optional[str], PropertyInfo(alias="seniorityDate")]

    substitute_for_employment: Annotated[Optional[Iterable[int]], PropertyInfo(alias="substituteForEmployment")]

    working_hours_arrangement: Annotated[Optional[str], PropertyInfo(alias="workingHoursArrangement")]

    working_hours_per_week: Annotated[Optional[float], PropertyInfo(alias="workingHoursPerWeek")]

    work_relation_type: Annotated[Optional[str], PropertyInfo(alias="workRelationType")]


class PersonalIdentification(TypedDict, total=False):
    id_country: Annotated[Optional[str], PropertyInfo(alias="idCountry")]

    id_number: Annotated[Optional[str], PropertyInfo(alias="idNumber")]

    id_type: Annotated[Optional[str], PropertyInfo(alias="idType")]

    passport_country: Annotated[Optional[str], PropertyInfo(alias="passportCountry")]

    passport_number: Annotated[Optional[str], PropertyInfo(alias="passportNumber")]


class UserAddressInfoPostAddress(TypedDict, total=False):
    address: Required[Optional[str]]

    city: Required[Optional[str]]

    country: Required[Optional[str]]

    building_entrance: Annotated[Optional[str], PropertyInfo(alias="buildingEntrance")]

    municipality: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]


class UserAddressInfoVisitAddress(TypedDict, total=False):
    address: Required[Optional[str]]

    city: Required[Optional[str]]

    country: Required[Optional[str]]

    building_entrance: Annotated[Optional[str], PropertyInfo(alias="buildingEntrance")]

    municipality: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]


class UserAddressInfo(TypedDict, total=False):
    id: Optional[int]

    name: Optional[str]

    post_address: Annotated[Optional[UserAddressInfoPostAddress], PropertyInfo(alias="postAddress")]

    type: Literal["additional", "primary"]

    visit_address: Annotated[UserAddressInfoVisitAddress, PropertyInfo(alias="visitAddress")]


class User(TypedDict, total=False):
    first_name: Required[Annotated[Optional[str], PropertyInfo(alias="firstName")]]

    last_name: Required[Annotated[Optional[str], PropertyInfo(alias="lastName")]]

    id: Optional[str]
    """Internal ID (UUID) of the user assigned to the employment.

    If NULL - new user will be created.
    """

    account_number: Annotated[Optional[str], PropertyInfo(alias="accountNumber")]

    active_directory_login: Annotated[Optional[str], PropertyInfo(alias="activeDirectoryLogin")]

    address_info: Annotated[Iterable[UserAddressInfo], PropertyInfo(alias="addressInfo")]

    country_of_bank: Annotated[Optional[str], PropertyInfo(alias="countryOfBank")]

    country_of_origin: Annotated[Optional[str], PropertyInfo(alias="countryOfOrigin")]

    date_of_birth: Annotated[Union[str, datetime, None], PropertyInfo(alias="dateOfBirth", format="iso8601")]

    email: Optional[str]

    email_private: Annotated[Optional[str], PropertyInfo(alias="emailPrivate")]

    email_work: Annotated[Optional[str], PropertyInfo(alias="emailWork")]

    gender: Optional[str]

    home_phone: Annotated[Optional[str], PropertyInfo(alias="homePhone")]

    iban: Optional[str]
    """
    If `iban` is provided then also `accountNumber` and `countryOfBank` must be
    provided.
    """

    initials: Optional[str]

    language: Optional[str]

    login_method: Annotated[Literal["AUTH0", "ACTIVE_DIRECTORY", "NO_USER"], PropertyInfo(alias="loginMethod")]

    office_phone: Annotated[Optional[str], PropertyInfo(alias="officePhone")]

    phone_number_private: Annotated[Optional[str], PropertyInfo(alias="phoneNumberPrivate")]

    phone_number_work: Annotated[Optional[str], PropertyInfo(alias="phoneNumberWork")]


class CompanyEmployeeCustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]

    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]


_CompanyEmployeeFreeEmployerReservedKeywords = TypedDict(
    "_CompanyEmployeeFreeEmployerReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class CompanyEmployeeFreeEmployer(_CompanyEmployeeFreeEmployerReservedKeywords, total=False):
    to: Optional[str]


_CompanyEmployeeResidencePermitReservedKeywords = TypedDict(
    "_CompanyEmployeeResidencePermitReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class CompanyEmployeeResidencePermit(_CompanyEmployeeResidencePermitReservedKeywords, total=False):
    to: Optional[str]


_CompanyEmployeeWorkPermitReservedKeywords = TypedDict(
    "_CompanyEmployeeWorkPermitReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class CompanyEmployeeWorkPermit(_CompanyEmployeeWorkPermitReservedKeywords, total=False):
    to: Optional[str]


class CompanyEmployee(TypedDict, total=False):
    custom_fields: Annotated[Iterable[CompanyEmployeeCustomField], PropertyInfo(alias="customFields")]

    employee_id: Annotated[Optional[str], PropertyInfo(alias="employeeId")]
    """External ID of a company employee object. It's called "employee ID" in UI."""

    free_employer: Annotated[Optional[CompanyEmployeeFreeEmployer], PropertyInfo(alias="freeEmployer")]

    main_employer: Annotated[Optional[bool], PropertyInfo(alias="mainEmployer")]

    ready_for_payment: Annotated[bool, PropertyInfo(alias="readyForPayment")]

    residence_permit: Annotated[Optional[CompanyEmployeeResidencePermit], PropertyInfo(alias="residencePermit")]

    resource_type: Annotated[Optional[int], PropertyInfo(alias="resourceType")]

    salary_number: Annotated[Optional[str], PropertyInfo(alias="salaryNumber")]

    self_sickness: Annotated[Optional[str], PropertyInfo(alias="selfSickness")]

    seniority_date: Annotated[Optional[str], PropertyInfo(alias="seniorityDate")]

    termination_seniority_date: Annotated[Optional[str], PropertyInfo(alias="terminationSeniorityDate")]

    work_permit: Annotated[Optional[CompanyEmployeeWorkPermit], PropertyInfo(alias="workPermit")]


class TaskTemplateChange(TypedDict, total=False):
    actor_employment_id: Annotated[int, PropertyInfo(alias="actorEmploymentId")]

    task_template_id: Annotated[int, PropertyInfo(alias="taskTemplateId")]
