# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UserCreateResponse", "Address"]


class Address(BaseModel):
    address_line1: Optional[str] = FieldInfo(alias="addressLine1", default=None)

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    zip_code: Optional[str] = FieldInfo(alias="zipCode", default=None)


class UserCreateResponse(BaseModel):
    id: str

    address: Optional[Address] = None

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
