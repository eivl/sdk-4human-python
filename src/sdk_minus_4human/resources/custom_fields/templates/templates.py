# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .global_ import (
    GlobalResource,
    AsyncGlobalResource,
    GlobalResourceWithRawResponse,
    AsyncGlobalResourceWithRawResponse,
    GlobalResourceWithStreamingResponse,
    AsyncGlobalResourceWithStreamingResponse,
)
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
from ....types.custom_fields import template_create_params, template_update_params
from ....types.custom_fields.template_list_response import TemplateListResponse
from ....types.custom_fields.template_create_response import TemplateCreateResponse
from ....types.custom_fields.template_update_response import TemplateUpdateResponse
from ....types.custom_fields.template_retrieve_response import TemplateRetrieveResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    @cached_property
    def global_(self) -> GlobalResource:
        return GlobalResource(self._client)

    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str],
        external_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemplateCreateResponse:
        """
        Custom field template is a structure that contains custom fields definitions and
        can be assigned to one or more companies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/custom-fields/templates",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateResponse,
        )

    def retrieve(
        self,
        company_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemplateRetrieveResponse:
        """
        Get custom fields template assigned to company with given database id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/personnel/custom-fields/templates/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRetrieveResponse,
        )

    def update(
        self,
        template_id: str,
        *,
        description: Optional[str],
        external_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemplateUpdateResponse:
        """
        Use this endpoint to modify custom field templates designated for assignment to
        companies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._put(
            f"/personnel/custom-fields/templates/{template_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                },
                template_update_params.TemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemplateListResponse:
        """Response returns company list paired with custom field templates."""
        return self._get(
            "/personnel/custom-fields/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateListResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    @cached_property
    def global_(self) -> AsyncGlobalResource:
        return AsyncGlobalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str],
        external_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemplateCreateResponse:
        """
        Custom field template is a structure that contains custom fields definitions and
        can be assigned to one or more companies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/custom-fields/templates",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateResponse,
        )

    async def retrieve(
        self,
        company_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemplateRetrieveResponse:
        """
        Get custom fields template assigned to company with given database id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/personnel/custom-fields/templates/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRetrieveResponse,
        )

    async def update(
        self,
        template_id: str,
        *,
        description: Optional[str],
        external_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemplateUpdateResponse:
        """
        Use this endpoint to modify custom field templates designated for assignment to
        companies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._put(
            f"/personnel/custom-fields/templates/{template_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "name": name,
                },
                template_update_params.TemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemplateListResponse:
        """Response returns company list paired with custom field templates."""
        return await self._get(
            "/personnel/custom-fields/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateListResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_raw_response_wrapper(
            templates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            templates.retrieve,
        )
        self.update = to_raw_response_wrapper(
            templates.update,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )

    @cached_property
    def global_(self) -> GlobalResourceWithRawResponse:
        return GlobalResourceWithRawResponse(self._templates.global_)


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_raw_response_wrapper(
            templates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            templates.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            templates.update,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )

    @cached_property
    def global_(self) -> AsyncGlobalResourceWithRawResponse:
        return AsyncGlobalResourceWithRawResponse(self._templates.global_)


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_streamed_response_wrapper(
            templates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            templates.update,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )

    @cached_property
    def global_(self) -> GlobalResourceWithStreamingResponse:
        return GlobalResourceWithStreamingResponse(self._templates.global_)


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_streamed_response_wrapper(
            templates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )

    @cached_property
    def global_(self) -> AsyncGlobalResourceWithStreamingResponse:
        return AsyncGlobalResourceWithStreamingResponse(self._templates.global_)
