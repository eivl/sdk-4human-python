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
from ...types.users import login_method_update_params
from ..._base_client import (
    make_request_options,
)
from ...types.users.login_method_update_response import LoginMethodUpdateResponse

__all__ = ["LoginMethodResource", "AsyncLoginMethodResource"]


class LoginMethodResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoginMethodResourceWithRawResponse:
        return LoginMethodResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginMethodResourceWithStreamingResponse:
        return LoginMethodResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        active_directory_login: Optional[str],
        email: Optional[str],
        login_method: Literal["NO_USER", "ACTIVE_DIRECTORY", "AUTH0"],
        should_send_email: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoginMethodUpdateResponse:
        """
        Edit user login method.

        Args:
          should_send_email: Param determines if email with details of login method should be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/users/login-method/{user_id}",
            body=maybe_transform(
                {
                    "active_directory_login": active_directory_login,
                    "email": email,
                    "login_method": login_method,
                },
                login_method_update_params.LoginMethodUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"should_send_email": should_send_email}, login_method_update_params.LoginMethodUpdateParams
                ),
            ),
            cast_to=LoginMethodUpdateResponse,
        )


class AsyncLoginMethodResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoginMethodResourceWithRawResponse:
        return AsyncLoginMethodResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginMethodResourceWithStreamingResponse:
        return AsyncLoginMethodResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        active_directory_login: Optional[str],
        email: Optional[str],
        login_method: Literal["NO_USER", "ACTIVE_DIRECTORY", "AUTH0"],
        should_send_email: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoginMethodUpdateResponse:
        """
        Edit user login method.

        Args:
          should_send_email: Param determines if email with details of login method should be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/users/login-method/{user_id}",
            body=await async_maybe_transform(
                {
                    "active_directory_login": active_directory_login,
                    "email": email,
                    "login_method": login_method,
                },
                login_method_update_params.LoginMethodUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"should_send_email": should_send_email}, login_method_update_params.LoginMethodUpdateParams
                ),
            ),
            cast_to=LoginMethodUpdateResponse,
        )


class LoginMethodResourceWithRawResponse:
    def __init__(self, login_method: LoginMethodResource) -> None:
        self._login_method = login_method

        self.update = to_raw_response_wrapper(
            login_method.update,
        )


class AsyncLoginMethodResourceWithRawResponse:
    def __init__(self, login_method: AsyncLoginMethodResource) -> None:
        self._login_method = login_method

        self.update = async_to_raw_response_wrapper(
            login_method.update,
        )


class LoginMethodResourceWithStreamingResponse:
    def __init__(self, login_method: LoginMethodResource) -> None:
        self._login_method = login_method

        self.update = to_streamed_response_wrapper(
            login_method.update,
        )


class AsyncLoginMethodResourceWithStreamingResponse:
    def __init__(self, login_method: AsyncLoginMethodResource) -> None:
        self._login_method = login_method

        self.update = async_to_streamed_response_wrapper(
            login_method.update,
        )
