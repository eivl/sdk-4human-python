# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "HistoryListResponse",
    "Item",
    "ItemChild",
    "ItemChildChronicallySick",
    "ItemConnectedEmployeeData",
    "ItemIdentification",
    "ItemIntegrations",
    "ItemIntegrationsV4",
    "ItemLoginMethod",
    "ItemNextOfKin",
    "ItemNextOfKinAddress",
    "ItemPaymentDetails",
    "ItemPersonalIdentification",
    "ItemPrivateContactDetails",
    "ItemPrivateContactDetailsAddressInfo",
    "ItemPrivateContactDetailsAddressInfoPostAddress",
    "ItemPrivateContactDetailsAddressInfoVisitAddress",
    "ItemPrivateContactDetailsContactInfo",
    "ItemPrivateContactDetailsContactInfoAdditionalContact",
    "ItemUserCalculatedStatus",
    "ItemWorkContactDetails",
    "ItemWorkContactDetailsAddressInfo",
    "ItemWorkContactDetailsAddressInfoPostAddress",
    "ItemWorkContactDetailsAddressInfoVisitAddress",
    "ItemWorkContactDetailsContactInfo",
    "ItemWorkContactDetailsContactInfoAdditionalContact",
]


class ItemChildChronicallySick(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class ItemChild(BaseModel):
    id: Optional[str] = None

    birth_date: Optional[str] = FieldInfo(alias="birthDate", default=None)

    chronically_sick: Optional[ItemChildChronicallySick] = FieldInfo(alias="chronicallySick", default=None)

    do_i_have_care: Optional[bool] = FieldInfo(alias="doIHaveCare", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    firstname: Optional[str] = None

    gender: Optional[Literal["-", "M", "F"]] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    single_parent: Optional[bool] = FieldInfo(alias="singleParent", default=None)

    surname: Optional[str] = None


class ItemConnectedEmployeeData(BaseModel):
    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)

    organization_number: Optional[str] = FieldInfo(alias="organizationNumber", default=None)


class ItemIdentification(BaseModel):
    id: int

    id_country: Optional[str] = FieldInfo(alias="idCountry", default=None)

    id_number: Optional[str] = FieldInfo(alias="idNumber", default=None)

    id_type: Optional[str] = FieldInfo(alias="idType", default=None)


class ItemIntegrationsV4(BaseModel):
    enabled: Optional[bool] = None


class ItemIntegrations(BaseModel):
    v4: Optional[ItemIntegrationsV4] = None


class ItemLoginMethod(BaseModel):
    active_directory_login: Optional[str] = FieldInfo(alias="activeDirectoryLogin", default=None)

    email: Optional[str] = None

    login_method: Optional[Literal["NO_USER", "AUTH0", "ACTIVE_DIRECTORY"]] = FieldInfo(
        alias="loginMethod", default=None
    )


class ItemNextOfKinAddress(BaseModel):
    address_line1: Optional[str] = FieldInfo(alias="addressLine1", default=None)

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class ItemNextOfKin(BaseModel):
    id: Optional[str] = None

    address: Optional[ItemNextOfKinAddress] = None

    comment: Optional[str] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    firstname: Optional[str] = None

    gender: Optional[Literal["-", "M", "F"]] = None

    relationship_type: Optional[str] = FieldInfo(alias="relationshipType", default=None)

    surname: Optional[str] = None


class ItemPaymentDetails(BaseModel):
    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)

    country_of_bank: Optional[str] = FieldInfo(alias="countryOfBank", default=None)

    iban: Optional[str] = None


class ItemPersonalIdentification(BaseModel):
    id_country: Optional[str] = FieldInfo(alias="idCountry", default=None)

    id_number: Optional[str] = FieldInfo(alias="idNumber", default=None)

    id_type: Optional[str] = FieldInfo(alias="idType", default=None)

    passport_country: Optional[str] = FieldInfo(alias="passportCountry", default=None)

    passport_number: Optional[str] = FieldInfo(alias="passportNumber", default=None)


class ItemPrivateContactDetailsAddressInfoPostAddress(BaseModel):
    address: Optional[str] = None

    building_entrance: Optional[str] = FieldInfo(alias="buildingEntrance", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class ItemPrivateContactDetailsAddressInfoVisitAddress(BaseModel):
    address: Optional[str] = None

    building_entrance: Optional[str] = FieldInfo(alias="buildingEntrance", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class ItemPrivateContactDetailsAddressInfo(BaseModel):
    id: Optional[int] = None

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)

    is_company_location: Optional[bool] = FieldInfo(alias="isCompanyLocation", default=None)

    is_post_address_available: Optional[bool] = FieldInfo(alias="isPostAddressAvailable", default=None)

    name: Optional[str] = None

    post_address: Optional[ItemPrivateContactDetailsAddressInfoPostAddress] = FieldInfo(
        alias="postAddress", default=None
    )

    type: Optional[Literal["additional", "primary"]] = None

    visit_address: Optional[ItemPrivateContactDetailsAddressInfoVisitAddress] = FieldInfo(
        alias="visitAddress", default=None
    )


class ItemPrivateContactDetailsContactInfoAdditionalContact(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class ItemPrivateContactDetailsContactInfo(BaseModel):
    additional_contact: Optional[List[ItemPrivateContactDetailsContactInfoAdditionalContact]] = FieldInfo(
        alias="additionalContact", default=None
    )

    email: Optional[str] = None

    mobile_phone: Optional[str] = FieldInfo(alias="mobilePhone", default=None)

    phone: Optional[str] = None


class ItemPrivateContactDetails(BaseModel):
    address_info: Optional[List[ItemPrivateContactDetailsAddressInfo]] = FieldInfo(alias="addressInfo", default=None)

    contact_info: Optional[ItemPrivateContactDetailsContactInfo] = FieldInfo(alias="contactInfo", default=None)


class ItemUserCalculatedStatus(BaseModel):
    remaining_days: Optional[int] = FieldInfo(alias="remainingDays", default=None)

    status: Optional[str] = None


class ItemWorkContactDetailsAddressInfoPostAddress(BaseModel):
    address: Optional[str] = None

    building_entrance: Optional[str] = FieldInfo(alias="buildingEntrance", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class ItemWorkContactDetailsAddressInfoVisitAddress(BaseModel):
    address: Optional[str] = None

    building_entrance: Optional[str] = FieldInfo(alias="buildingEntrance", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class ItemWorkContactDetailsAddressInfo(BaseModel):
    id: Optional[int] = None

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)

    is_company_location: Optional[bool] = FieldInfo(alias="isCompanyLocation", default=None)

    is_post_address_available: Optional[bool] = FieldInfo(alias="isPostAddressAvailable", default=None)

    name: Optional[str] = None

    post_address: Optional[ItemWorkContactDetailsAddressInfoPostAddress] = FieldInfo(alias="postAddress", default=None)

    type: Optional[Literal["additional", "primary"]] = None

    visit_address: Optional[ItemWorkContactDetailsAddressInfoVisitAddress] = FieldInfo(
        alias="visitAddress", default=None
    )


class ItemWorkContactDetailsContactInfoAdditionalContact(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class ItemWorkContactDetailsContactInfo(BaseModel):
    additional_contact: Optional[List[ItemWorkContactDetailsContactInfoAdditionalContact]] = FieldInfo(
        alias="additionalContact", default=None
    )

    email: Optional[str] = None

    mobile_phone: Optional[str] = FieldInfo(alias="mobilePhone", default=None)

    phone: Optional[str] = None


class ItemWorkContactDetails(BaseModel):
    address_info: Optional[List[ItemWorkContactDetailsAddressInfo]] = FieldInfo(alias="addressInfo", default=None)

    contact_info: Optional[ItemWorkContactDetailsContactInfo] = FieldInfo(alias="contactInfo", default=None)


class Item(BaseModel):
    id: Optional[str] = None

    alias: Optional[str] = None

    children: Optional[List[ItemChild]] = None

    connected_employee_data: Optional[List[ItemConnectedEmployeeData]] = FieldInfo(
        alias="connectedEmployeeData", default=None
    )

    country_of_origin: Optional[str] = FieldInfo(alias="countryOfOrigin", default=None)

    date_of_birth: Optional[str] = FieldInfo(alias="dateOfBirth", default=None)

    effective_status: Optional[str] = FieldInfo(alias="effectiveStatus", default=None)

    effective_status_date: Optional[str] = FieldInfo(alias="effectiveStatusDate", default=None)

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    gender: Optional[str] = None

    identification: Optional[List[ItemIdentification]] = None

    initials: Optional[str] = None

    instance_employee_id: Optional[str] = FieldInfo(alias="instanceEmployeeId", default=None)

    integrations: Optional[ItemIntegrations] = None

    login_method: Optional[ItemLoginMethod] = FieldInfo(alias="loginMethod", default=None)

    marital_status: Optional[str] = FieldInfo(alias="maritalStatus", default=None)

    nationality: Optional[str] = None

    next_of_kin: Optional[List[ItemNextOfKin]] = FieldInfo(alias="nextOfKin", default=None)

    payment_details: Optional[ItemPaymentDetails] = FieldInfo(alias="paymentDetails", default=None)

    personal_identification: Optional[ItemPersonalIdentification] = FieldInfo(
        alias="personalIdentification", default=None
    )

    private_contact_details: Optional[ItemPrivateContactDetails] = FieldInfo(
        alias="privateContactDetails", default=None
    )

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    reference_id: Optional[int] = FieldInfo(alias="referenceId", default=None)

    registered_by: Optional[str] = FieldInfo(alias="registeredBy", default=None)

    surname: Optional[str] = None

    user_calculated_status: Optional[ItemUserCalculatedStatus] = FieldInfo(alias="userCalculatedStatus", default=None)

    uuid: Optional[str] = None

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)

    work_contact_details: Optional[ItemWorkContactDetails] = FieldInfo(alias="workContactDetails", default=None)


class HistoryListResponse(BaseModel):
    items: List[Item]

    limit: int

    page: int

    pages: int

    total: int
