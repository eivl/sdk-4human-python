# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccessGroupAssignParams"]


class AccessGroupAssignParams(TypedDict, total=False):
    group_ids: Required[Annotated[List[str], PropertyInfo(alias="groupIds")]]
    """Array of access group UUIDs"""

    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]
