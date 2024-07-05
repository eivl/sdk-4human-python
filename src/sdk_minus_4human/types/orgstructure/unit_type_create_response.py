# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UnitTypeCreateResponse"]


class UnitTypeCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unit type internal ID"""

    description: Optional[str] = None
    """Unit type additional description"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID of unit type, allowing to store the ID of the client's system"""

    name: Optional[str] = None
    """Unit type name"""

    status: Optional[Literal["active", "draft", "archived"]] = None
    """Unit type status"""

    type_id: Optional[str] = FieldInfo(alias="typeId", default=None)
    """Unit type string identified, used for translation purposes.

    Although the name is fixed, typeId might be used to represent a translatable
    entity.
    """
