# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["FieldCreateResponse", "Item", "ItemPlacing"]


class ItemPlacing(BaseModel):
    context: Optional[Literal["employment", "companyEmployee"]] = None

    section: Optional[Literal["details"]] = None


class Item(BaseModel):
    id: str

    children: Optional[List[object]] = None

    description: Optional[str] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    external_name: Optional[str] = FieldInfo(alias="externalName", default=None)

    internal_id: Optional[str] = FieldInfo(alias="internalId", default=None)

    mandatory: Optional[bool] = None

    name: str

    status: Literal["ACTIVE", "INACTIVE"]

    field_type: Optional[Literal["structure"]] = FieldInfo(alias="fieldType", default=None)

    icon_color: Optional[
        Literal[
            "darkblue100",
            "royalBlue100",
            "secondary105",
            "dodgerBlue100",
            "khaki100",
            "mediumPurple100",
            "indigo100",
            "purple100",
            "violetRed100",
            "hotPink100",
            "chocolate100",
            "dimGray100",
            "orangeRed100",
            "lightCoral100",
            "primaryBlack100",
            "teal100",
            "green130",
            "darkGreen100",
            "green110",
            "seaGreen100",
        ]
    ] = FieldInfo(alias="iconColor", default=None)

    is_global: Optional[bool] = FieldInfo(alias="isGlobal", default=None)

    placing: Optional[ItemPlacing] = None

    validators: Optional[List[Optional[str]]] = None


class FieldCreateResponse(BaseModel):
    items: List[Item]
