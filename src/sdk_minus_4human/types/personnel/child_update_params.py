# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ChildUpdateParams", "ChronicallySick"]


class ChildUpdateParams(TypedDict, total=False):
    birth_date: Annotated[str, PropertyInfo(alias="birthDate")]

    chronically_sick: Annotated[ChronicallySick, PropertyInfo(alias="chronicallySick")]

    do_i_have_care: Annotated[bool, PropertyInfo(alias="doIHaveCare")]

    firstname: str

    gender: Optional[Literal["-", "M", "F"]]

    phone_number: Annotated[Optional[str], PropertyInfo(alias="phoneNumber")]

    single_parent: Annotated[bool, PropertyInfo(alias="singleParent")]

    surname: str


_ChronicallySickReservedKeywords = TypedDict(
    "_ChronicallySickReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class ChronicallySick(_ChronicallySickReservedKeywords, total=False):
    to: Required[Optional[str]]
