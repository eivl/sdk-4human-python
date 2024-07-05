# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UnitTypeListResponse", "Item"]


class Item(BaseModel):
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


class UnitTypeListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None
    """Currently used limit requested for pagination purposes"""

    page: Optional[int] = None
    """Current page when paginating"""

    pages: Optional[int] = None
    """Number of pages with regard to total number of records and page size"""

    total: Optional[int] = None
    """Total number of items in the system"""
