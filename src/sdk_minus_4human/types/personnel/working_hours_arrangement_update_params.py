# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WorkingHoursArrangementUpdateParams"]


class WorkingHoursArrangementUpdateParams(TypedDict, total=False):
    external: bool
    """Param determines if `id` is external (`externalId`) or internal (`id`)"""

    description: Optional[str]

    external_id: Annotated[Optional[str], PropertyInfo(alias="externalId")]

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]

    name: str

    status: Literal["active", "archived"]

    working_hours_per_week: Annotated[float, PropertyInfo(alias="workingHoursPerWeek")]
