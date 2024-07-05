# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["DimensionUpdateParams"]


class DimensionUpdateParams(TypedDict, total=False):
    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    external_name: Annotated[str, PropertyInfo(alias="externalName")]

    internal_id: Annotated[str, PropertyInfo(alias="internalId")]

    name: str
