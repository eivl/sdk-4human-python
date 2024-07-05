# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResourceTypeCreateParams"]


class ResourceTypeCreateParams(TypedDict, total=False):
    description: Required[Optional[str]]

    name: Required[str]

    type_id: Required[Annotated[str, PropertyInfo(alias="typeId")]]
