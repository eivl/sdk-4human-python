# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FeatureStatusRetrieveResponse"]


class FeatureStatusRetrieveResponse(BaseModel):
    feature_name: str = FieldInfo(alias="featureName")
    """Name of the integration."""

    instance_id: str = FieldInfo(alias="instanceId")
    """ID of the instance."""

    id: Optional[int] = None
    """The ID of the object."""

    auto_trigger: Optional[bool] = FieldInfo(alias="autoTrigger", default=None)
    """Indicates if the integration pipelines in azure should be auto-triggered."""

    cron_expression: Optional[str] = FieldInfo(alias="cronExpression", default=None)
    """Cron expression for scheduling (optional run hours may be provided instead)."""

    export_custom_fields: Optional[bool] = FieldInfo(alias="exportCustomFields", default=None)
    """Indicates if custom fields should be exported (optional)."""

    factory_name: Optional[str] = FieldInfo(alias="factoryName", default=None)
    """Name of the factory (optional for ADF integrations)."""

    is_aggregate_custom_fields: Optional[bool] = FieldInfo(alias="isAggregateCustomFields", default=None)
    """Indicates if aggregated custom fields are exported."""

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """Indicates whether the integration is enabled."""

    is_extended_custom_fields: Optional[bool] = FieldInfo(alias="isExtendedCustomFields", default=None)
    """Indicates if custom fields are extended."""

    is_re_run: Optional[bool] = FieldInfo(alias="isReRun", default=None)
    """Indicates if integration waits to re-run."""

    message: Optional[str] = None
    """message (i.e. error description)."""

    next_cron_run_date: Optional[str] = FieldInfo(alias="nextCronRunDate", default=None)
    """Date for the next scheduled cron run (optional, will be calculated)."""

    priority_descending: Optional[int] = FieldInfo(alias="priorityDescending", default=None)
    """Priority in queue descending order (optional)."""

    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)
    """ID of the request filled automatically on run by API."""

    re_run_counter: Optional[int] = FieldInfo(alias="reRunCounter", default=None)
    """Counter for re-runs if integration error occurs.

    (max 3, later integration will be bypassed to not block others)
    """

    resource_group_name: Optional[str] = FieldInfo(alias="resourceGroupName", default=None)
    """Name of the resource group (optional for ADF integrations)."""

    run_hours: Optional[List[str]] = FieldInfo(alias="runHours", default=None)
    """
    Array of hours in which the integration should run (optional cron may be
    provided instead).
    """

    status: Optional[Literal["IN_PROGRESS", "ERROR"]] = None
    """Status of integration."""

    status_updated_at: Optional[str] = FieldInfo(alias="statusUpdatedAt", default=None)
    """
    Date when the status was last updated (status is updated at error, in progress
    or end of export).
    """

    trigger_name: Optional[str] = FieldInfo(alias="triggerName", default=None)
    """Name of the trigger (optional for ADF integrations)."""

    use_effective_status: Optional[bool] = FieldInfo(alias="useEffectiveStatus", default=None)
    """Indicates if effective status is used."""
