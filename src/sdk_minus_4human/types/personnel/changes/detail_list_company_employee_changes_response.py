# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Union, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .detail_list_company_employee_changes_response import (
    ItemRelatedChangesCustomFieldUnnamedTypeWithobjectParent0ItemRelatedChangesCustomFieldUnnamedTypeWithobjectParent0Item,
)

__all__ = [
    "DetailListCompanyEmployeeChangesResponse",
    "Item",
    "ItemActions",
    "ItemIdentifiers",
    "ItemIdentifiersCompanyEmployee",
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
    can_add_addendum: Optional[bool] = FieldInfo(alias="canAddAddendum", default=None)
    """Flag indicating if an addendum can be added."""

    can_add_work_agreement: Optional[bool] = FieldInfo(alias="canAddWorkAgreement", default=None)
    """Flag indicating if a work agreement can be added."""

    can_be_approved: Optional[bool] = FieldInfo(alias="canBeApproved", default=None)
    """Flag indicating if the employment can be approved."""

    can_be_confirmed: Optional[bool] = FieldInfo(alias="canBeConfirmed", default=None)
    """Flag indicating if the employment can be confirmed."""

    can_be_rejected: Optional[bool] = FieldInfo(alias="canBeRejected", default=None)
    """Flag indicating if the employment can be rejected."""

    can_cancel_snapshot: Optional[bool] = FieldInfo(alias="canCancelSnapshot", default=None)
    """Flag indicating if the snapshot can be canceled."""

    can_unlink_addendum: Optional[bool] = FieldInfo(alias="canUnlinkAddendum", default=None)
    """Flag indicating if the addendum can be unlinked."""


class ItemIdentifiers(BaseModel):
    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """The ID of the employee associated with the employment."""

    number: Optional[str] = None
    """The number associated with the employment."""


class ItemIdentifiersCompanyEmployee(BaseModel):
    database_id: Optional[int] = FieldInfo(alias="databaseId", default=None)
    """Reference database id of the employee associated with the employment."""

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """The Employee ID of the employee associated with the employment."""

    organisation_number: Optional[str] = FieldInfo(alias="organisationNumber", default=None)
    """Id of company from brreg (in case of norway company) or other system."""


class ItemPosition(BaseModel):
    employment_id: Optional[int] = FieldInfo(alias="employmentId", default=None)
    """The ID of the employment."""

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The job title of the employment."""


class ItemRegisteredBy(BaseModel):
    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """The full name of the user who registered the employment."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The ID of the user who registered the employment."""


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
        ) -> ItemRelatedChangesCustomFieldUnnamedTypeWithobjectParent0ItemRelatedChangesCustomFieldUnnamedTypeWithobjectParent0Item:
            ...


ItemRelatedChanges = Union[List[ItemRelatedChangesUnionMember0], ItemRelatedChangesCustomField]


class Item(BaseModel):
    id: Optional[str] = None
    """The internal ID of the changed employment."""

    actions: Optional[ItemActions] = None
    """Actions that can be performed on the employment."""

    addendum_id: Optional[int] = FieldInfo(alias="addendumId", default=None)
    """The ID of the addendum related to the employment."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """The date when the employment was created."""

    document_id: Optional[int] = FieldInfo(alias="documentId", default=None)
    """The ID of the document related to the employment."""

    identifiers: Optional[ItemIdentifiers] = None
    """Identifiers of the employee associated with the employment."""

    identifiers_company_employee: Optional[ItemIdentifiersCompanyEmployee] = FieldInfo(
        alias="identifiersCompanyEmployee", default=None
    )
    """Identifiers of the employee associated with the employment."""

    position: Optional[ItemPosition] = None

    reference_id: Optional[str] = FieldInfo(alias="referenceId", default=None)
    """The reference ID of the employment."""

    registered_by: Optional[ItemRegisteredBy] = FieldInfo(alias="registeredBy", default=None)

    related_changes: Optional[ItemRelatedChanges] = FieldInfo(alias="relatedChanges", default=None)
    """Either an array or an object.

    Response becomes object if customFields are defined.
    """

    snapshot_id: Optional[str] = FieldInfo(alias="snapshotId", default=None)
    """The snapshot ID of the employment."""

    status: Optional[str] = None
    """The status of the employment."""

    type: Optional[str] = None
    """The type of employment."""

    valid_from: Optional[str] = FieldInfo(alias="validFrom", default=None)
    """The start date of the change."""

    valid_to: Optional[str] = FieldInfo(alias="validTo", default=None)
    """The end date of the change."""

    waiting_for_addendum: Optional[bool] = FieldInfo(alias="waitingForAddendum", default=None)
    """Flag indicating if the employment is waiting for an addendum."""

    waiting_for_document: Optional[str] = FieldInfo(alias="waitingForDocument", default=None)
    """The document the employment is waiting for."""


class DetailListCompanyEmployeeChangesResponse(BaseModel):
    items: Optional[List[Item]] = None
    """List of changed employments."""

    users: Optional[List[str]] = None
    """List of changed users (IDs)."""
