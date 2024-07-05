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
from ...types.personnel.hr_role_list_response import HrRoleListResponse

__all__ = ["HrRolesResource", "AsyncHrRolesResource"]


class HrRolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HrRolesResourceWithRawResponse:
        return HrRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HrRolesResourceWithStreamingResponse:
        return HrRolesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HrRoleListResponse:
        """Get personnel HR roles list."""
        return self._get(
            "/personnel/hr-roles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HrRoleListResponse,
        )


class AsyncHrRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHrRolesResourceWithRawResponse:
        return AsyncHrRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHrRolesResourceWithStreamingResponse:
        return AsyncHrRolesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HrRoleListResponse:
        """Get personnel HR roles list."""
        return await self._get(
            "/personnel/hr-roles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HrRoleListResponse,
        )


class HrRolesResourceWithRawResponse:
    def __init__(self, hr_roles: HrRolesResource) -> None:
        self._hr_roles = hr_roles

        self.list = to_raw_response_wrapper(
            hr_roles.list,
        )


class AsyncHrRolesResourceWithRawResponse:
    def __init__(self, hr_roles: AsyncHrRolesResource) -> None:
        self._hr_roles = hr_roles

        self.list = async_to_raw_response_wrapper(
            hr_roles.list,
        )


class HrRolesResourceWithStreamingResponse:
    def __init__(self, hr_roles: HrRolesResource) -> None:
        self._hr_roles = hr_roles

        self.list = to_streamed_response_wrapper(
            hr_roles.list,
        )


class AsyncHrRolesResourceWithStreamingResponse:
    def __init__(self, hr_roles: AsyncHrRolesResource) -> None:
        self._hr_roles = hr_roles

        self.list = async_to_streamed_response_wrapper(
            hr_roles.list,
        )
