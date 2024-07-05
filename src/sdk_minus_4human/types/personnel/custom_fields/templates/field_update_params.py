# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["FieldUpdateParams", "Placing"]


class FieldUpdateParams(TypedDict, total=False):
    template_id: Required[Annotated[str, PropertyInfo(alias="templateId")]]

    external_id: Required[Annotated[str, PropertyInfo(alias="externalId")]]

    external_name: Required[Annotated[str, PropertyInfo(alias="externalName")]]

    internal_id: Required[Annotated[Optional[str], PropertyInfo(alias="internalId")]]

    name: Required[Optional[str]]

    placing: Optional[Placing]

    validators: Optional[List[Optional[str]]]


class Placing(TypedDict, total=False):
    context: Optional[Literal["employment", "companyEmployee"]]

    section: Optional[Literal["details"]]
