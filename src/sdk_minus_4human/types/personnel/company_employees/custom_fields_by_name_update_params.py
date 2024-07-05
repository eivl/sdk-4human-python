# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CustomFieldsByNameUpdateParams", "CustomField", "EffectiveDates"]


class CustomFieldsByNameUpdateParams(TypedDict, total=False):
    external: bool
    """Param determines if id of employment is external (employeeId) or internal (id)"""

    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]

    effective_dates: Annotated[EffectiveDates, PropertyInfo(alias="effectiveDates")]
    """If effectiveDates are not provided, the changes will be immediate"""


class CustomField(TypedDict, total=False):
    field_external_id: Annotated[str, PropertyInfo(alias="fieldExternalId")]

    field_external_name: Annotated[Optional[str], PropertyInfo(alias="fieldExternalName")]

    value: Optional[str]
    """For custom fields of type date, time and timezone must be reset e.g.

    1986-03-28T00:00:00+00:00
    """

    value_external_id: Annotated[Optional[str], PropertyInfo(alias="valueExternalId")]

    value_external_name: Annotated[Optional[str], PropertyInfo(alias="valueExternalName")]


class EffectiveDates(TypedDict, total=False):
    comment: Required[Optional[str]]

    end_validity_date: Required[Annotated[Optional[str], PropertyInfo(alias="endValidityDate")]]

    immediate: Required[Optional[bool]]

    start_validity_date: Required[Annotated[Optional[str], PropertyInfo(alias="startValidityDate")]]
