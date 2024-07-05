# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OrgstructureUnitRetrieveResponse",
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
]


class AncestorCompany(BaseModel):
    company_country: Optional[str] = FieldInfo(alias="companyCountry", default=None)
    """ISO 3166-1 alpha-3 country code"""

    company_logo_url: Optional[str] = FieldInfo(alias="companyLogoUrl", default=None)
    """URL of the company's logo"""

    organization_number: Optional[str] = FieldInfo(alias="organizationNumber", default=None)
    """
    ID of the company from the business register (e.g., in Norway) or another system
    """


class AncestorLeader(BaseModel):
    id: str
    """Database ID of the ancestor unit manager"""

    display_name: str = FieldInfo(alias="displayName")
    """Display name of the ancestor unit manager"""

    picture: str
    """URL of the ancestor unit manager's picture"""


class CompanyLocationPostAddress(BaseModel):
    address: Optional[str] = None
    """Street address for posts"""

    city: Optional[str] = None
    """City for posts"""

    municipality: Optional[str] = None
    """Municipality for posts"""

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)
    """ZIP code for posts"""


class CompanyLocationVisitAddress(BaseModel):
    address: Optional[str] = None
    """Street address for visits"""

    city: Optional[str] = None
    """City for visits"""

    municipality: Optional[str] = None
    """Municipality for visits"""

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)
    """ZIP code for visits"""


class CompanyLocation(BaseModel):
    id: Optional[int] = None
    """Internal ID of the company location"""

    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)
    """Company location ID from UI"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID of the location"""

    name: Optional[str] = None
    """Name of the company location"""

    post_address: Optional[CompanyLocationPostAddress] = FieldInfo(alias="postAddress", default=None)
    """Post address of the location"""

    visit_address: Optional[CompanyLocationVisitAddress] = FieldInfo(alias="visitAddress", default=None)
    """Visit address of the location"""


class CustomField(BaseModel):
    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Date when the custom field was created"""

    field: Optional[str] = None
    """Name of the custom field"""

    field_created_at: Optional[str] = FieldInfo(alias="fieldCreatedAt", default=None)
    """Date when the custom field was created"""

    field_external_id: Optional[str] = FieldInfo(alias="fieldExternalId", default=None)
    """External ID of custom field"""

    field_external_name: Optional[str] = FieldInfo(alias="fieldExternalName", default=None)
    """External name of the custom field"""

    field_id: Optional[str] = FieldInfo(alias="fieldId", default=None)
    """UUID of a given custom field"""

    field_template_external_id: Optional[str] = FieldInfo(alias="fieldTemplateExternalId", default=None)
    """External ID of a given custom field template"""

    field_template_external_name: Optional[str] = FieldInfo(alias="fieldTemplateExternalName", default=None)
    """External name of a given custom field template"""

    field_template_id: Optional[str] = FieldInfo(alias="fieldTemplateId", default=None)
    """UUID of a given custom field template"""

    field_template_name: Optional[str] = FieldInfo(alias="fieldTemplateName", default=None)
    """Name of the custom field template"""

    field_updated_at: Optional[str] = FieldInfo(alias="fieldUpdatedAt", default=None)
    """Date when the custom field was updated"""

    has_custom_fields: Optional[bool] = FieldInfo(alias="hasCustomFields", default=None)
    """Indicates if there are custom fields associated with the unit"""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """Date when the custom field was updated"""

    value: Optional[str] = None
    """Name of value in the custom field"""

    value_created_at: Optional[str] = FieldInfo(alias="valueCreatedAt", default=None)
    """Date when custom field value was created"""

    value_external_id: Optional[str] = FieldInfo(alias="valueExternalId", default=None)
    """External ID of the value in the custom field"""

    value_external_name: Optional[str] = FieldInfo(alias="valueExternalName", default=None)
    """External name of the value in the custom field"""

    value_id: Optional[str] = FieldInfo(alias="valueId", default=None)
    """UUID of a given value of a custom field"""

    value_updated_at: Optional[str] = FieldInfo(alias="valueUpdatedAt", default=None)
    """Date when custom field value was updated"""


class Leader(BaseModel):
    id: str
    """Database ID of the manager"""

    display_name: str = FieldInfo(alias="displayName")
    """Display name of the manager"""

    picture: str
    """URL of the manager's picture"""


class LocationPostAddress(BaseModel):
    address: Optional[str] = None
    """Street address of the post address"""

    city: Optional[str] = None
    """City of the post address"""

    municipality: Optional[str] = None
    """Municipality of the post address"""

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)
    """ZIP code of the post address"""


class LocationVisitAddress(BaseModel):
    address: Optional[str] = None
    """Street address of the location"""

    city: Optional[str] = None
    """City of the location"""

    municipality: Optional[str] = None
    """Municipality of the location"""

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)
    """ZIP code of the location"""


class Location(BaseModel):
    id: Optional[int] = None
    """Internal ID of the location"""

    company_number: Optional[str] = FieldInfo(alias="companyNumber", default=None)
    """Identifier of location (companyLocationId from UI)"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID of the location"""

    name: Optional[str] = None
    """Name of the location"""

    post_address: Optional[LocationPostAddress] = FieldInfo(alias="postAddress", default=None)
    """Post address of the location"""

    visit_address: Optional[LocationVisitAddress] = FieldInfo(alias="visitAddress", default=None)
    """Address of the location"""


class OrgstructureUnitRetrieveResponse(BaseModel):
    id: Optional[int] = None
    """Internal organization unit ID"""

    ancestor_company: Optional[AncestorCompany] = FieldInfo(alias="ancestorCompany", default=None)
    """Entity that represents ancestor company"""

    ancestor_leader: Optional[AncestorLeader] = FieldInfo(alias="ancestorLeader", default=None)
    """Entity that represents ancestor unit manager"""

    ancestor_leader_id: Optional[int] = FieldInfo(alias="ancestorLeaderId", default=None)
    """ID of the ancestor leader"""

    ancestors: Optional[List[int]] = None
    """Array of ancestors' IDs of a given unit (in a tree)"""

    company: Optional[bool] = None
    """
    Flag indicating whether the unit is a company (true) or not (false - regular
    unit)
    """

    company_country: Optional[str] = FieldInfo(alias="companyCountry", default=None)
    """ISO 3166-1 alpha-3 country code of the company"""

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)
    """Database ID of the company"""

    company_location: Optional[CompanyLocation] = FieldInfo(alias="companyLocation", default=None)
    """Company location details"""

    company_logo_url: Optional[str] = FieldInfo(alias="companyLogoUrl", default=None)
    """URL of the company's logo"""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """Name of the company"""

    custom_fields: Optional[List[CustomField]] = FieldInfo(alias="customFields", default=None)
    """List of custom fields associated with the unit"""

    descendants: Optional[List[int]] = None
    """Array of descendants' IDs of a given unit (in a tree)"""

    employee_count: Optional[int] = FieldInfo(alias="employeeCount", default=None)
    """Number of employees in the unit"""

    evolution_id: Optional[int] = FieldInfo(alias="evolutionId", default=None)
    """ID of unit used for integration between v4 systems"""

    fte_sum: Optional[str] = FieldInfo(alias="fteSum", default=None)
    """Sum of Full-Time Equivalents (FTEs) in the unit"""

    has_company: Optional[bool] = FieldInfo(alias="hasCompany", default=None)
    """Flag indicating if the unit has a company associated with it"""

    has_selected_company_number: Optional[bool] = FieldInfo(alias="hasSelectedCompanyNumber", default=None)
    """
    Flag determining if the location is directly set for this unit (true) or is
    inherited from the parent company (false)
    """

    leader: Optional[Leader] = None
    """Entity that represents unit manager"""

    leader_id: Optional[int] = FieldInfo(alias="leaderId", default=None)
    """ID of the unit's leader (same as manager - backward compatibility field)"""

    locations: Optional[List[Location]] = None

    manager_id: Optional[int] = FieldInfo(alias="managerId", default=None)
    """Manager ID (manager's personnel employment ID) of a unit"""

    manager_id_ext: Optional[str] = FieldInfo(alias="managerIdExt", default=None)
    """External ID ("Number") of a manager's personnel employment"""

    name: Optional[str] = None
    """Name of the organization unit"""

    organization_number: Optional[str] = FieldInfo(alias="organizationNumber", default=None)
    """
    ID of the company from the business register (e.g., in Norway) or another system
    """

    parent_id: Optional[int] = FieldInfo(alias="parentId", default=None)
    """ID of the parent unit"""

    ready_for_payment_message: Optional[str] = FieldInfo(alias="readyForPaymentMessage", default=None)
    """Message indicating readiness for payment"""

    selected_company_number: Optional[str] = FieldInfo(alias="selectedCompanyNumber", default=None)
    """Location of this unit (value from property `locations.companyNumber`)"""

    status: Optional[str] = None
    """Status of the unit"""

    unit_id: Optional[str] = FieldInfo(alias="unitId", default=None)
    """External ID of the unit"""

    unit_type_id: Optional[str] = FieldInfo(alias="unitTypeId", default=None)
    """UUID that represents unit type"""
