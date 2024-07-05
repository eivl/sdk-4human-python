# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .fields import (
    FieldsResource,
    AsyncFieldsResource,
    FieldsResourceWithRawResponse,
    AsyncFieldsResourceWithRawResponse,
    FieldsResourceWithStreamingResponse,
    AsyncFieldsResourceWithStreamingResponse,
)
from .values import (
    ValuesResource,
    AsyncValuesResource,
    ValuesResourceWithRawResponse,
    AsyncValuesResourceWithRawResponse,
    ValuesResourceWithStreamingResponse,
    AsyncValuesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .fields.fields import FieldsResource, AsyncFieldsResource
from .values.values import ValuesResource, AsyncValuesResource
from ...._base_client import (
    make_request_options,
)
from ....types.personnel import custom_field_change_status_params
from .templates.templates import TemplatesResource, AsyncTemplatesResource
from ....types.personnel.custom_field_change_status_response import CustomFieldChangeStatusResponse

__all__ = ["CustomFieldsResource", "AsyncCustomFieldsResource"]


class CustomFieldsResource(SyncAPIResource):
    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def fields(self) -> FieldsResource:
        return FieldsResource(self._client)

    @cached_property
    def values(self) -> ValuesResource:
        return ValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomFieldsResourceWithRawResponse:
        return CustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomFieldsResourceWithStreamingResponse:
        return CustomFieldsResourceWithStreamingResponse(self)

    def change_status(
        self,
        *,
        path_id: str,
        body_id: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomFieldChangeStatusResponse:
        """
        Enable or disable custom field or dimension with given id is possible only if
        given custom field/dimension is not in use.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._patch(
            f"/personnel/custom-fields/change-status/{path_id}",
            body=maybe_transform({"id": body_id}, custom_field_change_status_params.CustomFieldChangeStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldChangeStatusResponse,
        )


class AsyncCustomFieldsResource(AsyncAPIResource):
    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def fields(self) -> AsyncFieldsResource:
        return AsyncFieldsResource(self._client)

    @cached_property
    def values(self) -> AsyncValuesResource:
        return AsyncValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomFieldsResourceWithRawResponse:
        return AsyncCustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomFieldsResourceWithStreamingResponse:
        return AsyncCustomFieldsResourceWithStreamingResponse(self)

    async def change_status(
        self,
        *,
        path_id: str,
        body_id: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomFieldChangeStatusResponse:
        """
        Enable or disable custom field or dimension with given id is possible only if
        given custom field/dimension is not in use.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._patch(
            f"/personnel/custom-fields/change-status/{path_id}",
            body=await async_maybe_transform(
                {"id": body_id}, custom_field_change_status_params.CustomFieldChangeStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldChangeStatusResponse,
        )


class CustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.change_status = to_raw_response_wrapper(
            custom_fields.change_status,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._custom_fields.templates)

    @cached_property
    def fields(self) -> FieldsResourceWithRawResponse:
        return FieldsResourceWithRawResponse(self._custom_fields.fields)

    @cached_property
    def values(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self._custom_fields.values)


class AsyncCustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.change_status = async_to_raw_response_wrapper(
            custom_fields.change_status,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._custom_fields.templates)

    @cached_property
    def fields(self) -> AsyncFieldsResourceWithRawResponse:
        return AsyncFieldsResourceWithRawResponse(self._custom_fields.fields)

    @cached_property
    def values(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self._custom_fields.values)


class CustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.change_status = to_streamed_response_wrapper(
            custom_fields.change_status,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._custom_fields.templates)

    @cached_property
    def fields(self) -> FieldsResourceWithStreamingResponse:
        return FieldsResourceWithStreamingResponse(self._custom_fields.fields)

    @cached_property
    def values(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self._custom_fields.values)


class AsyncCustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.change_status = async_to_streamed_response_wrapper(
            custom_fields.change_status,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._custom_fields.templates)

    @cached_property
    def fields(self) -> AsyncFieldsResourceWithStreamingResponse:
        return AsyncFieldsResourceWithStreamingResponse(self._custom_fields.fields)

    @cached_property
    def values(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self._custom_fields.values)
