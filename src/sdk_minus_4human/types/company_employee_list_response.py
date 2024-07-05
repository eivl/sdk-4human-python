# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CompanyEmployeeListResponse",
    "Item",
    "ItemFreeEmployer",
    "ItemPrimaryEmployment",
    "ItemPrimaryLocation",
    "ItemResidencePermit",
    "ItemResourceType",
    "ItemWorkPermit",
]


class ItemFreeEmployer(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class ItemPrimaryEmployment(BaseModel):
    id: Optional[int] = None

    fte_factor: Optional[float] = FieldInfo(alias="fteFactor", default=None)

    id_ext: Optional[str] = FieldInfo(alias="idExt", default=None)

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
    id: int

    name: str

    type_id: str = FieldInfo(alias="typeId")


class ItemWorkPermit(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class Item(BaseModel):
    id: Optional[int] = None

    company_employee_calculated_status: Optional[str] = FieldInfo(alias="companyEmployeeCalculatedStatus", default=None)

    company_employee_offboarding_date: Optional[str] = FieldInfo(alias="companyEmployeeOffboardingDate", default=None)

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    countries_of_employments: Optional[List[str]] = FieldInfo(alias="countriesOfEmployments", default=None)

    effective_status: Optional[
        Literal[
            "past",
            "current",
            "current_copy",
            "future",
            "replaced",
            "canceled",
            "effected",
            "approved",
            "for_approval",
            "for_confirmation",
            "rejected",
            "confirmed",
        ]
    ] = FieldInfo(alias="effectiveStatus", default=None)

    effective_status_date: Optional[str] = FieldInfo(alias="effectiveStatusDate", default=None)

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)

    employment_count: Optional[int] = FieldInfo(alias="employmentCount", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    free_employer: Optional[ItemFreeEmployer] = FieldInfo(alias="freeEmployer", default=None)

    has_main_employer: Optional[bool] = FieldInfo(alias="hasMainEmployer", default=None)

    main_employer: Optional[bool] = FieldInfo(alias="mainEmployer", default=None)

    max_date_follow_up_sickness: Optional[str] = FieldInfo(alias="maxDateFollowUpSickness", default=None)

    max_date_sickness_refund: Optional[str] = FieldInfo(alias="maxDateSicknessRefund", default=None)

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

    uuid: Optional[str] = None

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)

    work_permit: Optional[ItemWorkPermit] = FieldInfo(alias="workPermit", default=None)

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


class CompanyEmployeeListResponse(BaseModel):
    items: List[Item]

    limit: int

    page: int

    pages: int

    total: int
