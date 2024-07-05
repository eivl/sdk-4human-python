# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DetailRetrieveResponse", "Agreements"]


class Agreements(BaseModel):
    hide_employee_id_strategy_modal: Optional[bool] = FieldInfo(alias="hideEmployeeIdStrategyModal", default=None)


class DetailRetrieveResponse(BaseModel):
    id: Optional[str] = None

    agreements: Optional[Agreements] = None

    application_language: Optional[str] = FieldInfo(alias="applicationLanguage", default=None)

    calculated_language: Optional[str] = FieldInfo(alias="calculatedLanguage", default=None)

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    email: Optional[str] = None

    employment_id: Optional[int] = FieldInfo(alias="employmentId", default=None)

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    instance_language: Optional[str] = FieldInfo(alias="instanceLanguage", default=None)

    instance_owner: Optional[bool] = FieldInfo(alias="instanceOwner", default=None)

    language: Optional[str] = None

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    permissions: Optional[List[str]] = None

    personal_permissions: Optional[List[str]] = FieldInfo(alias="personalPermissions", default=None)

    picture: Optional[str] = None

    roles: Optional[List[str]] = None

    status: Optional[int] = None
