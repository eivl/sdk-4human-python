# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PersonnelUpdateParams", "CustomField"]


class PersonnelUpdateParams(TypedDict, total=False):
    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]


class CustomField(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]

    value_id: Required[Annotated[Optional[str], PropertyInfo(alias="valueId")]]

    value: Optional[str]
