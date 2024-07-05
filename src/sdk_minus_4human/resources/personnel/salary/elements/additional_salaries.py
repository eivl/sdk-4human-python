# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import (
    make_request_options,
)
from .....types.personnel.salary.elements import (
    additional_salary_list_params,
    additional_salary_create_params,
    additional_salary_update_params,
)
from .....types.personnel.salary.elements.additional_salary_list_response import AdditionalSalaryListResponse
from .....types.personnel.salary.elements.additional_salary_create_response import AdditionalSalaryCreateResponse
from .....types.personnel.salary.elements.additional_salary_update_response import AdditionalSalaryUpdateResponse
from .....types.personnel.salary.elements.additional_salary_retrieve_response import AdditionalSalaryRetrieveResponse

__all__ = ["AdditionalSalariesResource", "AsyncAdditionalSalariesResource"]


class AdditionalSalariesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdditionalSalariesResourceWithRawResponse:
        return AdditionalSalariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdditionalSalariesResourceWithStreamingResponse:
        return AdditionalSalariesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: Optional[str],
        currency: Optional[str],
        description: Optional[str],
        external_id: str,
        include_to_contract: bool,
        individual: bool,
        internal_id: str,
        job_ids: Optional[Iterable[int]],
        mandatory: bool,
        name: str,
        org_unit_ids: Optional[Iterable[int]],
        period: Optional[
            Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
        ],
        show_in_profile: bool,
        status: Literal["active"],
        type: Literal["rate", "text"],
        additional_main_salary: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalSalaryCreateResponse:
        """
        Create additional salary.

        Args:
          org_unit_ids: Does not work currently, it is for future uses

          show_in_profile: Does not affect the system, will be supported in next version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/salary/elements/additional-salaries",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                    "external_id": external_id,
                    "include_to_contract": include_to_contract,
                    "individual": individual,
                    "internal_id": internal_id,
                    "job_ids": job_ids,
                    "mandatory": mandatory,
                    "name": name,
                    "org_unit_ids": org_unit_ids,
                    "period": period,
                    "show_in_profile": show_in_profile,
                    "status": status,
                    "type": type,
                    "additional_main_salary": additional_main_salary,
                },
                additional_salary_create_params.AdditionalSalaryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdditionalSalaryCreateResponse,
        )

    def retrieve(
        self,
        additional_salary_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalSalaryRetrieveResponse:
        """
        Get additional salary with given id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/personnel/salary/elements/additional-salaries/{additional_salary_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdditionalSalaryRetrieveResponse,
        )

    def update(
        self,
        additional_salary_id: int,
        *,
        additional_main_salary: bool | NotGiven = NOT_GIVEN,
        amount: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_dates: additional_salary_update_params.EffectiveDates | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        include_to_contract: bool | NotGiven = NOT_GIVEN,
        individual: bool | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        job_ids: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        mandatory: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        org_unit_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        period: Optional[
            Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
        ]
        | NotGiven = NOT_GIVEN,
        show_in_profile: bool | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        type: Literal["rate", "text"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalSalaryUpdateResponse:
        """
        Edit single field of additional salary with given id.

        Args:
          effective_dates: - If effectiveDates are not provided, the changes will be immediate.
              - Only following fields can be scheduled: `amount`, `currency`, `description`.
                Other fields will be changed immediately.

          org_unit_ids: Does not work currently, it is for future uses

          show_in_profile: Does not affect the system, will be supported in next version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/personnel/salary/elements/additional-salaries/{additional_salary_id}",
            body=maybe_transform(
                {
                    "additional_main_salary": additional_main_salary,
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                    "effective_dates": effective_dates,
                    "external_id": external_id,
                    "include_to_contract": include_to_contract,
                    "individual": individual,
                    "internal_id": internal_id,
                    "job_ids": job_ids,
                    "mandatory": mandatory,
                    "name": name,
                    "org_unit_ids": org_unit_ids,
                    "period": period,
                    "show_in_profile": show_in_profile,
                    "status": status,
                    "type": type,
                },
                additional_salary_update_params.AdditionalSalaryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdditionalSalaryUpdateResponse,
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
    ) -> AdditionalSalaryListResponse:
        """
        Get list of additional salaries.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/salary/elements/additional-salaries",
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
                    additional_salary_list_params.AdditionalSalaryListParams,
                ),
            ),
            cast_to=AdditionalSalaryListResponse,
        )


class AsyncAdditionalSalariesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdditionalSalariesResourceWithRawResponse:
        return AsyncAdditionalSalariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdditionalSalariesResourceWithStreamingResponse:
        return AsyncAdditionalSalariesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: Optional[str],
        currency: Optional[str],
        description: Optional[str],
        external_id: str,
        include_to_contract: bool,
        individual: bool,
        internal_id: str,
        job_ids: Optional[Iterable[int]],
        mandatory: bool,
        name: str,
        org_unit_ids: Optional[Iterable[int]],
        period: Optional[
            Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
        ],
        show_in_profile: bool,
        status: Literal["active"],
        type: Literal["rate", "text"],
        additional_main_salary: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalSalaryCreateResponse:
        """
        Create additional salary.

        Args:
          org_unit_ids: Does not work currently, it is for future uses

          show_in_profile: Does not affect the system, will be supported in next version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/salary/elements/additional-salaries",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                    "external_id": external_id,
                    "include_to_contract": include_to_contract,
                    "individual": individual,
                    "internal_id": internal_id,
                    "job_ids": job_ids,
                    "mandatory": mandatory,
                    "name": name,
                    "org_unit_ids": org_unit_ids,
                    "period": period,
                    "show_in_profile": show_in_profile,
                    "status": status,
                    "type": type,
                    "additional_main_salary": additional_main_salary,
                },
                additional_salary_create_params.AdditionalSalaryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdditionalSalaryCreateResponse,
        )

    async def retrieve(
        self,
        additional_salary_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalSalaryRetrieveResponse:
        """
        Get additional salary with given id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/personnel/salary/elements/additional-salaries/{additional_salary_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdditionalSalaryRetrieveResponse,
        )

    async def update(
        self,
        additional_salary_id: int,
        *,
        additional_main_salary: bool | NotGiven = NOT_GIVEN,
        amount: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_dates: additional_salary_update_params.EffectiveDates | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        include_to_contract: bool | NotGiven = NOT_GIVEN,
        individual: bool | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        job_ids: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        mandatory: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        org_unit_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        period: Optional[
            Literal["SALARY_PERIOD_HOUR", "SALARY_PERIOD_WEEK", "SALARY_PERIOD_MONTH", "SALARY_PERIOD_YEAR"]
        ]
        | NotGiven = NOT_GIVEN,
        show_in_profile: bool | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        type: Literal["rate", "text"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalSalaryUpdateResponse:
        """
        Edit single field of additional salary with given id.

        Args:
          effective_dates: - If effectiveDates are not provided, the changes will be immediate.
              - Only following fields can be scheduled: `amount`, `currency`, `description`.
                Other fields will be changed immediately.

          org_unit_ids: Does not work currently, it is for future uses

          show_in_profile: Does not affect the system, will be supported in next version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/personnel/salary/elements/additional-salaries/{additional_salary_id}",
            body=await async_maybe_transform(
                {
                    "additional_main_salary": additional_main_salary,
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                    "effective_dates": effective_dates,
                    "external_id": external_id,
                    "include_to_contract": include_to_contract,
                    "individual": individual,
                    "internal_id": internal_id,
                    "job_ids": job_ids,
                    "mandatory": mandatory,
                    "name": name,
                    "org_unit_ids": org_unit_ids,
                    "period": period,
                    "show_in_profile": show_in_profile,
                    "status": status,
                    "type": type,
                },
                additional_salary_update_params.AdditionalSalaryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdditionalSalaryUpdateResponse,
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
    ) -> AdditionalSalaryListResponse:
        """
        Get list of additional salaries.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/salary/elements/additional-salaries",
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
                    additional_salary_list_params.AdditionalSalaryListParams,
                ),
            ),
            cast_to=AdditionalSalaryListResponse,
        )


class AdditionalSalariesResourceWithRawResponse:
    def __init__(self, additional_salaries: AdditionalSalariesResource) -> None:
        self._additional_salaries = additional_salaries

        self.create = to_raw_response_wrapper(
            additional_salaries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            additional_salaries.retrieve,
        )
        self.update = to_raw_response_wrapper(
            additional_salaries.update,
        )
        self.list = to_raw_response_wrapper(
            additional_salaries.list,
        )


class AsyncAdditionalSalariesResourceWithRawResponse:
    def __init__(self, additional_salaries: AsyncAdditionalSalariesResource) -> None:
        self._additional_salaries = additional_salaries

        self.create = async_to_raw_response_wrapper(
            additional_salaries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            additional_salaries.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            additional_salaries.update,
        )
        self.list = async_to_raw_response_wrapper(
            additional_salaries.list,
        )


class AdditionalSalariesResourceWithStreamingResponse:
    def __init__(self, additional_salaries: AdditionalSalariesResource) -> None:
        self._additional_salaries = additional_salaries

        self.create = to_streamed_response_wrapper(
            additional_salaries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            additional_salaries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            additional_salaries.update,
        )
        self.list = to_streamed_response_wrapper(
            additional_salaries.list,
        )


class AsyncAdditionalSalariesResourceWithStreamingResponse:
    def __init__(self, additional_salaries: AsyncAdditionalSalariesResource) -> None:
        self._additional_salaries = additional_salaries

        self.create = async_to_streamed_response_wrapper(
            additional_salaries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            additional_salaries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            additional_salaries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            additional_salaries.list,
        )
