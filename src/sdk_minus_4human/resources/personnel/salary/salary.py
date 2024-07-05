# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .elements import (
    ElementsResource,
    AsyncElementsResource,
    ElementsResourceWithRawResponse,
    AsyncElementsResourceWithRawResponse,
    ElementsResourceWithStreamingResponse,
    AsyncElementsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .elements.elements import ElementsResource, AsyncElementsResource

__all__ = ["SalaryResource", "AsyncSalaryResource"]


class SalaryResource(SyncAPIResource):
    @cached_property
    def elements(self) -> ElementsResource:
        return ElementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SalaryResourceWithRawResponse:
        return SalaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalaryResourceWithStreamingResponse:
        return SalaryResourceWithStreamingResponse(self)


class AsyncSalaryResource(AsyncAPIResource):
    @cached_property
    def elements(self) -> AsyncElementsResource:
        return AsyncElementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSalaryResourceWithRawResponse:
        return AsyncSalaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalaryResourceWithStreamingResponse:
        return AsyncSalaryResourceWithStreamingResponse(self)


class SalaryResourceWithRawResponse:
    def __init__(self, salary: SalaryResource) -> None:
        self._salary = salary

    @cached_property
    def elements(self) -> ElementsResourceWithRawResponse:
        return ElementsResourceWithRawResponse(self._salary.elements)


class AsyncSalaryResourceWithRawResponse:
    def __init__(self, salary: AsyncSalaryResource) -> None:
        self._salary = salary

    @cached_property
    def elements(self) -> AsyncElementsResourceWithRawResponse:
        return AsyncElementsResourceWithRawResponse(self._salary.elements)


class SalaryResourceWithStreamingResponse:
    def __init__(self, salary: SalaryResource) -> None:
        self._salary = salary

    @cached_property
    def elements(self) -> ElementsResourceWithStreamingResponse:
        return ElementsResourceWithStreamingResponse(self._salary.elements)


class AsyncSalaryResourceWithStreamingResponse:
    def __init__(self, salary: AsyncSalaryResource) -> None:
        self._salary = salary

    @cached_property
    def elements(self) -> AsyncElementsResourceWithStreamingResponse:
        return AsyncElementsResourceWithStreamingResponse(self._salary.elements)
