# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ValueUpdatePartialParams"]


class ValueUpdatePartialParams(TypedDict, total=False):
    return_single_item: Annotated[bool, PropertyInfo(alias="returnSingleItem")]
    """
    Param determines whether a single item or the entire tree structure will be
    returned in the response
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    Can be treated as "Id of value from external system" used to find values in hr
    master by their own known id.
    """

    external_name: Annotated[str, PropertyInfo(alias="externalName")]
    """
    Can be treated as "Name of value from external system" used to find values in hr
    master by their own known name.
    """

    internal_id: Annotated[Optional[str], PropertyInfo(alias="internalId")]

    name: Optional[str]
    """Field contains name of custom field value or custom value provided by user (i.e.

    text, number, date)
    """
