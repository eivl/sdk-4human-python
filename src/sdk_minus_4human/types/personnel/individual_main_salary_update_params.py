# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IndividualMainSalaryUpdateParams"]


class IndividualMainSalaryUpdateParams(TypedDict, total=False):
    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]

    job_type_ids: Annotated[Optional[Iterable[int]], PropertyInfo(alias="jobTypeIds")]

    name: str

    period: Literal[
        "INDIVIDUAL_MAIN_SALARY_PERIOD_HOUR",
        "INDIVIDUAL_MAIN_SALARY_PERIOD_WEEK",
        "INDIVIDUAL_MAIN_SALARY_PERIOD_MONTH",
        "INDIVIDUAL_MAIN_SALARY_PERIOD_YEAR",
    ]

    rate_based_on_wha: Annotated[bool, PropertyInfo(alias="rateBasedOnWHA")]

    status: Literal["active", "inactive", "archived"]
