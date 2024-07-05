# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmploymentRetrieveParams"]


class EmploymentRetrieveParams(TypedDict, total=False):
    external: bool
    """
    Param determines if "employmentId" is external (field called "number") or
    internal (field called "id")
    """

    on_given_date: Annotated[str, PropertyInfo(alias="onGivenDate")]
    """Param allows you to specify effective date of employment data."""
