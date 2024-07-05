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
from ....types.custom_fields.templates.global_retrieve_response import GlobalRetrieveResponse

__all__ = ["GlobalResource", "AsyncGlobalResource"]


class GlobalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalResourceWithRawResponse:
        return GlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalResourceWithStreamingResponse:
        return GlobalResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalRetrieveResponse:
        """
        Global custom fields are assigned to user directly and not supports inheritance.
        """
        return self._get(
            "/personnel/custom-fields/templates/global",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalRetrieveResponse,
        )


class AsyncGlobalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalResourceWithRawResponse:
        return AsyncGlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalResourceWithStreamingResponse:
        return AsyncGlobalResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalRetrieveResponse:
        """
        Global custom fields are assigned to user directly and not supports inheritance.
        """
        return await self._get(
            "/personnel/custom-fields/templates/global",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalRetrieveResponse,
        )


class GlobalResourceWithRawResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.retrieve = to_raw_response_wrapper(
            global_.retrieve,
        )


class AsyncGlobalResourceWithRawResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.retrieve = async_to_raw_response_wrapper(
            global_.retrieve,
        )


class GlobalResourceWithStreamingResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.retrieve = to_streamed_response_wrapper(
            global_.retrieve,
        )


class AsyncGlobalResourceWithStreamingResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.retrieve = async_to_streamed_response_wrapper(
            global_.retrieve,
        )
