# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.competence.skill_types.configuration_list_response import ConfigurationListResponse

__all__ = ["ConfigurationResource", "AsyncConfigurationResource"]


class ConfigurationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationResourceWithRawResponse:
        return ConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationResourceWithStreamingResponse:
        return ConfigurationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationListResponse:
        """
        This endpoint returns whole structure of skill type needed to generate empty
        form by fronted site.
        """
        return self._get(
            "/competence/skill-types/configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationListResponse,
        )


class AsyncConfigurationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationResourceWithRawResponse:
        return AsyncConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationResourceWithStreamingResponse:
        return AsyncConfigurationResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationListResponse:
        """
        This endpoint returns whole structure of skill type needed to generate empty
        form by fronted site.
        """
        return await self._get(
            "/competence/skill-types/configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationListResponse,
        )


class ConfigurationResourceWithRawResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.list = to_raw_response_wrapper(
            configuration.list,
        )


class AsyncConfigurationResourceWithRawResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.list = async_to_raw_response_wrapper(
            configuration.list,
        )


class ConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.list = to_streamed_response_wrapper(
            configuration.list,
        )


class AsyncConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.list = async_to_streamed_response_wrapper(
            configuration.list,
        )
