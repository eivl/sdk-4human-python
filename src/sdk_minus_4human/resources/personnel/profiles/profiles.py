# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
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
from ....types.personnel.profile_retrieve_response import ProfileRetrieveResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileRetrieveResponse:
        """
        Get user profile data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/personnel/profiles/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )


class AsyncProfilesResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileRetrieveResponse:
        """
        Get user profile data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/personnel/profiles/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.retrieve = to_raw_response_wrapper(
            profiles.retrieve,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._profiles.history)


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.retrieve = async_to_raw_response_wrapper(
            profiles.retrieve,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._profiles.history)


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.retrieve = to_streamed_response_wrapper(
            profiles.retrieve,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._profiles.history)


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.retrieve = async_to_streamed_response_wrapper(
            profiles.retrieve,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._profiles.history)
