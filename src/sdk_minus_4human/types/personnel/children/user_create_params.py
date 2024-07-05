# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserCreateParams", "ChronicallySick"]


class UserCreateParams(TypedDict, total=False):
    birth_date: Required[Annotated[str, PropertyInfo(alias="birthDate")]]

    chronically_sick: Required[Annotated[ChronicallySick, PropertyInfo(alias="chronicallySick")]]

    do_i_have_care: Required[Annotated[bool, PropertyInfo(alias="doIHaveCare")]]

    firstname: Required[str]

    phone_number: Required[Annotated[Optional[str], PropertyInfo(alias="phoneNumber")]]

    single_parent: Required[Annotated[bool, PropertyInfo(alias="singleParent")]]

    surname: Required[str]

    external_id: Annotated[Optional[str], PropertyInfo(alias="externalId")]
    """
    To post externalId use additional parameter forceExternalId otherwise field will
    be ignored
    """

    force_external_id: Annotated[Optional[bool], PropertyInfo(alias="forceExternalId")]

    gender: Optional[Literal["-", "M", "F"]]


_ChronicallySickReservedKeywords = TypedDict(
    "_ChronicallySickReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class ChronicallySick(_ChronicallySickReservedKeywords, total=False):
    to: Required[Optional[str]]
