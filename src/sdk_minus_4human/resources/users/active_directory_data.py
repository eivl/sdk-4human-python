# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.users import active_directory_data_update_params
from ..._base_client import (
    make_request_options,
)
from ...types.users.active_directory_data_update_response import ActiveDirectoryDataUpdateResponse

__all__ = ["ActiveDirectoryDataResource", "AsyncActiveDirectoryDataResource"]


class ActiveDirectoryDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActiveDirectoryDataResourceWithRawResponse:
        return ActiveDirectoryDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActiveDirectoryDataResourceWithStreamingResponse:
        return ActiveDirectoryDataResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        active_directory_username: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActiveDirectoryDataUpdateResponse:
        """
        Edit user active directory data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/users/active-directory-data/{user_id}",
            body=maybe_transform(
                {
                    "active_directory_username": active_directory_username,
                    "email": email,
                },
                active_directory_data_update_params.ActiveDirectoryDataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveDirectoryDataUpdateResponse,
        )


class AsyncActiveDirectoryDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActiveDirectoryDataResourceWithRawResponse:
        return AsyncActiveDirectoryDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActiveDirectoryDataResourceWithStreamingResponse:
        return AsyncActiveDirectoryDataResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        active_directory_username: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActiveDirectoryDataUpdateResponse:
        """
        Edit user active directory data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/users/active-directory-data/{user_id}",
            body=await async_maybe_transform(
                {
                    "active_directory_username": active_directory_username,
                    "email": email,
                },
                active_directory_data_update_params.ActiveDirectoryDataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActiveDirectoryDataUpdateResponse,
        )


class ActiveDirectoryDataResourceWithRawResponse:
    def __init__(self, active_directory_data: ActiveDirectoryDataResource) -> None:
        self._active_directory_data = active_directory_data

        self.update = to_raw_response_wrapper(
            active_directory_data.update,
        )


class AsyncActiveDirectoryDataResourceWithRawResponse:
    def __init__(self, active_directory_data: AsyncActiveDirectoryDataResource) -> None:
        self._active_directory_data = active_directory_data

        self.update = async_to_raw_response_wrapper(
            active_directory_data.update,
        )


class ActiveDirectoryDataResourceWithStreamingResponse:
    def __init__(self, active_directory_data: ActiveDirectoryDataResource) -> None:
        self._active_directory_data = active_directory_data

        self.update = to_streamed_response_wrapper(
            active_directory_data.update,
        )


class AsyncActiveDirectoryDataResourceWithStreamingResponse:
    def __init__(self, active_directory_data: AsyncActiveDirectoryDataResource) -> None:
        self._active_directory_data = active_directory_data

        self.update = async_to_streamed_response_wrapper(
            active_directory_data.update,
        )
