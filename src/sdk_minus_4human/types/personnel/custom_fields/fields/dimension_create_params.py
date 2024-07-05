# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["DimensionCreateParams"]


class DimensionCreateParams(TypedDict, total=False):
    external_id: Required[Annotated[str, PropertyInfo(alias="externalId")]]

    external_name: Required[Annotated[str, PropertyInfo(alias="externalName")]]

    internal_id: Required[Annotated[str, PropertyInfo(alias="internalId")]]

    name: Required[str]
