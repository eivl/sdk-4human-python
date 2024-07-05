# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.users import access_group_assign_params
from ...._base_client import (
    make_request_options,
)
from ....types.users.access_group_list_response import AccessGroupListResponse
from ....types.users.access_group_assign_response import AccessGroupAssignResponse

__all__ = ["AccessGroupsResource", "AsyncAccessGroupsResource"]


class AccessGroupsResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccessGroupsResourceWithRawResponse:
        return AccessGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessGroupsResourceWithStreamingResponse:
        return AccessGroupsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessGroupListResponse:
        """Get personnel access groups."""
        return self._get(
            "/users/access-groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupListResponse,
        )

    def assign(
        self,
        *,
        group_ids: List[str],
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessGroupAssignResponse:
        """This endpoint allows to assign/un-assign access groups for user.

        It overwrites
        existing custom access groups (leaves only default for user only).<br /> List of
        access groups in the endpoint GET /personnel/access-groups.

        Args:
          group_ids: Array of access group UUIDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/users/access-groups/assign",
            body=maybe_transform(
                {
                    "group_ids": group_ids,
                    "user_id": user_id,
                },
                access_group_assign_params.AccessGroupAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupAssignResponse,
        )


class AsyncAccessGroupsResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccessGroupsResourceWithRawResponse:
        return AsyncAccessGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessGroupsResourceWithStreamingResponse:
        return AsyncAccessGroupsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessGroupListResponse:
        """Get personnel access groups."""
        return await self._get(
            "/users/access-groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupListResponse,
        )

    async def assign(
        self,
        *,
        group_ids: List[str],
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessGroupAssignResponse:
        """This endpoint allows to assign/un-assign access groups for user.

        It overwrites
        existing custom access groups (leaves only default for user only).<br /> List of
        access groups in the endpoint GET /personnel/access-groups.

        Args:
          group_ids: Array of access group UUIDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/users/access-groups/assign",
            body=await async_maybe_transform(
                {
                    "group_ids": group_ids,
                    "user_id": user_id,
                },
                access_group_assign_params.AccessGroupAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupAssignResponse,
        )


class AccessGroupsResourceWithRawResponse:
    def __init__(self, access_groups: AccessGroupsResource) -> None:
        self._access_groups = access_groups

        self.list = to_raw_response_wrapper(
            access_groups.list,
        )
        self.assign = to_raw_response_wrapper(
            access_groups.assign,
        )

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._access_groups.user)


class AsyncAccessGroupsResourceWithRawResponse:
    def __init__(self, access_groups: AsyncAccessGroupsResource) -> None:
        self._access_groups = access_groups

        self.list = async_to_raw_response_wrapper(
            access_groups.list,
        )
        self.assign = async_to_raw_response_wrapper(
            access_groups.assign,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._access_groups.user)


class AccessGroupsResourceWithStreamingResponse:
    def __init__(self, access_groups: AccessGroupsResource) -> None:
        self._access_groups = access_groups

        self.list = to_streamed_response_wrapper(
            access_groups.list,
        )
        self.assign = to_streamed_response_wrapper(
            access_groups.assign,
        )

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._access_groups.user)


class AsyncAccessGroupsResourceWithStreamingResponse:
    def __init__(self, access_groups: AsyncAccessGroupsResource) -> None:
        self._access_groups = access_groups

        self.list = async_to_streamed_response_wrapper(
            access_groups.list,
        )
        self.assign = async_to_streamed_response_wrapper(
            access_groups.assign,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._access_groups.user)
