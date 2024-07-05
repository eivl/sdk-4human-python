# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UnitTypeUpdateFieldParams"]


class UnitTypeUpdateFieldParams(TypedDict, total=False):
    description: Optional[str]
    """Unit type additional description"""

    external_id: Annotated[Optional[str], PropertyInfo(alias="externalId")]
    """External ID of unit type, allowing to store the ID of the client's system"""

    name: str
    """Unit type name"""

    status: Literal["active", "draft", "archived"]
    """Unit type status, might be"""

    type_id: Annotated[Optional[str], PropertyInfo(alias="typeId")]
    """Unit type string identified, used for translation purposes.

    Although the name is fixed, typeId might be used to represent a translatable
    entity.
    """
