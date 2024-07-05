# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["DeductionRetrieveResponse", "Job"]


class Job(BaseModel):
    id: int

    title: str


class DeductionRetrieveResponse(BaseModel):
    id: Optional[int] = None

    additional_main_salary: Optional[bool] = FieldInfo(alias="additionalMainSalary", default=None)

    amount: Optional[str] = None

    currency: Optional[str] = None

    description: Optional[str] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    include_to_contract: Optional[bool] = FieldInfo(alias="includeToContract", default=None)

    individual: Optional[bool] = None

    internal_id: Optional[str] = FieldInfo(alias="internalId", default=None)

    jobs: Optional[List[Job]] = None

    mandatory: Optional[bool] = None

    name: Optional[str] = None

    org_units: Optional[List[object]] = FieldInfo(alias="orgUnits", default=None)

    period: Optional[
        Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
    ] = None

    show_in_profile: Optional[bool] = FieldInfo(alias="showInProfile", default=None)

    status: Optional[Literal["active", "inactive"]] = None

    type: Optional[Literal["rate", "text"]] = None
