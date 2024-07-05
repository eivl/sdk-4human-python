# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UnitUpdateParams", "CustomField"]


class UnitUpdateParams(TypedDict, total=False):
    name: Required[str]

    unit_id: Required[Annotated[str, PropertyInfo(alias="unitId")]]
    """Additional unit identifier, to be used freely by the application users."""

    external: bool
    """Param determines if id of unit is external (unitId) or internal (id)"""

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]

    manager_id: Annotated[Optional[int], PropertyInfo(alias="managerId")]
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    parent_id: Annotated[Optional[int], PropertyInfo(alias="parentId")]
    """database id of parent unit."""

    selected_company_number: Annotated[Optional[str], PropertyInfo(alias="selectedCompanyNumber")]

    status: Literal["ACTIVE", "INACTIVE"]
    """Unit status"""

    unit_type_id: Annotated[str, PropertyInfo(alias="unitTypeId")]
    """ID of a unit type"""


class CustomField(TypedDict, total=False):
    field_id: Annotated[str, PropertyInfo(alias="fieldId")]
    """UUID of a given custom field"""

    value_id: Annotated[Optional[str], PropertyInfo(alias="valueId")]
    """UUID of a given value of a custom field"""
