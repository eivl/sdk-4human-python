# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.orgstructure import (
    unit_type_list_params,
    unit_type_create_params,
    unit_type_update_params,
    unit_type_update_field_params,
)
from ...types.orgstructure.unit_type_list_response import UnitTypeListResponse
from ...types.orgstructure.unit_type_create_response import UnitTypeCreateResponse
from ...types.orgstructure.unit_type_update_response import UnitTypeUpdateResponse
from ...types.orgstructure.unit_type_retrieve_response import UnitTypeRetrieveResponse
from ...types.orgstructure.unit_type_update_field_response import UnitTypeUpdateFieldResponse

__all__ = ["UnitTypesResource", "AsyncUnitTypesResource"]


class UnitTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnitTypesResourceWithRawResponse:
        return UnitTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnitTypesResourceWithStreamingResponse:
        return UnitTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str],
        external_id: Optional[str],
        name: str,
        status: Literal["active", "draft", "archived"],
        type_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeCreateResponse:
        """
        This endpoint allows you to create a unit type which can then be used as a unit
        type when creating units.

        Args:
          description: Unit type additional description

          external_id: External ID of unit type, allowing to store the ID of the client's system

          name: Unit type name

          status: Unit type status

          type_id: Unit type string identified, used for translation purposes. Although the name is
              fixed, typeId might be used to represent a translatable entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/orgstructure/unit-types",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                    "status": status,
                    "type_id": type_id,
                },
                unit_type_create_params.UnitTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTypeCreateResponse,
        )

    def retrieve(
        self,
        unit_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeRetrieveResponse:
        """
        This endpoint allows you to get the single unit type by its internal 4human's
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unit_type_id:
            raise ValueError(f"Expected a non-empty value for `unit_type_id` but received {unit_type_id!r}")
        return self._get(
            f"/orgstructure/unit-types/{unit_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTypeRetrieveResponse,
        )

    def update(
        self,
        unit_type_id: str,
        *,
        description: Optional[str],
        external_id: Optional[str],
        name: str,
        status: Literal["active", "draft", "archived"],
        type_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeUpdateResponse:
        """
        This endpoint allows you to update a single unit type identified by its internal
        4human's ID.

        Args:
          description: Unit type additional description

          external_id: External ID of unit type, allowing to store the ID of the client's system

          name: Unit type name

          status: Unit type status

          type_id: Unit type string identified, used for translation purposes. Although the name is
              fixed, typeId might be used to represent a translatable entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unit_type_id:
            raise ValueError(f"Expected a non-empty value for `unit_type_id` but received {unit_type_id!r}")
        return self._put(
            f"/orgstructure/unit-types/{unit_type_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                    "status": status,
                    "type_id": type_id,
                },
                unit_type_update_params.UnitTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTypeUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeListResponse:
        """This endpoint can be used to fetch list of unit types.

        It is paginated in case
        you want to show the list of unit types in a paginated way.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/orgstructure/unit-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    unit_type_list_params.UnitTypeListParams,
                ),
            ),
            cast_to=UnitTypeListResponse,
        )

    def update_field(
        self,
        unit_type_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "draft", "archived"] | NotGiven = NOT_GIVEN,
        type_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeUpdateFieldResponse:
        """
        This endpoint allows you to update a single field in the unit type definition.
        Edited unit type is identified by its internal 4human's ID.

        Args:
          description: Unit type additional description

          external_id: External ID of unit type, allowing to store the ID of the client's system

          name: Unit type name

          status: Unit type status, might be

          type_id: Unit type string identified, used for translation purposes. Although the name is
              fixed, typeId might be used to represent a translatable entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unit_type_id:
            raise ValueError(f"Expected a non-empty value for `unit_type_id` but received {unit_type_id!r}")
        return self._patch(
            f"/orgstructure/unit-types/{unit_type_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                    "status": status,
                    "type_id": type_id,
                },
                unit_type_update_field_params.UnitTypeUpdateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTypeUpdateFieldResponse,
        )


class AsyncUnitTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnitTypesResourceWithRawResponse:
        return AsyncUnitTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnitTypesResourceWithStreamingResponse:
        return AsyncUnitTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str],
        external_id: Optional[str],
        name: str,
        status: Literal["active", "draft", "archived"],
        type_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeCreateResponse:
        """
        This endpoint allows you to create a unit type which can then be used as a unit
        type when creating units.

        Args:
          description: Unit type additional description

          external_id: External ID of unit type, allowing to store the ID of the client's system

          name: Unit type name

          status: Unit type status

          type_id: Unit type string identified, used for translation purposes. Although the name is
              fixed, typeId might be used to represent a translatable entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/orgstructure/unit-types",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                    "status": status,
                    "type_id": type_id,
                },
                unit_type_create_params.UnitTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTypeCreateResponse,
        )

    async def retrieve(
        self,
        unit_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeRetrieveResponse:
        """
        This endpoint allows you to get the single unit type by its internal 4human's
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unit_type_id:
            raise ValueError(f"Expected a non-empty value for `unit_type_id` but received {unit_type_id!r}")
        return await self._get(
            f"/orgstructure/unit-types/{unit_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTypeRetrieveResponse,
        )

    async def update(
        self,
        unit_type_id: str,
        *,
        description: Optional[str],
        external_id: Optional[str],
        name: str,
        status: Literal["active", "draft", "archived"],
        type_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeUpdateResponse:
        """
        This endpoint allows you to update a single unit type identified by its internal
        4human's ID.

        Args:
          description: Unit type additional description

          external_id: External ID of unit type, allowing to store the ID of the client's system

          name: Unit type name

          status: Unit type status

          type_id: Unit type string identified, used for translation purposes. Although the name is
              fixed, typeId might be used to represent a translatable entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unit_type_id:
            raise ValueError(f"Expected a non-empty value for `unit_type_id` but received {unit_type_id!r}")
        return await self._put(
            f"/orgstructure/unit-types/{unit_type_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                    "status": status,
                    "type_id": type_id,
                },
                unit_type_update_params.UnitTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTypeUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeListResponse:
        """This endpoint can be used to fetch list of unit types.

        It is paginated in case
        you want to show the list of unit types in a paginated way.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/orgstructure/unit-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    unit_type_list_params.UnitTypeListParams,
                ),
            ),
            cast_to=UnitTypeListResponse,
        )

    async def update_field(
        self,
        unit_type_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "draft", "archived"] | NotGiven = NOT_GIVEN,
        type_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnitTypeUpdateFieldResponse:
        """
        This endpoint allows you to update a single field in the unit type definition.
        Edited unit type is identified by its internal 4human's ID.

        Args:
          description: Unit type additional description

          external_id: External ID of unit type, allowing to store the ID of the client's system

          name: Unit type name

          status: Unit type status, might be

          type_id: Unit type string identified, used for translation purposes. Although the name is
              fixed, typeId might be used to represent a translatable entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unit_type_id:
            raise ValueError(f"Expected a non-empty value for `unit_type_id` but received {unit_type_id!r}")
        return await self._patch(
            f"/orgstructure/unit-types/{unit_type_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                    "status": status,
                    "type_id": type_id,
                },
                unit_type_update_field_params.UnitTypeUpdateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTypeUpdateFieldResponse,
        )


class UnitTypesResourceWithRawResponse:
    def __init__(self, unit_types: UnitTypesResource) -> None:
        self._unit_types = unit_types

        self.create = to_raw_response_wrapper(
            unit_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            unit_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            unit_types.update,
        )
        self.list = to_raw_response_wrapper(
            unit_types.list,
        )
        self.update_field = to_raw_response_wrapper(
            unit_types.update_field,
        )


class AsyncUnitTypesResourceWithRawResponse:
    def __init__(self, unit_types: AsyncUnitTypesResource) -> None:
        self._unit_types = unit_types

        self.create = async_to_raw_response_wrapper(
            unit_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            unit_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            unit_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            unit_types.list,
        )
        self.update_field = async_to_raw_response_wrapper(
            unit_types.update_field,
        )


class UnitTypesResourceWithStreamingResponse:
    def __init__(self, unit_types: UnitTypesResource) -> None:
        self._unit_types = unit_types

        self.create = to_streamed_response_wrapper(
            unit_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            unit_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            unit_types.update,
        )
        self.list = to_streamed_response_wrapper(
            unit_types.list,
        )
        self.update_field = to_streamed_response_wrapper(
            unit_types.update_field,
        )


class AsyncUnitTypesResourceWithStreamingResponse:
    def __init__(self, unit_types: AsyncUnitTypesResource) -> None:
        self._unit_types = unit_types

        self.create = async_to_streamed_response_wrapper(
            unit_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            unit_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            unit_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            unit_types.list,
        )
        self.update_field = async_to_streamed_response_wrapper(
            unit_types.update_field,
        )
