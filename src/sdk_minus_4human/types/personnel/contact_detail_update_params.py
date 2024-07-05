# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContactDetailUpdateParams"]


class ContactDetailUpdateParams(TypedDict, total=False):
    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    address: Optional[str]
    """Private primary address"""

    building_entrance: Annotated[Optional[str], PropertyInfo(alias="buildingEntrance")]
    """Private primary address"""

    city: Optional[str]
    """Private primary address"""

    country: Optional[str]
    """Private primary address"""

    municipality: Optional[str]
    """Private primary address"""

    private_email: Annotated[Optional[str], PropertyInfo(alias="privateEmail")]

    private_mobile_phone: Annotated[Optional[str], PropertyInfo(alias="privateMobilePhone")]

    private_phone: Annotated[Optional[str], PropertyInfo(alias="privatePhone")]

    work_email: Annotated[Optional[str], PropertyInfo(alias="workEmail")]

    work_mobile_phone: Annotated[Optional[str], PropertyInfo(alias="workMobilePhone")]

    work_phone: Annotated[Optional[str], PropertyInfo(alias="workPhone")]

    zip_code: Annotated[Optional[str], PropertyInfo(alias="zipCode")]
    """Private primary address"""
