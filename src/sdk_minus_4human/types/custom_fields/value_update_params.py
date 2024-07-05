# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ValueUpdateParams"]


class ValueUpdateParams(TypedDict, total=False):
    external_id: Required[Annotated[str, PropertyInfo(alias="externalId")]]
    """
    Can be treated as "Id of value from external system" used to find values in hr
    master by their own known id.
    """

    external_name: Required[Annotated[str, PropertyInfo(alias="externalName")]]
    """
    Can be treated as "Id of value from external system" used to find values in hr
    master by their own known id.
    """

    internal_id: Required[Annotated[Optional[str], PropertyInfo(alias="internalId")]]

    name: Required[Optional[str]]
    """Field contains name of custom field value or custom value provided by user (i.e.

    text, number, date)
    """

    return_single_item: Annotated[bool, PropertyInfo(alias="returnSingleItem")]
    """
    Param determines whether a single item or the entire tree structure will be
    returned in the response
    """
