# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.external_integrations.feature_status_retrieve_response import FeatureStatusRetrieveResponse

__all__ = ["FeatureStatusResource", "AsyncFeatureStatusResource"]


class FeatureStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeatureStatusResourceWithRawResponse:
        return FeatureStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeatureStatusResourceWithStreamingResponse:
        return FeatureStatusResourceWithStreamingResponse(self)

    def retrieve(
        self,
        feature_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeatureStatusRetrieveResponse:
        """
        Get information about single integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feature_name:
            raise ValueError(f"Expected a non-empty value for `feature_name` but received {feature_name!r}")
        return self._get(
            f"/external-integrations/status/{feature_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureStatusRetrieveResponse,
        )


class AsyncFeatureStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeatureStatusResourceWithRawResponse:
        return AsyncFeatureStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeatureStatusResourceWithStreamingResponse:
        return AsyncFeatureStatusResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        feature_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeatureStatusRetrieveResponse:
        """
        Get information about single integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feature_name:
            raise ValueError(f"Expected a non-empty value for `feature_name` but received {feature_name!r}")
        return await self._get(
            f"/external-integrations/status/{feature_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureStatusRetrieveResponse,
        )


class FeatureStatusResourceWithRawResponse:
    def __init__(self, feature_status: FeatureStatusResource) -> None:
        self._feature_status = feature_status

        self.retrieve = to_raw_response_wrapper(
            feature_status.retrieve,
        )


class AsyncFeatureStatusResourceWithRawResponse:
    def __init__(self, feature_status: AsyncFeatureStatusResource) -> None:
        self._feature_status = feature_status

        self.retrieve = async_to_raw_response_wrapper(
            feature_status.retrieve,
        )


class FeatureStatusResourceWithStreamingResponse:
    def __init__(self, feature_status: FeatureStatusResource) -> None:
        self._feature_status = feature_status

        self.retrieve = to_streamed_response_wrapper(
            feature_status.retrieve,
        )


class AsyncFeatureStatusResourceWithStreamingResponse:
    def __init__(self, feature_status: AsyncFeatureStatusResource) -> None:
        self._feature_status = feature_status

        self.retrieve = async_to_streamed_response_wrapper(
            feature_status.retrieve,
        )
