# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrgstructureListResponse", "Item", "ItemLocation", "ItemManager"]


class ItemLocation(BaseModel):
    id: Optional[int] = None
    """database id of location"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """external id of location"""

    inherited: Optional[bool] = None
    """true if location is inherited from parent unit.

    Locations are inherited from level of company and below (but in scope of
    company)
    """

    org_unit_name: Optional[str] = FieldInfo(alias="orgUnitName", default=None)
    """name of unit that location belongs to"""


class ItemManager(BaseModel):
    id: Optional[int] = None
    """database id of unit manager"""

    inherited: Optional[bool] = None

    org_unit_name: Optional[str] = FieldInfo(alias="orgUnitName", default=None)
    """name of unit or company"""


class Item(BaseModel):
    id: Optional[int] = None
    """database id of unit"""

    ancestors: Optional[List[int]] = None
    """
    These are the units that are higher up in the hierarchy relative to the current
    unit. They are essentially the parent units of the current unit.
    """

    children: Optional[List[object]] = None
    """contains child units of the current unit"""

    company: Optional[bool] = None
    """true if unit is company false if unit."""

    company_country: Optional[str] = FieldInfo(alias="companyCountry", default=None)
    """ISO 3166-1 alpha-3 country code"""

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)
    """database id of company"""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """Name of the company"""

    descendants: Optional[List[int]] = None
    """
    These are the units that are lower down in the hierarchy relative to the current
    unit. They are essentially the child units of the current unit.
    """

    has_company: Optional[bool] = FieldInfo(alias="hasCompany", default=None)
    """true if unit has company"""

    leader_id: Optional[int] = FieldInfo(alias="leaderId", default=None)
    """Manager ID which is in fact an employment ID (personnel employment ID)"""

    level: Optional[int] = None
    """level of unit in hierarchy"""

    location: Optional[ItemLocation] = None

    manager: Optional[ItemManager] = None
    """Entity that represents unit manager"""

    name: Optional[str] = None
    """name of unit or company"""

    parent_id: Optional[int] = FieldInfo(alias="parentId", default=None)
    """database id of parent unit"""

    salary_system_company_id: Optional[str] = FieldInfo(alias="salarySystemCompanyId", default=None)
    """Additional unit identifier, to be used freely by the application users"""

    status: Optional[Literal["ACTIVE", "INACTIVE"]] = None

    unit_id: Optional[str] = FieldInfo(alias="unitId", default=None)
    """Additional unit identifier, to be used freely by the application users."""


class OrgstructureListResponse(BaseModel):
    items: Optional[List[Item]] = None

    total: Optional[int] = None
