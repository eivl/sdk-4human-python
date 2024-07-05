# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.users.logged_user.detail_retrieve_response import DetailRetrieveResponse

__all__ = ["DetailsResource", "AsyncDetailsResource"]


class DetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsResourceWithRawResponse:
        return DetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsResourceWithStreamingResponse:
        return DetailsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRetrieveResponse:
        """Get logged user profile data."""
        return self._get(
            "/users/logged-user/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveResponse,
        )


class AsyncDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsResourceWithRawResponse:
        return AsyncDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsResourceWithStreamingResponse:
        return AsyncDetailsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRetrieveResponse:
        """Get logged user profile data."""
        return await self._get(
            "/users/logged-user/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveResponse,
        )


class DetailsResourceWithRawResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.retrieve = to_raw_response_wrapper(
            details.retrieve,
        )


class AsyncDetailsResourceWithRawResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.retrieve = async_to_raw_response_wrapper(
            details.retrieve,
        )


class DetailsResourceWithStreamingResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.retrieve = to_streamed_response_wrapper(
            details.retrieve,
        )


class AsyncDetailsResourceWithStreamingResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.retrieve = async_to_streamed_response_wrapper(
            details.retrieve,
        )
