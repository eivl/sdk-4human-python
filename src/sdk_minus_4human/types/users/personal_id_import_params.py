# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PersonalIDImportParams"]


class PersonalIDImportParams(TypedDict, total=False):
    id_country: Required[Annotated[Optional[str], PropertyInfo(alias="idCountry")]]
    """Country of document"""

    id_number: Required[Annotated[Optional[str], PropertyInfo(alias="idNumber")]]
    """Document number"""

    id_type: Required[Annotated[Optional[Literal["none", "alternative_id", "ssn"]], PropertyInfo(alias="idType")]]
    """Type of document"""

    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    passport_country: Annotated[Optional[str], PropertyInfo(alias="passportCountry")]
    """Country of passport"""

    passport_number: Annotated[Optional[str], PropertyInfo(alias="passportNumber")]
    """Passport number"""
