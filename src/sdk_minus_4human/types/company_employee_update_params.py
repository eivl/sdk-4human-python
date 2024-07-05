# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CompanyEmployeeUpdateParams",
    "CustomField",
    "EffectiveDates",
    "FreeEmployer",
    "IndustryID",
    "IndustryIDFile",
    "ResidencePermit",
    "WorkPermit",
]


class CompanyEmployeeUpdateParams(TypedDict, total=False):
    custom_fields: Required[Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]]

    effective_dates: Required[Annotated[EffectiveDates, PropertyInfo(alias="effectiveDates")]]

    employee_id: Required[Annotated[str, PropertyInfo(alias="employeeId")]]

    free_employer: Required[Annotated[Optional[FreeEmployer], PropertyInfo(alias="freeEmployer")]]

    industry_ids: Required[Annotated[Iterable[IndustryID], PropertyInfo(alias="industryIds")]]

    main_employer: Required[Annotated[bool, PropertyInfo(alias="mainEmployer")]]

    primary_employment_id: Required[Annotated[int, PropertyInfo(alias="primaryEmploymentId")]]

    ready_for_payment: Required[Annotated[bool, PropertyInfo(alias="readyForPayment")]]

    residence_permit: Required[Annotated[Optional[ResidencePermit], PropertyInfo(alias="residencePermit")]]

    resource_type: Required[Annotated[Optional[int], PropertyInfo(alias="resourceType")]]

    salary_number: Required[Annotated[Optional[str], PropertyInfo(alias="salaryNumber")]]

    self_sickness: Required[Annotated[Optional[str], PropertyInfo(alias="selfSickness")]]

    seniority_date: Required[Annotated[Optional[str], PropertyInfo(alias="seniorityDate")]]

    termination_seniority_date: Required[Annotated[Optional[str], PropertyInfo(alias="terminationSeniorityDate")]]

    work_permit: Required[Annotated[Optional[WorkPermit], PropertyInfo(alias="workPermit")]]

    work_status: Required[Annotated[str, PropertyInfo(alias="workStatus")]]

    external: bool
    """
    Param determines if id of company employee is external (employeeId) or internal
    (id)
    """

    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    max_date_follow_up_sickness: Annotated[Optional[str], PropertyInfo(alias="maxDateFollowUpSickness")]

    max_date_sickness_refund: Annotated[Optional[str], PropertyInfo(alias="maxDateSicknessRefund")]

    retirement_date: Annotated[Optional[str], PropertyInfo(alias="retirementDate")]


class CustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]

    value_id: Required[Annotated[Optional[str], PropertyInfo(alias="valueId")]]

    value: Optional[str]
    """This value will be set only if "valueId" is not provided"""


class EffectiveDates(TypedDict, total=False):
    comment: Required[Optional[str]]

    end_validity_date: Required[
        Annotated[Union[str, datetime, None], PropertyInfo(alias="endValidityDate", format="iso8601")]
    ]

    immediate: Required[Optional[bool]]

    start_validity_date: Required[
        Annotated[Union[str, datetime, None], PropertyInfo(alias="startValidityDate", format="iso8601")]
    ]


_FreeEmployerReservedKeywords = TypedDict(
    "_FreeEmployerReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class FreeEmployer(_FreeEmployerReservedKeywords, total=False):
    to: Optional[str]


class IndustryIDFile(TypedDict, total=False):
    id: Required[str]

    original_name: Required[Annotated[str, PropertyInfo(alias="originalName")]]


class IndustryID(TypedDict, total=False):
    additional_info: Required[Annotated[Optional[str], PropertyInfo(alias="additionalInfo")]]

    card_number: Required[Annotated[str, PropertyInfo(alias="cardNumber")]]

    country_issue: Required[Annotated[Optional[str], PropertyInfo(alias="countryIssue")]]

    expiry_date: Required[Annotated[Optional[str], PropertyInfo(alias="expiryDate")]]

    file: Required[Optional[IndustryIDFile]]

    industry_branch_id: Required[Annotated[int, PropertyInfo(alias="industryBranchId")]]

    issue_date: Required[Annotated[Optional[str], PropertyInfo(alias="issueDate")]]

    id: Optional[int]
    """
    If `id` is provided then existing industry will be replaced, otherwise a new
    industry will be added
    """


_ResidencePermitReservedKeywords = TypedDict(
    "_ResidencePermitReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class ResidencePermit(_ResidencePermitReservedKeywords, total=False):
    to: Optional[str]


_WorkPermitReservedKeywords = TypedDict(
    "_WorkPermitReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class WorkPermit(_WorkPermitReservedKeywords, total=False):
    to: Optional[str]
