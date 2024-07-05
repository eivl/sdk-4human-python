# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import workplan_list_params, workplan_create_params, workplan_delete_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.workplan_list_response import WorkplanListResponse
from ..types.workplan_delete_response import WorkplanDeleteResponse

__all__ = ["WorkplansResource", "AsyncWorkplansResource"]


class WorkplansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkplansResourceWithRawResponse:
        return WorkplansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkplansResourceWithStreamingResponse:
        return WorkplansResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        calendar_days: Iterable[workplan_create_params.CalendarDay],
        date_from: str,
        date_to: str,
        company_employee_ids: Iterable[float] | NotGiven = NOT_GIVEN,
        company_id: float | NotGiven = NOT_GIVEN,
        employee_ids: List[str] | NotGiven = NOT_GIVEN,
        employment_ids: Iterable[float] | NotGiven = NOT_GIVEN,
        source_system: Optional[str] | NotGiven = NOT_GIVEN,
        unit_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This endpoint allows to create a new work plan.

        Body represents JavaScript array with json objects as elements. Each json object
        values need to satisfy json requirements. A value can be a string in double
        quotes or a number. At least one of the following parameters is required:
        employeeIds, companyEmployeeIds or employmentIds. For employeeId or
        companyEmployeeId either companyId or unitId is needed. If provided, data is
        created for all employments assigned to it.

        If employeeIds or companyEmployeeIds are provided, data is created for all
        employments assigned to this company employee.

        An employment work plan's dateFrom has to be before or equal to dateTo
        parameter. Maximum work plan's dateTo is limited to 18 months from current day.
        Hours for each date (calendarDays) must be specified within the dateFrom and
        dateTo parameters.

        Possible combinations:

        employeeIds -> create work plan calendar days hours per employee (applies to all
        employments)

        companyEmployeeIds -> create work plan calendar days hours per employee (applies
        to all employments)

        employmentIds -> create work plan calendar days hours per employment

        unitId - create work plan calendar days hours per company using unitId (applies
        to all employments in a given company by unit_id)

        companyId - create work plan calendar days hours per company (applies to all
        employments in a given company)

        When both unitId and employeeIds are provided -> create work plan calendar days
        hours per employee (all employments)

        When unitId and companyEmployeeIds are provided-> create work plan calendar days
        hours per employee (all employments)

        When companyId and employeeIds are provided -> create work plan calendar days
        hours per employee (all employments)

        When companyId and companyEmployeeIds are provided-> create work plan calendar
        days hours per employee (all employments)

        Args:
          date_from: The start date of the work plan. Format like 2023-06-05T00:00:00+00:00

          date_to: The end date of the work plan. Format like 2023-06-05T00:00:00+00:00

          source_system: Name of the system that the work plan was originally created in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/workplans",
            body=maybe_transform(
                {
                    "calendar_days": calendar_days,
                    "date_from": date_from,
                    "date_to": date_to,
                    "company_employee_ids": company_employee_ids,
                    "company_id": company_id,
                    "employee_ids": employee_ids,
                    "employment_ids": employment_ids,
                    "source_system": source_system,
                    "unit_id": unit_id,
                },
                workplan_create_params.WorkplanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        date_from: Union[str, date],
        date_to: Union[str, date],
        company_employee_id: str | NotGiven = NOT_GIVEN,
        company_id: int | NotGiven = NOT_GIVEN,
        created_at_from: Union[str, date] | NotGiven = NOT_GIVEN,
        created_at_to: Union[str, date] | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        employment_id: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        origin: Literal["registered_by_api", "generated_from_work_plan"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        source_system: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkplanListResponse:
        """
        This endpoint allows retrieving a list of work plan days for employments with
        filtering and pagination. It is mandatory to set "dateFrom" and "dateTo". One of
        three request options must be set: "employmentId" or "companyEmployeeId" or
        "employeeId" with "companyId".

        Args:
          date_from: Lists work plan days that are equal or after this date using ATOM format
              Y-m-d\\TTH:i:sP

          date_to: Lists work plan days that are equal or before this date using ATOM format
              Y-m-d\\TTH:i:sP

          company_employee_id: Filters work plan days by company employee id

          company_id: Filters work plan days by company id

          created_at_from: Lists work plan days that are created on or after this date using ATOM format
              Y-m-d\\TTH:i:sP

          created_at_to: Lists work plan days that are created on or before this date using ATOM format
              Y-m-d\\TTH:i:sP

          employee_id: Filters work plan days by employee id, needs to be used with "companyId"
              parameter

          employment_id: Filters work plan days by employment id

          limit: Max returned results, default value is 100

          origin: Filters work plan days by it`s origin

          page: Results page, default value is 1

          source_system: Filters work plan days by a phrase identifying the system which is the source of
              the work plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/workplans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "company_employee_id": company_employee_id,
                        "company_id": company_id,
                        "created_at_from": created_at_from,
                        "created_at_to": created_at_to,
                        "employee_id": employee_id,
                        "employment_id": employment_id,
                        "limit": limit,
                        "origin": origin,
                        "page": page,
                        "source_system": source_system,
                    },
                    workplan_list_params.WorkplanListParams,
                ),
            ),
            cast_to=WorkplanListResponse,
        )

    def delete(
        self,
        *,
        date_from: str,
        date_to: str,
        company_employee_id: Optional[int] | NotGiven = NOT_GIVEN,
        company_id: Optional[int] | NotGiven = NOT_GIVEN,
        employee_id: Optional[str] | NotGiven = NOT_GIVEN,
        employment_id: Optional[int] | NotGiven = NOT_GIVEN,
        unit_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkplanDeleteResponse:
        """
        This endpoint allows to delete a work plan.

        Body represents JavaScript array with json objects as elements. Each json object
        values need to satisfy json requirements. A value can be a string in double
        quotes or a number. At least one from following two groups is required:
        employeeId, companyEmployeeId or employmentId unitId or companyId Employment
        work plan calendar days are deleted for employments. CompanyId / unitId has to
        indicate a company level organisation unit. If provided, data is deleted for all
        employments assigned to it. Maximum date range possible to delete is one month.
        For employeeId either companyId or unitId is needed.

        If employeeId or companyEmployeeId provided data is deleted for all employments
        assigned to this company employee.

        In order to be able to delete employment work plan calendar days an employment
        has to have an active imported employment work plan. An employment work plan's
        start day has to be before or equal to dateFrom parameter.

        Possible combinations:

        employeeId -> delete work plan calendar days hours per employee (applies to all
        employments)

        companyEmployeeId -> delete work plan calendar days hours per employee (applies
        to all employments)

        employmentId -> delete work plan calendar days hours per employment

        unitId - delete work plan calendar days hours per company using unitid (applies
        to all employments in a given company by unit_id)

        companyId - delete work plan calendar days hours per company (applies to all
        employments in a given company)

        When both unitId and employeeId are provided -> delete work plan calendar days
        hours per employee (all employments)

        When unitId and companyEmployeeId are provided-> delete work plan calendar days
        hours per employee (all employments)

        When companyId and employeeId are provided -> delete work plan calendar days
        hours per employee (all employments)

        When companyId and companyEmployeeId are provided-> delete work plan calendar
        days hours per employee (all employments)

        Args:
          date_from: The start date of the absence. Format like 2023-06-05T00:00:00+00:00

          date_to: The end date of the absence. Format like 2023-06-05T00:00:00+00:00

          company_employee_id: Database identifier for company-employee (id field)

          company_id: Database identifier for company-employee (company field)

          employee_id: Database identifier for company-employee (employee_id field)

          employment_id: Database identifier for employment (id field)

          unit_id: Database identifier for organizational_unit (unit_id field)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/workplans",
            body=maybe_transform(
                {
                    "date_from": date_from,
                    "date_to": date_to,
                    "company_employee_id": company_employee_id,
                    "company_id": company_id,
                    "employee_id": employee_id,
                    "employment_id": employment_id,
                    "unit_id": unit_id,
                },
                workplan_delete_params.WorkplanDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkplanDeleteResponse,
        )


class AsyncWorkplansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkplansResourceWithRawResponse:
        return AsyncWorkplansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkplansResourceWithStreamingResponse:
        return AsyncWorkplansResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        calendar_days: Iterable[workplan_create_params.CalendarDay],
        date_from: str,
        date_to: str,
        company_employee_ids: Iterable[float] | NotGiven = NOT_GIVEN,
        company_id: float | NotGiven = NOT_GIVEN,
        employee_ids: List[str] | NotGiven = NOT_GIVEN,
        employment_ids: Iterable[float] | NotGiven = NOT_GIVEN,
        source_system: Optional[str] | NotGiven = NOT_GIVEN,
        unit_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This endpoint allows to create a new work plan.

        Body represents JavaScript array with json objects as elements. Each json object
        values need to satisfy json requirements. A value can be a string in double
        quotes or a number. At least one of the following parameters is required:
        employeeIds, companyEmployeeIds or employmentIds. For employeeId or
        companyEmployeeId either companyId or unitId is needed. If provided, data is
        created for all employments assigned to it.

        If employeeIds or companyEmployeeIds are provided, data is created for all
        employments assigned to this company employee.

        An employment work plan's dateFrom has to be before or equal to dateTo
        parameter. Maximum work plan's dateTo is limited to 18 months from current day.
        Hours for each date (calendarDays) must be specified within the dateFrom and
        dateTo parameters.

        Possible combinations:

        employeeIds -> create work plan calendar days hours per employee (applies to all
        employments)

        companyEmployeeIds -> create work plan calendar days hours per employee (applies
        to all employments)

        employmentIds -> create work plan calendar days hours per employment

        unitId - create work plan calendar days hours per company using unitId (applies
        to all employments in a given company by unit_id)

        companyId - create work plan calendar days hours per company (applies to all
        employments in a given company)

        When both unitId and employeeIds are provided -> create work plan calendar days
        hours per employee (all employments)

        When unitId and companyEmployeeIds are provided-> create work plan calendar days
        hours per employee (all employments)

        When companyId and employeeIds are provided -> create work plan calendar days
        hours per employee (all employments)

        When companyId and companyEmployeeIds are provided-> create work plan calendar
        days hours per employee (all employments)

        Args:
          date_from: The start date of the work plan. Format like 2023-06-05T00:00:00+00:00

          date_to: The end date of the work plan. Format like 2023-06-05T00:00:00+00:00

          source_system: Name of the system that the work plan was originally created in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/workplans",
            body=await async_maybe_transform(
                {
                    "calendar_days": calendar_days,
                    "date_from": date_from,
                    "date_to": date_to,
                    "company_employee_ids": company_employee_ids,
                    "company_id": company_id,
                    "employee_ids": employee_ids,
                    "employment_ids": employment_ids,
                    "source_system": source_system,
                    "unit_id": unit_id,
                },
                workplan_create_params.WorkplanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        date_from: Union[str, date],
        date_to: Union[str, date],
        company_employee_id: str | NotGiven = NOT_GIVEN,
        company_id: int | NotGiven = NOT_GIVEN,
        created_at_from: Union[str, date] | NotGiven = NOT_GIVEN,
        created_at_to: Union[str, date] | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        employment_id: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        origin: Literal["registered_by_api", "generated_from_work_plan"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        source_system: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkplanListResponse:
        """
        This endpoint allows retrieving a list of work plan days for employments with
        filtering and pagination. It is mandatory to set "dateFrom" and "dateTo". One of
        three request options must be set: "employmentId" or "companyEmployeeId" or
        "employeeId" with "companyId".

        Args:
          date_from: Lists work plan days that are equal or after this date using ATOM format
              Y-m-d\\TTH:i:sP

          date_to: Lists work plan days that are equal or before this date using ATOM format
              Y-m-d\\TTH:i:sP

          company_employee_id: Filters work plan days by company employee id

          company_id: Filters work plan days by company id

          created_at_from: Lists work plan days that are created on or after this date using ATOM format
              Y-m-d\\TTH:i:sP

          created_at_to: Lists work plan days that are created on or before this date using ATOM format
              Y-m-d\\TTH:i:sP

          employee_id: Filters work plan days by employee id, needs to be used with "companyId"
              parameter

          employment_id: Filters work plan days by employment id

          limit: Max returned results, default value is 100

          origin: Filters work plan days by it`s origin

          page: Results page, default value is 1

          source_system: Filters work plan days by a phrase identifying the system which is the source of
              the work plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/workplans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_from": date_from,
                        "date_to": date_to,
                        "company_employee_id": company_employee_id,
                        "company_id": company_id,
                        "created_at_from": created_at_from,
                        "created_at_to": created_at_to,
                        "employee_id": employee_id,
                        "employment_id": employment_id,
                        "limit": limit,
                        "origin": origin,
                        "page": page,
                        "source_system": source_system,
                    },
                    workplan_list_params.WorkplanListParams,
                ),
            ),
            cast_to=WorkplanListResponse,
        )

    async def delete(
        self,
        *,
        date_from: str,
        date_to: str,
        company_employee_id: Optional[int] | NotGiven = NOT_GIVEN,
        company_id: Optional[int] | NotGiven = NOT_GIVEN,
        employee_id: Optional[str] | NotGiven = NOT_GIVEN,
        employment_id: Optional[int] | NotGiven = NOT_GIVEN,
        unit_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkplanDeleteResponse:
        """
        This endpoint allows to delete a work plan.

        Body represents JavaScript array with json objects as elements. Each json object
        values need to satisfy json requirements. A value can be a string in double
        quotes or a number. At least one from following two groups is required:
        employeeId, companyEmployeeId or employmentId unitId or companyId Employment
        work plan calendar days are deleted for employments. CompanyId / unitId has to
        indicate a company level organisation unit. If provided, data is deleted for all
        employments assigned to it. Maximum date range possible to delete is one month.
        For employeeId either companyId or unitId is needed.

        If employeeId or companyEmployeeId provided data is deleted for all employments
        assigned to this company employee.

        In order to be able to delete employment work plan calendar days an employment
        has to have an active imported employment work plan. An employment work plan's
        start day has to be before or equal to dateFrom parameter.

        Possible combinations:

        employeeId -> delete work plan calendar days hours per employee (applies to all
        employments)

        companyEmployeeId -> delete work plan calendar days hours per employee (applies
        to all employments)

        employmentId -> delete work plan calendar days hours per employment

        unitId - delete work plan calendar days hours per company using unitid (applies
        to all employments in a given company by unit_id)

        companyId - delete work plan calendar days hours per company (applies to all
        employments in a given company)

        When both unitId and employeeId are provided -> delete work plan calendar days
        hours per employee (all employments)

        When unitId and companyEmployeeId are provided-> delete work plan calendar days
        hours per employee (all employments)

        When companyId and employeeId are provided -> delete work plan calendar days
        hours per employee (all employments)

        When companyId and companyEmployeeId are provided-> delete work plan calendar
        days hours per employee (all employments)

        Args:
          date_from: The start date of the absence. Format like 2023-06-05T00:00:00+00:00

          date_to: The end date of the absence. Format like 2023-06-05T00:00:00+00:00

          company_employee_id: Database identifier for company-employee (id field)

          company_id: Database identifier for company-employee (company field)

          employee_id: Database identifier for company-employee (employee_id field)

          employment_id: Database identifier for employment (id field)

          unit_id: Database identifier for organizational_unit (unit_id field)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/workplans",
            body=await async_maybe_transform(
                {
                    "date_from": date_from,
                    "date_to": date_to,
                    "company_employee_id": company_employee_id,
                    "company_id": company_id,
                    "employee_id": employee_id,
                    "employment_id": employment_id,
                    "unit_id": unit_id,
                },
                workplan_delete_params.WorkplanDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkplanDeleteResponse,
        )


class WorkplansResourceWithRawResponse:
    def __init__(self, workplans: WorkplansResource) -> None:
        self._workplans = workplans

        self.create = to_raw_response_wrapper(
            workplans.create,
        )
        self.list = to_raw_response_wrapper(
            workplans.list,
        )
        self.delete = to_raw_response_wrapper(
            workplans.delete,
        )


class AsyncWorkplansResourceWithRawResponse:
    def __init__(self, workplans: AsyncWorkplansResource) -> None:
        self._workplans = workplans

        self.create = async_to_raw_response_wrapper(
            workplans.create,
        )
        self.list = async_to_raw_response_wrapper(
            workplans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workplans.delete,
        )


class WorkplansResourceWithStreamingResponse:
    def __init__(self, workplans: WorkplansResource) -> None:
        self._workplans = workplans

        self.create = to_streamed_response_wrapper(
            workplans.create,
        )
        self.list = to_streamed_response_wrapper(
            workplans.list,
        )
        self.delete = to_streamed_response_wrapper(
            workplans.delete,
        )


class AsyncWorkplansResourceWithStreamingResponse:
    def __init__(self, workplans: AsyncWorkplansResource) -> None:
        self._workplans = workplans

        self.create = async_to_streamed_response_wrapper(
            workplans.create,
        )
        self.list = async_to_streamed_response_wrapper(
            workplans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workplans.delete,
        )
