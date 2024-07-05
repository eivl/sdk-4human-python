# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TemplateRetrieveResponse"]


class TemplateRetrieveResponse(BaseModel):
    id: str

    children: Optional[List[object]] = None

    description: Optional[str] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    external_name: Optional[str] = FieldInfo(alias="externalName", default=None)

    internal_id: Optional[str] = FieldInfo(alias="internalId", default=None)

    mandatory: Optional[bool] = None

    name: str

    status: Literal["ACTIVE", "INACTIVE"]
