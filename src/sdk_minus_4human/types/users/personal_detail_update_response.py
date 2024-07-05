# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PersonalDetailUpdateResponse",
    "Child",
    "ChildChronicallySick",
    "Identification",
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
    id: str

    birth_date: str = FieldInfo(alias="birthDate")

    chronically_sick: ChildChronicallySick = FieldInfo(alias="chronicallySick")

    do_i_have_care: bool = FieldInfo(alias="doIHaveCare")

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    firstname: str

    gender: Optional[Literal["-", "M", "F"]] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    single_parent: bool = FieldInfo(alias="singleParent")

    surname: str


class Identification(BaseModel):
    id: int

    id_country: Optional[str] = FieldInfo(alias="idCountry", default=None)

    id_number: Optional[str] = FieldInfo(alias="idNumber", default=None)

    id_type: Optional[str] = FieldInfo(alias="idType", default=None)


class NextOfKinAddress(BaseModel):
    address_line1: Optional[str] = FieldInfo(alias="addressLine1", default=None)

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class NextOfKin(BaseModel):
    id: str

    address: Optional[NextOfKinAddress] = None

    comment: Optional[str] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    firstname: str

    gender: Optional[Literal["-", "M", "F"]] = None

    relationship_type: Literal[
        "notDefined",
        "children",
        "parent",
        "partner",
        "family",
        "friend",
        "other",
        "cohabitant",
        "mother",
        "father",
        "married",
    ] = FieldInfo(alias="relationshipType")

    surname: str


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
    id: int

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    is_company_location: bool = FieldInfo(alias="isCompanyLocation")

    name: Optional[str] = None

    post_address: Optional[PrivateContactDetailsAddressInfoPostAddress] = FieldInfo(alias="postAddress", default=None)

    type: Literal["primary", "additional"]

    visit_address: Optional[PrivateContactDetailsAddressInfoVisitAddress] = FieldInfo(
        alias="visitAddress", default=None
    )

    is_post_address_available: Optional[bool] = FieldInfo(alias="isPostAddressAvailable", default=None)


class PrivateContactDetailsContactInfoAdditionalContact(BaseModel):
    name: str

    value: str


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

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    is_company_location: bool = FieldInfo(alias="isCompanyLocation")

    name: Optional[str] = None

    post_address: Optional[WorkContactDetailsAddressInfoPostAddress] = FieldInfo(alias="postAddress", default=None)

    type: Literal["primary", "additional"]

    visit_address: Optional[WorkContactDetailsAddressInfoVisitAddress] = FieldInfo(alias="visitAddress", default=None)

    is_post_address_available: Optional[bool] = FieldInfo(alias="isPostAddressAvailable", default=None)


class WorkContactDetailsContactInfoAdditionalContact(BaseModel):
    name: str

    value: str


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


class PersonalDetailUpdateResponse(BaseModel):
    id: Optional[str] = None

    alias: Optional[str] = None

    children: Optional[List[Child]] = None

    country_of_origin: Optional[str] = FieldInfo(alias="countryOfOrigin", default=None)

    date_of_birth: Optional[str] = FieldInfo(alias="dateOfBirth", default=None)

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    gender: Optional[Literal["-", "M", "F"]] = None

    identification: Optional[List[Identification]] = None

    initials: Optional[str] = None

    instance_employee_id: Optional[str] = FieldInfo(alias="instanceEmployeeId", default=None)

    marital_status: Optional[
        Literal[
            "unmarried",
            "married",
            "widowed",
            "divorced",
            "separated",
            "registeredPartner",
            "separatedPartner",
            "divorcedPartner",
            "survivingPartner",
            "cohabitant",
        ]
    ] = FieldInfo(alias="maritalStatus", default=None)

    nationality: Optional[str] = None

    next_of_kin: Optional[List[NextOfKin]] = FieldInfo(alias="nextOfKin", default=None)

    payment_details: Optional[PaymentDetails] = FieldInfo(alias="paymentDetails", default=None)

    personal_identification: Optional[PersonalIdentification] = FieldInfo(alias="personalIdentification", default=None)

    private_contact_details: Optional[PrivateContactDetails] = FieldInfo(alias="privateContactDetails", default=None)

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    surname: Optional[str] = None

    work_contact_details: Optional[WorkContactDetails] = FieldInfo(alias="workContactDetails", default=None)
