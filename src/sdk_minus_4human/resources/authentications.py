# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import authentication_create_params
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
from ..types.authentication_create_response import AuthenticationCreateResponse

__all__ = ["AuthenticationsResource", "AsyncAuthenticationsResource"]


class AuthenticationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticationsResourceWithRawResponse:
        return AuthenticationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationsResourceWithStreamingResponse:
        return AuthenticationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: Literal["client_credentials"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationCreateResponse:
        """
        You can generate the client_id and client_secret in the master management panel
        under the instance user section. If you don't have access, contact the 4human
        support team to get the credentials. The API user will have the same permissions
        as the user in the UI. client_id and client_secret are valid permanent until
        user regenerates them. They are valid only for active instance users.

        Args:
          client_id: Value is unique for each api user in instance. Must be generated for each
              instance user individually.

          client_secret: Value is unique for each api user in instance. Must be generated for each
              instance user individually.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                },
                authentication_create_params.AuthenticationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCreateResponse,
        )


class AsyncAuthenticationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationsResourceWithRawResponse:
        return AsyncAuthenticationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationsResourceWithStreamingResponse:
        return AsyncAuthenticationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: Literal["client_credentials"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationCreateResponse:
        """
        You can generate the client_id and client_secret in the master management panel
        under the instance user section. If you don't have access, contact the 4human
        support team to get the credentials. The API user will have the same permissions
        as the user in the UI. client_id and client_secret are valid permanent until
        user regenerates them. They are valid only for active instance users.

        Args:
          client_id: Value is unique for each api user in instance. Must be generated for each
              instance user individually.

          client_secret: Value is unique for each api user in instance. Must be generated for each
              instance user individually.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/token",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                },
                authentication_create_params.AuthenticationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCreateResponse,
        )


class AuthenticationsResourceWithRawResponse:
    def __init__(self, authentications: AuthenticationsResource) -> None:
        self._authentications = authentications

        self.create = to_raw_response_wrapper(
            authentications.create,
        )


class AsyncAuthenticationsResourceWithRawResponse:
    def __init__(self, authentications: AsyncAuthenticationsResource) -> None:
        self._authentications = authentications

        self.create = async_to_raw_response_wrapper(
            authentications.create,
        )


class AuthenticationsResourceWithStreamingResponse:
    def __init__(self, authentications: AuthenticationsResource) -> None:
        self._authentications = authentications

        self.create = to_streamed_response_wrapper(
            authentications.create,
        )


class AsyncAuthenticationsResourceWithStreamingResponse:
    def __init__(self, authentications: AsyncAuthenticationsResource) -> None:
        self._authentications = authentications

        self.create = async_to_streamed_response_wrapper(
            authentications.create,
        )
