# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["BenefitUpdateParams", "EffectiveDates"]


class BenefitUpdateParams(TypedDict, total=False):
    additional_main_salary: Annotated[bool, PropertyInfo(alias="additionalMainSalary")]

    amount: Optional[str]

    currency: Optional[str]

    description: Optional[str]

    effective_dates: Annotated[EffectiveDates, PropertyInfo(alias="effectiveDates")]
    """
    - If effectiveDates are not provided, the changes will be immediate.
    - Only following fields can be scheduled: `amount`, `currency`, `description`.
      Other fields will be changed immediately.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    include_to_contract: Annotated[bool, PropertyInfo(alias="includeToContract")]

    individual: bool

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]

    job_ids: Annotated[Optional[Iterable[int]], PropertyInfo(alias="jobIds")]

    mandatory: bool

    name: str

    org_unit_ids: Annotated[Iterable[int], PropertyInfo(alias="orgUnitIds")]
    """Does not work currently, it is for future uses"""

    period: Optional[Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]]

    show_in_profile: Annotated[bool, PropertyInfo(alias="showInProfile")]
    """Does not affect the system, will be supported in next version"""

    status: Literal["active", "inactive"]

    type: Literal["rate", "text"]


class EffectiveDates(TypedDict, total=False):
    comment: Required[Optional[str]]

    end_validity_date: Required[
        Annotated[Union[str, datetime, None], PropertyInfo(alias="endValidityDate", format="iso8601")]
    ]

    immediate: Required[Optional[bool]]

    start_validity_date: Required[
        Annotated[Union[str, datetime, None], PropertyInfo(alias="startValidityDate", format="iso8601")]
    ]
