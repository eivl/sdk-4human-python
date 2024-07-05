# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NextOfKinUpdateParams", "Address"]


class NextOfKinUpdateParams(TypedDict, total=False):
    address: Address

    comment: Optional[str]

    firstname: str

    gender: Optional[Literal["-", "M", "F"]]

    relationship_type: Annotated[
        Literal[
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
        ],
        PropertyInfo(alias="relationshipType"),
    ]

    surname: str


class Address(TypedDict, total=False):
    address_line1: Annotated[Optional[str], PropertyInfo(alias="addressLine1")]

    address_line2: Annotated[Optional[str], PropertyInfo(alias="addressLine2")]

    city: Optional[str]

    country: Optional[str]

    email: Optional[str]

    phone: Optional[str]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]
