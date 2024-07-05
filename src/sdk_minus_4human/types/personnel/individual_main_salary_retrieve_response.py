# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IndividualMainSalaryRetrieveResponse", "JobType"]


class JobType(BaseModel):
    id: int

    title: str


class IndividualMainSalaryRetrieveResponse(BaseModel):
    id: Optional[int] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    internal_id: Optional[str] = FieldInfo(alias="internalId", default=None)

    job_types: Optional[List[JobType]] = FieldInfo(alias="jobTypes", default=None)

    name: Optional[str] = None

    period: Optional[
        Literal[
            "INDIVIDUAL_MAIN_SALARY_PERIOD_HOUR",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_WEEK",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_MONTH",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_YEAR",
        ]
    ] = None

    rate_based_on_wha: Optional[bool] = FieldInfo(alias="rateBasedOnWHA", default=None)

    status: Optional[Literal["active", "archived", "inactive"]] = None
