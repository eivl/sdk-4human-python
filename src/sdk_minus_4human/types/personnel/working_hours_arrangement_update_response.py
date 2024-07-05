# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WorkingHoursArrangementUpdateResponse"]


class WorkingHoursArrangementUpdateResponse(BaseModel):
    id: Optional[str] = None

    description: Optional[str] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    internal_id: Optional[str] = FieldInfo(alias="internalId", default=None)

    name: Optional[str] = None

    status: Optional[str] = None

    working_hours_per_week: Optional[float] = FieldInfo(alias="workingHoursPerWeek", default=None)
