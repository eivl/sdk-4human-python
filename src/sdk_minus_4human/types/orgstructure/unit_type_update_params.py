# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UnitTypeUpdateParams"]


class UnitTypeUpdateParams(TypedDict, total=False):
    description: Required[Optional[str]]
    """Unit type additional description"""

    external_id: Required[Annotated[Optional[str], PropertyInfo(alias="externalId")]]
    """External ID of unit type, allowing to store the ID of the client's system"""

    name: Required[str]
    """Unit type name"""

    status: Required[Literal["active", "draft", "archived"]]
    """Unit type status"""

    type_id: Required[Annotated[Optional[str], PropertyInfo(alias="typeId")]]
    """Unit type string identified, used for translation purposes.

    Although the name is fixed, typeId might be used to represent a translatable
    entity.
    """
