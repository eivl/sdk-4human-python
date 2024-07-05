# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ...types import external_integration_run_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from .feature_status import (
    FeatureStatusResource,
    AsyncFeatureStatusResource,
    FeatureStatusResourceWithRawResponse,
    AsyncFeatureStatusResourceWithRawResponse,
    FeatureStatusResourceWithStreamingResponse,
    AsyncFeatureStatusResourceWithStreamingResponse,
)
from ...types.external_integration_run_response import ExternalIntegrationRunResponse

__all__ = ["ExternalIntegrationsResource", "AsyncExternalIntegrationsResource"]


class ExternalIntegrationsResource(SyncAPIResource):
    @cached_property
    def feature_status(self) -> FeatureStatusResource:
        return FeatureStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExternalIntegrationsResourceWithRawResponse:
        return ExternalIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalIntegrationsResourceWithStreamingResponse:
        return ExternalIntegrationsResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        feature_name: str,
        cron_expression: Optional[str] | NotGiven = NOT_GIVEN,
        run_hours: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalIntegrationRunResponse:
        """
        Run Integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external-integrations/run",
            body=maybe_transform(
                {
                    "feature_name": feature_name,
                    "cron_expression": cron_expression,
                    "run_hours": run_hours,
                },
                external_integration_run_params.ExternalIntegrationRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalIntegrationRunResponse,
        )


class AsyncExternalIntegrationsResource(AsyncAPIResource):
    @cached_property
    def feature_status(self) -> AsyncFeatureStatusResource:
        return AsyncFeatureStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExternalIntegrationsResourceWithRawResponse:
        return AsyncExternalIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalIntegrationsResourceWithStreamingResponse:
        return AsyncExternalIntegrationsResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        feature_name: str,
        cron_expression: Optional[str] | NotGiven = NOT_GIVEN,
        run_hours: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalIntegrationRunResponse:
        """
        Run Integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external-integrations/run",
            body=await async_maybe_transform(
                {
                    "feature_name": feature_name,
                    "cron_expression": cron_expression,
                    "run_hours": run_hours,
                },
                external_integration_run_params.ExternalIntegrationRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalIntegrationRunResponse,
        )


class ExternalIntegrationsResourceWithRawResponse:
    def __init__(self, external_integrations: ExternalIntegrationsResource) -> None:
        self._external_integrations = external_integrations

        self.run = to_raw_response_wrapper(
            external_integrations.run,
        )

    @cached_property
    def feature_status(self) -> FeatureStatusResourceWithRawResponse:
        return FeatureStatusResourceWithRawResponse(self._external_integrations.feature_status)


class AsyncExternalIntegrationsResourceWithRawResponse:
    def __init__(self, external_integrations: AsyncExternalIntegrationsResource) -> None:
        self._external_integrations = external_integrations

        self.run = async_to_raw_response_wrapper(
            external_integrations.run,
        )

    @cached_property
    def feature_status(self) -> AsyncFeatureStatusResourceWithRawResponse:
        return AsyncFeatureStatusResourceWithRawResponse(self._external_integrations.feature_status)


class ExternalIntegrationsResourceWithStreamingResponse:
    def __init__(self, external_integrations: ExternalIntegrationsResource) -> None:
        self._external_integrations = external_integrations

        self.run = to_streamed_response_wrapper(
            external_integrations.run,
        )

    @cached_property
    def feature_status(self) -> FeatureStatusResourceWithStreamingResponse:
        return FeatureStatusResourceWithStreamingResponse(self._external_integrations.feature_status)


class AsyncExternalIntegrationsResourceWithStreamingResponse:
    def __init__(self, external_integrations: AsyncExternalIntegrationsResource) -> None:
        self._external_integrations = external_integrations

        self.run = async_to_streamed_response_wrapper(
            external_integrations.run,
        )

    @cached_property
    def feature_status(self) -> AsyncFeatureStatusResourceWithStreamingResponse:
        return AsyncFeatureStatusResourceWithStreamingResponse(self._external_integrations.feature_status)
