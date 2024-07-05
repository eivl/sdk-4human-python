# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SalaryElementsResource", "AsyncSalaryElementsResource"]


class SalaryElementsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> SalaryElementsResourceWithRawResponse:
        return SalaryElementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalaryElementsResourceWithStreamingResponse:
        return SalaryElementsResourceWithStreamingResponse(self)


class AsyncSalaryElementsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSalaryElementsResourceWithRawResponse:
        return AsyncSalaryElementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalaryElementsResourceWithStreamingResponse:
        return AsyncSalaryElementsResourceWithStreamingResponse(self)


class SalaryElementsResourceWithRawResponse:
    def __init__(self, salary_elements: SalaryElementsResource) -> None:
        self._salary_elements = salary_elements

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._salary_elements.history)


class AsyncSalaryElementsResourceWithRawResponse:
    def __init__(self, salary_elements: AsyncSalaryElementsResource) -> None:
        self._salary_elements = salary_elements

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._salary_elements.history)


class SalaryElementsResourceWithStreamingResponse:
    def __init__(self, salary_elements: SalaryElementsResource) -> None:
        self._salary_elements = salary_elements

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._salary_elements.history)


class AsyncSalaryElementsResourceWithStreamingResponse:
    def __init__(self, salary_elements: AsyncSalaryElementsResource) -> None:
        self._salary_elements = salary_elements

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._salary_elements.history)
