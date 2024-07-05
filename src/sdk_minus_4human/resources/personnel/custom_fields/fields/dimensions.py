# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import (
    make_request_options,
)
from .....types.personnel.custom_fields.fields import dimension_create_params, dimension_update_params
from .....types.personnel.custom_fields.fields.dimension_create_response import DimensionCreateResponse
from .....types.personnel.custom_fields.fields.dimension_update_response import DimensionUpdateResponse

__all__ = ["DimensionsResource", "AsyncDimensionsResource"]


class DimensionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DimensionsResourceWithRawResponse:
        return DimensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DimensionsResourceWithStreamingResponse:
        return DimensionsResourceWithStreamingResponse(self)

    def create(
        self,
        field_id: str,
        *,
        external_id: str,
        external_name: str,
        internal_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DimensionCreateResponse:
        """Create custom field dimension for given field.

        Each custom field level is called
        dimension. Custom field may have multiple levels of dimensions. One dimension
        can be added at a given level.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return self._post(
            f"/personnel/custom-fields/fields/{field_id}/dimensions",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "external_name": external_name,
                    "internal_id": internal_id,
                    "name": name,
                },
                dimension_create_params.DimensionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DimensionCreateResponse,
        )

    def update(
        self,
        dimension_id: str,
        *,
        external_id: str | NotGiven = NOT_GIVEN,
        external_name: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DimensionUpdateResponse:
        """
        Edit single field of custom field dimension with given UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension_id:
            raise ValueError(f"Expected a non-empty value for `dimension_id` but received {dimension_id!r}")
        return self._patch(
            f"/personnel/custom-fields/fields/dimensions/{dimension_id}",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "external_name": external_name,
                    "internal_id": internal_id,
                    "name": name,
                },
                dimension_update_params.DimensionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DimensionUpdateResponse,
        )


class AsyncDimensionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDimensionsResourceWithRawResponse:
        return AsyncDimensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDimensionsResourceWithStreamingResponse:
        return AsyncDimensionsResourceWithStreamingResponse(self)

    async def create(
        self,
        field_id: str,
        *,
        external_id: str,
        external_name: str,
        internal_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DimensionCreateResponse:
        """Create custom field dimension for given field.

        Each custom field level is called
        dimension. Custom field may have multiple levels of dimensions. One dimension
        can be added at a given level.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return await self._post(
            f"/personnel/custom-fields/fields/{field_id}/dimensions",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "external_name": external_name,
                    "internal_id": internal_id,
                    "name": name,
                },
                dimension_create_params.DimensionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DimensionCreateResponse,
        )

    async def update(
        self,
        dimension_id: str,
        *,
        external_id: str | NotGiven = NOT_GIVEN,
        external_name: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DimensionUpdateResponse:
        """
        Edit single field of custom field dimension with given UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension_id:
            raise ValueError(f"Expected a non-empty value for `dimension_id` but received {dimension_id!r}")
        return await self._patch(
            f"/personnel/custom-fields/fields/dimensions/{dimension_id}",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "external_name": external_name,
                    "internal_id": internal_id,
                    "name": name,
                },
                dimension_update_params.DimensionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DimensionUpdateResponse,
        )


class DimensionsResourceWithRawResponse:
    def __init__(self, dimensions: DimensionsResource) -> None:
        self._dimensions = dimensions

        self.create = to_raw_response_wrapper(
            dimensions.create,
        )
        self.update = to_raw_response_wrapper(
            dimensions.update,
        )


class AsyncDimensionsResourceWithRawResponse:
    def __init__(self, dimensions: AsyncDimensionsResource) -> None:
        self._dimensions = dimensions

        self.create = async_to_raw_response_wrapper(
            dimensions.create,
        )
        self.update = async_to_raw_response_wrapper(
            dimensions.update,
        )


class DimensionsResourceWithStreamingResponse:
    def __init__(self, dimensions: DimensionsResource) -> None:
        self._dimensions = dimensions

        self.create = to_streamed_response_wrapper(
            dimensions.create,
        )
        self.update = to_streamed_response_wrapper(
            dimensions.update,
        )


class AsyncDimensionsResourceWithStreamingResponse:
    def __init__(self, dimensions: AsyncDimensionsResource) -> None:
        self._dimensions = dimensions

        self.create = async_to_streamed_response_wrapper(
            dimensions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            dimensions.update,
        )
