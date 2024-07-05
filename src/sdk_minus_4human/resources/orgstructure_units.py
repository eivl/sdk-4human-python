# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    orgstructure_unit_create_params,
    orgstructure_unit_update_params,
    orgstructure_unit_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.orgstructure_unit_create_response import OrgstructureUnitCreateResponse
from ..types.orgstructure_unit_update_response import OrgstructureUnitUpdateResponse
from ..types.orgstructure_unit_retrieve_response import OrgstructureUnitRetrieveResponse

__all__ = ["OrgstructureUnitsResource", "AsyncOrgstructureUnitsResource"]


class OrgstructureUnitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrgstructureUnitsResourceWithRawResponse:
        return OrgstructureUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgstructureUnitsResourceWithStreamingResponse:
        return OrgstructureUnitsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        unit_type_id: str,
        custom_fields: Iterable[orgstructure_unit_create_params.CustomField] | NotGiven = NOT_GIVEN,
        manager_id: Optional[int] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        unit_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgstructureUnitCreateResponse:
        """
        Using this endpoint you can create an <b>organization unit</b> within the
        existing tree. You need to know its parent and manager, although it's not
        required which will result in a non-managed unit. The request requires
        additional information like status and <b>unit type ID</b> which can be fetched
        using additional endpoint <b>GET /orgstructure/unit-types</b>. <br/><br/> What
        you need to do is to give the <b>unit's name</b> and additional data. You can
        use the <b>unitId field</b> to be able to insert your system's ID into our
        system. It's highly recommended that this unitID is unique, so that the item
        might be uniquely identified in any additional requests.<br/><br/> You can also
        set up <b>custom field values</b> for the created unit but you need to deliver
        their UUIDs which means that they need to be primarily created or fetched using
        Custom fields endpoints.

        Args:
          name: Name of the new unit

          unit_type_id: ID of a unit type

          custom_fields: Custom field values, assigned to a given organizational unit.

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          parent_id: ID of the parent organization structure unit. It might be null if root unit is
              added. The ID is the internal 4human's unit ID.

          selected_company_number: Additional company number coming from BRREG

          status: Unit status

          unit_id: Additional unit identifier, to be used freely by the application users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/orgstructure/units",
            body=maybe_transform(
                {
                    "name": name,
                    "unit_type_id": unit_type_id,
                    "custom_fields": custom_fields,
                    "manager_id": manager_id,
                    "parent_id": parent_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "unit_id": unit_id,
                },
                orgstructure_unit_create_params.OrgstructureUnitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgstructureUnitCreateResponse,
        )

    def retrieve(
        self,
        organization_unit_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        with_soft_deleted: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgstructureUnitRetrieveResponse:
        """
        Thanks to this endpoint you can get details information about <b>organization
        unit</b> In order to fetch data either internal or external organization id is
        required. Type of id sent is the request is determined by the <b>external</b>
        parameter. <b>withSoftDeleted</b> as expected allows to fetch organization
        units' data that have been deleted

        Args:
          external: Param determines if id of unit is external (unitId) or internal (id)

          with_soft_deleted: Param determines if deleted unit should be fetched

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_unit_id:
            raise ValueError(
                f"Expected a non-empty value for `organization_unit_id` but received {organization_unit_id!r}"
            )
        return self._get(
            f"/orgstructure/units/{organization_unit_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external": external,
                        "with_soft_deleted": with_soft_deleted,
                    },
                    orgstructure_unit_retrieve_params.OrgstructureUnitRetrieveParams,
                ),
            ),
            cast_to=OrgstructureUnitRetrieveResponse,
        )

    def update(
        self,
        organization_unit_id: str,
        *,
        name: str,
        unit_id: str,
        unit_type_id: str,
        external: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[orgstructure_unit_update_params.CustomField] | NotGiven = NOT_GIVEN,
        manager_id: Optional[int] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgstructureUnitUpdateResponse:
        """This endpoint allows to update data about existing organization unit.

        More than
        one field can be updated using a single request. An internal or external
        organization unit must be provided as a parameter. Type of id sent is the
        request is determined by the <b>external</b> parameter. In order to update
        particular existing organization unit please provide fields name with new
        values.

        Args:
          unit_id: Additional unit identifier, to be used freely by the application users

          external: Param determines if id of unit is external (unitId) or internal (id)

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          parent_id: ID of the parent organization structure unit. It might be null if root unit is
              added. The ID is the internal 4human's unit ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_unit_id:
            raise ValueError(
                f"Expected a non-empty value for `organization_unit_id` but received {organization_unit_id!r}"
            )
        return self._put(
            f"/orgstructure/units/{organization_unit_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "unit_id": unit_id,
                    "unit_type_id": unit_type_id,
                    "custom_fields": custom_fields,
                    "manager_id": manager_id,
                    "parent_id": parent_id,
                    "status": status,
                },
                orgstructure_unit_update_params.OrgstructureUnitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external": external}, orgstructure_unit_update_params.OrgstructureUnitUpdateParams
                ),
            ),
            cast_to=OrgstructureUnitUpdateResponse,
        )


class AsyncOrgstructureUnitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrgstructureUnitsResourceWithRawResponse:
        return AsyncOrgstructureUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgstructureUnitsResourceWithStreamingResponse:
        return AsyncOrgstructureUnitsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        unit_type_id: str,
        custom_fields: Iterable[orgstructure_unit_create_params.CustomField] | NotGiven = NOT_GIVEN,
        manager_id: Optional[int] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        unit_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgstructureUnitCreateResponse:
        """
        Using this endpoint you can create an <b>organization unit</b> within the
        existing tree. You need to know its parent and manager, although it's not
        required which will result in a non-managed unit. The request requires
        additional information like status and <b>unit type ID</b> which can be fetched
        using additional endpoint <b>GET /orgstructure/unit-types</b>. <br/><br/> What
        you need to do is to give the <b>unit's name</b> and additional data. You can
        use the <b>unitId field</b> to be able to insert your system's ID into our
        system. It's highly recommended that this unitID is unique, so that the item
        might be uniquely identified in any additional requests.<br/><br/> You can also
        set up <b>custom field values</b> for the created unit but you need to deliver
        their UUIDs which means that they need to be primarily created or fetched using
        Custom fields endpoints.

        Args:
          name: Name of the new unit

          unit_type_id: ID of a unit type

          custom_fields: Custom field values, assigned to a given organizational unit.

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          parent_id: ID of the parent organization structure unit. It might be null if root unit is
              added. The ID is the internal 4human's unit ID.

          selected_company_number: Additional company number coming from BRREG

          status: Unit status

          unit_id: Additional unit identifier, to be used freely by the application users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/orgstructure/units",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "unit_type_id": unit_type_id,
                    "custom_fields": custom_fields,
                    "manager_id": manager_id,
                    "parent_id": parent_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "unit_id": unit_id,
                },
                orgstructure_unit_create_params.OrgstructureUnitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgstructureUnitCreateResponse,
        )

    async def retrieve(
        self,
        organization_unit_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        with_soft_deleted: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgstructureUnitRetrieveResponse:
        """
        Thanks to this endpoint you can get details information about <b>organization
        unit</b> In order to fetch data either internal or external organization id is
        required. Type of id sent is the request is determined by the <b>external</b>
        parameter. <b>withSoftDeleted</b> as expected allows to fetch organization
        units' data that have been deleted

        Args:
          external: Param determines if id of unit is external (unitId) or internal (id)

          with_soft_deleted: Param determines if deleted unit should be fetched

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_unit_id:
            raise ValueError(
                f"Expected a non-empty value for `organization_unit_id` but received {organization_unit_id!r}"
            )
        return await self._get(
            f"/orgstructure/units/{organization_unit_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external": external,
                        "with_soft_deleted": with_soft_deleted,
                    },
                    orgstructure_unit_retrieve_params.OrgstructureUnitRetrieveParams,
                ),
            ),
            cast_to=OrgstructureUnitRetrieveResponse,
        )

    async def update(
        self,
        organization_unit_id: str,
        *,
        name: str,
        unit_id: str,
        unit_type_id: str,
        external: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[orgstructure_unit_update_params.CustomField] | NotGiven = NOT_GIVEN,
        manager_id: Optional[int] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgstructureUnitUpdateResponse:
        """This endpoint allows to update data about existing organization unit.

        More than
        one field can be updated using a single request. An internal or external
        organization unit must be provided as a parameter. Type of id sent is the
        request is determined by the <b>external</b> parameter. In order to update
        particular existing organization unit please provide fields name with new
        values.

        Args:
          unit_id: Additional unit identifier, to be used freely by the application users

          external: Param determines if id of unit is external (unitId) or internal (id)

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          parent_id: ID of the parent organization structure unit. It might be null if root unit is
              added. The ID is the internal 4human's unit ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_unit_id:
            raise ValueError(
                f"Expected a non-empty value for `organization_unit_id` but received {organization_unit_id!r}"
            )
        return await self._put(
            f"/orgstructure/units/{organization_unit_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "unit_id": unit_id,
                    "unit_type_id": unit_type_id,
                    "custom_fields": custom_fields,
                    "manager_id": manager_id,
                    "parent_id": parent_id,
                    "status": status,
                },
                orgstructure_unit_update_params.OrgstructureUnitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, orgstructure_unit_update_params.OrgstructureUnitUpdateParams
                ),
            ),
            cast_to=OrgstructureUnitUpdateResponse,
        )


class OrgstructureUnitsResourceWithRawResponse:
    def __init__(self, orgstructure_units: OrgstructureUnitsResource) -> None:
        self._orgstructure_units = orgstructure_units

        self.create = to_raw_response_wrapper(
            orgstructure_units.create,
        )
        self.retrieve = to_raw_response_wrapper(
            orgstructure_units.retrieve,
        )
        self.update = to_raw_response_wrapper(
            orgstructure_units.update,
        )


class AsyncOrgstructureUnitsResourceWithRawResponse:
    def __init__(self, orgstructure_units: AsyncOrgstructureUnitsResource) -> None:
        self._orgstructure_units = orgstructure_units

        self.create = async_to_raw_response_wrapper(
            orgstructure_units.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            orgstructure_units.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            orgstructure_units.update,
        )


class OrgstructureUnitsResourceWithStreamingResponse:
    def __init__(self, orgstructure_units: OrgstructureUnitsResource) -> None:
        self._orgstructure_units = orgstructure_units

        self.create = to_streamed_response_wrapper(
            orgstructure_units.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            orgstructure_units.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            orgstructure_units.update,
        )


class AsyncOrgstructureUnitsResourceWithStreamingResponse:
    def __init__(self, orgstructure_units: AsyncOrgstructureUnitsResource) -> None:
        self._orgstructure_units = orgstructure_units

        self.create = async_to_streamed_response_wrapper(
            orgstructure_units.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            orgstructure_units.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            orgstructure_units.update,
        )
