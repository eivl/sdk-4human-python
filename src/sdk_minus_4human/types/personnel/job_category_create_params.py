# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobCategoryCreateParams"]


class JobCategoryCreateParams(TypedDict, total=False):
    description: Required[Optional[str]]
    """Job category additional description"""

    external_id: Required[Annotated[Optional[str], PropertyInfo(alias="externalId")]]
    """External ID, allowing to store the ID of the client's system"""

    internal_id: Required[Annotated[str, PropertyInfo(alias="internalId")]]
    """Internal ID provided, must be unique"""

    name: Required[str]
    """Job category name, must be unique"""
