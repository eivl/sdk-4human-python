# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserCreateParams", "Address"]


class UserCreateParams(TypedDict, total=False):
    address: Required[Address]

    comment: Required[Optional[str]]

    firstname: Required[str]

    relationship_type: Required[
        Annotated[
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
    ]

    surname: Required[str]

    external_id: Annotated[Optional[str], PropertyInfo(alias="externalId")]
    """
    To post external id use additional parameter forceExternalId otherwise field
    will be ignored
    """

    force_external_id: Annotated[Optional[bool], PropertyInfo(alias="forceExternalId")]

    gender: Optional[Literal["-", "M", "F"]]


class Address(TypedDict, total=False):
    address_line1: Required[Annotated[Optional[str], PropertyInfo(alias="addressLine1")]]

    address_line2: Required[Annotated[Optional[str], PropertyInfo(alias="addressLine2")]]

    city: Required[Optional[str]]

    country: Required[Optional[str]]

    email: Required[Optional[str]]

    phone: Required[Optional[str]]

    zip_code: Required[Annotated[Optional[str], PropertyInfo(alias="zipCode")]]
