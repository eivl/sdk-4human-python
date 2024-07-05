# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "FormerCreateParams",
    "CompanyEmployee",
    "CompanyEmployeeCustomField",
    "CompanyEmployeeFreeEmployer",
    "CompanyEmployeeResidencePermit",
    "CompanyEmployeeWorkPermit",
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
]


class FormerCreateParams(TypedDict, total=False):
    company_employee: Required[Annotated[Optional[CompanyEmployee], PropertyInfo(alias="companyEmployee")]]

    employment: Required[Employment]

    internal_termination_reason_id: Required[Annotated[str, PropertyInfo(alias="internalTerminationReasonId")]]
    """
    Internal termination reason ID, from instance section settings > termination
    reasons
    """

    personal_identification: Required[Annotated[PersonalIdentification, PropertyInfo(alias="personalIdentification")]]

    termination_reason_id: Required[Annotated[str, PropertyInfo(alias="terminationReasonId")]]
    """Termination reason ID, from master management Terminate Reasons (id)"""

    user: Required[User]

    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """


class CompanyEmployeeCustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]
    """UUID of a given custom field"""

    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]
    """UUID of a given custom field value"""

    value: str
    """
    This value will be set only if "valueId" is not provided, contains free text
    value.
    """


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


class EmploymentAdditionalSalary(TypedDict, total=False):
    id: Required[int]

    amount: Optional[str]
    """Should be not provided if additional salary is global."""

    currency: Optional[str]
    """ISO 4217 code. Should be not provided if additional salary is global."""

    details: Optional[str]
    """should be not provided if additional salary is global."""


class EmploymentBenefit(TypedDict, total=False):
    id: Required[int]

    amount: Optional[str]
    """should be not provided if benefit is global."""

    currency: Optional[str]
    """ISO 4217 code. Should be not provided if benefit is global."""

    details: Optional[str]
    """should be not provided if benefit is global."""


class EmploymentCustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]
    """UUID of a given custom field"""

    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]
    """UUID of a given value of a custom field"""


class EmploymentDeduction(TypedDict, total=False):
    id: Required[int]
    """deduction referenceId."""

    amount: Optional[str]
    """should be not provided if deduction is global."""

    currency: Optional[str]
    """ISO 4217 code. Should be not provided if deduction is global"""

    details: Optional[str]
    """should be not provided if deduction is global."""


class EmploymentMainSalary(TypedDict, total=False):
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


class Employment(TypedDict, total=False):
    hr_role_id: Required[Annotated[str, PropertyInfo(alias="hrRoleId")]]

    job_id: Required[Annotated[int, PropertyInfo(alias="jobId")]]

    org_units_with_advanced_access: Required[
        Annotated[Optional[Iterable[int]], PropertyInfo(alias="orgUnitsWithAdvancedAccess")]
    ]
    """list of orgUnits that employment has access to (only for partial access roles)"""

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]

    additional_salaries: Annotated[
        Optional[Iterable[EmploymentAdditionalSalary]], PropertyInfo(alias="additionalSalaries")
    ]

    benefits: Optional[Iterable[EmploymentBenefit]]

    comment: Optional[str]

    cost_place: Annotated[Optional[str], PropertyInfo(alias="costPlace")]

    custom_fields: Annotated[Iterable[EmploymentCustomField], PropertyInfo(alias="customFields")]

    deductions: Optional[Iterable[EmploymentDeduction]]
    """Each deduction may be individual or global.

    Individual means is selected in profile of each employment. Global means values
    are common for all employments.
    """

    email_work: Annotated[Optional[str], PropertyInfo(alias="emailWork")]

    employee_type: Annotated[Optional[str], PropertyInfo(alias="employeeType")]
    """EmployeeType ID"""

    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]

    external_id: Annotated[Optional[str], PropertyInfo(alias="externalId")]

    first_working_day: Annotated[Optional[str], PropertyInfo(alias="firstWorkingDay")]
    """Date of the first working day"""

    fte_factor: Annotated[Optional[float], PropertyInfo(alias="fteFactor")]
    """Decimal precision 0.00001"""

    last_working_day: Annotated[Optional[str], PropertyInfo(alias="lastWorkingDay")]
    """Date of the last working day"""

    location: Optional[str]
    """Id of employment location."""

    main_salary: Annotated[EmploymentMainSalary, PropertyInfo(alias="mainSalary")]

    main_workplace: Annotated[Optional[str], PropertyInfo(alias="mainWorkplace")]

    manager_id: Annotated[Optional[int], PropertyInfo(alias="managerId")]
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    notice_period: Annotated[Optional[str], PropertyInfo(alias="noticePeriod")]

    number: Optional[str]

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
    """ISO 3166-1 alpha-3 code"""

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
    """login method NO_USER means that user should be created without login method.

    And should be selected later.
    """

    office_phone: Annotated[Optional[str], PropertyInfo(alias="officePhone")]

    phone_number_private: Annotated[Optional[str], PropertyInfo(alias="phoneNumberPrivate")]

    phone_number_work: Annotated[Optional[str], PropertyInfo(alias="phoneNumberWork")]
