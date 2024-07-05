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
from .occupational_codes import (
    OccupationalCodesResource,
    AsyncOccupationalCodesResource,
    OccupationalCodesResourceWithRawResponse,
    AsyncOccupationalCodesResourceWithRawResponse,
    OccupationalCodesResourceWithStreamingResponse,
    AsyncOccupationalCodesResourceWithStreamingResponse,
)
from ....types.personnel.dictionary_list_response import DictionaryListResponse

__all__ = ["DictionaryResource", "AsyncDictionaryResource"]


class DictionaryResource(SyncAPIResource):
    @cached_property
    def occupational_codes(self) -> OccupationalCodesResource:
        return OccupationalCodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DictionaryResourceWithRawResponse:
        return DictionaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DictionaryResourceWithStreamingResponse:
        return DictionaryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DictionaryListResponse:
        """
        Get dictionaries for workRelationType, workingHoursArrangement, workStatus,
        salaryType.
        """
        return self._get(
            "/personnel/dictionary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DictionaryListResponse,
        )


class AsyncDictionaryResource(AsyncAPIResource):
    @cached_property
    def occupational_codes(self) -> AsyncOccupationalCodesResource:
        return AsyncOccupationalCodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDictionaryResourceWithRawResponse:
        return AsyncDictionaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDictionaryResourceWithStreamingResponse:
        return AsyncDictionaryResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DictionaryListResponse:
        """
        Get dictionaries for workRelationType, workingHoursArrangement, workStatus,
        salaryType.
        """
        return await self._get(
            "/personnel/dictionary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DictionaryListResponse,
        )


class DictionaryResourceWithRawResponse:
    def __init__(self, dictionary: DictionaryResource) -> None:
        self._dictionary = dictionary

        self.list = to_raw_response_wrapper(
            dictionary.list,
        )

    @cached_property
    def occupational_codes(self) -> OccupationalCodesResourceWithRawResponse:
        return OccupationalCodesResourceWithRawResponse(self._dictionary.occupational_codes)


class AsyncDictionaryResourceWithRawResponse:
    def __init__(self, dictionary: AsyncDictionaryResource) -> None:
        self._dictionary = dictionary

        self.list = async_to_raw_response_wrapper(
            dictionary.list,
        )

    @cached_property
    def occupational_codes(self) -> AsyncOccupationalCodesResourceWithRawResponse:
        return AsyncOccupationalCodesResourceWithRawResponse(self._dictionary.occupational_codes)


class DictionaryResourceWithStreamingResponse:
    def __init__(self, dictionary: DictionaryResource) -> None:
        self._dictionary = dictionary

        self.list = to_streamed_response_wrapper(
            dictionary.list,
        )

    @cached_property
    def occupational_codes(self) -> OccupationalCodesResourceWithStreamingResponse:
        return OccupationalCodesResourceWithStreamingResponse(self._dictionary.occupational_codes)


class AsyncDictionaryResourceWithStreamingResponse:
    def __init__(self, dictionary: AsyncDictionaryResource) -> None:
        self._dictionary = dictionary

        self.list = async_to_streamed_response_wrapper(
            dictionary.list,
        )

    @cached_property
    def occupational_codes(self) -> AsyncOccupationalCodesResourceWithStreamingResponse:
        return AsyncOccupationalCodesResourceWithStreamingResponse(self._dictionary.occupational_codes)
