# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["FieldCreateParams", "Placing"]


class FieldCreateParams(TypedDict, total=False):
    external_id: Required[Annotated[str, PropertyInfo(alias="externalId")]]

    external_name: Required[Annotated[str, PropertyInfo(alias="externalName")]]

    internal_id: Required[Annotated[str, PropertyInfo(alias="internalId")]]

    name: Required[str]

    children: Iterable[object]

    field_type: Annotated[Literal["structure", "date", "input", "textArea", "select"], PropertyInfo(alias="fieldType")]

    placing: Placing

    validators: Optional[List[Literal["short", "medium", "long", "email", "number", "phone"]]]


class Placing(TypedDict, total=False):
    context: Required[Literal["employment", "companyEmployee", "global"]]

    section: Required[
        Literal[
            "employment",
            "details",
            "access",
            "timePeriods",
            "salary",
            "costPlace",
            "contact",
            "employeeDetails",
            "industryId",
            "employeeTimePeriods",
            "personalDetails",
            "login",
            "identification",
            "privateContactDetails",
            "paymentDetails",
            "nextOfKin",
            "children",
        ]
    ]
