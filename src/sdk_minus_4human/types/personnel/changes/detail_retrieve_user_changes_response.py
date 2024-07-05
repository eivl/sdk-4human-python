# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .detail_retrieve_user_changes_response import (
    ItemRelatedChangesCustomFieldUnnamedTypeWithobjectParent2ItemRelatedChangesCustomFieldUnnamedTypeWithobjectParent2Item,
)

__all__ = [
    "DetailRetrieveUserChangesResponse",
    "Item",
    "ItemActions",
    "ItemIdentifiers",
    "ItemIdentifiersUserInCompany",
    "ItemPosition",
    "ItemRegisteredBy",
    "ItemRelatedChanges",
    "ItemRelatedChangesUnionMember0",
    "ItemRelatedChangesCustomField",
    "ItemRelatedChangesCustomFieldCustomField",
    "ItemRelatedChangesCustomFieldCustomFieldNewValueProperties",
    "ItemRelatedChangesCustomFieldCustomFieldOldValueProperties",
]


class ItemActions(BaseModel):
    can_be_approved: Optional[bool] = FieldInfo(alias="canBeApproved", default=None)
    """Flag indicating if the change can be approved."""

    can_be_confirmed: Optional[bool] = FieldInfo(alias="canBeConfirmed", default=None)
    """Flag indicating if the change can be confirmed."""

    can_be_rejected: Optional[bool] = FieldInfo(alias="canBeRejected", default=None)
    """Flag indicating if the change can be rejected."""

    can_cancel_snapshot: Optional[bool] = FieldInfo(alias="canCancelSnapshot", default=None)
    """Flag indicating if the snapshot can be canceled."""


class ItemIdentifiers(BaseModel):
    birthdate: Optional[str] = None
    """The birthdate of the user."""

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """
    This field, in the scope of user changes, will be empty but is returned to be
    compatible with changes endpoints.
    """

    number: Optional[str] = None
    """
    This field, in the scope of user changes, will be empty but is returned to be
    compatible with changes endpoints.
    """


class ItemIdentifiersUserInCompany(BaseModel):
    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)
    """The ID of the company."""

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """The employee ID in the company."""

    organisation_number: Optional[str] = FieldInfo(alias="organisationNumber", default=None)
    """The organization number associated with the user."""


class ItemPosition(BaseModel):
    employment_id: Optional[int] = FieldInfo(alias="employmentId", default=None)
    """The ID of the personal attribute."""

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The job title of the personal attribute."""


class ItemRegisteredBy(BaseModel):
    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """The full name of the user who registered the personal attribute."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The ID of the user who registered the personal attribute."""


class ItemRelatedChangesUnionMember0(BaseModel):
    name: Optional[str] = None
    """The name of the related change."""

    new_value: Optional[str] = FieldInfo(alias="newValue", default=None)
    """The new value of the related change."""

    new_value_properties: Optional[object] = FieldInfo(alias="newValueProperties", default=None)
    """List of values related to the new changed value."""

    old_value: Optional[str] = FieldInfo(alias="oldValue", default=None)
    """The old value of the related change."""

    old_value_properties: Optional[object] = FieldInfo(alias="oldValueProperties", default=None)
    """List of values related to old changed value."""


class ItemRelatedChangesCustomFieldCustomFieldNewValueProperties(BaseModel):
    new_value: Optional[str] = FieldInfo(alias="newValue", default=None)

    new_value_id: Optional[str] = FieldInfo(alias="newValueId", default=None)

    value_path: Optional[str] = FieldInfo(alias="valuePath", default=None)


class ItemRelatedChangesCustomFieldCustomFieldOldValueProperties(BaseModel):
    old_value: Optional[str] = FieldInfo(alias="oldValue", default=None)

    old_value_id: Optional[str] = FieldInfo(alias="oldValueId", default=None)

    value_path: Optional[str] = FieldInfo(alias="valuePath", default=None)


class ItemRelatedChangesCustomFieldCustomField(BaseModel):
    custom_field_name: Optional[str] = FieldInfo(alias="customFieldName", default=None)

    field_id: Optional[str] = FieldInfo(alias="fieldId", default=None)

    new_value: Optional[str] = FieldInfo(alias="newValue", default=None)

    new_value_id: Optional[str] = FieldInfo(alias="newValueId", default=None)

    new_value_properties: Optional[ItemRelatedChangesCustomFieldCustomFieldNewValueProperties] = FieldInfo(
        alias="newValueProperties", default=None
    )

    old_value: Optional[str] = FieldInfo(alias="oldValue", default=None)

    old_value_id: Optional[str] = FieldInfo(alias="oldValueId", default=None)

    old_value_properties: Optional[ItemRelatedChangesCustomFieldCustomFieldOldValueProperties] = FieldInfo(
        alias="oldValueProperties", default=None
    )


class ItemRelatedChangesCustomField(BaseModel):
    custom_field: Optional[List[ItemRelatedChangesCustomFieldCustomField]] = FieldInfo(
        alias="customField", default=None
    )

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(
            self, attr: str
        ) -> ItemRelatedChangesCustomFieldUnnamedTypeWithobjectParent2ItemRelatedChangesCustomFieldUnnamedTypeWithobjectParent2Item:
            ...


ItemRelatedChanges = Union[List[ItemRelatedChangesUnionMember0], ItemRelatedChangesCustomField]


class Item(BaseModel):
    id: Optional[str] = None
    """The internal ID of the changed personal attribute."""

    actions: Optional[ItemActions] = None
    """Actions that can be performed on the personal attribute."""

    comment: Optional[str] = None
    """
    This field, in the scope of user changes, will be empty but is returned to be
    compatible with changes endpoints.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date when the personal attribute snapshot was created."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """The full name of the user."""

    identifiers: Optional[ItemIdentifiers] = None
    """Identifiers associated with the personal attribute."""

    identifiers_user_in_company: Optional[List[List[ItemIdentifiersUserInCompany]]] = FieldInfo(
        alias="identifiersUserInCompany", default=None
    )
    """Identifiers associated with the user in the company."""

    position: Optional[ItemPosition] = None
    """The position details."""

    reference_id: Optional[str] = FieldInfo(alias="referenceId", default=None)
    """The reference ID of the personal attribute."""

    registered_by: Optional[ItemRegisteredBy] = FieldInfo(alias="registeredBy", default=None)
    """The user who registered the change."""

    related_changes: Optional[ItemRelatedChanges] = FieldInfo(alias="relatedChanges", default=None)
    """Either an array or an object.

    Response becomes object if customFields are defined.
    """

    snapshot_id: Optional[str] = FieldInfo(alias="snapshotId", default=None)
    """The snapshot ID of the personal attribute."""

    status: Optional[str] = None
    """The status of the personal attribute snapshot."""

    total_comments: Optional[int] = FieldInfo(alias="totalComments", default=None)
    """The total number of comments."""

    type: Optional[str] = None
    """The type of change."""

    valid_from: Optional[datetime] = FieldInfo(alias="validFrom", default=None)
    """The start date of the change."""

    valid_to: Optional[datetime] = FieldInfo(alias="validTo", default=None)
    """The end date of the change."""


class DetailRetrieveUserChangesResponse(BaseModel):
    items: Optional[List[Item]] = None
    """List of changes on the user profile."""

    limit: Optional[int] = None
    """The limit of items per page."""

    page: Optional[int] = None
    """The current page number."""

    pages: Optional[int] = None
    """The total number of pages."""

    total: Optional[int] = None
    """The total number of items."""
