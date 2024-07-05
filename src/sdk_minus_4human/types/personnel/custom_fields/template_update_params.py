# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TemplateUpdateParams"]


class TemplateUpdateParams(TypedDict, total=False):
    description: Optional[str]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    name: str
