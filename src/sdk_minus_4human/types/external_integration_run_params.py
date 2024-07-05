# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExternalIntegrationRunParams"]


class ExternalIntegrationRunParams(TypedDict, total=False):
    feature_name: Required[Annotated[str, PropertyInfo(alias="featureName")]]

    cron_expression: Annotated[Optional[str], PropertyInfo(alias="cronExpression")]

    run_hours: Annotated[List[str], PropertyInfo(alias="runHours")]
