# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResourceTypeUpdateParams"]


class ResourceTypeUpdateParams(TypedDict, total=False):
    description: Optional[str]

    name: str

    status: Literal["active", "archived"]

    type_id: Annotated[str, PropertyInfo(alias="typeId")]
