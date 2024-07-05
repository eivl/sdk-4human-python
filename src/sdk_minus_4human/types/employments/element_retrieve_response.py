# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ElementRetrieveResponse", "AdditionalSalary", "Benefit", "Deduction"]


class AdditionalSalary(BaseModel):
    id: Optional[int] = None

    amount: Optional[float] = None

    currency: Optional[str] = None

    details: Optional[str] = None

    individual: Optional[bool] = None

    name: Optional[str] = None

    period: Optional[
        Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
    ] = None

    type: Optional[Literal["text", "rate"]] = None


class Benefit(BaseModel):
    id: Optional[int] = None

    amount: Optional[float] = None

    currency: Optional[str] = None

    details: Optional[str] = None

    individual: Optional[bool] = None

    name: Optional[str] = None

    period: Optional[
        Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
    ] = None

    type: Optional[Literal["text", "rate"]] = None


class Deduction(BaseModel):
    id: Optional[int] = None

    amount: Optional[float] = None

    currency: Optional[str] = None

    details: Optional[str] = None

    individual: Optional[bool] = None

    name: Optional[str] = None

    period: Optional[
        Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
    ] = None

    type: Optional[Literal["text", "rate"]] = None


class ElementRetrieveResponse(BaseModel):
    additional_salaries: Optional[List[AdditionalSalary]] = FieldInfo(alias="additionalSalaries", default=None)

    benefits: Optional[List[Benefit]] = None

    deductions: Optional[List[Deduction]] = None
