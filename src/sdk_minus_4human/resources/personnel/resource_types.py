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
from ...types.personnel import resource_type_create_params, resource_type_update_params
from ...types.personnel.resource_type_create_response import ResourceTypeCreateResponse
from ...types.personnel.resource_type_update_response import ResourceTypeUpdateResponse
from ...types.personnel.resource_type_retrieve_response import ResourceTypeRetrieveResponse

__all__ = ["ResourceTypesResource", "AsyncResourceTypesResource"]


class ResourceTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceTypesResourceWithRawResponse:
        return ResourceTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceTypesResourceWithStreamingResponse:
        return ResourceTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str],
        name: str,
        type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceTypeCreateResponse:
        """
        Create resource type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/resource-types",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "type_id": type_id,
                },
                resource_type_create_params.ResourceTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceTypeCreateResponse,
        )

    def retrieve(
        self,
        resource_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceTypeRetrieveResponse:
        """
        Get resource type with given id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resource_type_id:
            raise ValueError(f"Expected a non-empty value for `resource_type_id` but received {resource_type_id!r}")
        return self._get(
            f"/personnel/resource-types/{resource_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceTypeRetrieveResponse,
        )

    def update(
        self,
        resource_type_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived"] | NotGiven = NOT_GIVEN,
        type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceTypeUpdateResponse:
        """
        Edit single field in resource type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resource_type_id:
            raise ValueError(f"Expected a non-empty value for `resource_type_id` but received {resource_type_id!r}")
        return self._patch(
            f"/personnel/resource-types/{resource_type_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                    "type_id": type_id,
                },
                resource_type_update_params.ResourceTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceTypeUpdateResponse,
        )


class AsyncResourceTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceTypesResourceWithRawResponse:
        return AsyncResourceTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceTypesResourceWithStreamingResponse:
        return AsyncResourceTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str],
        name: str,
        type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceTypeCreateResponse:
        """
        Create resource type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/resource-types",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "type_id": type_id,
                },
                resource_type_create_params.ResourceTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceTypeCreateResponse,
        )

    async def retrieve(
        self,
        resource_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceTypeRetrieveResponse:
        """
        Get resource type with given id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resource_type_id:
            raise ValueError(f"Expected a non-empty value for `resource_type_id` but received {resource_type_id!r}")
        return await self._get(
            f"/personnel/resource-types/{resource_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceTypeRetrieveResponse,
        )

    async def update(
        self,
        resource_type_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived"] | NotGiven = NOT_GIVEN,
        type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceTypeUpdateResponse:
        """
        Edit single field in resource type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resource_type_id:
            raise ValueError(f"Expected a non-empty value for `resource_type_id` but received {resource_type_id!r}")
        return await self._patch(
            f"/personnel/resource-types/{resource_type_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                    "type_id": type_id,
                },
                resource_type_update_params.ResourceTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceTypeUpdateResponse,
        )


class ResourceTypesResourceWithRawResponse:
    def __init__(self, resource_types: ResourceTypesResource) -> None:
        self._resource_types = resource_types

        self.create = to_raw_response_wrapper(
            resource_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            resource_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            resource_types.update,
        )


class AsyncResourceTypesResourceWithRawResponse:
    def __init__(self, resource_types: AsyncResourceTypesResource) -> None:
        self._resource_types = resource_types

        self.create = async_to_raw_response_wrapper(
            resource_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            resource_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            resource_types.update,
        )


class ResourceTypesResourceWithStreamingResponse:
    def __init__(self, resource_types: ResourceTypesResource) -> None:
        self._resource_types = resource_types

        self.create = to_streamed_response_wrapper(
            resource_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            resource_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            resource_types.update,
        )


class AsyncResourceTypesResourceWithStreamingResponse:
    def __init__(self, resource_types: AsyncResourceTypesResource) -> None:
        self._resource_types = resource_types

        self.create = async_to_streamed_response_wrapper(
            resource_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            resource_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            resource_types.update,
        )
