# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SalaryRegulationListResponse", "Item", "ItemRegulationStep"]


class ItemRegulationStep(BaseModel):
    step_amount: Optional[float] = FieldInfo(alias="stepAmount", default=None)
    """The monetary value associated with the salary step."""

    step_created_at: Optional[datetime] = FieldInfo(alias="stepCreatedAt", default=None)
    """The date and time when the salary step was created."""

    step_external_id: Optional[str] = FieldInfo(alias="stepExternalId", default=None)
    """
    External identifier for the step, usable for integrations with external systems.
    """

    step_id: Optional[int] = FieldInfo(alias="stepId", default=None)
    """Unique identifier for one version of the salary step within the system."""

    step_last_edit_at: Optional[datetime] = FieldInfo(alias="stepLastEditAt", default=None)
    """The date and time when the salary step was last edited."""

    step_name: Optional[str] = FieldInfo(alias="stepName", default=None)
    """The name designated to the specific salary step."""

    step_reference_id: Optional[int] = FieldInfo(alias="stepReferenceId", default=None)
    """
    Internal 4human's reference ID that defines a group of versions of one salary
    regulation step
    """

    step_symbol: Optional[str] = FieldInfo(alias="stepSymbol", default=None)
    """Symbol representing the salary step."""

    step_updated_by: Optional[str] = FieldInfo(alias="stepUpdatedBy", default=None)
    """The unique identifier for the user who last updated the step."""


class Item(BaseModel):
    regulation_created_at: Optional[datetime] = FieldInfo(alias="regulationCreatedAt", default=None)
    """The date and time when the salary regulation was created."""

    regulation_currency: Optional[str] = FieldInfo(alias="regulationCurrency", default=None)
    """The currency in which the salary is regulated."""

    regulation_description: Optional[str] = FieldInfo(alias="regulationDescription", default=None)
    """Detailed description of the salary regulation."""

    regulation_external_id: Optional[str] = FieldInfo(alias="regulationExternalId", default=None)
    """
    External identifier for the regulation, usable for integrations with external
    systems.
    """

    regulation_id: Optional[int] = FieldInfo(alias="regulationId", default=None)
    """Unique identifier for the version of regulation within the system."""

    regulation_internal_id: Optional[str] = FieldInfo(alias="regulationInternalId", default=None)
    """Internal identifier for the regulation within the system."""

    regulation_last_edit_at: Optional[datetime] = FieldInfo(alias="regulationLastEditAt", default=None)
    """The date and time when the salary regulation was last edited."""

    regulation_name: Optional[str] = FieldInfo(alias="regulationName", default=None)
    """The name designated to the specific salary regulation version."""

    regulation_period: Optional[str] = FieldInfo(alias="regulationPeriod", default=None)
    """The frequency at which the salary regulation is reviewed."""

    regulation_reference_id: Optional[int] = FieldInfo(alias="regulationReferenceId", default=None)
    """
    Internal 4human's reference ID that defines a group of versions of one salary
    regulation.
    """

    regulation_status: Optional[Literal["for_confirmation", "past", "current", "future"]] = FieldInfo(
        alias="regulationStatus", default=None
    )
    """Defines the record's status.

    It may be past, current (current version) or future. Records with current status
    are version currently in forcy.
    """

    regulation_steps: Optional[List[ItemRegulationStep]] = FieldInfo(alias="regulationSteps", default=None)

    regulation_updated_by: Optional[str] = FieldInfo(alias="regulationUpdatedBy", default=None)
    """The unique identifier for the user who last updated the regulation."""

    regulation_valid_from: Optional[datetime] = FieldInfo(alias="regulationValidFrom", default=None)
    """The date from which the salary regulation is valid."""

    regulation_valid_to: Optional[datetime] = FieldInfo(alias="regulationValidTo", default=None)
    """The date until which the salary regulation is valid."""


class SalaryRegulationListResponse(BaseModel):
    items: List[Item]

    limit: int
    """Maximum number of records to return per page."""

    page: int
    """Current page number."""

    pages: int
    """Total number of pages."""

    total: int
    """Total number of records."""
