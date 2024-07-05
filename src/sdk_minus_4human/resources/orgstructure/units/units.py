# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from .changes import (
    ChangesResource,
    AsyncChangesResource,
    ChangesResourceWithRawResponse,
    AsyncChangesResourceWithRawResponse,
    ChangesResourceWithStreamingResponse,
    AsyncChangesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.orgstructure import unit_update_params
from ....types.orgstructure.unit_update_response import UnitUpdateResponse

__all__ = ["UnitsResource", "AsyncUnitsResource"]


class UnitsResource(SyncAPIResource):
    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> UnitsResourceWithRawResponse:
        return UnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnitsResourceWithStreamingResponse:
        return UnitsResourceWithStreamingResponse(self)

    def update(
        self,
        organization_unit_id: str,
        *,
        name: str,
        unit_id: str,
        external: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[unit_update_params.CustomField] | NotGiven = NOT_GIVEN,
        manager_id: Optional[int] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        unit_type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitUpdateResponse:
        """
        This endpoint allows to update a single property of existing organization unit.
        An internal or external organization unit must be provided as a parameter. Type
        of id sent is the request is determined by the <b>external</b> parameter. In
        order to update particular existing organization unit please provide field name
        with new value.

        Args:
          unit_id: Additional unit identifier, to be used freely by the application users.

          external: Param determines if id of unit is external (unitId) or internal (id)

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          parent_id: database id of parent unit.

          status: Unit status

          unit_type_id: ID of a unit type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_unit_id:
            raise ValueError(
                f"Expected a non-empty value for `organization_unit_id` but received {organization_unit_id!r}"
            )
        return self._patch(
            f"/orgstructure/units/{organization_unit_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "unit_id": unit_id,
                    "custom_fields": custom_fields,
                    "manager_id": manager_id,
                    "parent_id": parent_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "unit_type_id": unit_type_id,
                },
                unit_update_params.UnitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"external": external}, unit_update_params.UnitUpdateParams),
            ),
            cast_to=UnitUpdateResponse,
        )


class AsyncUnitsResource(AsyncAPIResource):
    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUnitsResourceWithRawResponse:
        return AsyncUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnitsResourceWithStreamingResponse:
        return AsyncUnitsResourceWithStreamingResponse(self)

    async def update(
        self,
        organization_unit_id: str,
        *,
        name: str,
        unit_id: str,
        external: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[unit_update_params.CustomField] | NotGiven = NOT_GIVEN,
        manager_id: Optional[int] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        unit_type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitUpdateResponse:
        """
        This endpoint allows to update a single property of existing organization unit.
        An internal or external organization unit must be provided as a parameter. Type
        of id sent is the request is determined by the <b>external</b> parameter. In
        order to update particular existing organization unit please provide field name
        with new value.

        Args:
          unit_id: Additional unit identifier, to be used freely by the application users.

          external: Param determines if id of unit is external (unitId) or internal (id)

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          parent_id: database id of parent unit.

          status: Unit status

          unit_type_id: ID of a unit type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_unit_id:
            raise ValueError(
                f"Expected a non-empty value for `organization_unit_id` but received {organization_unit_id!r}"
            )
        return await self._patch(
            f"/orgstructure/units/{organization_unit_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "unit_id": unit_id,
                    "custom_fields": custom_fields,
                    "manager_id": manager_id,
                    "parent_id": parent_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "unit_type_id": unit_type_id,
                },
                unit_update_params.UnitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"external": external}, unit_update_params.UnitUpdateParams),
            ),
            cast_to=UnitUpdateResponse,
        )


class UnitsResourceWithRawResponse:
    def __init__(self, units: UnitsResource) -> None:
        self._units = units

        self.update = to_raw_response_wrapper(
            units.update,
        )

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._units.changes)


class AsyncUnitsResourceWithRawResponse:
    def __init__(self, units: AsyncUnitsResource) -> None:
        self._units = units

        self.update = async_to_raw_response_wrapper(
            units.update,
        )

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._units.changes)


class UnitsResourceWithStreamingResponse:
    def __init__(self, units: UnitsResource) -> None:
        self._units = units

        self.update = to_streamed_response_wrapper(
            units.update,
        )

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._units.changes)


class AsyncUnitsResourceWithStreamingResponse:
    def __init__(self, units: AsyncUnitsResource) -> None:
        self._units = units

        self.update = async_to_streamed_response_wrapper(
            units.update,
        )

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._units.changes)
