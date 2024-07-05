# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
from ...types.absences import deleted_absence_list_params
from ...types.absences.deleted_absence_list_response import DeletedAbsenceListResponse

__all__ = ["DeletedAbsencesResource", "AsyncDeletedAbsencesResource"]


class DeletedAbsencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeletedAbsencesResourceWithRawResponse:
        return DeletedAbsencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeletedAbsencesResourceWithStreamingResponse:
        return DeletedAbsencesResourceWithStreamingResponse(self)

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
    ) -> DeletedAbsenceListResponse:
        """
        This endpoint allows retrieving a list of deleted absences, with optional
        filtering and pagination.

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

          employee_id: Filters absences by employee ID (UUID). Employee ID refers to the employee that
              the absence is created for.

          external_absence_id: Filters absences by absence external id.

          instance_id: Filters absences by instance ID (UUID).

          limit: Max returned results. Default 100.

          origin: Filters absences by the way the absence was registered in the system.

          page: Results page. Default 1.

          status: Filters absences by absence status. Allowed values are for_approval, approved,
              rejected.

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
            "/absences/deleted-absences",
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
                        "status": status,
                        "updated_at_from": updated_at_from,
                        "updated_at_to": updated_at_to,
                        "updated_by": updated_by,
                        "user_id": user_id,
                    },
                    deleted_absence_list_params.DeletedAbsenceListParams,
                ),
            ),
            cast_to=DeletedAbsenceListResponse,
        )


class AsyncDeletedAbsencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeletedAbsencesResourceWithRawResponse:
        return AsyncDeletedAbsencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeletedAbsencesResourceWithStreamingResponse:
        return AsyncDeletedAbsencesResourceWithStreamingResponse(self)

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
    ) -> DeletedAbsenceListResponse:
        """
        This endpoint allows retrieving a list of deleted absences, with optional
        filtering and pagination.

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

          employee_id: Filters absences by employee ID (UUID). Employee ID refers to the employee that
              the absence is created for.

          external_absence_id: Filters absences by absence external id.

          instance_id: Filters absences by instance ID (UUID).

          limit: Max returned results. Default 100.

          origin: Filters absences by the way the absence was registered in the system.

          page: Results page. Default 1.

          status: Filters absences by absence status. Allowed values are for_approval, approved,
              rejected.

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
            "/absences/deleted-absences",
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
                        "status": status,
                        "updated_at_from": updated_at_from,
                        "updated_at_to": updated_at_to,
                        "updated_by": updated_by,
                        "user_id": user_id,
                    },
                    deleted_absence_list_params.DeletedAbsenceListParams,
                ),
            ),
            cast_to=DeletedAbsenceListResponse,
        )


class DeletedAbsencesResourceWithRawResponse:
    def __init__(self, deleted_absences: DeletedAbsencesResource) -> None:
        self._deleted_absences = deleted_absences

        self.list = to_raw_response_wrapper(
            deleted_absences.list,
        )


class AsyncDeletedAbsencesResourceWithRawResponse:
    def __init__(self, deleted_absences: AsyncDeletedAbsencesResource) -> None:
        self._deleted_absences = deleted_absences

        self.list = async_to_raw_response_wrapper(
            deleted_absences.list,
        )


class DeletedAbsencesResourceWithStreamingResponse:
    def __init__(self, deleted_absences: DeletedAbsencesResource) -> None:
        self._deleted_absences = deleted_absences

        self.list = to_streamed_response_wrapper(
            deleted_absences.list,
        )


class AsyncDeletedAbsencesResourceWithStreamingResponse:
    def __init__(self, deleted_absences: AsyncDeletedAbsencesResource) -> None:
        self._deleted_absences = deleted_absences

        self.list = async_to_streamed_response_wrapper(
            deleted_absences.list,
        )
