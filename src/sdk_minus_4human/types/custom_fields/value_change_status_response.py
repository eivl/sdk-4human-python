# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ValueChangeStatusResponse", "Items", "ItemsItem", "ItemsItemPlacing", "UnionMember1", "UnionMember1Placing"]


class ItemsItemPlacing(BaseModel):
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


class ItemsItem(BaseModel):
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

    placing: Optional[ItemsItemPlacing] = None
    """Placing object defines scope in witch custom field should be displayed.

    (i.g. global defines custom fields direct assigned to user)
    """

    status: Literal["ACTIVE", "INACTIVE"]


class Items(BaseModel):
    items: List[ItemsItem]


class UnionMember1Placing(BaseModel):
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


class UnionMember1(BaseModel):
    id: str

    children: Optional[List[object]] = None

    children_dimension_id: Optional[str] = FieldInfo(alias="childrenDimensionId", default=None)

    children_dimension_name: Optional[str] = FieldInfo(alias="childrenDimensionName", default=None)

    children_dimension_status: Optional[Literal["ACTIVE", "INACTIVE"]] = FieldInfo(
        alias="childrenDimensionStatus", default=None
    )

    dimension_id: str = FieldInfo(alias="dimensionId")

    dimension_name: str = FieldInfo(alias="dimensionName")

    dimension_status: Literal["ACTIVE", "INACTIVE"] = FieldInfo(alias="dimensionStatus")

    external_id: str = FieldInfo(alias="externalId")
    """
    Can be treated as "Id of value from external system" used to find values in hr
    master by their own known id.
    """

    external_name: Optional[str] = FieldInfo(alias="externalName", default=None)
    """
    Can be treated as "Name of value from external system" used to find values in hr
    master by their own known name.
    """

    field_type: Literal["structure", "select"] = FieldInfo(alias="fieldType")

    internal_id: str = FieldInfo(alias="internalId")

    is_value: bool = FieldInfo(alias="isValue")

    name: str

    placing: Optional[UnionMember1Placing] = None

    status: Literal["ACTIVE", "INACTIVE"]


ValueChangeStatusResponse = Union[Items, UnionMember1]
