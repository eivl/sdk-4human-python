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
from .....types.personnel.salary.elements import deduction_list_params, deduction_create_params, deduction_update_params
from .....types.personnel.salary.elements.deduction_list_response import DeductionListResponse
from .....types.personnel.salary.elements.deduction_create_response import DeductionCreateResponse
from .....types.personnel.salary.elements.deduction_update_response import DeductionUpdateResponse
from .....types.personnel.salary.elements.deduction_retrieve_response import DeductionRetrieveResponse

__all__ = ["DeductionsResource", "AsyncDeductionsResource"]


class DeductionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeductionsResourceWithRawResponse:
        return DeductionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeductionsResourceWithStreamingResponse:
        return DeductionsResourceWithStreamingResponse(self)

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
    ) -> DeductionCreateResponse:
        """
        Create salary deduction.

        Args:
          org_unit_ids: Does not work currently, it is for future uses

          show_in_profile: Does not affect the system, will be supported in next version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/salary/elements/deductions",
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
                deduction_create_params.DeductionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeductionCreateResponse,
        )

    def retrieve(
        self,
        deduction_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeductionRetrieveResponse:
        """
        Get salary deduction with given id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/personnel/salary/elements/deductions/{deduction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeductionRetrieveResponse,
        )

    def update(
        self,
        deduction_id: int,
        *,
        additional_main_salary: bool | NotGiven = NOT_GIVEN,
        amount: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_dates: deduction_update_params.EffectiveDates | NotGiven = NOT_GIVEN,
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
    ) -> DeductionUpdateResponse:
        """
        Edit single field of salary deduction with given id.

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
            f"/personnel/salary/elements/deductions/{deduction_id}",
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
                deduction_update_params.DeductionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeductionUpdateResponse,
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
    ) -> DeductionListResponse:
        """
        Get list of salary deductions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/salary/elements/deductions",
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
                    deduction_list_params.DeductionListParams,
                ),
            ),
            cast_to=DeductionListResponse,
        )


class AsyncDeductionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeductionsResourceWithRawResponse:
        return AsyncDeductionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeductionsResourceWithStreamingResponse:
        return AsyncDeductionsResourceWithStreamingResponse(self)

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
    ) -> DeductionCreateResponse:
        """
        Create salary deduction.

        Args:
          org_unit_ids: Does not work currently, it is for future uses

          show_in_profile: Does not affect the system, will be supported in next version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/salary/elements/deductions",
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
                deduction_create_params.DeductionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeductionCreateResponse,
        )

    async def retrieve(
        self,
        deduction_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeductionRetrieveResponse:
        """
        Get salary deduction with given id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/personnel/salary/elements/deductions/{deduction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeductionRetrieveResponse,
        )

    async def update(
        self,
        deduction_id: int,
        *,
        additional_main_salary: bool | NotGiven = NOT_GIVEN,
        amount: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        effective_dates: deduction_update_params.EffectiveDates | NotGiven = NOT_GIVEN,
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
    ) -> DeductionUpdateResponse:
        """
        Edit single field of salary deduction with given id.

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
            f"/personnel/salary/elements/deductions/{deduction_id}",
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
                deduction_update_params.DeductionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeductionUpdateResponse,
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
    ) -> DeductionListResponse:
        """
        Get list of salary deductions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/salary/elements/deductions",
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
                    deduction_list_params.DeductionListParams,
                ),
            ),
            cast_to=DeductionListResponse,
        )


class DeductionsResourceWithRawResponse:
    def __init__(self, deductions: DeductionsResource) -> None:
        self._deductions = deductions

        self.create = to_raw_response_wrapper(
            deductions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deductions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            deductions.update,
        )
        self.list = to_raw_response_wrapper(
            deductions.list,
        )


class AsyncDeductionsResourceWithRawResponse:
    def __init__(self, deductions: AsyncDeductionsResource) -> None:
        self._deductions = deductions

        self.create = async_to_raw_response_wrapper(
            deductions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deductions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            deductions.update,
        )
        self.list = async_to_raw_response_wrapper(
            deductions.list,
        )


class DeductionsResourceWithStreamingResponse:
    def __init__(self, deductions: DeductionsResource) -> None:
        self._deductions = deductions

        self.create = to_streamed_response_wrapper(
            deductions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deductions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            deductions.update,
        )
        self.list = to_streamed_response_wrapper(
            deductions.list,
        )


class AsyncDeductionsResourceWithStreamingResponse:
    def __init__(self, deductions: AsyncDeductionsResource) -> None:
        self._deductions = deductions

        self.create = async_to_streamed_response_wrapper(
            deductions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deductions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            deductions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            deductions.list,
        )
