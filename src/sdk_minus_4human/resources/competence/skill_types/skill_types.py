# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from .configuration import (
    ConfigurationResource,
    AsyncConfigurationResource,
    ConfigurationResourceWithRawResponse,
    AsyncConfigurationResourceWithRawResponse,
    ConfigurationResourceWithStreamingResponse,
    AsyncConfigurationResourceWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.competence import skill_type_list_params
from ....types.competence.skill_type_list_response import SkillTypeListResponse

__all__ = ["SkillTypesResource", "AsyncSkillTypesResource"]


class SkillTypesResource(SyncAPIResource):
    @cached_property
    def configuration(self) -> ConfigurationResource:
        return ConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> SkillTypesResourceWithRawResponse:
        return SkillTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillTypesResourceWithStreamingResponse:
        return SkillTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeListResponse:
        """
        Get list of competence skill types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/competence/skill-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    skill_type_list_params.SkillTypeListParams,
                ),
            ),
            cast_to=SkillTypeListResponse,
        )


class AsyncSkillTypesResource(AsyncAPIResource):
    @cached_property
    def configuration(self) -> AsyncConfigurationResource:
        return AsyncConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSkillTypesResourceWithRawResponse:
        return AsyncSkillTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillTypesResourceWithStreamingResponse:
        return AsyncSkillTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeListResponse:
        """
        Get list of competence skill types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/competence/skill-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    skill_type_list_params.SkillTypeListParams,
                ),
            ),
            cast_to=SkillTypeListResponse,
        )


class SkillTypesResourceWithRawResponse:
    def __init__(self, skill_types: SkillTypesResource) -> None:
        self._skill_types = skill_types

        self.list = to_raw_response_wrapper(
            skill_types.list,
        )

    @cached_property
    def configuration(self) -> ConfigurationResourceWithRawResponse:
        return ConfigurationResourceWithRawResponse(self._skill_types.configuration)


class AsyncSkillTypesResourceWithRawResponse:
    def __init__(self, skill_types: AsyncSkillTypesResource) -> None:
        self._skill_types = skill_types

        self.list = async_to_raw_response_wrapper(
            skill_types.list,
        )

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithRawResponse:
        return AsyncConfigurationResourceWithRawResponse(self._skill_types.configuration)


class SkillTypesResourceWithStreamingResponse:
    def __init__(self, skill_types: SkillTypesResource) -> None:
        self._skill_types = skill_types

        self.list = to_streamed_response_wrapper(
            skill_types.list,
        )

    @cached_property
    def configuration(self) -> ConfigurationResourceWithStreamingResponse:
        return ConfigurationResourceWithStreamingResponse(self._skill_types.configuration)


class AsyncSkillTypesResourceWithStreamingResponse:
    def __init__(self, skill_types: AsyncSkillTypesResource) -> None:
        self._skill_types = skill_types

        self.list = async_to_streamed_response_wrapper(
            skill_types.list,
        )

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithStreamingResponse:
        return AsyncConfigurationResourceWithStreamingResponse(self._skill_types.configuration)