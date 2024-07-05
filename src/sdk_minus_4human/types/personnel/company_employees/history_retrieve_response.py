# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "HistoryRetrieveResponse",
    "Item",
    "ItemCustomField",
    "ItemFreeEmployer",
    "ItemIndustryID",
    "ItemIndustryIDFile",
    "ItemIndustryIDIndustryBranchID",
    "ItemPrimaryEmployment",
    "ItemPrimaryLocation",
    "ItemResidencePermit",
    "ItemResourceType",
    "ItemWorkPermit",
]


class ItemCustomField(BaseModel):
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


class ItemFreeEmployer(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class ItemIndustryIDFile(BaseModel):
    id: str

    original_name: str = FieldInfo(alias="originalName")


class ItemIndustryIDIndustryBranchID(BaseModel):
    id: Optional[int] = None

    branch_name: Optional[str] = FieldInfo(alias="branchName", default=None)

    name: Optional[str] = None


class ItemIndustryID(BaseModel):
    id: Optional[int] = None

    additional_info: Optional[str] = FieldInfo(alias="additionalInfo", default=None)

    card_number: Optional[str] = FieldInfo(alias="cardNumber", default=None)

    country_issue: Optional[str] = FieldInfo(alias="countryIssue", default=None)

    expiry_date: Optional[str] = FieldInfo(alias="expiryDate", default=None)

    file: Optional[ItemIndustryIDFile] = None

    industry_branch_id: Optional[ItemIndustryIDIndustryBranchID] = FieldInfo(alias="industryBranchId", default=None)

    issue_date: Optional[str] = FieldInfo(alias="issueDate", default=None)


class ItemPrimaryEmployment(BaseModel):
    id: Optional[int] = None

    fte_factor: Optional[float] = FieldInfo(alias="fteFactor", default=None)

    id_ext: Optional[str] = FieldInfo(alias="idExt", default=None)

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)

    org_unit_external_id: Optional[str] = FieldInfo(alias="orgUnitExternalId", default=None)
    """External ID of organization unit (field called "unitId")"""

    org_unit_id: Optional[int] = FieldInfo(alias="orgUnitId", default=None)


class ItemPrimaryLocation(BaseModel):
    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    name: Optional[str] = None


class ItemResidencePermit(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class ItemResourceType(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    type_id: Optional[str] = FieldInfo(alias="typeId", default=None)


class ItemWorkPermit(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class Item(BaseModel):
    id: Optional[int] = None

    company_employee_calculated_status: Optional[str] = FieldInfo(alias="companyEmployeeCalculatedStatus", default=None)

    company_employee_offboarding_date: Optional[str] = FieldInfo(alias="companyEmployeeOffboardingDate", default=None)

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    countries_of_employments: Optional[List[str]] = FieldInfo(alias="countriesOfEmployments", default=None)

    custom_fields: Optional[List[ItemCustomField]] = FieldInfo(alias="customFields", default=None)

    effective_status: Optional[str] = FieldInfo(alias="effectiveStatus", default=None)

    effective_status_date: Optional[str] = FieldInfo(alias="effectiveStatusDate", default=None)

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)

    employment_count: Optional[int] = FieldInfo(alias="employmentCount", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    free_employer: Optional[ItemFreeEmployer] = FieldInfo(alias="freeEmployer", default=None)

    has_main_employer: Optional[bool] = FieldInfo(alias="hasMainEmployer", default=None)

    industry_ids: Optional[List[ItemIndustryID]] = FieldInfo(alias="industryIds", default=None)

    main_employer: Optional[bool] = FieldInfo(alias="mainEmployer", default=None)

    max_date_follow_up_sickness: Optional[str] = FieldInfo(alias="maxDateFollowUpSickness", default=None)

    max_date_sickness_refund: Optional[str] = FieldInfo(alias="maxDateSicknessRefund", default=None)

    next_snapshot_id: Optional[str] = FieldInfo(alias="nextSnapshotId", default=None)

    previous_snapshot_id: Optional[str] = FieldInfo(alias="previousSnapshotId", default=None)

    primary_employment: Optional[ItemPrimaryEmployment] = FieldInfo(alias="primaryEmployment", default=None)

    primary_location: Optional[ItemPrimaryLocation] = FieldInfo(alias="primaryLocation", default=None)

    ready_for_payment: Optional[bool] = FieldInfo(alias="readyForPayment", default=None)

    ready_for_payment_message: Optional[str] = FieldInfo(alias="readyForPaymentMessage", default=None)

    reference_id: Optional[int] = FieldInfo(alias="referenceId", default=None)

    residence_permit: Optional[ItemResidencePermit] = FieldInfo(alias="residencePermit", default=None)

    resource_type: Optional[ItemResourceType] = FieldInfo(alias="resourceType", default=None)

    retirement_date: Optional[str] = FieldInfo(alias="retirementDate", default=None)

    salary_number: Optional[str] = FieldInfo(alias="salaryNumber", default=None)

    salary_system_company_id: Optional[str] = FieldInfo(alias="salarySystemCompanyId", default=None)

    self_sickness: Optional[str] = FieldInfo(alias="selfSickness", default=None)

    seniority_date: Optional[str] = FieldInfo(alias="seniorityDate", default=None)

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    status_date: Optional[str] = FieldInfo(alias="statusDate", default=None)

    termination_seniority_date: Optional[str] = FieldInfo(alias="terminationSeniorityDate", default=None)

    total_fte_factor: Optional[float] = FieldInfo(alias="totalFteFactor", default=None)

    user_calculated_status: Optional[str] = FieldInfo(alias="userCalculatedStatus", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    user_status: Optional[str] = FieldInfo(alias="userStatus", default=None)

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)

    work_permit: Optional[ItemWorkPermit] = FieldInfo(alias="workPermit", default=None)

    work_status: Optional[str] = FieldInfo(alias="workStatus", default=None)


class HistoryRetrieveResponse(BaseModel):
    items: List[Item]

    limit: int

    page: int

    pages: int

    total: int
