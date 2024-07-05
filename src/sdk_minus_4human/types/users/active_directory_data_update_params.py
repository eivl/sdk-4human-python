# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActiveDirectoryDataUpdateParams"]


class ActiveDirectoryDataUpdateParams(TypedDict, total=False):
    active_directory_username: Annotated[Optional[str], PropertyInfo(alias="activeDirectoryUsername")]

    email: Optional[str]
