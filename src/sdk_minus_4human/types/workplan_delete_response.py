# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkplanDeleteResponse"]


class WorkplanDeleteResponse(BaseModel):
    employment_work_plan_calendar_delete_employment_ids_failure: Optional[List[float]] = FieldInfo(
        alias="employmentWorkPlanCalendarDeleteEmploymentIdsFailure", default=None
    )

    employment_work_plan_calendar_delete_employment_ids_success: Optional[List[float]] = FieldInfo(
        alias="employmentWorkPlanCalendarDeleteEmploymentIdsSuccess", default=None
    )
