# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AbsenceCodeListParams"]


class AbsenceCodeListParams(TypedDict, total=False):
    category: Literal["leave_of_absence", "other", "sick_leave", "vacation", "working"]
    """Filters absences by absence code category."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """Filters absences by absence code external ID."""

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]
    """Filters absences by absence code internal ID."""

    limit: int
    """Max returned results. Default 100."""

    page: int
    """Results page. Default 1."""

    status: Literal["active", "inactive", "archived"]
    """Filters absences by absence status."""

    type: Literal["self_certified", "documented", "paid", "not_paid", "sick_child", "no_types"]
    """Filters absences by absence code type."""
