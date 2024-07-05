# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["BenefitCreateParams"]


class BenefitCreateParams(TypedDict, total=False):
    amount: Required[Optional[str]]

    currency: Required[Optional[str]]

    description: Required[Optional[str]]

    external_id: Required[Annotated[str, PropertyInfo(alias="externalId")]]

    include_to_contract: Required[Annotated[bool, PropertyInfo(alias="includeToContract")]]

    individual: Required[bool]

    internal_id: Required[Annotated[str, PropertyInfo(alias="internalId")]]

    job_ids: Required[Annotated[Optional[Iterable[int]], PropertyInfo(alias="jobIds")]]

    mandatory: Required[bool]

    name: Required[str]

    org_unit_ids: Required[Annotated[Optional[Iterable[int]], PropertyInfo(alias="orgUnitIds")]]
    """Does not work currently, it is for future uses"""

    period: Required[
        Optional[Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]]
    ]

    show_in_profile: Required[Annotated[bool, PropertyInfo(alias="showInProfile")]]
    """Does not affect the system, will be supported in next version"""

    status: Required[Literal["active"]]

    type: Required[Literal["rate", "text"]]

    additional_main_salary: Annotated[bool, PropertyInfo(alias="additionalMainSalary")]
