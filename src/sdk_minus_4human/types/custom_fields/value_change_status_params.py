# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ValueChangeStatusParams"]


class ValueChangeStatusParams(TypedDict, total=False):
    return_single_item: Annotated[bool, PropertyInfo(alias="returnSingleItem")]
    """
    Param determines whether a single item or the entire tree structure will be
    returned in the response
    """

    id: Literal["ACTIVE", "INACTIVE"]
