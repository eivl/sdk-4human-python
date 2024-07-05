# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PersonnelUpdateResponse", "CustomField"]


class CustomField(BaseModel):
    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    field: Optional[str] = None

    field_created_at: Optional[str] = FieldInfo(alias="fieldCreatedAt", default=None)

    field_external_id: Optional[str] = FieldInfo(alias="fieldExternalId", default=None)

    field_external_name: Optional[str] = FieldInfo(alias="fieldExternalName", default=None)

    field_id: Optional[str] = FieldInfo(alias="fieldId", default=None)

    field_updated_at: Optional[str] = FieldInfo(alias="fieldUpdatedAt", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    value: Optional[str] = None

    value_created_at: Optional[str] = FieldInfo(alias="valueCreatedAt", default=None)

    value_external_id: Optional[str] = FieldInfo(alias="valueExternalId", default=None)

    value_external_name: Optional[str] = FieldInfo(alias="valueExternalName", default=None)

    value_id: Optional[str] = FieldInfo(alias="valueId", default=None)

    value_updated_at: Optional[str] = FieldInfo(alias="valueUpdatedAt", default=None)


class PersonnelUpdateResponse(BaseModel):
    custom_fields: Optional[List[CustomField]] = FieldInfo(alias="customFields", default=None)
