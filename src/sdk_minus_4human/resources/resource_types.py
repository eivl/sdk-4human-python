# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import resource_type_list_params
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
from ..types.resource_type_list_response import ResourceTypeListResponse

__all__ = ["ResourceTypesResource", "AsyncResourceTypesResource"]


class ResourceTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceTypesResourceWithRawResponse:
        return ResourceTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceTypesResourceWithStreamingResponse:
        return ResourceTypesResourceWithStreamingResponse(self)

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
    ) -> ResourceTypeListResponse:
        """
        Get resource types list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/resource-types",
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
                    resource_type_list_params.ResourceTypeListParams,
                ),
            ),
            cast_to=ResourceTypeListResponse,
        )


class AsyncResourceTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceTypesResourceWithRawResponse:
        return AsyncResourceTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceTypesResourceWithStreamingResponse:
        return AsyncResourceTypesResourceWithStreamingResponse(self)

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
    ) -> ResourceTypeListResponse:
        """
        Get resource types list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/resource-types",
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
                    resource_type_list_params.ResourceTypeListParams,
                ),
            ),
            cast_to=ResourceTypeListResponse,
        )


class ResourceTypesResourceWithRawResponse:
    def __init__(self, resource_types: ResourceTypesResource) -> None:
        self._resource_types = resource_types

        self.list = to_raw_response_wrapper(
            resource_types.list,
        )


class AsyncResourceTypesResourceWithRawResponse:
    def __init__(self, resource_types: AsyncResourceTypesResource) -> None:
        self._resource_types = resource_types

        self.list = async_to_raw_response_wrapper(
            resource_types.list,
        )


class ResourceTypesResourceWithStreamingResponse:
    def __init__(self, resource_types: ResourceTypesResource) -> None:
        self._resource_types = resource_types

        self.list = to_streamed_response_wrapper(
            resource_types.list,
        )


class AsyncResourceTypesResourceWithStreamingResponse:
    def __init__(self, resource_types: AsyncResourceTypesResource) -> None:
        self._resource_types = resource_types

        self.list = async_to_streamed_response_wrapper(
            resource_types.list,
        )
