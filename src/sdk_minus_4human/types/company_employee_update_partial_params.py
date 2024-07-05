# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CompanyEmployeeUpdatePartialParams",
    "CustomField",
    "EffectiveDates",
    "FreeEmployer",
    "ResidencePermit",
    "WorkPermit",
]


class CompanyEmployeeUpdatePartialParams(TypedDict, total=False):
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

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]

    effective_dates: Annotated[EffectiveDates, PropertyInfo(alias="effectiveDates")]
    """If effectiveDates are not provided, the changes will be immediate"""

    employee_id: Annotated[str, PropertyInfo(alias="employeeId")]

    free_employer: Annotated[Optional[FreeEmployer], PropertyInfo(alias="freeEmployer")]

    main_employer: Annotated[bool, PropertyInfo(alias="mainEmployer")]

    max_date_follow_up_sickness: Annotated[Optional[str], PropertyInfo(alias="maxDateFollowUpSickness")]

    max_date_sickness_refund: Annotated[Optional[str], PropertyInfo(alias="maxDateSicknessRefund")]

    primary_employment_id: Annotated[int, PropertyInfo(alias="primaryEmploymentId")]

    ready_for_payment: Annotated[bool, PropertyInfo(alias="readyForPayment")]

    residence_permit: Annotated[Optional[ResidencePermit], PropertyInfo(alias="residencePermit")]

    resource_type: Annotated[Optional[int], PropertyInfo(alias="resourceType")]

    retirement_date: Annotated[Optional[str], PropertyInfo(alias="retirementDate")]

    salary_number: Annotated[Optional[str], PropertyInfo(alias="salaryNumber")]

    self_sickness: Annotated[Optional[str], PropertyInfo(alias="selfSickness")]

    seniority_date: Annotated[Optional[str], PropertyInfo(alias="seniorityDate")]

    termination_seniority_date: Annotated[Optional[str], PropertyInfo(alias="terminationSeniorityDate")]

    work_permit: Annotated[Optional[WorkPermit], PropertyInfo(alias="workPermit")]

    work_status: Annotated[str, PropertyInfo(alias="workStatus")]


class CustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]

    value: Optional[str]
    """This value will be set only if "valueId" is not provided"""

    value_id: Annotated[Optional[str], PropertyInfo(alias="valueId")]


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
