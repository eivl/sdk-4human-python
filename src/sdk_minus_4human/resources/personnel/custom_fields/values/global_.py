# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.personnel.custom_fields.values.global_list_response import GlobalListResponse

__all__ = ["GlobalResource", "AsyncGlobalResource"]


class GlobalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalResourceWithRawResponse:
        return GlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalResourceWithStreamingResponse:
        return GlobalResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalListResponse:
        """Global custom fields are common for all users in instance.

        On UI it references
        to: Settings -> Custom fields -> Personal Fields. Endpoint displays list of
        items, each representing a custom field value and its associated details. Each
        custom field may have tree structure of "Attributes" called "dimensions" Each
        dimension may have its own set of value.
        """
        return self._get(
            "/personnel/custom-fields/values/global/tree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalListResponse,
        )


class AsyncGlobalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalResourceWithRawResponse:
        return AsyncGlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalResourceWithStreamingResponse:
        return AsyncGlobalResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalListResponse:
        """Global custom fields are common for all users in instance.

        On UI it references
        to: Settings -> Custom fields -> Personal Fields. Endpoint displays list of
        items, each representing a custom field value and its associated details. Each
        custom field may have tree structure of "Attributes" called "dimensions" Each
        dimension may have its own set of value.
        """
        return await self._get(
            "/personnel/custom-fields/values/global/tree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalListResponse,
        )


class GlobalResourceWithRawResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.list = to_raw_response_wrapper(
            global_.list,
        )


class AsyncGlobalResourceWithRawResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.list = async_to_raw_response_wrapper(
            global_.list,
        )


class GlobalResourceWithStreamingResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.list = to_streamed_response_wrapper(
            global_.list,
        )


class AsyncGlobalResourceWithStreamingResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.list = async_to_streamed_response_wrapper(
            global_.list,
        )
