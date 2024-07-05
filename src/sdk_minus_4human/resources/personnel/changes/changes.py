# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from typing_extensions import Literal

import httpx

from .details import (
    DetailsResource,
    AsyncDetailsResource,
    DetailsResourceWithRawResponse,
    AsyncDetailsResourceWithRawResponse,
    DetailsResourceWithStreamingResponse,
    AsyncDetailsResourceWithStreamingResponse,
)
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
from ....types.personnel import change_list_params
from ....types.personnel.change_list_response import ChangeListResponse

__all__ = ["ChangesResource", "AsyncChangesResource"]


class ChangesResource(SyncAPIResource):
    @cached_property
    def details(self) -> DetailsResource:
        return DetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        from_: Union[int, str],
        to: Union[int, str],
        company_id: int | NotGiven = NOT_GIVEN,
        external: bool | NotGiven = NOT_GIVEN,
        format: Literal["timestamp", "date", "dateTime"] | NotGiven = NOT_GIVEN,
        organisation_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChangeListResponse:
        """
        This endpoint allows to get the ID list (internal or external) of changed
        employments, company-employees and users in specified date range.

        Args:
          from_: Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
              ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`

          to: Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
              selected `format`

          company_id: database id of company

          external: Param determines if returned ID is external or internal: Fields used as external
              ID:

              - `number` field in employment object
              - `employeeId` field in company-employee object
              - there is no external ID for user object, so always internal ID is returned

          format: Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
              8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters

          organisation_number: ID of the company fetched from [brreg.no](https://www.brreg.no) for norway or
              custom one for other countries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ChangeListResponse,
            self._get(
                "/personnel/changes",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "from_": from_,
                            "to": to,
                            "company_id": company_id,
                            "external": external,
                            "format": format,
                            "organisation_number": organisation_number,
                        },
                        change_list_params.ChangeListParams,
                    ),
                ),
                cast_to=cast(
                    Any, ChangeListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncChangesResource(AsyncAPIResource):
    @cached_property
    def details(self) -> AsyncDetailsResource:
        return AsyncDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        from_: Union[int, str],
        to: Union[int, str],
        company_id: int | NotGiven = NOT_GIVEN,
        external: bool | NotGiven = NOT_GIVEN,
        format: Literal["timestamp", "date", "dateTime"] | NotGiven = NOT_GIVEN,
        organisation_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChangeListResponse:
        """
        This endpoint allows to get the ID list (internal or external) of changed
        employments, company-employees and users in specified date range.

        Args:
          from_: Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
              ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`

          to: Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
              selected `format`

          company_id: database id of company

          external: Param determines if returned ID is external or internal: Fields used as external
              ID:

              - `number` field in employment object
              - `employeeId` field in company-employee object
              - there is no external ID for user object, so always internal ID is returned

          format: Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
              8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters

          organisation_number: ID of the company fetched from [brreg.no](https://www.brreg.no) for norway or
              custom one for other countries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ChangeListResponse,
            await self._get(
                "/personnel/changes",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "from_": from_,
                            "to": to,
                            "company_id": company_id,
                            "external": external,
                            "format": format,
                            "organisation_number": organisation_number,
                        },
                        change_list_params.ChangeListParams,
                    ),
                ),
                cast_to=cast(
                    Any, ChangeListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ChangesResourceWithRawResponse:
    def __init__(self, changes: ChangesResource) -> None:
        self._changes = changes

        self.list = to_raw_response_wrapper(
            changes.list,
        )

    @cached_property
    def details(self) -> DetailsResourceWithRawResponse:
        return DetailsResourceWithRawResponse(self._changes.details)


class AsyncChangesResourceWithRawResponse:
    def __init__(self, changes: AsyncChangesResource) -> None:
        self._changes = changes

        self.list = async_to_raw_response_wrapper(
            changes.list,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithRawResponse:
        return AsyncDetailsResourceWithRawResponse(self._changes.details)


class ChangesResourceWithStreamingResponse:
    def __init__(self, changes: ChangesResource) -> None:
        self._changes = changes

        self.list = to_streamed_response_wrapper(
            changes.list,
        )

    @cached_property
    def details(self) -> DetailsResourceWithStreamingResponse:
        return DetailsResourceWithStreamingResponse(self._changes.details)


class AsyncChangesResourceWithStreamingResponse:
    def __init__(self, changes: AsyncChangesResource) -> None:
        self._changes = changes

        self.list = async_to_streamed_response_wrapper(
            changes.list,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithStreamingResponse:
        return AsyncDetailsResourceWithStreamingResponse(self._changes.details)
