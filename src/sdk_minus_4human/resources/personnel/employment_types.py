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
from ...types.personnel.employment_type_list_response import EmploymentTypeListResponse

__all__ = ["EmploymentTypesResource", "AsyncEmploymentTypesResource"]


class EmploymentTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmploymentTypesResourceWithRawResponse:
        return EmploymentTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmploymentTypesResourceWithStreamingResponse:
        return EmploymentTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentTypeListResponse:
        """Returns existing employment types flat list."""
        return self._get(
            "/personnel/employment-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmploymentTypeListResponse,
        )


class AsyncEmploymentTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmploymentTypesResourceWithRawResponse:
        return AsyncEmploymentTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmploymentTypesResourceWithStreamingResponse:
        return AsyncEmploymentTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentTypeListResponse:
        """Returns existing employment types flat list."""
        return await self._get(
            "/personnel/employment-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmploymentTypeListResponse,
        )


class EmploymentTypesResourceWithRawResponse:
    def __init__(self, employment_types: EmploymentTypesResource) -> None:
        self._employment_types = employment_types

        self.list = to_raw_response_wrapper(
            employment_types.list,
        )


class AsyncEmploymentTypesResourceWithRawResponse:
    def __init__(self, employment_types: AsyncEmploymentTypesResource) -> None:
        self._employment_types = employment_types

        self.list = async_to_raw_response_wrapper(
            employment_types.list,
        )


class EmploymentTypesResourceWithStreamingResponse:
    def __init__(self, employment_types: EmploymentTypesResource) -> None:
        self._employment_types = employment_types

        self.list = to_streamed_response_wrapper(
            employment_types.list,
        )


class AsyncEmploymentTypesResourceWithStreamingResponse:
    def __init__(self, employment_types: AsyncEmploymentTypesResource) -> None:
        self._employment_types = employment_types

        self.list = async_to_streamed_response_wrapper(
            employment_types.list,
        )
