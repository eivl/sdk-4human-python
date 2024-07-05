# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...._base_client import (
    make_request_options,
)
from ....types.personnel.dictionary import occupational_code_list_params
from ....types.personnel.dictionary.occupational_code_list_response import OccupationalCodeListResponse

__all__ = ["OccupationalCodesResource", "AsyncOccupationalCodesResource"]


class OccupationalCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OccupationalCodesResourceWithRawResponse:
        return OccupationalCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OccupationalCodesResourceWithStreamingResponse:
        return OccupationalCodesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        country: str,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OccupationalCodeListResponse:
        """
        Get Occupational by country and query params.

        Args:
          country: country - code of the country with occupational code, e.g. 'NOR'

          query: query - phrase to search occupational code by the title, e.g. 'KORIN'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/dictionary/occupational-codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "query": query,
                    },
                    occupational_code_list_params.OccupationalCodeListParams,
                ),
            ),
            cast_to=OccupationalCodeListResponse,
        )


class AsyncOccupationalCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOccupationalCodesResourceWithRawResponse:
        return AsyncOccupationalCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOccupationalCodesResourceWithStreamingResponse:
        return AsyncOccupationalCodesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        country: str,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OccupationalCodeListResponse:
        """
        Get Occupational by country and query params.

        Args:
          country: country - code of the country with occupational code, e.g. 'NOR'

          query: query - phrase to search occupational code by the title, e.g. 'KORIN'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/dictionary/occupational-codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "query": query,
                    },
                    occupational_code_list_params.OccupationalCodeListParams,
                ),
            ),
            cast_to=OccupationalCodeListResponse,
        )


class OccupationalCodesResourceWithRawResponse:
    def __init__(self, occupational_codes: OccupationalCodesResource) -> None:
        self._occupational_codes = occupational_codes

        self.list = to_raw_response_wrapper(
            occupational_codes.list,
        )


class AsyncOccupationalCodesResourceWithRawResponse:
    def __init__(self, occupational_codes: AsyncOccupationalCodesResource) -> None:
        self._occupational_codes = occupational_codes

        self.list = async_to_raw_response_wrapper(
            occupational_codes.list,
        )


class OccupationalCodesResourceWithStreamingResponse:
    def __init__(self, occupational_codes: OccupationalCodesResource) -> None:
        self._occupational_codes = occupational_codes

        self.list = to_streamed_response_wrapper(
            occupational_codes.list,
        )


class AsyncOccupationalCodesResourceWithStreamingResponse:
    def __init__(self, occupational_codes: AsyncOccupationalCodesResource) -> None:
        self._occupational_codes = occupational_codes

        self.list = async_to_streamed_response_wrapper(
            occupational_codes.list,
        )
