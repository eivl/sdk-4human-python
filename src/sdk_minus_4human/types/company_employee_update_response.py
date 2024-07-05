# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CompanyEmployeeUpdateResponse",
    "CustomField",
    "FreeEmployer",
    "IndustryID",
    "IndustryIDFile",
    "IndustryIDIndustryBranchID",
    "PrimaryEmployment",
    "PrimaryLocation",
    "ResidencePermit",
    "ResourceType",
    "WorkPermit",
]


class CustomField(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    field: Optional[str] = None

    field_created_at: Optional[datetime] = FieldInfo(alias="fieldCreatedAt", default=None)

    field_external_id: Optional[str] = FieldInfo(alias="fieldExternalId", default=None)

    field_external_name: Optional[str] = FieldInfo(alias="fieldExternalName", default=None)

    field_id: Optional[str] = FieldInfo(alias="fieldId", default=None)

    field_updated_at: Optional[datetime] = FieldInfo(alias="fieldUpdatedAt", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    value: Optional[str] = None

    value_created_at: Optional[datetime] = FieldInfo(alias="valueCreatedAt", default=None)

    value_external_id: Optional[str] = FieldInfo(alias="valueExternalId", default=None)

    value_external_name: Optional[str] = FieldInfo(alias="valueExternalName", default=None)

    value_id: Optional[str] = FieldInfo(alias="valueId", default=None)

    value_updated_at: Optional[datetime] = FieldInfo(alias="valueUpdatedAt", default=None)


class FreeEmployer(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class IndustryIDFile(BaseModel):
    id: str

    original_name: str = FieldInfo(alias="originalName")


class IndustryIDIndustryBranchID(BaseModel):
    id: Optional[int] = None

    branch_name: Optional[str] = FieldInfo(alias="branchName", default=None)

    name: Optional[str] = None


class IndustryID(BaseModel):
    id: Optional[int] = None

    additional_info: Optional[str] = FieldInfo(alias="additionalInfo", default=None)

    card_number: Optional[str] = FieldInfo(alias="cardNumber", default=None)

    country_issue: Optional[str] = FieldInfo(alias="countryIssue", default=None)

    expiry_date: Optional[str] = FieldInfo(alias="expiryDate", default=None)

    file: Optional[IndustryIDFile] = None

    industry_branch_id: Optional[IndustryIDIndustryBranchID] = FieldInfo(alias="industryBranchId", default=None)

    issue_date: Optional[str] = FieldInfo(alias="issueDate", default=None)


class PrimaryEmployment(BaseModel):
    id: Optional[int] = None

    fte_factor: Optional[float] = FieldInfo(alias="fteFactor", default=None)

    id_ext: Optional[str] = FieldInfo(alias="idExt", default=None)

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)

    org_unit_external_id: Optional[str] = FieldInfo(alias="orgUnitExternalId", default=None)
    """External ID of organization unit (field called "unitId")"""

    org_unit_id: Optional[int] = FieldInfo(alias="orgUnitId", default=None)


class PrimaryLocation(BaseModel):
    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    name: Optional[str] = None


class ResidencePermit(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class ResourceType(BaseModel):
    id: int

    name: str

    type_id: str = FieldInfo(alias="typeId")


class WorkPermit(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class CompanyEmployeeUpdateResponse(BaseModel):
    id: Optional[int] = None

    company_employee_calculated_status: Optional[Literal["active", "inactive", "offboarding", "pending"]] = FieldInfo(
        alias="companyEmployeeCalculatedStatus", default=None
    )

    company_employee_offboarding_date: Optional[str] = FieldInfo(alias="companyEmployeeOffboardingDate", default=None)

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    countries_of_employments: Optional[List[str]] = FieldInfo(alias="countriesOfEmployments", default=None)

    custom_fields: Optional[List[CustomField]] = FieldInfo(alias="customFields", default=None)

    effective_status: Optional[str] = FieldInfo(alias="effectiveStatus", default=None)

    effective_status_date: Optional[str] = FieldInfo(alias="effectiveStatusDate", default=None)

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)

    employment_count: Optional[int] = FieldInfo(alias="employmentCount", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    free_employer: Optional[FreeEmployer] = FieldInfo(alias="freeEmployer", default=None)

    has_main_employer: Optional[bool] = FieldInfo(alias="hasMainEmployer", default=None)

    industry_ids: Optional[List[IndustryID]] = FieldInfo(alias="industryIds", default=None)

    main_employer: Optional[bool] = FieldInfo(alias="mainEmployer", default=None)

    max_date_follow_up_sickness: Optional[str] = FieldInfo(alias="maxDateFollowUpSickness", default=None)

    max_date_sickness_refund: Optional[str] = FieldInfo(alias="maxDateSicknessRefund", default=None)

    next_snapshot_id: Optional[str] = FieldInfo(alias="nextSnapshotId", default=None)

    previous_snapshot_id: Optional[str] = FieldInfo(alias="previousSnapshotId", default=None)

    primary_employment: Optional[PrimaryEmployment] = FieldInfo(alias="primaryEmployment", default=None)

    primary_location: Optional[PrimaryLocation] = FieldInfo(alias="primaryLocation", default=None)

    ready_for_payment: Optional[bool] = FieldInfo(alias="readyForPayment", default=None)
    """Field not available if related employment is in "candidate" status"""

    ready_for_payment_message: Optional[str] = FieldInfo(alias="readyForPaymentMessage", default=None)
    """Field not available if related employment is in "candidate" status"""

    reference_id: Optional[int] = FieldInfo(alias="referenceId", default=None)

    residence_permit: Optional[ResidencePermit] = FieldInfo(alias="residencePermit", default=None)

    resource_type: Optional[ResourceType] = FieldInfo(alias="resourceType", default=None)

    retirement_date: Optional[str] = FieldInfo(alias="retirementDate", default=None)

    salary_number: Optional[str] = FieldInfo(alias="salaryNumber", default=None)

    salary_system_company_id: Optional[str] = FieldInfo(alias="salarySystemCompanyId", default=None)

    self_sickness: Optional[str] = FieldInfo(alias="selfSickness", default=None)

    seniority_date: Optional[str] = FieldInfo(alias="seniorityDate", default=None)

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    status_date: Optional[str] = FieldInfo(alias="statusDate", default=None)

    termination_seniority_date: Optional[str] = FieldInfo(alias="terminationSeniorityDate", default=None)

    total_fte_factor: Optional[float] = FieldInfo(alias="totalFteFactor", default=None)

    user_calculated_status: Optional[
        Literal["active", "invited", "offboarding", "offboardingSoon", "inactive", "expired", "uninvited"]
    ] = FieldInfo(alias="userCalculatedStatus", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    user_status: Optional[Literal["active", "invited"]] = FieldInfo(alias="userStatus", default=None)

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)

    work_permit: Optional[WorkPermit] = FieldInfo(alias="workPermit", default=None)

    work_status: Optional[
        Literal[
            "WORK_STATUS_ACTIVE",
            "WORK_STATUS_RESIGNED",
            "WORK_STATUS_SICK_WITHOUT_PAYMENT",
            "WORK_STATUS_SICK",
            "WORK_STATUS_LEAVE",
            "WORK_STATUS_LEAVE_WITHOUT_PAYMENT",
            "WORK_STATUS_TEMPORARILY_LAID_OFF",
            "WORK_STATUS_TEMPORARILY_ACTIVE",
        ]
    ] = FieldInfo(alias="workStatus", default=None)
