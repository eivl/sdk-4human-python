# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HistoryListParams"]


class HistoryListParams(TypedDict, total=False):
    changes_from: Annotated[int, PropertyInfo(alias="changesFrom")]
    """Determines if snapshot was created or updated from selected unix timestamp."""

    changes_to: Annotated[int, PropertyInfo(alias="changesTo")]
    """Determines if snapshot was created or updated to selected unix timestamp."""

    effective_statuses: Annotated[str, PropertyInfo(alias="effectiveStatuses")]
    """Filter by effective status of snapshot - comma separated list.

    Available values are: ["past", "current", "future", "replaced", "canceled",
    "effected", "approved", "for_approval", "for_confirmation", "rejected"] Its
    possible to filter by multiple statuses (each should be comma separated)
    """

    external: bool
    """Param determines if id of employment is external (number) or internal (id)"""

    limit: int
    """Number of records returned in one request"""

    page: int
    """Number of returned page"""

    valid_from: Annotated[int, PropertyInfo(alias="validFrom")]

    valid_to: Annotated[int, PropertyInfo(alias="validTo")]