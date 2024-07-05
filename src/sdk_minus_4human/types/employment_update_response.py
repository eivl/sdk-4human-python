# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EmploymentUpdateResponse",
    "AdditionalSalary",
    "Benefit",
    "Company",
    "CompanyLocation",
    "CompanyLocationVisitAddress",
    "CustomField",
    "Deduction",
    "DocumentStatus",
    "EmployeeType",
    "HrRole",
    "Job",
    "JobOccupationalCode",
    "MainSalary",
    "Manager",
    "OccupationalCode",
    "OrgUnit",
    "SalaryRate",
    "SubstituteForEmployment",
    "User",
]


class AdditionalSalary(BaseModel):
    id: int

    amount: Optional[str] = None

    currency: Optional[str] = None

    has_changed: bool = FieldInfo(alias="hasChanged")

    has_changes_during_snapshot: bool = FieldInfo(alias="hasChangesDuringSnapshot")

    name: str

    period: str

    type: str

    value_type: str = FieldInfo(alias="valueType")

    details: Optional[str] = None


class Benefit(BaseModel):
    id: int

    amount: Optional[str] = None

    currency: Optional[str] = None

    has_changed: bool = FieldInfo(alias="hasChanged")

    has_changes_during_snapshot: bool = FieldInfo(alias="hasChangesDuringSnapshot")

    name: str

    period: str

    type: str

    value_type: str = FieldInfo(alias="valueType")

    details: Optional[str] = None


class Company(BaseModel):
    id: Optional[int] = None
    """Internal ID of the company"""

    name: Optional[str] = None
    """Name of the company"""


class CompanyLocationVisitAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class CompanyLocation(BaseModel):
    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    name: Optional[str] = None

    visit_address: Optional[CompanyLocationVisitAddress] = FieldInfo(alias="visitAddress", default=None)


class CustomField(BaseModel):
    field: Optional[str] = None
    """Custom field name"""

    field_external_id: Optional[str] = FieldInfo(alias="fieldExternalId", default=None)

    field_external_name: Optional[str] = FieldInfo(alias="fieldExternalName", default=None)

    field_id: Optional[str] = FieldInfo(alias="fieldId", default=None)
    """UUID of a given custom field"""

    field_template_external_id: Optional[str] = FieldInfo(alias="fieldTemplateExternalId", default=None)

    field_template_external_name: Optional[str] = FieldInfo(alias="fieldTemplateExternalName", default=None)

    field_template_id: Optional[str] = FieldInfo(alias="fieldTemplateId", default=None)

    field_template_name: Optional[str] = FieldInfo(alias="fieldTemplateName", default=None)

    has_custom_fields: Optional[bool] = FieldInfo(alias="hasCustomFields", default=None)
    """Indicator if Employment has custom fields assigned directly.

    If they are inherited flag equals false
    """

    value: Optional[str] = None
    """
    Custom field value (name in case of structured fields, or free typed value in
    case of text/date/numeric fields). Field may have various length depends on
    enabled validator up to 1000.
    """

    value_external_id: Optional[str] = FieldInfo(alias="valueExternalId", default=None)

    value_external_name: Optional[str] = FieldInfo(alias="valueExternalName", default=None)

    value_id: Optional[str] = FieldInfo(alias="valueId", default=None)
    """UUID of a given value of a custom field"""


class Deduction(BaseModel):
    id: int

    amount: Optional[str] = None

    currency: Optional[str] = None

    has_changed: bool = FieldInfo(alias="hasChanged")

    has_changes_during_snapshot: bool = FieldInfo(alias="hasChangesDuringSnapshot")

    name: str

    period: str

    type: str

    value_type: str = FieldInfo(alias="valueType")

    details: Optional[str] = None


class DocumentStatus(BaseModel):
    status: Optional[
        Literal[
            "COVERED_BY_EXISTING_DOCUMENT",
            "LEAVE_IT_FOR_LATER",
            "WORK_AGREEMENT_COVERED_BY_EXISTING_DOCUMENT",
            "WORK_AGREEMENT_LEAVE_IT_FOR_LATER",
            "CANDIDATE_EXISTING_AGREEMENT",
            "CANDIDATE_OTHER_DOCUMENTS",
            "CANDIDATE_WITHOUT_AGREEMENT",
            "DOCUMENT_STATUS_IN_PROGRESS",
            "DOCUMENT_STATUS_FOR_SIGNING",
            "DOCUMENT_STATUS_CANDIDATE_APPROVAL",
            "CANDIDATE_REJECT",
        ]
    ] = None

    status_date: Optional[datetime] = FieldInfo(alias="statusDate", default=None)


class EmployeeType(BaseModel):
    id: str

    employee_type: str = FieldInfo(alias="employeeType")

    employment_type: str = FieldInfo(alias="employmentType")

    employment_type_id: str = FieldInfo(alias="employmentTypeId")

    status: Literal["active", "archived"]

    type_id: str = FieldInfo(alias="typeId")


class HrRole(BaseModel):
    id: str

    title: Optional[str] = None


class JobOccupationalCode(BaseModel):
    code: str

    country: str

    name: str


class Job(BaseModel):
    id: int

    created_at: str = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    evolution_id: Optional[int] = FieldInfo(alias="evolutionId", default=None)

    number: str

    occupational_codes: List[JobOccupationalCode] = FieldInfo(alias="occupationalCodes")

    status: str

    title: str


class MainSalary(BaseModel):
    id: Optional[int] = None
    """Internal 4human's ID of individual main salary which can be assigned"""

    amount: Optional[str] = None
    """The amount associated with the individual main salary."""

    currency: Optional[str] = None
    """The currency in which the individual main salary is disbursed i.g NOK, EUR, USD"""

    name: Optional[str] = None
    """The name designated to the specific individual main salary"""

    period: Optional[
        Literal[
            "INDIVIDUAL_MAIN_SALARY_PERIOD_HOUR",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_WEEK",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_MONTH",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_YEAR",
        ]
    ] = None
    """The frequency at which the main salary is disbursed."""

    regulation_currency: Optional[str] = FieldInfo(alias="regulationCurrency", default=None)
    """The currency used for the salary regulation"""

    regulation_external_id: Optional[str] = FieldInfo(alias="regulationExternalId", default=None)
    """External ID of salary regulation"""

    regulation_internal_id: Optional[str] = FieldInfo(alias="regulationInternalId", default=None)
    """Internal ID of salary regulation"""

    regulation_name: Optional[str] = FieldInfo(alias="regulationName", default=None)
    """Name of the salary regulation which is assigned to employment"""

    regulation_period: Optional[Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]] = FieldInfo(
        alias="regulationPeriod", default=None
    )
    """The payment frequency set for the salary regulation"""

    regulation_reference_id: Optional[int] = FieldInfo(alias="regulationReferenceId", default=None)
    """
    Internal 4human's reference ID that defines a group of versions of one salary
    regulation
    """

    step_amount: Optional[str] = FieldInfo(alias="stepAmount", default=None)
    """Assigned amount for the salary regulation step"""

    step_external_id: Optional[str] = FieldInfo(alias="stepExternalId", default=None)
    """Assigned externalId for salary regulation step"""

    step_name: Optional[str] = FieldInfo(alias="stepName", default=None)
    """The name given to the specific salary regulation step"""

    step_reference_id: Optional[int] = FieldInfo(alias="stepReferenceId", default=None)
    """
    Internal 4human's reference ID that defines a group of versions of one salary
    regulation step
    """

    step_symbol: Optional[str] = FieldInfo(alias="stepSymbol", default=None)
    """The symbol representing assigned salary regulation step"""

    type: Optional[Literal["MAIN_SALARY_TYPE_INDIVIDUAL", "MAIN_SALARY_TYPE_REGULATION"]] = None
    """The type of the main salary that is assigned to the employment."""


class Manager(BaseModel):
    id: Optional[int] = None
    """
    ID of the manager (internal ID of the employment who is the manager of the given
    employment)
    """

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """Employee ID of a company employee of a manager"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Employment External ID of a manager (additional external ID of a manager)"""

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)

    name: Optional[str] = None
    """First and last name of a manager of a given employment"""

    number: Optional[str] = None
    """Employment Number of a manager (external ID of a manager)"""

    photo: Optional[str] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """User ID (UUID) of a manager"""


class OccupationalCode(BaseModel):
    code: str

    country: str

    name: str


class OrgUnit(BaseModel):
    id: int

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID of organization unit (field called "unitId")"""

    name: Optional[str] = None


class SalaryRate(BaseModel):
    calculated_monthly_rate: Optional[str] = FieldInfo(alias="calculatedMonthlyRate", default=None)

    calculated_yearly_rate: Optional[str] = FieldInfo(alias="calculatedYearlyRate", default=None)

    hourly_rate: Optional[str] = FieldInfo(alias="hourlyRate", default=None)

    monthly_rate: Optional[str] = FieldInfo(alias="monthlyRate", default=None)

    yearly_rate: Optional[str] = FieldInfo(alias="yearlyRate", default=None)


class SubstituteForEmployment(BaseModel):
    id: Optional[int] = None

    value: Optional[str] = None


class User(BaseModel):
    id: Optional[str] = None
    """Internal ID (UUID) of the user assigned to a given employment"""

    name: Optional[str] = None
    """First and last name of the user assigned to the employment"""

    photo: Optional[str] = None


class EmploymentUpdateResponse(BaseModel):
    id: int
    """Internal ID of an employment"""

    additional_salaries: Optional[List[AdditionalSalary]] = FieldInfo(alias="additionalSalaries", default=None)

    benefits: Optional[List[Benefit]] = None

    comment: Optional[str] = None

    company: Optional[Company] = None
    """Company in which the employment is registered (org unit with flag "company")"""

    company_location: Optional[CompanyLocation] = FieldInfo(alias="companyLocation", default=None)

    cost_place: Optional[str] = FieldInfo(alias="costPlace", default=None)

    country: Optional[str] = None

    created_at: str = FieldInfo(alias="createdAt")
    """Date of employment creation"""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")

    deductions: Optional[List[Deduction]] = None

    document_status: Optional[DocumentStatus] = FieldInfo(alias="documentStatus", default=None)

    effective_status: Literal[
        "past",
        "current",
        "future",
        "replaced",
        "canceled",
        "effected",
        "approved",
        "for_approval",
        "for_confirmation",
        "rejected",
    ] = FieldInfo(alias="effectiveStatus")
    """Defines the record's status.

    It may be past, current (current version) or future (or some other helper
    statuses). Usually - when consuming API - records with current status are valid.
    """

    effective_status_date: Optional[str] = FieldInfo(alias="effectiveStatusDate", default=None)
    """
    Start date from which the given record is valid (may be null if no changes have
    been yet registered)
    """

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """This is an external identifier of company-employee (employeeId field)"""

    employee_type: Optional[EmployeeType] = FieldInfo(alias="employeeType", default=None)

    employment_calculated_status: Optional[
        Literal["vacant", "active", "terminating", "former", "dueForTermination", "pastDueTermination", "pending"]
    ] = FieldInfo(alias="employmentCalculatedStatus", default=None)

    employment_status: Optional[str] = FieldInfo(alias="employmentStatus", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Additional external ID of the employment"""

    first_working_day: Optional[str] = FieldInfo(alias="firstWorkingDay", default=None)

    fte_factor: Optional[float] = FieldInfo(alias="fteFactor", default=None)
    """Decimal precision 0.00001"""

    has_employment_location: bool = FieldInfo(alias="hasEmploymentLocation")

    has_employment_manager: bool = FieldInfo(alias="hasEmploymentManager")

    has_occupational_code: bool = FieldInfo(alias="hasOccupationalCode")

    hr_role: HrRole = FieldInfo(alias="hrRole")

    is_last_employment: bool = FieldInfo(alias="isLastEmployment")

    is_primary_employment: bool = FieldInfo(alias="isPrimaryEmployment")

    job: Job

    last_working_day: Optional[str] = FieldInfo(alias="lastWorkingDay", default=None)

    main_salary: Optional[MainSalary] = FieldInfo(alias="mainSalary", default=None)

    main_workplace_id: Optional[str] = FieldInfo(alias="mainWorkplaceId", default=None)
    """ID of main workplace"""

    manager: Manager

    manager_for_unit: Optional[str] = FieldInfo(alias="managerForUnit", default=None)

    next_snapshot_id: Optional[str] = FieldInfo(alias="nextSnapshotId", default=None)

    notice_period: Optional[str] = FieldInfo(alias="noticePeriod", default=None)
    """
    concatenation of value + measurement unit units are first letter of time range
    (d - days, w -weeks, m - months, y - years) example value `2w` - two weeks
    """

    number: str
    """Company number of an employment.

    It's considered as an external ID of a given employment.
    """

    occupational_code: Optional[OccupationalCode] = FieldInfo(alias="occupationalCode", default=None)

    org_unit: Optional[OrgUnit] = FieldInfo(alias="orgUnit", default=None)

    overtime_allowance: Optional[Literal["FIELD_OVERTIME_ALLOWANCE_YES", "FIELD_OVERTIME_ALLOWANCE_NO"]] = FieldInfo(
        alias="overtimeAllowance", default=None
    )

    personal_job_description: Optional[str] = FieldInfo(alias="personalJobDescription", default=None)

    position_title: Optional[str] = FieldInfo(alias="positionTitle", default=None)

    present_fte_factor: Optional[float] = FieldInfo(alias="presentFteFactor", default=None)
    """Decimal precision 0.00001"""

    previous_snapshot_id: Optional[str] = FieldInfo(alias="previousSnapshotId", default=None)

    probation_period: Optional[str] = FieldInfo(alias="probationPeriod", default=None)
    """
    concatenation of value + measurement unit units are first letter of time range
    (d - days, w -weeks, m - months, y - years) example value `2w` - two weeks
    """

    reason_for_employment: Optional[str] = FieldInfo(alias="reasonForEmployment", default=None)

    reference_id: Optional[int] = FieldInfo(alias="referenceId", default=None)
    """Reference ID of a given record.

    For past/future records it is the ID of the current record (currently valid)
    """

    salary_rate: Optional[SalaryRate] = FieldInfo(alias="salaryRate", default=None)

    salary_seniority_date: Optional[str] = FieldInfo(alias="salarySeniorityDate", default=None)

    salary_system_company_id: Optional[str] = FieldInfo(alias="salarySystemCompanyId", default=None)

    salary_type: Optional[
        Literal["piecework_remuneration", "fixed_salary", "fees", "commission_percentage", "hourly_wage"]
    ] = FieldInfo(alias="salaryType", default=None)

    seniority_date: Optional[str] = FieldInfo(alias="seniorityDate", default=None)

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    status_date: Optional[str] = FieldInfo(alias="statusDate", default=None)

    substitute_for_employment: Optional[List[SubstituteForEmployment]] = FieldInfo(
        alias="substituteForEmployment", default=None
    )

    terminate_reason: Optional[str] = FieldInfo(alias="terminateReason", default=None)

    termination_or_offboarding_date: Optional[str] = FieldInfo(alias="terminationOrOffboardingDate", default=None)
    """Date of termination of the employment"""

    user: Optional[User] = None

    uuid: str
    """UUID identifier of a given employment"""

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)
    """Date from which the given record is valid (refers to effective dates)"""

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)
    """Date to which the given record is valid (refers to effective dates)"""

    working_hours_arrangement: Optional[str] = FieldInfo(alias="workingHoursArrangement", default=None)

    working_hours_per_week: Optional[float] = FieldInfo(alias="workingHoursPerWeek", default=None)

    work_relation_type: Optional[str] = FieldInfo(alias="workRelationType", default=None)
