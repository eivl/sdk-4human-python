# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CustomFieldsResource", "AsyncCustomFieldsResource"]


class CustomFieldsResource(SyncAPIResource):
    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomFieldsResourceWithRawResponse:
        return CustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomFieldsResourceWithStreamingResponse:
        return CustomFieldsResourceWithStreamingResponse(self)


class AsyncCustomFieldsResource(AsyncAPIResource):
    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomFieldsResourceWithRawResponse:
        return AsyncCustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomFieldsResourceWithStreamingResponse:
        return AsyncCustomFieldsResourceWithStreamingResponse(self)


class CustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._custom_fields.templates)


class AsyncCustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._custom_fields.templates)


class CustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._custom_fields.templates)


class AsyncCustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._custom_fields.templates)
