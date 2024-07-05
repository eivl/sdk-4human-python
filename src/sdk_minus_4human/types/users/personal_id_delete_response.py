# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PersonalIDDeleteResponse",
    "Child",
    "ChildChronicallySick",
    "ConnectedEmployeeData",
    "Identification",
    "Integrations",
    "IntegrationsV4",
    "LoginMethod",
    "NextOfKin",
    "NextOfKinAddress",
    "PaymentDetails",
    "PersonalIdentification",
    "PrivateContactDetails",
    "PrivateContactDetailsAddressInfo",
    "PrivateContactDetailsAddressInfoPostAddress",
    "PrivateContactDetailsAddressInfoVisitAddress",
    "PrivateContactDetailsContactInfo",
    "PrivateContactDetailsContactInfoAdditionalContact",
    "UserCalculatedStatus",
    "WorkContactDetails",
    "WorkContactDetailsAddressInfo",
    "WorkContactDetailsAddressInfoPostAddress",
    "WorkContactDetailsAddressInfoVisitAddress",
    "WorkContactDetailsContactInfo",
    "WorkContactDetailsContactInfoAdditionalContact",
]


class ChildChronicallySick(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class Child(BaseModel):
    id: Optional[str] = None

    birth_date: Optional[str] = FieldInfo(alias="birthDate", default=None)

    chronically_sick: Optional[ChildChronicallySick] = FieldInfo(alias="chronicallySick", default=None)

    do_i_have_care: Optional[bool] = FieldInfo(alias="doIHaveCare", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    firstname: Optional[str] = None

    gender: Optional[Literal["-", "M", "F"]] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    single_parent: Optional[bool] = FieldInfo(alias="singleParent", default=None)

    surname: Optional[str] = None


class ConnectedEmployeeData(BaseModel):
    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)

    organization_number: Optional[str] = FieldInfo(alias="organizationNumber", default=None)


class Identification(BaseModel):
    id: int

    id_country: Optional[str] = FieldInfo(alias="idCountry", default=None)

    id_number: Optional[str] = FieldInfo(alias="idNumber", default=None)

    id_type: Optional[str] = FieldInfo(alias="idType", default=None)


class IntegrationsV4(BaseModel):
    enabled: Optional[bool] = None


class Integrations(BaseModel):
    v4: Optional[IntegrationsV4] = None


class LoginMethod(BaseModel):
    active_directory_login: Optional[str] = FieldInfo(alias="activeDirectoryLogin", default=None)

    email: Optional[str] = None

    login_method: Optional[Literal["NO_USER", "AUTH0", "ACTIVE_DIRECTORY"]] = FieldInfo(
        alias="loginMethod", default=None
    )


class NextOfKinAddress(BaseModel):
    address_line1: Optional[str] = FieldInfo(alias="addressLine1", default=None)

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class NextOfKin(BaseModel):
    id: Optional[str] = None

    address: Optional[NextOfKinAddress] = None

    comment: Optional[str] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    firstname: Optional[str] = None

    gender: Optional[Literal["-", "M", "F"]] = None

    relationship_type: Optional[str] = FieldInfo(alias="relationshipType", default=None)

    surname: Optional[str] = None


class PaymentDetails(BaseModel):
    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)

    country_of_bank: Optional[str] = FieldInfo(alias="countryOfBank", default=None)

    iban: Optional[str] = None


class PersonalIdentification(BaseModel):
    id_country: Optional[str] = FieldInfo(alias="idCountry", default=None)

    id_number: Optional[str] = FieldInfo(alias="idNumber", default=None)

    id_type: Optional[str] = FieldInfo(alias="idType", default=None)

    passport_country: Optional[str] = FieldInfo(alias="passportCountry", default=None)

    passport_number: Optional[str] = FieldInfo(alias="passportNumber", default=None)


class PrivateContactDetailsAddressInfoPostAddress(BaseModel):
    address: Optional[str] = None

    building_entrance: Optional[str] = FieldInfo(alias="buildingEntrance", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class PrivateContactDetailsAddressInfoVisitAddress(BaseModel):
    address: Optional[str] = None

    building_entrance: Optional[str] = FieldInfo(alias="buildingEntrance", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class PrivateContactDetailsAddressInfo(BaseModel):
    id: Optional[int] = None

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)

    is_company_location: Optional[bool] = FieldInfo(alias="isCompanyLocation", default=None)

    is_post_address_available: Optional[bool] = FieldInfo(alias="isPostAddressAvailable", default=None)

    name: Optional[str] = None

    post_address: Optional[PrivateContactDetailsAddressInfoPostAddress] = FieldInfo(alias="postAddress", default=None)

    type: Optional[Literal["additional", "primary"]] = None

    visit_address: Optional[PrivateContactDetailsAddressInfoVisitAddress] = FieldInfo(
        alias="visitAddress", default=None
    )


class PrivateContactDetailsContactInfoAdditionalContact(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class PrivateContactDetailsContactInfo(BaseModel):
    additional_contact: Optional[List[PrivateContactDetailsContactInfoAdditionalContact]] = FieldInfo(
        alias="additionalContact", default=None
    )

    email: Optional[str] = None

    mobile_phone: Optional[str] = FieldInfo(alias="mobilePhone", default=None)

    phone: Optional[str] = None


class PrivateContactDetails(BaseModel):
    address_info: Optional[List[PrivateContactDetailsAddressInfo]] = FieldInfo(alias="addressInfo", default=None)

    contact_info: Optional[PrivateContactDetailsContactInfo] = FieldInfo(alias="contactInfo", default=None)


class UserCalculatedStatus(BaseModel):
    remaining_days: Optional[int] = FieldInfo(alias="remainingDays", default=None)

    status: Optional[str] = None


class WorkContactDetailsAddressInfoPostAddress(BaseModel):
    address: Optional[str] = None

    building_entrance: Optional[str] = FieldInfo(alias="buildingEntrance", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class WorkContactDetailsAddressInfoVisitAddress(BaseModel):
    address: Optional[str] = None

    building_entrance: Optional[str] = FieldInfo(alias="buildingEntrance", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    municipality: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class WorkContactDetailsAddressInfo(BaseModel):
    id: Optional[int] = None

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)

    is_company_location: Optional[bool] = FieldInfo(alias="isCompanyLocation", default=None)

    is_post_address_available: Optional[bool] = FieldInfo(alias="isPostAddressAvailable", default=None)

    name: Optional[str] = None

    post_address: Optional[WorkContactDetailsAddressInfoPostAddress] = FieldInfo(alias="postAddress", default=None)

    type: Optional[Literal["additional", "primary"]] = None

    visit_address: Optional[WorkContactDetailsAddressInfoVisitAddress] = FieldInfo(alias="visitAddress", default=None)


class WorkContactDetailsContactInfoAdditionalContact(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class WorkContactDetailsContactInfo(BaseModel):
    additional_contact: Optional[List[WorkContactDetailsContactInfoAdditionalContact]] = FieldInfo(
        alias="additionalContact", default=None
    )

    email: Optional[str] = None

    mobile_phone: Optional[str] = FieldInfo(alias="mobilePhone", default=None)

    phone: Optional[str] = None


class WorkContactDetails(BaseModel):
    address_info: Optional[List[WorkContactDetailsAddressInfo]] = FieldInfo(alias="addressInfo", default=None)

    contact_info: Optional[WorkContactDetailsContactInfo] = FieldInfo(alias="contactInfo", default=None)


class PersonalIDDeleteResponse(BaseModel):
    id: Optional[str] = None

    alias: Optional[str] = None

    children: Optional[List[Child]] = None

    connected_employee_data: Optional[List[ConnectedEmployeeData]] = FieldInfo(
        alias="connectedEmployeeData", default=None
    )

    country_of_origin: Optional[str] = FieldInfo(alias="countryOfOrigin", default=None)

    date_of_birth: Optional[str] = FieldInfo(alias="dateOfBirth", default=None)

    effective_status: Optional[str] = FieldInfo(alias="effectiveStatus", default=None)

    effective_status_date: Optional[str] = FieldInfo(alias="effectiveStatusDate", default=None)

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    gender: Optional[str] = None

    identification: Optional[List[Identification]] = None

    initials: Optional[str] = None

    instance_employee_id: Optional[str] = FieldInfo(alias="instanceEmployeeId", default=None)

    integrations: Optional[Integrations] = None

    login_method: Optional[LoginMethod] = FieldInfo(alias="loginMethod", default=None)

    marital_status: Optional[str] = FieldInfo(alias="maritalStatus", default=None)

    nationality: Optional[str] = None

    next_of_kin: Optional[List[NextOfKin]] = FieldInfo(alias="nextOfKin", default=None)

    payment_details: Optional[PaymentDetails] = FieldInfo(alias="paymentDetails", default=None)

    personal_identification: Optional[PersonalIdentification] = FieldInfo(alias="personalIdentification", default=None)

    private_contact_details: Optional[PrivateContactDetails] = FieldInfo(alias="privateContactDetails", default=None)

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    reference_id: Optional[int] = FieldInfo(alias="referenceId", default=None)

    registered_by: Optional[str] = FieldInfo(alias="registeredBy", default=None)

    surname: Optional[str] = None

    user_calculated_status: Optional[UserCalculatedStatus] = FieldInfo(alias="userCalculatedStatus", default=None)

    uuid: Optional[str] = None

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)

    work_contact_details: Optional[WorkContactDetails] = FieldInfo(alias="workContactDetails", default=None)
