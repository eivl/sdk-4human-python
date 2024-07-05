# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["JobCategoryUpdateParams"]


class JobCategoryUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Job category additional description"""

    external_id: Annotated[Optional[str], PropertyInfo(alias="externalId")]
    """External ID, allowing to store the ID of the client's system"""

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]
    """Internal ID provided, must be unique"""

    name: str
    """Job category name, must be unique"""
