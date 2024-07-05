# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ...types.users import by_login_create_params
from ..._base_client import (
    make_request_options,
)
from ...types.users.by_login_create_response import ByLoginCreateResponse

__all__ = ["ByLoginResource", "AsyncByLoginResource"]


class ByLoginResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ByLoginResourceWithRawResponse:
        return ByLoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByLoginResourceWithStreamingResponse:
        return ByLoginResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: List[str],
        find_by: Literal["activeDirectoryUsername", "email"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByLoginCreateResponse:
        """Retrieve users by login.

        It's important to note that this endpoint solely
        utilizes data for search purposes and does not create any new entities.

        Args:
          find_by: filter users by given type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/by-login",
            body=maybe_transform(body, by_login_create_params.ByLoginCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"find_by": find_by}, by_login_create_params.ByLoginCreateParams),
            ),
            cast_to=ByLoginCreateResponse,
        )


class AsyncByLoginResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncByLoginResourceWithRawResponse:
        return AsyncByLoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByLoginResourceWithStreamingResponse:
        return AsyncByLoginResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: List[str],
        find_by: Literal["activeDirectoryUsername", "email"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByLoginCreateResponse:
        """Retrieve users by login.

        It's important to note that this endpoint solely
        utilizes data for search purposes and does not create any new entities.

        Args:
          find_by: filter users by given type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/by-login",
            body=await async_maybe_transform(body, by_login_create_params.ByLoginCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"find_by": find_by}, by_login_create_params.ByLoginCreateParams),
            ),
            cast_to=ByLoginCreateResponse,
        )


class ByLoginResourceWithRawResponse:
    def __init__(self, by_login: ByLoginResource) -> None:
        self._by_login = by_login

        self.create = to_raw_response_wrapper(
            by_login.create,
        )


class AsyncByLoginResourceWithRawResponse:
    def __init__(self, by_login: AsyncByLoginResource) -> None:
        self._by_login = by_login

        self.create = async_to_raw_response_wrapper(
            by_login.create,
        )


class ByLoginResourceWithStreamingResponse:
    def __init__(self, by_login: ByLoginResource) -> None:
        self._by_login = by_login

        self.create = to_streamed_response_wrapper(
            by_login.create,
        )


class AsyncByLoginResourceWithStreamingResponse:
    def __init__(self, by_login: AsyncByLoginResource) -> None:
        self._by_login = by_login

        self.create = async_to_streamed_response_wrapper(
            by_login.create,
        )
