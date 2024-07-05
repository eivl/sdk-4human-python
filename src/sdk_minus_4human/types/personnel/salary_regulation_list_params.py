# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalaryRegulationListParams"]


class SalaryRegulationListParams(TypedDict, total=False):
    limit: int

    page: int

    reference_id: Annotated[str, PropertyInfo(alias="referenceId")]
