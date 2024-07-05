# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.personnel.company_employees import history_retrieve_params
from ....types.personnel.company_employees.history_retrieve_response import HistoryRetrieveResponse

__all__ = ["HistoryResource", "AsyncHistoryResource"]


class HistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        company_employee_id: str,
        *,
        changes_from: int | NotGiven = NOT_GIVEN,
        changes_to: int | NotGiven = NOT_GIVEN,
        effective_statuses: str | NotGiven = NOT_GIVEN,
        external: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        organization_number: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["createdAt", "effectiveStatus", "effectiveStatusDate", "updatedAt", "validFrom"]
        | NotGiven = NOT_GIVEN,
        sort_dir: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        valid_from: int | NotGiven = NOT_GIVEN,
        valid_to: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoryRetrieveResponse:
        """
        Get company employee history.

        Args:
          changes_from: Determines if snapshot was created or updated from selected unix timestamp.

          changes_to: Determines if snapshot was created or updated to selected unix timestamp.

          effective_statuses: Filter by effective status of snapshot - comma separated list. Available values
              are: ["past", "current", "future", "replaced", "canceled", "effected",
              "approved", "for_approval", "for_confirmation", "rejected"] Its possible to
              filter by multiple statuses (each should be comma separated)

          external: Param determines if id of company employee is external (employeeId) or internal
              (id)

          organization_number: organizational number of primary employment from company employee.

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
            f"/personnel/company-employees/{company_employee_id}/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "changes_from": changes_from,
                        "changes_to": changes_to,
                        "effective_statuses": effective_statuses,
                        "external": external,
                        "limit": limit,
                        "organization_number": organization_number,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_dir": sort_dir,
                        "valid_from": valid_from,
                        "valid_to": valid_to,
                    },
                    history_retrieve_params.HistoryRetrieveParams,
                ),
            ),
            cast_to=HistoryRetrieveResponse,
        )


class AsyncHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        company_employee_id: str,
        *,
        changes_from: int | NotGiven = NOT_GIVEN,
        changes_to: int | NotGiven = NOT_GIVEN,
        effective_statuses: str | NotGiven = NOT_GIVEN,
        external: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        organization_number: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["createdAt", "effectiveStatus", "effectiveStatusDate", "updatedAt", "validFrom"]
        | NotGiven = NOT_GIVEN,
        sort_dir: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        valid_from: int | NotGiven = NOT_GIVEN,
        valid_to: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoryRetrieveResponse:
        """
        Get company employee history.

        Args:
          changes_from: Determines if snapshot was created or updated from selected unix timestamp.

          changes_to: Determines if snapshot was created or updated to selected unix timestamp.

          effective_statuses: Filter by effective status of snapshot - comma separated list. Available values
              are: ["past", "current", "future", "replaced", "canceled", "effected",
              "approved", "for_approval", "for_confirmation", "rejected"] Its possible to
              filter by multiple statuses (each should be comma separated)

          external: Param determines if id of company employee is external (employeeId) or internal
              (id)

          organization_number: organizational number of primary employment from company employee.

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
            f"/personnel/company-employees/{company_employee_id}/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "changes_from": changes_from,
                        "changes_to": changes_to,
                        "effective_statuses": effective_statuses,
                        "external": external,
                        "limit": limit,
                        "organization_number": organization_number,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_dir": sort_dir,
                        "valid_from": valid_from,
                        "valid_to": valid_to,
                    },
                    history_retrieve_params.HistoryRetrieveParams,
                ),
            ),
            cast_to=HistoryRetrieveResponse,
        )


class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.retrieve = to_raw_response_wrapper(
            history.retrieve,
        )


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.retrieve = async_to_raw_response_wrapper(
            history.retrieve,
        )


class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.retrieve = to_streamed_response_wrapper(
            history.retrieve,
        )


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.retrieve = async_to_streamed_response_wrapper(
            history.retrieve,
        )