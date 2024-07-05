# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomFieldChangeStatusParams"]


class CustomFieldChangeStatusParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    body_id: Annotated[Literal["ACTIVE", "INACTIVE"], PropertyInfo(alias="id")]
