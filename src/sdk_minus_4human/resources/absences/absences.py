# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ...types import (
    absence_list_params,
    absence_create_params,
    absence_delete_params,
    absence_update_params,
)
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
from .absence_codes import (
    AbsenceCodesResource,
    AsyncAbsenceCodesResource,
    AbsenceCodesResourceWithRawResponse,
    AsyncAbsenceCodesResourceWithRawResponse,
    AbsenceCodesResourceWithStreamingResponse,
    AsyncAbsenceCodesResourceWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from .deleted_absences import (
    DeletedAbsencesResource,
    AsyncDeletedAbsencesResource,
    DeletedAbsencesResourceWithRawResponse,
    AsyncDeletedAbsencesResourceWithRawResponse,
    DeletedAbsencesResourceWithStreamingResponse,
    AsyncDeletedAbsencesResourceWithStreamingResponse,
)
from ...types.absence_list_response import AbsenceListResponse
from ...types.absence_create_response import AbsenceCreateResponse
from ...types.absence_delete_response import AbsenceDeleteResponse
from ...types.absence_update_response import AbsenceUpdateResponse

__all__ = ["AbsencesResource", "AsyncAbsencesResource"]


class AbsencesResource(SyncAPIResource):
    @cached_property
    def deleted_absences(self) -> DeletedAbsencesResource:
        return DeletedAbsencesResource(self._client)

    @cached_property
    def absence_codes(self) -> AbsenceCodesResource:
        return AbsenceCodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AbsencesResourceWithRawResponse:
        return AbsencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AbsencesResourceWithStreamingResponse:
        return AbsencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        absences: Iterable[absence_create_params.Absence] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceCreateResponse:
        """
        Base on the parameters and create bulk functionality to create multiple new
        absences with given attributes, where field absences represents JavaScript array
        with json objects as elements.

        Field absences represents JavaScript array with json objects as elements.

        Each json object values need to satisfy json requirements. A value can be a
        string in double quotes, or a number, or true or false or null.

        One of the following parameters is required: employeeId or companyEmployeeId.

        When only employeeId or companyEmployeeId is provided then also unitId or
        companyId is required and absence is registered for all employments.

        When employmentId is provided then absence is registered only for provided ids.

        ExternalAbsenceId has to be unique for a given instance.

        Absence calculation

        hours & percentage represent absenceCalculation value. Furthermore, these
        indicate absence absenceCalculation type.

        when only "hours" is provided absenceCalculation is hours

        when only ”percentage” is provided absenceCalculation is percentage

        when 100% absenceCalculation is full_day

        when there's no “full_day” option available for a given absence code then 100%
        is stored/displayed

        when hours and percentage are provided absenceCalculation: hours

        Absence status

        It is optional to provide absence status value that absences should be created
        with.

        if the status is not provided the imported absence will be treated as approved.

        Absence request limit

        There is a limit for the number of absences that will be imported per request.
        The limit is set to 50 absences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/absences",
            body=maybe_transform({"absences": absences}, absence_create_params.AbsenceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbsenceCreateResponse,
        )

    def update(
        self,
        *,
        absences: Iterable[absence_update_params.Absence] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceUpdateResponse:
        """
        Bulk endpoint that allows to update multiple absences using one request.

        Request body contains two fields: `absences` and `external`.

        `Absences` which is used to pass the list of objects that declare fields You
        want to update along with values to be set.

        It is not mandatory to include all absence fields in the absence updates, use
        only the ones that You want to change.

        The only mandatory field is `id` which is used to identify the absence You want
        to update.

        `External` field is used to determine whether the `id` field in `absences`
        identifies absence by internal id or by

        external id - which is `externalAbsenceId` field value.

        There is a limit for the number of absences that will be updated per request.
        The limit is set to `50` absences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/absences",
            body=maybe_transform({"absences": absences}, absence_update_params.AbsenceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbsenceUpdateResponse,
        )

    def list(
        self,
        *,
        absence_code_category: Literal["leave_of_absence", "other", "sick_leave", "vacation", "working"]
        | NotGiven = NOT_GIVEN,
        absence_code_external_id: str | NotGiven = NOT_GIVEN,
        absence_code_ids: str | NotGiven = NOT_GIVEN,
        absence_code_internal_id: str | NotGiven = NOT_GIVEN,
        absence_code_type: Literal["self_certified", "documented", "paid", "not_paid", "sick_child", "no_types"]
        | NotGiven = NOT_GIVEN,
        company_employee_id: str | NotGiven = NOT_GIVEN,
        company_id: int | NotGiven = NOT_GIVEN,
        created_at_from: Union[str, date] | NotGiven = NOT_GIVEN,
        created_at_to: Union[str, date] | NotGiven = NOT_GIVEN,
        created_by: str | NotGiven = NOT_GIVEN,
        date_from: Union[str, date] | NotGiven = NOT_GIVEN,
        date_to: Union[str, date] | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        external_absence_id: str | NotGiven = NOT_GIVEN,
        instance_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        origin: Literal["ABSENCE_REGISTERED_BY_API", "ABSENCE_REGISTERED_MANUALLY", "ABSENCE_REGISTERED_FROM_SICK_NOTE"]
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        source_system: str | NotGiven = NOT_GIVEN,
        status: Literal["for_approval", "approved", "rejected"] | NotGiven = NOT_GIVEN,
        updated_at_from: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_at_to: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_by: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceListResponse:
        """
        This endpoint allows retrieving a list of absences, with optional filtering and
        pagination.

        Args:
          absence_code_category: Filters absences by absence code category.

          absence_code_external_id: Filters absences by absence code external ID.

          absence_code_ids: Filters absences by absence codes. Multiple absence codes can be specified by
              comma-separated values.

          absence_code_internal_id: Filters absences by absence code internal ID.

          absence_code_type: Filters absences by absence code type.

          company_employee_id: Filters absences by company employee id. Company employee id refers to employee
              that absence is created for.

          company_id: Filters absences by company ID.

          created_at_from: Lists absences that were created after (or equal to) the specified date.

          created_at_to: Lists absences that were created before (or equal to) the specified date.

          created_by: Filters absences by user id (uuid) that created an absence.

          date_from: Lists absences that have date_from after (or equal to) the specified date.

          date_to: Lists absences that have date_from before (or equal to) the specified date.

          employee_id: Filters absences by employee id. Employee id refers to employee that absence is
              created for.

          external_absence_id: Filters absences by absence external id.

          instance_id: Filters absences by instance ID (UUID).

          limit: Max returned results. Default 100.

          origin: Filters absences by the way the absence was registered in the system.

          page: Results page. Default 1.

          source_system: Filters absences by name of the system that is responsible for the absence
              creation.

          status: Filters absences by absence status.

          updated_at_from: Lists absences that were updated after (or equal to) the specified date.

          updated_at_to: Lists absences that were updated before (or equal to) the specified date.

          updated_by: Filters absences by employee ID (UUID) that updated the absence.

          user_id: Filters absences by user id (uuid). User id refers to employee that absence is
              created for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/absences",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "absence_code_category": absence_code_category,
                        "absence_code_external_id": absence_code_external_id,
                        "absence_code_ids": absence_code_ids,
                        "absence_code_internal_id": absence_code_internal_id,
                        "absence_code_type": absence_code_type,
                        "company_employee_id": company_employee_id,
                        "company_id": company_id,
                        "created_at_from": created_at_from,
                        "created_at_to": created_at_to,
                        "created_by": created_by,
                        "date_from": date_from,
                        "date_to": date_to,
                        "employee_id": employee_id,
                        "external_absence_id": external_absence_id,
                        "instance_id": instance_id,
                        "limit": limit,
                        "origin": origin,
                        "page": page,
                        "source_system": source_system,
                        "status": status,
                        "updated_at_from": updated_at_from,
                        "updated_at_to": updated_at_to,
                        "updated_by": updated_by,
                        "user_id": user_id,
                    },
                    absence_list_params.AbsenceListParams,
                ),
            ),
            cast_to=AbsenceListResponse,
        )

    def delete(
        self,
        *,
        company_employee_id: Optional[int] | NotGiven = NOT_GIVEN,
        company_id: Optional[int] | NotGiven = NOT_GIVEN,
        created_by: Optional[str] | NotGiven = NOT_GIVEN,
        date_from: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        date_to: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        employee_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_absence_code_ids: List[str] | NotGiven = NOT_GIVEN,
        external_absence_id: Iterable[int] | NotGiven = NOT_GIVEN,
        internal_absence_id: Iterable[int] | NotGiven = NOT_GIVEN,
        origin: Optional[
            Literal["ABSENCE_REGISTERED_BY_API", "ABSENCE_REGISTERED_MANUALLY", "ABSENCE_REGISTERED_FROM_SICK_NOTE"]
        ]
        | NotGiven = NOT_GIVEN,
        source_system: Optional[str] | NotGiven = NOT_GIVEN,
        unit_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceDeleteResponse:
        """
        This endpoint allows you to delete a single absence or absences in a specified
        period limited by parameters.

        When externalAbsenceId or internalAbsenceId is provided then dateFrom and dateTo
        are irrelevant.

        When employeeId is provided then also unitId or companyId is required and all
        absence for this employee of a given company will be deleted.

        When dateFrom and dateTo are provided, other parameters are not required When
        dateFrom and dateTo are provided then all absences within this period are
        deleted.

        When source system and unitId or companyId are provided in one request then only
        absences for a given unitId/companyId will be deleted.

        Only one unitId, companyId, employeeId or sourceSystem can be provided in one
        request. The same rules apply to origin field.

        "Rule for overlapping scenario:"

        Given "date from" or "data to" overlaps with at least one day of the absence

        When "Delete" request is performed

        Then absence days are cut according to requested "Date from" or/and "Date to"

        Args:
          company_employee_id: Database identifier for company-employee (id field)

          company_id: The ID of the company.

          created_by: UserId that created absence

          date_from: The start date of the absence. Format like 2023-06-05T00:00:00+00:00

          date_to: The end date of the absence. Format like 2023-06-05T00:00:00+00:00

          employee_id: Identifier for company-employee (employee id field)

          external_absence_code_ids: External ID for absence code

          external_absence_id: Endpoint accepts both string and int. But the value is saved as a string. So if
              1 provided it will be saved as '1'

          internal_absence_id: Endpoint accepts both string and int. But the value is saved as a string. So if
              1 provided it will be saved as '1'

          origin: The way absence was registered in the system (e.g. ABSENCE_REGISTERED_MANUALLY)

          source_system: Name of the system that is responsible for the absence creation

          unit_id: Identifier for company by unit id field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/absences",
            body=maybe_transform(
                {
                    "company_employee_id": company_employee_id,
                    "company_id": company_id,
                    "created_by": created_by,
                    "date_from": date_from,
                    "date_to": date_to,
                    "employee_id": employee_id,
                    "external_absence_code_ids": external_absence_code_ids,
                    "external_absence_id": external_absence_id,
                    "internal_absence_id": internal_absence_id,
                    "origin": origin,
                    "source_system": source_system,
                    "unit_id": unit_id,
                },
                absence_delete_params.AbsenceDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbsenceDeleteResponse,
        )


class AsyncAbsencesResource(AsyncAPIResource):
    @cached_property
    def deleted_absences(self) -> AsyncDeletedAbsencesResource:
        return AsyncDeletedAbsencesResource(self._client)

    @cached_property
    def absence_codes(self) -> AsyncAbsenceCodesResource:
        return AsyncAbsenceCodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAbsencesResourceWithRawResponse:
        return AsyncAbsencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAbsencesResourceWithStreamingResponse:
        return AsyncAbsencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        absences: Iterable[absence_create_params.Absence] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceCreateResponse:
        """
        Base on the parameters and create bulk functionality to create multiple new
        absences with given attributes, where field absences represents JavaScript array
        with json objects as elements.

        Field absences represents JavaScript array with json objects as elements.

        Each json object values need to satisfy json requirements. A value can be a
        string in double quotes, or a number, or true or false or null.

        One of the following parameters is required: employeeId or companyEmployeeId.

        When only employeeId or companyEmployeeId is provided then also unitId or
        companyId is required and absence is registered for all employments.

        When employmentId is provided then absence is registered only for provided ids.

        ExternalAbsenceId has to be unique for a given instance.

        Absence calculation

        hours & percentage represent absenceCalculation value. Furthermore, these
        indicate absence absenceCalculation type.

        when only "hours" is provided absenceCalculation is hours

        when only ”percentage” is provided absenceCalculation is percentage

        when 100% absenceCalculation is full_day

        when there's no “full_day” option available for a given absence code then 100%
        is stored/displayed

        when hours and percentage are provided absenceCalculation: hours

        Absence status

        It is optional to provide absence status value that absences should be created
        with.

        if the status is not provided the imported absence will be treated as approved.

        Absence request limit

        There is a limit for the number of absences that will be imported per request.
        The limit is set to 50 absences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/absences",
            body=await async_maybe_transform({"absences": absences}, absence_create_params.AbsenceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbsenceCreateResponse,
        )

    async def update(
        self,
        *,
        absences: Iterable[absence_update_params.Absence] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceUpdateResponse:
        """
        Bulk endpoint that allows to update multiple absences using one request.

        Request body contains two fields: `absences` and `external`.

        `Absences` which is used to pass the list of objects that declare fields You
        want to update along with values to be set.

        It is not mandatory to include all absence fields in the absence updates, use
        only the ones that You want to change.

        The only mandatory field is `id` which is used to identify the absence You want
        to update.

        `External` field is used to determine whether the `id` field in `absences`
        identifies absence by internal id or by

        external id - which is `externalAbsenceId` field value.

        There is a limit for the number of absences that will be updated per request.
        The limit is set to `50` absences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/absences",
            body=await async_maybe_transform({"absences": absences}, absence_update_params.AbsenceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbsenceUpdateResponse,
        )

    async def list(
        self,
        *,
        absence_code_category: Literal["leave_of_absence", "other", "sick_leave", "vacation", "working"]
        | NotGiven = NOT_GIVEN,
        absence_code_external_id: str | NotGiven = NOT_GIVEN,
        absence_code_ids: str | NotGiven = NOT_GIVEN,
        absence_code_internal_id: str | NotGiven = NOT_GIVEN,
        absence_code_type: Literal["self_certified", "documented", "paid", "not_paid", "sick_child", "no_types"]
        | NotGiven = NOT_GIVEN,
        company_employee_id: str | NotGiven = NOT_GIVEN,
        company_id: int | NotGiven = NOT_GIVEN,
        created_at_from: Union[str, date] | NotGiven = NOT_GIVEN,
        created_at_to: Union[str, date] | NotGiven = NOT_GIVEN,
        created_by: str | NotGiven = NOT_GIVEN,
        date_from: Union[str, date] | NotGiven = NOT_GIVEN,
        date_to: Union[str, date] | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        external_absence_id: str | NotGiven = NOT_GIVEN,
        instance_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        origin: Literal["ABSENCE_REGISTERED_BY_API", "ABSENCE_REGISTERED_MANUALLY", "ABSENCE_REGISTERED_FROM_SICK_NOTE"]
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        source_system: str | NotGiven = NOT_GIVEN,
        status: Literal["for_approval", "approved", "rejected"] | NotGiven = NOT_GIVEN,
        updated_at_from: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_at_to: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_by: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceListResponse:
        """
        This endpoint allows retrieving a list of absences, with optional filtering and
        pagination.

        Args:
          absence_code_category: Filters absences by absence code category.

          absence_code_external_id: Filters absences by absence code external ID.

          absence_code_ids: Filters absences by absence codes. Multiple absence codes can be specified by
              comma-separated values.

          absence_code_internal_id: Filters absences by absence code internal ID.

          absence_code_type: Filters absences by absence code type.

          company_employee_id: Filters absences by company employee id. Company employee id refers to employee
              that absence is created for.

          company_id: Filters absences by company ID.

          created_at_from: Lists absences that were created after (or equal to) the specified date.

          created_at_to: Lists absences that were created before (or equal to) the specified date.

          created_by: Filters absences by user id (uuid) that created an absence.

          date_from: Lists absences that have date_from after (or equal to) the specified date.

          date_to: Lists absences that have date_from before (or equal to) the specified date.

          employee_id: Filters absences by employee id. Employee id refers to employee that absence is
              created for.

          external_absence_id: Filters absences by absence external id.

          instance_id: Filters absences by instance ID (UUID).

          limit: Max returned results. Default 100.

          origin: Filters absences by the way the absence was registered in the system.

          page: Results page. Default 1.

          source_system: Filters absences by name of the system that is responsible for the absence
              creation.

          status: Filters absences by absence status.

          updated_at_from: Lists absences that were updated after (or equal to) the specified date.

          updated_at_to: Lists absences that were updated before (or equal to) the specified date.

          updated_by: Filters absences by employee ID (UUID) that updated the absence.

          user_id: Filters absences by user id (uuid). User id refers to employee that absence is
              created for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/absences",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "absence_code_category": absence_code_category,
                        "absence_code_external_id": absence_code_external_id,
                        "absence_code_ids": absence_code_ids,
                        "absence_code_internal_id": absence_code_internal_id,
                        "absence_code_type": absence_code_type,
                        "company_employee_id": company_employee_id,
                        "company_id": company_id,
                        "created_at_from": created_at_from,
                        "created_at_to": created_at_to,
                        "created_by": created_by,
                        "date_from": date_from,
                        "date_to": date_to,
                        "employee_id": employee_id,
                        "external_absence_id": external_absence_id,
                        "instance_id": instance_id,
                        "limit": limit,
                        "origin": origin,
                        "page": page,
                        "source_system": source_system,
                        "status": status,
                        "updated_at_from": updated_at_from,
                        "updated_at_to": updated_at_to,
                        "updated_by": updated_by,
                        "user_id": user_id,
                    },
                    absence_list_params.AbsenceListParams,
                ),
            ),
            cast_to=AbsenceListResponse,
        )

    async def delete(
        self,
        *,
        company_employee_id: Optional[int] | NotGiven = NOT_GIVEN,
        company_id: Optional[int] | NotGiven = NOT_GIVEN,
        created_by: Optional[str] | NotGiven = NOT_GIVEN,
        date_from: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        date_to: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        employee_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_absence_code_ids: List[str] | NotGiven = NOT_GIVEN,
        external_absence_id: Iterable[int] | NotGiven = NOT_GIVEN,
        internal_absence_id: Iterable[int] | NotGiven = NOT_GIVEN,
        origin: Optional[
            Literal["ABSENCE_REGISTERED_BY_API", "ABSENCE_REGISTERED_MANUALLY", "ABSENCE_REGISTERED_FROM_SICK_NOTE"]
        ]
        | NotGiven = NOT_GIVEN,
        source_system: Optional[str] | NotGiven = NOT_GIVEN,
        unit_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceDeleteResponse:
        """
        This endpoint allows you to delete a single absence or absences in a specified
        period limited by parameters.

        When externalAbsenceId or internalAbsenceId is provided then dateFrom and dateTo
        are irrelevant.

        When employeeId is provided then also unitId or companyId is required and all
        absence for this employee of a given company will be deleted.

        When dateFrom and dateTo are provided, other parameters are not required When
        dateFrom and dateTo are provided then all absences within this period are
        deleted.

        When source system and unitId or companyId are provided in one request then only
        absences for a given unitId/companyId will be deleted.

        Only one unitId, companyId, employeeId or sourceSystem can be provided in one
        request. The same rules apply to origin field.

        "Rule for overlapping scenario:"

        Given "date from" or "data to" overlaps with at least one day of the absence

        When "Delete" request is performed

        Then absence days are cut according to requested "Date from" or/and "Date to"

        Args:
          company_employee_id: Database identifier for company-employee (id field)

          company_id: The ID of the company.

          created_by: UserId that created absence

          date_from: The start date of the absence. Format like 2023-06-05T00:00:00+00:00

          date_to: The end date of the absence. Format like 2023-06-05T00:00:00+00:00

          employee_id: Identifier for company-employee (employee id field)

          external_absence_code_ids: External ID for absence code

          external_absence_id: Endpoint accepts both string and int. But the value is saved as a string. So if
              1 provided it will be saved as '1'

          internal_absence_id: Endpoint accepts both string and int. But the value is saved as a string. So if
              1 provided it will be saved as '1'

          origin: The way absence was registered in the system (e.g. ABSENCE_REGISTERED_MANUALLY)

          source_system: Name of the system that is responsible for the absence creation

          unit_id: Identifier for company by unit id field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/absences",
            body=await async_maybe_transform(
                {
                    "company_employee_id": company_employee_id,
                    "company_id": company_id,
                    "created_by": created_by,
                    "date_from": date_from,
                    "date_to": date_to,
                    "employee_id": employee_id,
                    "external_absence_code_ids": external_absence_code_ids,
                    "external_absence_id": external_absence_id,
                    "internal_absence_id": internal_absence_id,
                    "origin": origin,
                    "source_system": source_system,
                    "unit_id": unit_id,
                },
                absence_delete_params.AbsenceDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AbsenceDeleteResponse,
        )


class AbsencesResourceWithRawResponse:
    def __init__(self, absences: AbsencesResource) -> None:
        self._absences = absences

        self.create = to_raw_response_wrapper(
            absences.create,
        )
        self.update = to_raw_response_wrapper(
            absences.update,
        )
        self.list = to_raw_response_wrapper(
            absences.list,
        )
        self.delete = to_raw_response_wrapper(
            absences.delete,
        )

    @cached_property
    def deleted_absences(self) -> DeletedAbsencesResourceWithRawResponse:
        return DeletedAbsencesResourceWithRawResponse(self._absences.deleted_absences)

    @cached_property
    def absence_codes(self) -> AbsenceCodesResourceWithRawResponse:
        return AbsenceCodesResourceWithRawResponse(self._absences.absence_codes)


class AsyncAbsencesResourceWithRawResponse:
    def __init__(self, absences: AsyncAbsencesResource) -> None:
        self._absences = absences

        self.create = async_to_raw_response_wrapper(
            absences.create,
        )
        self.update = async_to_raw_response_wrapper(
            absences.update,
        )
        self.list = async_to_raw_response_wrapper(
            absences.list,
        )
        self.delete = async_to_raw_response_wrapper(
            absences.delete,
        )

    @cached_property
    def deleted_absences(self) -> AsyncDeletedAbsencesResourceWithRawResponse:
        return AsyncDeletedAbsencesResourceWithRawResponse(self._absences.deleted_absences)

    @cached_property
    def absence_codes(self) -> AsyncAbsenceCodesResourceWithRawResponse:
        return AsyncAbsenceCodesResourceWithRawResponse(self._absences.absence_codes)


class AbsencesResourceWithStreamingResponse:
    def __init__(self, absences: AbsencesResource) -> None:
        self._absences = absences

        self.create = to_streamed_response_wrapper(
            absences.create,
        )
        self.update = to_streamed_response_wrapper(
            absences.update,
        )
        self.list = to_streamed_response_wrapper(
            absences.list,
        )
        self.delete = to_streamed_response_wrapper(
            absences.delete,
        )

    @cached_property
    def deleted_absences(self) -> DeletedAbsencesResourceWithStreamingResponse:
        return DeletedAbsencesResourceWithStreamingResponse(self._absences.deleted_absences)

    @cached_property
    def absence_codes(self) -> AbsenceCodesResourceWithStreamingResponse:
        return AbsenceCodesResourceWithStreamingResponse(self._absences.absence_codes)


class AsyncAbsencesResourceWithStreamingResponse:
    def __init__(self, absences: AsyncAbsencesResource) -> None:
        self._absences = absences

        self.create = async_to_streamed_response_wrapper(
            absences.create,
        )
        self.update = async_to_streamed_response_wrapper(
            absences.update,
        )
        self.list = async_to_streamed_response_wrapper(
            absences.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            absences.delete,
        )

    @cached_property
    def deleted_absences(self) -> AsyncDeletedAbsencesResourceWithStreamingResponse:
        return AsyncDeletedAbsencesResourceWithStreamingResponse(self._absences.deleted_absences)

    @cached_property
    def absence_codes(self) -> AsyncAbsenceCodesResourceWithStreamingResponse:
        return AsyncAbsenceCodesResourceWithStreamingResponse(self._absences.absence_codes)
