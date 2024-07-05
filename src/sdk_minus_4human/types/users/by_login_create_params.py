# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ByLoginCreateParams"]


class ByLoginCreateParams(TypedDict, total=False):
    body: Required[List[str]]

    find_by: Annotated[Literal["activeDirectoryUsername", "email"], PropertyInfo(alias="findBy")]
    """filter users by given type"""
