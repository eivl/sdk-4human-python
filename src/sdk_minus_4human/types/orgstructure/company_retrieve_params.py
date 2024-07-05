# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CompanyRetrieveParams"]


class CompanyRetrieveParams(TypedDict, total=False):
    external: bool
    """Param determines if id of unit is external (unitId) or internal (id)"""

    on_given_date: Annotated[str, PropertyInfo(alias="onGivenDate")]
    """Param allows you to specify effective date of company employee data."""

    with_soft_deleted: Annotated[bool, PropertyInfo(alias="withSoftDeleted")]
    """Param determines if deleted company should be fetched"""
