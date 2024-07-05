# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CompanyUpdateParams",
    "CustomField",
    "Location",
    "LocationPostAddress",
    "LocationVisitAddress",
    "PostAddress",
    "VisitAddress",
]


class CompanyUpdateParams(TypedDict, total=False):
    manager_id: Required[Annotated[int, PropertyInfo(alias="managerId")]]

    organization_number: Required[Annotated[str, PropertyInfo(alias="organizationNumber")]]

    unit_id: Required[Annotated[str, PropertyInfo(alias="unitId")]]

    unit_type_id: Required[Annotated[str, PropertyInfo(alias="unitTypeId")]]

    external: bool
    """Param determines if id of unit is external (unitId) or internal (id)"""

    approval_policy: Annotated[
        Literal["noPolicy", "confirmation", "approvalAndConfirmation"], PropertyInfo(alias="approvalPolicy")
    ]

    candidate_approval_policy: Annotated[
        Literal["none", "candidateApproval", "candidateWithoutApproval"], PropertyInfo(alias="candidateApprovalPolicy")
    ]

    company_logo_url: Annotated[Optional[str], PropertyInfo(alias="companyLogoUrl")]

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]

    locations: Optional[Iterable[Location]]
    """
    For NOR country passing locations is not allowed as they are fetched from Brreg.
    """

    name: Optional[str]
    """For NOR country passing name is not allowed as its fetched from Brreg"""

    parent_id: Annotated[Optional[int], PropertyInfo(alias="parentId")]

    post_address: Annotated[Optional[PostAddress], PropertyInfo(alias="postAddress")]
    """For NOR country passing pody is not allowed as they are fetched from Brreg."""

    ready_for_payment_message: Annotated[Optional[str], PropertyInfo(alias="readyForPaymentMessage")]

    salary_system_company_id: Annotated[Optional[str], PropertyInfo(alias="salarySystemCompanyId")]

    selected_company_number: Annotated[Optional[str], PropertyInfo(alias="selectedCompanyNumber")]

    status: Literal["ACTIVE", "INACTIVE"]

    visit_address: Annotated[Optional[VisitAddress], PropertyInfo(alias="visitAddress")]
    """
    For NOR country visitAddress is not allowed as is fetched from Brreg and should
    be null.
    """


class CustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]

    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]


class LocationPostAddress(TypedDict, total=False):
    address: Optional[str]

    city: Optional[str]

    municipality: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]


class LocationVisitAddress(TypedDict, total=False):
    address: Optional[str]

    city: Optional[str]

    municipality: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]


class Location(TypedDict, total=False):
    id: Optional[int]

    company_number: Annotated[Optional[str], PropertyInfo(alias="companyNumber")]

    name: Optional[str]

    post_address: Annotated[LocationPostAddress, PropertyInfo(alias="postAddress")]

    visit_address: Annotated[LocationVisitAddress, PropertyInfo(alias="visitAddress")]


class PostAddress(TypedDict, total=False):
    address: Optional[str]

    city: Optional[str]

    municipality: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]


class VisitAddress(TypedDict, total=False):
    address: Optional[str]

    city: Optional[str]

    municipality: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]
