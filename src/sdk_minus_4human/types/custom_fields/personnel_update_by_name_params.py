# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PersonnelUpdateByNameParams", "CustomField"]


class PersonnelUpdateByNameParams(TypedDict, total=False):
    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]


class CustomField(TypedDict, total=False):
    field_external_id: Annotated[str, PropertyInfo(alias="fieldExternalId")]
    """External id of custom field"""

    field_external_name: Annotated[Optional[str], PropertyInfo(alias="fieldExternalName")]
    """External name of custom field"""

    value: Optional[str]
    """Contains free text value.

    For various validations may have different length. For date type validation it
    should contain date in format the ISO 8601 i.g. 2024-06-26T00:00:00+00:00
    """

    value_external_id: Annotated[Optional[str], PropertyInfo(alias="valueExternalId")]
    """External id of custom field value"""

    value_external_name: Annotated[Optional[str], PropertyInfo(alias="valueExternalName")]
    """External name of custom field value"""
