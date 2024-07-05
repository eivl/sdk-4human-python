# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import (
    make_request_options,
)
from ......types.personnel.custom_fields.templates import field_create_params, field_update_params
from ......types.personnel.custom_fields.templates.field_create_response import FieldCreateResponse
from ......types.personnel.custom_fields.templates.field_update_response import FieldUpdateResponse

__all__ = ["FieldsResource", "AsyncFieldsResource"]


class FieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FieldsResourceWithRawResponse:
        return FieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FieldsResourceWithStreamingResponse:
        return FieldsResourceWithStreamingResponse(self)

    def create(
        self,
        template_id: str,
        *,
        external_id: str,
        external_name: str,
        internal_id: str,
        name: str,
        children: Iterable[object] | NotGiven = NOT_GIVEN,
        field_type: Literal["structure", "date", "input", "textArea", "select"] | NotGiven = NOT_GIVEN,
        placing: field_create_params.Placing | NotGiven = NOT_GIVEN,
        validators: Optional[List[Literal["short", "medium", "long", "email", "number", "phone"]]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldCreateResponse:
        """Create custom field in a template identified by templateId UUID.

        Custom field
        template can be assigned to company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._post(
            f"/personnel/custom-fields/templates/{template_id}/fields",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "external_name": external_name,
                    "internal_id": internal_id,
                    "name": name,
                    "children": children,
                    "field_type": field_type,
                    "placing": placing,
                    "validators": validators,
                },
                field_create_params.FieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldCreateResponse,
        )

    def update(
        self,
        field_id: str,
        *,
        template_id: str,
        external_id: str,
        external_name: str,
        internal_id: Optional[str],
        name: Optional[str],
        placing: Optional[field_update_params.Placing] | NotGiven = NOT_GIVEN,
        validators: Optional[List[Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldUpdateResponse:
        """
        Edit single field of custom field in a given template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return self._patch(
            f"/personnel/custom-fields/templates/{template_id}/fields/{field_id}",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "external_name": external_name,
                    "internal_id": internal_id,
                    "name": name,
                    "placing": placing,
                    "validators": validators,
                },
                field_update_params.FieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldUpdateResponse,
        )


class AsyncFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFieldsResourceWithRawResponse:
        return AsyncFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFieldsResourceWithStreamingResponse:
        return AsyncFieldsResourceWithStreamingResponse(self)

    async def create(
        self,
        template_id: str,
        *,
        external_id: str,
        external_name: str,
        internal_id: str,
        name: str,
        children: Iterable[object] | NotGiven = NOT_GIVEN,
        field_type: Literal["structure", "date", "input", "textArea", "select"] | NotGiven = NOT_GIVEN,
        placing: field_create_params.Placing | NotGiven = NOT_GIVEN,
        validators: Optional[List[Literal["short", "medium", "long", "email", "number", "phone"]]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldCreateResponse:
        """Create custom field in a template identified by templateId UUID.

        Custom field
        template can be assigned to company.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._post(
            f"/personnel/custom-fields/templates/{template_id}/fields",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "external_name": external_name,
                    "internal_id": internal_id,
                    "name": name,
                    "children": children,
                    "field_type": field_type,
                    "placing": placing,
                    "validators": validators,
                },
                field_create_params.FieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldCreateResponse,
        )

    async def update(
        self,
        field_id: str,
        *,
        template_id: str,
        external_id: str,
        external_name: str,
        internal_id: Optional[str],
        name: Optional[str],
        placing: Optional[field_update_params.Placing] | NotGiven = NOT_GIVEN,
        validators: Optional[List[Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldUpdateResponse:
        """
        Edit single field of custom field in a given template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return await self._patch(
            f"/personnel/custom-fields/templates/{template_id}/fields/{field_id}",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "external_name": external_name,
                    "internal_id": internal_id,
                    "name": name,
                    "placing": placing,
                    "validators": validators,
                },
                field_update_params.FieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldUpdateResponse,
        )


class FieldsResourceWithRawResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

        self.create = to_raw_response_wrapper(
            fields.create,
        )
        self.update = to_raw_response_wrapper(
            fields.update,
        )


class AsyncFieldsResourceWithRawResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

        self.create = async_to_raw_response_wrapper(
            fields.create,
        )
        self.update = async_to_raw_response_wrapper(
            fields.update,
        )


class FieldsResourceWithStreamingResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

        self.create = to_streamed_response_wrapper(
            fields.create,
        )
        self.update = to_streamed_response_wrapper(
            fields.update,
        )


class AsyncFieldsResourceWithStreamingResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

        self.create = async_to_streamed_response_wrapper(
            fields.create,
        )
        self.update = async_to_streamed_response_wrapper(
            fields.update,
        )
