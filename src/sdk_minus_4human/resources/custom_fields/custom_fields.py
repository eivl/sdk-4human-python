# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .values import (
    ValuesResource,
    AsyncValuesResource,
    ValuesResourceWithRawResponse,
    AsyncValuesResourceWithRawResponse,
    ValuesResourceWithStreamingResponse,
    AsyncValuesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .personnel import (
    PersonnelResource,
    AsyncPersonnelResource,
    PersonnelResourceWithRawResponse,
    AsyncPersonnelResourceWithRawResponse,
    PersonnelResourceWithStreamingResponse,
    AsyncPersonnelResourceWithStreamingResponse,
)
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .templates.templates import TemplatesResource, AsyncTemplatesResource

__all__ = ["CustomFieldsResource", "AsyncCustomFieldsResource"]


class CustomFieldsResource(SyncAPIResource):
    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def values(self) -> ValuesResource:
        return ValuesResource(self._client)

    @cached_property
    def personnel(self) -> PersonnelResource:
        return PersonnelResource(self._client)

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
    def values(self) -> AsyncValuesResource:
        return AsyncValuesResource(self._client)

    @cached_property
    def personnel(self) -> AsyncPersonnelResource:
        return AsyncPersonnelResource(self._client)

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

    @cached_property
    def values(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self._custom_fields.values)

    @cached_property
    def personnel(self) -> PersonnelResourceWithRawResponse:
        return PersonnelResourceWithRawResponse(self._custom_fields.personnel)


class AsyncCustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._custom_fields.templates)

    @cached_property
    def values(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self._custom_fields.values)

    @cached_property
    def personnel(self) -> AsyncPersonnelResourceWithRawResponse:
        return AsyncPersonnelResourceWithRawResponse(self._custom_fields.personnel)


class CustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._custom_fields.templates)

    @cached_property
    def values(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self._custom_fields.values)

    @cached_property
    def personnel(self) -> PersonnelResourceWithStreamingResponse:
        return PersonnelResourceWithStreamingResponse(self._custom_fields.personnel)


class AsyncCustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._custom_fields.templates)

    @cached_property
    def values(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self._custom_fields.values)

    @cached_property
    def personnel(self) -> AsyncPersonnelResourceWithStreamingResponse:
        return AsyncPersonnelResourceWithStreamingResponse(self._custom_fields.personnel)
