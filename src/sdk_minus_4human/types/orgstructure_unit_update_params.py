# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgstructureUnitUpdateParams", "CustomField"]


class OrgstructureUnitUpdateParams(TypedDict, total=False):
    name: Required[str]

    unit_id: Required[Annotated[str, PropertyInfo(alias="unitId")]]
    """Additional unit identifier, to be used freely by the application users"""

    unit_type_id: Required[Annotated[str, PropertyInfo(alias="unitTypeId")]]

    external: bool
    """Param determines if id of unit is external (unitId) or internal (id)"""

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]

    manager_id: Annotated[Optional[int], PropertyInfo(alias="managerId")]
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    parent_id: Annotated[Optional[int], PropertyInfo(alias="parentId")]
    """ID of the parent organization structure unit.

    It might be null if root unit is added. The ID is the internal 4human's unit ID.
    """

    status: Literal["ACTIVE", "INACTIVE"]


class CustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]
    """UUID of a given custom field"""

    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]
    """UUID of a given value of a custom field"""
