# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ResourceTypeRetrieveResponse"]


class ResourceTypeRetrieveResponse(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    name: Optional[str] = None

    status: Optional[Literal["active", "archived"]] = None

    type_id: Optional[str] = FieldInfo(alias="typeId", default=None)
