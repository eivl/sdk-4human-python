# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TemplateUpdateParams"]


class TemplateUpdateParams(TypedDict, total=False):
    description: Required[Optional[str]]

    external_id: Required[Annotated[str, PropertyInfo(alias="externalId")]]

    name: Required[str]
