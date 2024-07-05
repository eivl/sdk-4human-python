# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgstructureUnitCreateParams", "CustomField"]


class OrgstructureUnitCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the new unit"""

    unit_type_id: Required[Annotated[str, PropertyInfo(alias="unitTypeId")]]
    """ID of a unit type"""

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]
    """Custom field values, assigned to a given organizational unit."""

    manager_id: Annotated[Optional[int], PropertyInfo(alias="managerId")]
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    parent_id: Annotated[Optional[int], PropertyInfo(alias="parentId")]
    """ID of the parent organization structure unit.

    It might be null if root unit is added. The ID is the internal 4human's unit ID.
    """

    selected_company_number: Annotated[Optional[str], PropertyInfo(alias="selectedCompanyNumber")]
    """Additional company number coming from BRREG"""

    status: Literal["ACTIVE", "INACTIVE"]
    """Unit status"""

    unit_id: Annotated[Optional[str], PropertyInfo(alias="unitId")]
    """Additional unit identifier, to be used freely by the application users."""


class CustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]
    """UUID of a given custom field"""

    value_id: Required[Annotated[str, PropertyInfo(alias="valueId")]]
    """UUID of a given value of a custom field"""
