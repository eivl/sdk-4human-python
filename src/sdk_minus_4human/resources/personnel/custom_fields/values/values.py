# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .company import (
    CompanyResource,
    AsyncCompanyResource,
    CompanyResourceWithRawResponse,
    AsyncCompanyResourceWithRawResponse,
    CompanyResourceWithStreamingResponse,
    AsyncCompanyResourceWithStreamingResponse,
)
from .global_ import (
    GlobalResource,
    AsyncGlobalResource,
    GlobalResourceWithRawResponse,
    AsyncGlobalResourceWithRawResponse,
    GlobalResourceWithStreamingResponse,
    AsyncGlobalResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ValuesResource", "AsyncValuesResource"]


class ValuesResource(SyncAPIResource):
    @cached_property
    def global_(self) -> GlobalResource:
        return GlobalResource(self._client)

    @cached_property
    def company(self) -> CompanyResource:
        return CompanyResource(self._client)

    @cached_property
    def with_raw_response(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self)


class AsyncValuesResource(AsyncAPIResource):
    @cached_property
    def global_(self) -> AsyncGlobalResource:
        return AsyncGlobalResource(self._client)

    @cached_property
    def company(self) -> AsyncCompanyResource:
        return AsyncCompanyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self)


class ValuesResourceWithRawResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

    @cached_property
    def global_(self) -> GlobalResourceWithRawResponse:
        return GlobalResourceWithRawResponse(self._values.global_)

    @cached_property
    def company(self) -> CompanyResourceWithRawResponse:
        return CompanyResourceWithRawResponse(self._values.company)


class AsyncValuesResourceWithRawResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

    @cached_property
    def global_(self) -> AsyncGlobalResourceWithRawResponse:
        return AsyncGlobalResourceWithRawResponse(self._values.global_)

    @cached_property
    def company(self) -> AsyncCompanyResourceWithRawResponse:
        return AsyncCompanyResourceWithRawResponse(self._values.company)


class ValuesResourceWithStreamingResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

    @cached_property
    def global_(self) -> GlobalResourceWithStreamingResponse:
        return GlobalResourceWithStreamingResponse(self._values.global_)

    @cached_property
    def company(self) -> CompanyResourceWithStreamingResponse:
        return CompanyResourceWithStreamingResponse(self._values.company)


class AsyncValuesResourceWithStreamingResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

    @cached_property
    def global_(self) -> AsyncGlobalResourceWithStreamingResponse:
        return AsyncGlobalResourceWithStreamingResponse(self._values.global_)

    @cached_property
    def company(self) -> AsyncCompanyResourceWithStreamingResponse:
        return AsyncCompanyResourceWithStreamingResponse(self._values.company)
