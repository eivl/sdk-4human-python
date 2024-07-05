# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IndividualMainSalaryCreateResponse", "Item", "ItemJobType"]


class ItemJobType(BaseModel):
    id: int

    title: str


class Item(BaseModel):
    id: Optional[int] = None

    job_types: Optional[List[ItemJobType]] = FieldInfo(alias="jobTypes", default=None)

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


class IndividualMainSalaryCreateResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
