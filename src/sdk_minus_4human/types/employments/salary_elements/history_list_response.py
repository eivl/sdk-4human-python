# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["HistoryListResponse", "Item", "ItemAdditionalSalary", "ItemBenefit", "ItemDeduction"]


class ItemAdditionalSalary(BaseModel):
    amount: Optional[str] = None

    currency: Optional[str] = None

    details: Optional[str] = None

    individual: bool

    name: Optional[str] = None

    period: Optional[
        Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
    ] = None

    reference_id: float = FieldInfo(alias="referenceId")

    snapshot_id: float = FieldInfo(alias="snapshotId")

    type: Literal["text", "rate"]

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)

    description: Optional[str] = None


class ItemBenefit(BaseModel):
    amount: Optional[str] = None

    currency: Optional[str] = None

    description: Optional[str] = None

    details: Optional[str] = None

    individual: Optional[bool] = None

    name: Optional[str] = None

    period: Optional[
        Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
    ] = None

    reference_id: Optional[float] = FieldInfo(alias="referenceId", default=None)

    snapshot_id: Optional[float] = FieldInfo(alias="snapshotId", default=None)

    type: Optional[Literal["text", "rate"]] = None

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)


class ItemDeduction(BaseModel):
    amount: Optional[str] = None

    currency: Optional[str] = None

    details: Optional[str] = None

    individual: bool

    name: Optional[str] = None

    period: Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]

    reference_id: float = FieldInfo(alias="referenceId")

    snapshot_id: float = FieldInfo(alias="snapshotId")

    type: Literal["text", "rate"]

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)

    description: Optional[str] = None


class Item(BaseModel):
    additional_salaries: Optional[List[ItemAdditionalSalary]] = FieldInfo(alias="additionalSalaries", default=None)

    benefits: Optional[List[ItemBenefit]] = None

    deductions: Optional[List[ItemDeduction]] = None

    effective_status: Optional[str] = FieldInfo(alias="effectiveStatus", default=None)

    snapshot_id: Optional[float] = FieldInfo(alias="snapshotId", default=None)

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)


class HistoryListResponse(BaseModel):
    items: List[Item]

    limit: float

    page: float

    pages: float

    total: float
