# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

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
from ...types.personnel import (
    individual_main_salary_list_params,
    individual_main_salary_create_params,
    individual_main_salary_update_params,
)
from ...types.personnel.individual_main_salary_list_response import IndividualMainSalaryListResponse
from ...types.personnel.individual_main_salary_create_response import IndividualMainSalaryCreateResponse
from ...types.personnel.individual_main_salary_update_response import IndividualMainSalaryUpdateResponse
from ...types.personnel.individual_main_salary_retrieve_response import IndividualMainSalaryRetrieveResponse

__all__ = ["IndividualMainSalariesResource", "AsyncIndividualMainSalariesResource"]


class IndividualMainSalariesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndividualMainSalariesResourceWithRawResponse:
        return IndividualMainSalariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndividualMainSalariesResourceWithStreamingResponse:
        return IndividualMainSalariesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_id: str,
        internal_id: str,
        job_type_ids: Optional[Iterable[int]],
        name: str,
        period: Literal[
            "INDIVIDUAL_MAIN_SALARY_PERIOD_HOUR",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_WEEK",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_MONTH",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_YEAR",
        ],
        rate_based_on_wha: bool,
        status: Literal["active", "archived", "inactive"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualMainSalaryCreateResponse:
        """
        This endpoint allows you to create a new record for an individual main salary.
        Please provide the necessary information about the main salary in the request
        body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/individual-main-salary",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "job_type_ids": job_type_ids,
                    "name": name,
                    "period": period,
                    "rate_based_on_wha": rate_based_on_wha,
                    "status": status,
                },
                individual_main_salary_create_params.IndividualMainSalaryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualMainSalaryCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualMainSalaryRetrieveResponse:
        """
        This endpoint allows you to retrieve an individual main salary record by its
        unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/personnel/individual-main-salary/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualMainSalaryRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        external_id: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        job_type_ids: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        period: Literal[
            "INDIVIDUAL_MAIN_SALARY_PERIOD_HOUR",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_WEEK",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_MONTH",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_YEAR",
        ]
        | NotGiven = NOT_GIVEN,
        rate_based_on_wha: bool | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive", "archived"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualMainSalaryUpdateResponse:
        """
        This endpoint allows you to update a single field of an existing individual main
        salary record by its unique identifier. Please provide the updated field in the
        request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/personnel/individual-main-salary/{id}",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "job_type_ids": job_type_ids,
                    "name": name,
                    "period": period,
                    "rate_based_on_wha": rate_based_on_wha,
                    "status": status,
                },
                individual_main_salary_update_params.IndividualMainSalaryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualMainSalaryUpdateResponse,
        )

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
    ) -> IndividualMainSalaryListResponse:
        """This endpoint allows you to retrieve a list of individual main salaries.

        The
        results can be paginated by using the 'limit' and 'page' parameters.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/individual-main-salary",
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
                    individual_main_salary_list_params.IndividualMainSalaryListParams,
                ),
            ),
            cast_to=IndividualMainSalaryListResponse,
        )


class AsyncIndividualMainSalariesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndividualMainSalariesResourceWithRawResponse:
        return AsyncIndividualMainSalariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndividualMainSalariesResourceWithStreamingResponse:
        return AsyncIndividualMainSalariesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_id: str,
        internal_id: str,
        job_type_ids: Optional[Iterable[int]],
        name: str,
        period: Literal[
            "INDIVIDUAL_MAIN_SALARY_PERIOD_HOUR",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_WEEK",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_MONTH",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_YEAR",
        ],
        rate_based_on_wha: bool,
        status: Literal["active", "archived", "inactive"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualMainSalaryCreateResponse:
        """
        This endpoint allows you to create a new record for an individual main salary.
        Please provide the necessary information about the main salary in the request
        body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/individual-main-salary",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "job_type_ids": job_type_ids,
                    "name": name,
                    "period": period,
                    "rate_based_on_wha": rate_based_on_wha,
                    "status": status,
                },
                individual_main_salary_create_params.IndividualMainSalaryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualMainSalaryCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualMainSalaryRetrieveResponse:
        """
        This endpoint allows you to retrieve an individual main salary record by its
        unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/personnel/individual-main-salary/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualMainSalaryRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        external_id: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        job_type_ids: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        period: Literal[
            "INDIVIDUAL_MAIN_SALARY_PERIOD_HOUR",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_WEEK",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_MONTH",
            "INDIVIDUAL_MAIN_SALARY_PERIOD_YEAR",
        ]
        | NotGiven = NOT_GIVEN,
        rate_based_on_wha: bool | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive", "archived"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualMainSalaryUpdateResponse:
        """
        This endpoint allows you to update a single field of an existing individual main
        salary record by its unique identifier. Please provide the updated field in the
        request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/personnel/individual-main-salary/{id}",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "job_type_ids": job_type_ids,
                    "name": name,
                    "period": period,
                    "rate_based_on_wha": rate_based_on_wha,
                    "status": status,
                },
                individual_main_salary_update_params.IndividualMainSalaryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualMainSalaryUpdateResponse,
        )

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
    ) -> IndividualMainSalaryListResponse:
        """This endpoint allows you to retrieve a list of individual main salaries.

        The
        results can be paginated by using the 'limit' and 'page' parameters.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/individual-main-salary",
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
                    individual_main_salary_list_params.IndividualMainSalaryListParams,
                ),
            ),
            cast_to=IndividualMainSalaryListResponse,
        )


class IndividualMainSalariesResourceWithRawResponse:
    def __init__(self, individual_main_salaries: IndividualMainSalariesResource) -> None:
        self._individual_main_salaries = individual_main_salaries

        self.create = to_raw_response_wrapper(
            individual_main_salaries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            individual_main_salaries.retrieve,
        )
        self.update = to_raw_response_wrapper(
            individual_main_salaries.update,
        )
        self.list = to_raw_response_wrapper(
            individual_main_salaries.list,
        )


class AsyncIndividualMainSalariesResourceWithRawResponse:
    def __init__(self, individual_main_salaries: AsyncIndividualMainSalariesResource) -> None:
        self._individual_main_salaries = individual_main_salaries

        self.create = async_to_raw_response_wrapper(
            individual_main_salaries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            individual_main_salaries.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            individual_main_salaries.update,
        )
        self.list = async_to_raw_response_wrapper(
            individual_main_salaries.list,
        )


class IndividualMainSalariesResourceWithStreamingResponse:
    def __init__(self, individual_main_salaries: IndividualMainSalariesResource) -> None:
        self._individual_main_salaries = individual_main_salaries

        self.create = to_streamed_response_wrapper(
            individual_main_salaries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            individual_main_salaries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            individual_main_salaries.update,
        )
        self.list = to_streamed_response_wrapper(
            individual_main_salaries.list,
        )


class AsyncIndividualMainSalariesResourceWithStreamingResponse:
    def __init__(self, individual_main_salaries: AsyncIndividualMainSalariesResource) -> None:
        self._individual_main_salaries = individual_main_salaries

        self.create = async_to_streamed_response_wrapper(
            individual_main_salaries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            individual_main_salaries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            individual_main_salaries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            individual_main_salaries.list,
        )
