# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .dimensions import (
    DimensionsResource,
    AsyncDimensionsResource,
    DimensionsResourceWithRawResponse,
    AsyncDimensionsResourceWithRawResponse,
    DimensionsResourceWithStreamingResponse,
    AsyncDimensionsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FieldsResource", "AsyncFieldsResource"]


class FieldsResource(SyncAPIResource):
    @cached_property
    def dimensions(self) -> DimensionsResource:
        return DimensionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FieldsResourceWithRawResponse:
        return FieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FieldsResourceWithStreamingResponse:
        return FieldsResourceWithStreamingResponse(self)


class AsyncFieldsResource(AsyncAPIResource):
    @cached_property
    def dimensions(self) -> AsyncDimensionsResource:
        return AsyncDimensionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFieldsResourceWithRawResponse:
        return AsyncFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFieldsResourceWithStreamingResponse:
        return AsyncFieldsResourceWithStreamingResponse(self)


class FieldsResourceWithRawResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

    @cached_property
    def dimensions(self) -> DimensionsResourceWithRawResponse:
        return DimensionsResourceWithRawResponse(self._fields.dimensions)


class AsyncFieldsResourceWithRawResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

    @cached_property
    def dimensions(self) -> AsyncDimensionsResourceWithRawResponse:
        return AsyncDimensionsResourceWithRawResponse(self._fields.dimensions)


class FieldsResourceWithStreamingResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

    @cached_property
    def dimensions(self) -> DimensionsResourceWithStreamingResponse:
        return DimensionsResourceWithStreamingResponse(self._fields.dimensions)


class AsyncFieldsResourceWithStreamingResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

    @cached_property
    def dimensions(self) -> AsyncDimensionsResourceWithStreamingResponse:
        return AsyncDimensionsResourceWithStreamingResponse(self._fields.dimensions)
