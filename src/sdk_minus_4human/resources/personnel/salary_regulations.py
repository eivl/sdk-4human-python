# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.personnel import salary_regulation_list_params
from ...types.personnel.salary_regulation_list_response import SalaryRegulationListResponse

__all__ = ["SalaryRegulationsResource", "AsyncSalaryRegulationsResource"]


class SalaryRegulationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SalaryRegulationsResourceWithRawResponse:
        return SalaryRegulationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalaryRegulationsResourceWithStreamingResponse:
        return SalaryRegulationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        reference_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalaryRegulationListResponse:
        """
        Get list of salary regulations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/salary-regulations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "reference_id": reference_id,
                    },
                    salary_regulation_list_params.SalaryRegulationListParams,
                ),
            ),
            cast_to=SalaryRegulationListResponse,
        )


class AsyncSalaryRegulationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSalaryRegulationsResourceWithRawResponse:
        return AsyncSalaryRegulationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalaryRegulationsResourceWithStreamingResponse:
        return AsyncSalaryRegulationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        reference_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalaryRegulationListResponse:
        """
        Get list of salary regulations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/salary-regulations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "reference_id": reference_id,
                    },
                    salary_regulation_list_params.SalaryRegulationListParams,
                ),
            ),
            cast_to=SalaryRegulationListResponse,
        )


class SalaryRegulationsResourceWithRawResponse:
    def __init__(self, salary_regulations: SalaryRegulationsResource) -> None:
        self._salary_regulations = salary_regulations

        self.list = to_raw_response_wrapper(
            salary_regulations.list,
        )


class AsyncSalaryRegulationsResourceWithRawResponse:
    def __init__(self, salary_regulations: AsyncSalaryRegulationsResource) -> None:
        self._salary_regulations = salary_regulations

        self.list = async_to_raw_response_wrapper(
            salary_regulations.list,
        )


class SalaryRegulationsResourceWithStreamingResponse:
    def __init__(self, salary_regulations: SalaryRegulationsResource) -> None:
        self._salary_regulations = salary_regulations

        self.list = to_streamed_response_wrapper(
            salary_regulations.list,
        )


class AsyncSalaryRegulationsResourceWithStreamingResponse:
    def __init__(self, salary_regulations: AsyncSalaryRegulationsResource) -> None:
        self._salary_regulations = salary_regulations

        self.list = async_to_streamed_response_wrapper(
            salary_regulations.list,
        )
