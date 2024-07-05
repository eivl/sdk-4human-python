# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WorkingHoursArrangementCreateParams"]


class WorkingHoursArrangementCreateParams(TypedDict, total=False):
    description: Required[Optional[str]]

    external_id: Required[Annotated[Optional[str], PropertyInfo(alias="externalId")]]

    internal_id: Required[Annotated[str, PropertyInfo(alias="internalId")]]

    name: Required[str]

    status: Required[Literal["active", "archived"]]

    working_hours_per_week: Required[Annotated[float, PropertyInfo(alias="workingHoursPerWeek")]]
