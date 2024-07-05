# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CompanyCreateParams",
    "Location",
    "LocationPostAddress",
    "LocationVisitAddress",
    "PostAddress",
    "VisitAddress",
]


class CompanyCreateParams(TypedDict, total=False):
    company_country: Required[Annotated[str, PropertyInfo(alias="companyCountry")]]
    """ISO 3166-1 alpha-3 country code"""

    manager_id: Required[Annotated[int, PropertyInfo(alias="managerId")]]
    """database id of unit manager."""

    organization_number: Required[Annotated[str, PropertyInfo(alias="organizationNumber")]]
    """
    For NOR country passing organizationNumber is not allowed as its fetched from
    Brreg
    """

    unit_type_id: Required[Annotated[str, PropertyInfo(alias="unitTypeId")]]

    approval_policy: Annotated[
        Literal["noPolicy", "confirmation", "approvalAndConfirmation"], PropertyInfo(alias="approvalPolicy")
    ]

    candidate_approval_policy: Annotated[
        Literal["none", "candidateApproval", "candidateWithoutApproval"], PropertyInfo(alias="candidateApprovalPolicy")
    ]

    company_logo_url: Annotated[Optional[str], PropertyInfo(alias="companyLogoUrl")]

    locations: Optional[Iterable[Location]]
    """
    For NOR country locations is not allowed as they are fetched from Brreg and
    should be null.
    """

    name: Optional[str]
    """For NOR country passing name is not allowed as its fetched from Brreg"""

    parent_id: Annotated[Optional[int], PropertyInfo(alias="parentId")]

    post_address: Annotated[Optional[PostAddress], PropertyInfo(alias="postAddress")]
    """
    For NOR country postAddress is not allowed as is fetched from Brreg and should
    be null.
    """

    salary_system_company_id: Annotated[Optional[str], PropertyInfo(alias="salarySystemCompanyId")]

    selected_company_number: Annotated[Optional[str], PropertyInfo(alias="selectedCompanyNumber")]

    status: Literal["ACTIVE", "INACTIVE"]

    unit_id: Annotated[Optional[str], PropertyInfo(alias="unitId")]

    visit_address: Annotated[VisitAddress, PropertyInfo(alias="visitAddress")]


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
