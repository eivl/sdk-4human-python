# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    company_employee_list_params,
    company_employee_update_params,
    company_employee_retrieve_params,
    company_employee_update_partial_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.company_employee_list_response import CompanyEmployeeListResponse
from ..types.company_employee_update_response import CompanyEmployeeUpdateResponse
from ..types.company_employee_retrieve_response import CompanyEmployeeRetrieveResponse
from ..types.company_employee_update_partial_response import CompanyEmployeeUpdatePartialResponse

__all__ = ["CompanyEmployeesResource", "AsyncCompanyEmployeesResource"]


class CompanyEmployeesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompanyEmployeesResourceWithRawResponse:
        return CompanyEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyEmployeesResourceWithStreamingResponse:
        return CompanyEmployeesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        company_employee_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyEmployeeRetrieveResponse:
        """
        Get company employee details.

        Args:
          external: Param determines if id of company employee is external (employeeId) or internal
              (id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_employee_id:
            raise ValueError(
                f"Expected a non-empty value for `company_employee_id` but received {company_employee_id!r}"
            )
        return self._get(
            f"/personnel/company-employees/{company_employee_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external": external}, company_employee_retrieve_params.CompanyEmployeeRetrieveParams
                ),
            ),
            cast_to=CompanyEmployeeRetrieveResponse,
        )

    def update(
        self,
        company_employee_id: int,
        *,
        custom_fields: Iterable[company_employee_update_params.CustomField],
        effective_dates: company_employee_update_params.EffectiveDates,
        employee_id: str,
        free_employer: Optional[company_employee_update_params.FreeEmployer],
        industry_ids: Iterable[company_employee_update_params.IndustryID],
        main_employer: bool,
        primary_employment_id: int,
        ready_for_payment: bool,
        residence_permit: Optional[company_employee_update_params.ResidencePermit],
        resource_type: Optional[int],
        salary_number: Optional[str],
        self_sickness: Optional[str],
        seniority_date: Optional[str],
        termination_seniority_date: Optional[str],
        work_permit: Optional[company_employee_update_params.WorkPermit],
        work_status: str,
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        max_date_follow_up_sickness: Optional[str] | NotGiven = NOT_GIVEN,
        max_date_sickness_refund: Optional[str] | NotGiven = NOT_GIVEN,
        retirement_date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyEmployeeUpdateResponse:
        """
        Update a company employee.

        Args:
          external: Param determines if id of company employee is external (employeeId) or internal
              (id)

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/personnel/company-employees/{company_employee_id}",
            body=maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "effective_dates": effective_dates,
                    "employee_id": employee_id,
                    "free_employer": free_employer,
                    "industry_ids": industry_ids,
                    "main_employer": main_employer,
                    "primary_employment_id": primary_employment_id,
                    "ready_for_payment": ready_for_payment,
                    "residence_permit": residence_permit,
                    "resource_type": resource_type,
                    "salary_number": salary_number,
                    "self_sickness": self_sickness,
                    "seniority_date": seniority_date,
                    "termination_seniority_date": termination_seniority_date,
                    "work_permit": work_permit,
                    "work_status": work_status,
                    "max_date_follow_up_sickness": max_date_follow_up_sickness,
                    "max_date_sickness_refund": max_date_sickness_refund,
                    "retirement_date": retirement_date,
                },
                company_employee_update_params.CompanyEmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external": external,
                        "force_no_approval_policy": force_no_approval_policy,
                    },
                    company_employee_update_params.CompanyEmployeeUpdateParams,
                ),
            ),
            cast_to=CompanyEmployeeUpdateResponse,
        )

    def list(
        self,
        *,
        company_id: int | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        employment_id: str | NotGiven = NOT_GIVEN,
        external: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyEmployeeListResponse:
        """
        Get company employees

        Args:
          external: Param determines if employmentId used in filter is external (number) or internal
              (id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/company-employees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "employee_id": employee_id,
                        "employment_id": employment_id,
                        "external": external,
                        "limit": limit,
                        "page": page,
                        "user_id": user_id,
                    },
                    company_employee_list_params.CompanyEmployeeListParams,
                ),
            ),
            cast_to=CompanyEmployeeListResponse,
        )

    def update_partial(
        self,
        company_employee_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[company_employee_update_partial_params.CustomField] | NotGiven = NOT_GIVEN,
        effective_dates: company_employee_update_partial_params.EffectiveDates | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        free_employer: Optional[company_employee_update_partial_params.FreeEmployer] | NotGiven = NOT_GIVEN,
        main_employer: bool | NotGiven = NOT_GIVEN,
        max_date_follow_up_sickness: Optional[str] | NotGiven = NOT_GIVEN,
        max_date_sickness_refund: Optional[str] | NotGiven = NOT_GIVEN,
        primary_employment_id: int | NotGiven = NOT_GIVEN,
        ready_for_payment: bool | NotGiven = NOT_GIVEN,
        residence_permit: Optional[company_employee_update_partial_params.ResidencePermit] | NotGiven = NOT_GIVEN,
        resource_type: Optional[int] | NotGiven = NOT_GIVEN,
        retirement_date: Optional[str] | NotGiven = NOT_GIVEN,
        salary_number: Optional[str] | NotGiven = NOT_GIVEN,
        self_sickness: Optional[str] | NotGiven = NOT_GIVEN,
        seniority_date: Optional[str] | NotGiven = NOT_GIVEN,
        termination_seniority_date: Optional[str] | NotGiven = NOT_GIVEN,
        work_permit: Optional[company_employee_update_partial_params.WorkPermit] | NotGiven = NOT_GIVEN,
        work_status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyEmployeeUpdatePartialResponse:
        """Only visible fields configured by field templates can be updated.

        Trying to
        update the not visible field will response with an error.<br /><br /> How to
        work with nested fields:

        - Industry - `"industryIds"`:
          - `"id": null` or missing `"id"` - will create a new industry
          - `"id": ...` - will edit particular industry
          - not listed industry will not be deleted/updated (there is no possible to
            delete industry)
        - Custom fields - `"customFields"`:
          - `"fieldId": ...` - will edit particular custom field
          - `"fieldId": ...` with `"valueId": null"` - will delete local value and start
            inheritance from company
          - not listed custom field will not be deleted/updated
        - Nested fields with date range `"from"`/`"to"`:
          - only provided property will be edited (e.g. to edit only from date, provide
            only `"from"` property)
          - `"from": null` - will delete from date
          - `"to": null` - will delete to date
          - not listed `"from"`/`"to"` will not deleted/updated value

        Args:
          external: Param determines if id of company employee is external (employeeId) or internal
              (id)

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          effective_dates: If effectiveDates are not provided, the changes will be immediate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_employee_id:
            raise ValueError(
                f"Expected a non-empty value for `company_employee_id` but received {company_employee_id!r}"
            )
        return self._patch(
            f"/personnel/company-employees/{company_employee_id}",
            body=maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "effective_dates": effective_dates,
                    "employee_id": employee_id,
                    "free_employer": free_employer,
                    "main_employer": main_employer,
                    "max_date_follow_up_sickness": max_date_follow_up_sickness,
                    "max_date_sickness_refund": max_date_sickness_refund,
                    "primary_employment_id": primary_employment_id,
                    "ready_for_payment": ready_for_payment,
                    "residence_permit": residence_permit,
                    "resource_type": resource_type,
                    "retirement_date": retirement_date,
                    "salary_number": salary_number,
                    "self_sickness": self_sickness,
                    "seniority_date": seniority_date,
                    "termination_seniority_date": termination_seniority_date,
                    "work_permit": work_permit,
                    "work_status": work_status,
                },
                company_employee_update_partial_params.CompanyEmployeeUpdatePartialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external": external,
                        "force_no_approval_policy": force_no_approval_policy,
                    },
                    company_employee_update_partial_params.CompanyEmployeeUpdatePartialParams,
                ),
            ),
            cast_to=CompanyEmployeeUpdatePartialResponse,
        )


class AsyncCompanyEmployeesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompanyEmployeesResourceWithRawResponse:
        return AsyncCompanyEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyEmployeesResourceWithStreamingResponse:
        return AsyncCompanyEmployeesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        company_employee_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyEmployeeRetrieveResponse:
        """
        Get company employee details.

        Args:
          external: Param determines if id of company employee is external (employeeId) or internal
              (id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_employee_id:
            raise ValueError(
                f"Expected a non-empty value for `company_employee_id` but received {company_employee_id!r}"
            )
        return await self._get(
            f"/personnel/company-employees/{company_employee_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, company_employee_retrieve_params.CompanyEmployeeRetrieveParams
                ),
            ),
            cast_to=CompanyEmployeeRetrieveResponse,
        )

    async def update(
        self,
        company_employee_id: int,
        *,
        custom_fields: Iterable[company_employee_update_params.CustomField],
        effective_dates: company_employee_update_params.EffectiveDates,
        employee_id: str,
        free_employer: Optional[company_employee_update_params.FreeEmployer],
        industry_ids: Iterable[company_employee_update_params.IndustryID],
        main_employer: bool,
        primary_employment_id: int,
        ready_for_payment: bool,
        residence_permit: Optional[company_employee_update_params.ResidencePermit],
        resource_type: Optional[int],
        salary_number: Optional[str],
        self_sickness: Optional[str],
        seniority_date: Optional[str],
        termination_seniority_date: Optional[str],
        work_permit: Optional[company_employee_update_params.WorkPermit],
        work_status: str,
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        max_date_follow_up_sickness: Optional[str] | NotGiven = NOT_GIVEN,
        max_date_sickness_refund: Optional[str] | NotGiven = NOT_GIVEN,
        retirement_date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyEmployeeUpdateResponse:
        """
        Update a company employee.

        Args:
          external: Param determines if id of company employee is external (employeeId) or internal
              (id)

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/personnel/company-employees/{company_employee_id}",
            body=await async_maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "effective_dates": effective_dates,
                    "employee_id": employee_id,
                    "free_employer": free_employer,
                    "industry_ids": industry_ids,
                    "main_employer": main_employer,
                    "primary_employment_id": primary_employment_id,
                    "ready_for_payment": ready_for_payment,
                    "residence_permit": residence_permit,
                    "resource_type": resource_type,
                    "salary_number": salary_number,
                    "self_sickness": self_sickness,
                    "seniority_date": seniority_date,
                    "termination_seniority_date": termination_seniority_date,
                    "work_permit": work_permit,
                    "work_status": work_status,
                    "max_date_follow_up_sickness": max_date_follow_up_sickness,
                    "max_date_sickness_refund": max_date_sickness_refund,
                    "retirement_date": retirement_date,
                },
                company_employee_update_params.CompanyEmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external": external,
                        "force_no_approval_policy": force_no_approval_policy,
                    },
                    company_employee_update_params.CompanyEmployeeUpdateParams,
                ),
            ),
            cast_to=CompanyEmployeeUpdateResponse,
        )

    async def list(
        self,
        *,
        company_id: int | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        employment_id: str | NotGiven = NOT_GIVEN,
        external: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyEmployeeListResponse:
        """
        Get company employees

        Args:
          external: Param determines if employmentId used in filter is external (number) or internal
              (id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/company-employees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "company_id": company_id,
                        "employee_id": employee_id,
                        "employment_id": employment_id,
                        "external": external,
                        "limit": limit,
                        "page": page,
                        "user_id": user_id,
                    },
                    company_employee_list_params.CompanyEmployeeListParams,
                ),
            ),
            cast_to=CompanyEmployeeListResponse,
        )

    async def update_partial(
        self,
        company_employee_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[company_employee_update_partial_params.CustomField] | NotGiven = NOT_GIVEN,
        effective_dates: company_employee_update_partial_params.EffectiveDates | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        free_employer: Optional[company_employee_update_partial_params.FreeEmployer] | NotGiven = NOT_GIVEN,
        main_employer: bool | NotGiven = NOT_GIVEN,
        max_date_follow_up_sickness: Optional[str] | NotGiven = NOT_GIVEN,
        max_date_sickness_refund: Optional[str] | NotGiven = NOT_GIVEN,
        primary_employment_id: int | NotGiven = NOT_GIVEN,
        ready_for_payment: bool | NotGiven = NOT_GIVEN,
        residence_permit: Optional[company_employee_update_partial_params.ResidencePermit] | NotGiven = NOT_GIVEN,
        resource_type: Optional[int] | NotGiven = NOT_GIVEN,
        retirement_date: Optional[str] | NotGiven = NOT_GIVEN,
        salary_number: Optional[str] | NotGiven = NOT_GIVEN,
        self_sickness: Optional[str] | NotGiven = NOT_GIVEN,
        seniority_date: Optional[str] | NotGiven = NOT_GIVEN,
        termination_seniority_date: Optional[str] | NotGiven = NOT_GIVEN,
        work_permit: Optional[company_employee_update_partial_params.WorkPermit] | NotGiven = NOT_GIVEN,
        work_status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyEmployeeUpdatePartialResponse:
        """Only visible fields configured by field templates can be updated.

        Trying to
        update the not visible field will response with an error.<br /><br /> How to
        work with nested fields:

        - Industry - `"industryIds"`:
          - `"id": null` or missing `"id"` - will create a new industry
          - `"id": ...` - will edit particular industry
          - not listed industry will not be deleted/updated (there is no possible to
            delete industry)
        - Custom fields - `"customFields"`:
          - `"fieldId": ...` - will edit particular custom field
          - `"fieldId": ...` with `"valueId": null"` - will delete local value and start
            inheritance from company
          - not listed custom field will not be deleted/updated
        - Nested fields with date range `"from"`/`"to"`:
          - only provided property will be edited (e.g. to edit only from date, provide
            only `"from"` property)
          - `"from": null` - will delete from date
          - `"to": null` - will delete to date
          - not listed `"from"`/`"to"` will not deleted/updated value

        Args:
          external: Param determines if id of company employee is external (employeeId) or internal
              (id)

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          effective_dates: If effectiveDates are not provided, the changes will be immediate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_employee_id:
            raise ValueError(
                f"Expected a non-empty value for `company_employee_id` but received {company_employee_id!r}"
            )
        return await self._patch(
            f"/personnel/company-employees/{company_employee_id}",
            body=await async_maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "effective_dates": effective_dates,
                    "employee_id": employee_id,
                    "free_employer": free_employer,
                    "main_employer": main_employer,
                    "max_date_follow_up_sickness": max_date_follow_up_sickness,
                    "max_date_sickness_refund": max_date_sickness_refund,
                    "primary_employment_id": primary_employment_id,
                    "ready_for_payment": ready_for_payment,
                    "residence_permit": residence_permit,
                    "resource_type": resource_type,
                    "retirement_date": retirement_date,
                    "salary_number": salary_number,
                    "self_sickness": self_sickness,
                    "seniority_date": seniority_date,
                    "termination_seniority_date": termination_seniority_date,
                    "work_permit": work_permit,
                    "work_status": work_status,
                },
                company_employee_update_partial_params.CompanyEmployeeUpdatePartialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external": external,
                        "force_no_approval_policy": force_no_approval_policy,
                    },
                    company_employee_update_partial_params.CompanyEmployeeUpdatePartialParams,
                ),
            ),
            cast_to=CompanyEmployeeUpdatePartialResponse,
        )


class CompanyEmployeesResourceWithRawResponse:
    def __init__(self, company_employees: CompanyEmployeesResource) -> None:
        self._company_employees = company_employees

        self.retrieve = to_raw_response_wrapper(
            company_employees.retrieve,
        )
        self.update = to_raw_response_wrapper(
            company_employees.update,
        )
        self.list = to_raw_response_wrapper(
            company_employees.list,
        )
        self.update_partial = to_raw_response_wrapper(
            company_employees.update_partial,
        )


class AsyncCompanyEmployeesResourceWithRawResponse:
    def __init__(self, company_employees: AsyncCompanyEmployeesResource) -> None:
        self._company_employees = company_employees

        self.retrieve = async_to_raw_response_wrapper(
            company_employees.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            company_employees.update,
        )
        self.list = async_to_raw_response_wrapper(
            company_employees.list,
        )
        self.update_partial = async_to_raw_response_wrapper(
            company_employees.update_partial,
        )


class CompanyEmployeesResourceWithStreamingResponse:
    def __init__(self, company_employees: CompanyEmployeesResource) -> None:
        self._company_employees = company_employees

        self.retrieve = to_streamed_response_wrapper(
            company_employees.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            company_employees.update,
        )
        self.list = to_streamed_response_wrapper(
            company_employees.list,
        )
        self.update_partial = to_streamed_response_wrapper(
            company_employees.update_partial,
        )


class AsyncCompanyEmployeesResourceWithStreamingResponse:
    def __init__(self, company_employees: AsyncCompanyEmployeesResource) -> None:
        self._company_employees = company_employees

        self.retrieve = async_to_streamed_response_wrapper(
            company_employees.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            company_employees.update,
        )
        self.list = async_to_streamed_response_wrapper(
            company_employees.list,
        )
        self.update_partial = async_to_streamed_response_wrapper(
            company_employees.update_partial,
        )
