# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.absences import absence_code_list_params
from ...types.absences.absence_code_list_response import AbsenceCodeListResponse

__all__ = ["AbsenceCodesResource", "AsyncAbsenceCodesResource"]


class AbsenceCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AbsenceCodesResourceWithRawResponse:
        return AbsenceCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AbsenceCodesResourceWithStreamingResponse:
        return AbsenceCodesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        category: Literal["leave_of_absence", "other", "sick_leave", "vacation", "working"] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive", "archived"] | NotGiven = NOT_GIVEN,
        type: Literal["self_certified", "documented", "paid", "not_paid", "sick_child", "no_types"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceCodeListResponse:
        """
        This endpoint allows retrieving a list of absence codes, with optional filtering
        and pagination.

        Args:
          category: Filters absences by absence code category.

          external_id: Filters absences by absence code external ID.

          internal_id: Filters absences by absence code internal ID.

          limit: Max returned results. Default 100.

          page: Results page. Default 1.

          status: Filters absences by absence status.

          type: Filters absences by absence code type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/absences/absence-codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "external_id": external_id,
                        "internal_id": internal_id,
                        "limit": limit,
                        "page": page,
                        "status": status,
                        "type": type,
                    },
                    absence_code_list_params.AbsenceCodeListParams,
                ),
            ),
            cast_to=AbsenceCodeListResponse,
        )


class AsyncAbsenceCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAbsenceCodesResourceWithRawResponse:
        return AsyncAbsenceCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAbsenceCodesResourceWithStreamingResponse:
        return AsyncAbsenceCodesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        category: Literal["leave_of_absence", "other", "sick_leave", "vacation", "working"] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive", "archived"] | NotGiven = NOT_GIVEN,
        type: Literal["self_certified", "documented", "paid", "not_paid", "sick_child", "no_types"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AbsenceCodeListResponse:
        """
        This endpoint allows retrieving a list of absence codes, with optional filtering
        and pagination.

        Args:
          category: Filters absences by absence code category.

          external_id: Filters absences by absence code external ID.

          internal_id: Filters absences by absence code internal ID.

          limit: Max returned results. Default 100.

          page: Results page. Default 1.

          status: Filters absences by absence status.

          type: Filters absences by absence code type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/absences/absence-codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "external_id": external_id,
                        "internal_id": internal_id,
                        "limit": limit,
                        "page": page,
                        "status": status,
                        "type": type,
                    },
                    absence_code_list_params.AbsenceCodeListParams,
                ),
            ),
            cast_to=AbsenceCodeListResponse,
        )


class AbsenceCodesResourceWithRawResponse:
    def __init__(self, absence_codes: AbsenceCodesResource) -> None:
        self._absence_codes = absence_codes

        self.list = to_raw_response_wrapper(
            absence_codes.list,
        )


class AsyncAbsenceCodesResourceWithRawResponse:
    def __init__(self, absence_codes: AsyncAbsenceCodesResource) -> None:
        self._absence_codes = absence_codes

        self.list = async_to_raw_response_wrapper(
            absence_codes.list,
        )


class AbsenceCodesResourceWithStreamingResponse:
    def __init__(self, absence_codes: AbsenceCodesResource) -> None:
        self._absence_codes = absence_codes

        self.list = to_streamed_response_wrapper(
            absence_codes.list,
        )


class AsyncAbsenceCodesResourceWithStreamingResponse:
    def __init__(self, absence_codes: AsyncAbsenceCodesResource) -> None:
        self._absence_codes = absence_codes

        self.list = async_to_streamed_response_wrapper(
            absence_codes.list,
        )
