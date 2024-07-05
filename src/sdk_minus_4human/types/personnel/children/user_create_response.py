# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["UserCreateResponse", "ChronicallySick"]


class ChronicallySick(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class UserCreateResponse(BaseModel):
    id: str

    birth_date: str = FieldInfo(alias="birthDate")

    chronically_sick: ChronicallySick = FieldInfo(alias="chronicallySick")

    do_i_have_care: bool = FieldInfo(alias="doIHaveCare")

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    firstname: str

    gender: Optional[Literal["-", "M", "F"]] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    single_parent: bool = FieldInfo(alias="singleParent")

    surname: str
