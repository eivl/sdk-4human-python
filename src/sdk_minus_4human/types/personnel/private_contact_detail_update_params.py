# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PrivateContactDetailUpdateParams",
    "AddressInfo",
    "AddressInfoVisitAddress",
    "AddressInfoPostAddress",
    "ContactInfo",
    "ContactInfoAdditionalContact",
]


class PrivateContactDetailUpdateParams(TypedDict, total=False):
    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    address_info: Annotated[Iterable[AddressInfo], PropertyInfo(alias="addressInfo")]

    contact_info: Annotated[ContactInfo, PropertyInfo(alias="contactInfo")]


class AddressInfoVisitAddress(TypedDict, total=False):
    address: Optional[str]

    building_entrance: Annotated[Optional[str], PropertyInfo(alias="buildingEntrance")]

    city: Optional[str]

    country: Optional[str]

    municipality: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]


class AddressInfoPostAddress(TypedDict, total=False):
    address: Optional[str]

    building_entrance: Annotated[Optional[str], PropertyInfo(alias="buildingEntrance")]

    city: Optional[str]

    country: Optional[str]

    municipality: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]


class AddressInfo(TypedDict, total=False):
    type: Required[Literal["primary", "additional"]]
    """Exactly one address has to be "primary" """

    visit_address: Required[Annotated[AddressInfoVisitAddress, PropertyInfo(alias="visitAddress")]]

    id: Optional[int]

    name: Optional[str]

    post_address: Annotated[Optional[AddressInfoPostAddress], PropertyInfo(alias="postAddress")]
    """
    At least one property must not be "null", otherwise whole postAddress should be
    set to "null"
    """


class ContactInfoAdditionalContact(TypedDict, total=False):
    name: Required[str]

    value: Required[str]


class ContactInfo(TypedDict, total=False):
    additional_contact: Annotated[Iterable[ContactInfoAdditionalContact], PropertyInfo(alias="additionalContact")]

    email: Optional[str]

    mobile_phone: Annotated[Optional[str], PropertyInfo(alias="mobilePhone")]

    phone: Optional[str]
