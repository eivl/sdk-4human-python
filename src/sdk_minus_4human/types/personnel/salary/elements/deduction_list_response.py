# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["DeductionListResponse", "Item", "ItemJob"]


class ItemJob(BaseModel):
    id: int

    title: str


class Item(BaseModel):
    id: Optional[int] = None

    additional_main_salary: Optional[bool] = FieldInfo(alias="additionalMainSalary", default=None)

    individual: Optional[bool] = None

    jobs: Optional[List[ItemJob]] = None

    mandatory: Optional[bool] = None

    name: Optional[str] = None

    org_units: Optional[List[object]] = FieldInfo(alias="orgUnits", default=None)

    period: Optional[
        Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
    ] = None

    status: Optional[Literal["active", "inactive"]] = None


class DeductionListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
