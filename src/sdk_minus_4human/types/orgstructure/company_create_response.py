# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CompanyCreateResponse",
    "AncestorCompany",
    "AncestorLeader",
    "CompanyLocation",
    "CompanyLocationPostAddress",
    "CompanyLocationVisitAddress",
    "CustomField",
    "Leader",
    "Location",
    "LocationPostAddress",
    "LocationVisitAddress",
    "PostAddress",
    "RemovedLocation",
    "VisitAddress",
]


class AncestorCompany(BaseModel):
    company_country: Optional[str] = FieldInfo(alias="companyCountry", default=None)

    company_logo_url: Optional[str] = FieldInfo(alias="companyLogoUrl", default=None)

    organization_number: Optional[str] = FieldInfo(alias="organizationNumber", default=None)
    """For NOR country this is number from Brreg"""


class AncestorLeader(BaseModel):
    id: Optional[str] = None

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    picture: Optional[str] = None


class CompanyLocationPostAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class CompanyLocationVisitAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class CompanyLocation(BaseModel):
    id: Optional[int] = None

    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    name: Optional[str] = None

    post_address: Optional[CompanyLocationPostAddress] = FieldInfo(alias="postAddress", default=None)

    visit_address: Optional[CompanyLocationVisitAddress] = FieldInfo(alias="visitAddress", default=None)


class CustomField(BaseModel):
    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    field: Optional[str] = None

    field_created_at: Optional[str] = FieldInfo(alias="fieldCreatedAt", default=None)

    field_external_id: Optional[str] = FieldInfo(alias="fieldExternalId", default=None)

    field_external_name: Optional[str] = FieldInfo(alias="fieldExternalName", default=None)

    field_id: Optional[str] = FieldInfo(alias="fieldId", default=None)
    """UUID of a given custom field"""

    field_template_external_id: Optional[str] = FieldInfo(alias="fieldTemplateExternalId", default=None)

    field_template_external_name: Optional[str] = FieldInfo(alias="fieldTemplateExternalName", default=None)

    field_template_id: Optional[str] = FieldInfo(alias="fieldTemplateId", default=None)

    field_template_name: Optional[str] = FieldInfo(alias="fieldTemplateName", default=None)

    field_updated_at: Optional[str] = FieldInfo(alias="fieldUpdatedAt", default=None)

    has_custom_fields: Optional[bool] = FieldInfo(alias="hasCustomFields", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    value: Optional[str] = None

    value_created_at: Optional[str] = FieldInfo(alias="valueCreatedAt", default=None)

    value_external_id: Optional[str] = FieldInfo(alias="valueExternalId", default=None)

    value_external_name: Optional[str] = FieldInfo(alias="valueExternalName", default=None)

    value_id: Optional[str] = FieldInfo(alias="valueId", default=None)
    """UUID of a given value of a custom field"""

    value_updated_at: Optional[str] = FieldInfo(alias="valueUpdatedAt", default=None)


class Leader(BaseModel):
    id: Optional[str] = None

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    picture: Optional[str] = None


class LocationPostAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class LocationVisitAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class Location(BaseModel):
    id: Optional[int] = None

    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    name: Optional[str] = None

    post_address: Optional[LocationPostAddress] = FieldInfo(alias="postAddress", default=None)

    visit_address: Optional[LocationVisitAddress] = FieldInfo(alias="visitAddress", default=None)


class PostAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class RemovedLocation(BaseModel):
    id: Optional[int] = None

    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)

    name: Optional[str] = None

    status: Optional[Literal["removed"]] = None


class VisitAddress(BaseModel):
    address: Optional[str] = None

    city: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class CompanyCreateResponse(BaseModel):
    id: Optional[int] = None

    ancestor_company: Optional[AncestorCompany] = FieldInfo(alias="ancestorCompany", default=None)

    ancestor_leader: Optional[AncestorLeader] = FieldInfo(alias="ancestorLeader", default=None)

    ancestor_leader_id: Optional[int] = FieldInfo(alias="ancestorLeaderId", default=None)

    ancestors: Optional[List[int]] = None

    approval_policy: Optional[Literal["noPolicy", "confirmation", "approvalAndConfirmation"]] = FieldInfo(
        alias="approvalPolicy", default=None
    )

    candidate_approval_policy: Optional[Literal["none", "candidateApproval", "candidateWithoutApproval"]] = FieldInfo(
        alias="candidateApprovalPolicy", default=None
    )

    company: Optional[bool] = None

    company_country: Optional[str] = FieldInfo(alias="companyCountry", default=None)

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    company_location: Optional[CompanyLocation] = FieldInfo(alias="companyLocation", default=None)

    company_logo_url: Optional[str] = FieldInfo(alias="companyLogoUrl", default=None)

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)

    custom_fields: Optional[List[CustomField]] = FieldInfo(alias="customFields", default=None)

    descendants: Optional[List[int]] = None

    employee_count: Optional[int] = FieldInfo(alias="employeeCount", default=None)

    evolution_id: Optional[int] = FieldInfo(alias="evolutionId", default=None)

    external_source: Optional[bool] = FieldInfo(alias="externalSource", default=None)

    fte_sum: Optional[str] = FieldInfo(alias="fteSum", default=None)

    has_company: Optional[bool] = FieldInfo(alias="hasCompany", default=None)

    last_locations_update: Optional[str] = FieldInfo(alias="lastLocationsUpdate", default=None)

    leader: Optional[Leader] = None
    """Entity that represents unit manager"""

    leader_id: Optional[int] = FieldInfo(alias="leaderId", default=None)
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    locations: Optional[List[Location]] = None

    manager_id: Optional[int] = FieldInfo(alias="managerId", default=None)
    """database id of unit manager."""

    manager_id_ext: Optional[str] = FieldInfo(alias="managerIdExt", default=None)
    """external id of unit manager (field number in database)"""

    name: Optional[str] = None

    organization_number: Optional[str] = FieldInfo(alias="organizationNumber", default=None)

    parent_id: Optional[int] = FieldInfo(alias="parentId", default=None)
    """database id of parent unit."""

    post_address: Optional[PostAddress] = FieldInfo(alias="postAddress", default=None)

    ready_for_payment_message: Optional[str] = FieldInfo(alias="readyForPaymentMessage", default=None)

    removed_locations: Optional[List[RemovedLocation]] = FieldInfo(alias="removedLocations", default=None)

    salary_system_company_id: Optional[str] = FieldInfo(alias="salarySystemCompanyId", default=None)

    selected_company_number: Optional[str] = FieldInfo(alias="selectedCompanyNumber", default=None)

    status: Optional[str] = None

    unit_id: Optional[str] = FieldInfo(alias="unitId", default=None)
    """Additional unit identifier, to be used freely by the application users."""

    unit_type_id: Optional[str] = FieldInfo(alias="unitTypeId", default=None)

    visit_address: Optional[VisitAddress] = FieldInfo(alias="visitAddress", default=None)
