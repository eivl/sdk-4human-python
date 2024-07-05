# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["GlobalListResponse", "Item", "ItemPlacing"]


class ItemPlacing(BaseModel):
    context: Optional[Literal["employment", "companyEmployee", "global"]] = None

    section: Optional[
        Literal[
            "details",
            "employment",
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
    ] = None
    """
    Section in simple way defines on UI "place where custom field should be
    displayed.
    """


class Item(BaseModel):
    id: str

    children: Optional[List[object]] = None

    children_dimension_id: Optional[str] = FieldInfo(alias="childrenDimensionId", default=None)
    """UUID of dimension"""

    children_dimension_name: Optional[str] = FieldInfo(alias="childrenDimensionName", default=None)
    """Name of sub level custom field attribute."""

    children_dimension_status: Optional[Literal["ACTIVE", "INACTIVE"]] = FieldInfo(
        alias="childrenDimensionStatus", default=None
    )

    dimension_id: str = FieldInfo(alias="dimensionId")
    """UUID of dimension (sub-attribute of custom field)"""

    dimension_name: str = FieldInfo(alias="dimensionName")
    """Name of sub level custom field attribute."""

    dimension_status: Literal["ACTIVE", "INACTIVE"] = FieldInfo(alias="dimensionStatus")

    external_id: str = FieldInfo(alias="externalId")
    """externalId of custom field value"""

    external_name: Optional[str] = FieldInfo(alias="externalName", default=None)
    """External name of custom field value"""

    field_type: Literal["structure", "select", "input", "textArea", "date", "checkbox"] = FieldInfo(alias="fieldType")

    internal_id: str = FieldInfo(alias="internalId")
    """internalId of custom field value"""

    is_value: bool = FieldInfo(alias="isValue")
    """determines if dimension contains custom value."""

    name: str
    """Name of custom field value"""

    placing: Optional[ItemPlacing] = None
    """Placing object defines scope in witch custom field should be displayed.

    (i.g. global defines custom fields direct assigned to user)
    """

    status: Literal["ACTIVE", "INACTIVE"]


class GlobalListResponse(BaseModel):
    items: List[Item]
