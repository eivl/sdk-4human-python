# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
    working_hours_arrangement_list_params,
    working_hours_arrangement_create_params,
    working_hours_arrangement_update_params,
    working_hours_arrangement_retrieve_params,
)
from ...types.personnel.working_hours_arrangement_list_response import WorkingHoursArrangementListResponse
from ...types.personnel.working_hours_arrangement_create_response import WorkingHoursArrangementCreateResponse
from ...types.personnel.working_hours_arrangement_update_response import WorkingHoursArrangementUpdateResponse
from ...types.personnel.working_hours_arrangement_retrieve_response import WorkingHoursArrangementRetrieveResponse

__all__ = ["WorkingHoursArrangementsResource", "AsyncWorkingHoursArrangementsResource"]


class WorkingHoursArrangementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkingHoursArrangementsResourceWithRawResponse:
        return WorkingHoursArrangementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkingHoursArrangementsResourceWithStreamingResponse:
        return WorkingHoursArrangementsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str],
        external_id: Optional[str],
        internal_id: str,
        name: str,
        status: Literal["active", "archived"],
        working_hours_per_week: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkingHoursArrangementCreateResponse:
        """
        Create working hours arrangement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/working-hours-arrangements",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "name": name,
                    "status": status,
                    "working_hours_per_week": working_hours_per_week,
                },
                working_hours_arrangement_create_params.WorkingHoursArrangementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkingHoursArrangementCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkingHoursArrangementRetrieveResponse:
        """
        Get working hours arrangement by identifier.

        Args:
          external: Param determines if `id` is external (`externalId`) or internal (`id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/personnel/working-hours-arrangements/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external": external},
                    working_hours_arrangement_retrieve_params.WorkingHoursArrangementRetrieveParams,
                ),
            ),
            cast_to=WorkingHoursArrangementRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived"] | NotGiven = NOT_GIVEN,
        working_hours_per_week: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkingHoursArrangementUpdateResponse:
        """
        Edit part of working hours arrangement.

        Args:
          external: Param determines if `id` is external (`externalId`) or internal (`id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/personnel/working-hours-arrangements/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "name": name,
                    "status": status,
                    "working_hours_per_week": working_hours_per_week,
                },
                working_hours_arrangement_update_params.WorkingHoursArrangementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external": external}, working_hours_arrangement_update_params.WorkingHoursArrangementUpdateParams
                ),
            ),
            cast_to=WorkingHoursArrangementUpdateResponse,
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
    ) -> WorkingHoursArrangementListResponse:
        """
        Get working hours arrangements list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/working-hours-arrangements",
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
                    working_hours_arrangement_list_params.WorkingHoursArrangementListParams,
                ),
            ),
            cast_to=WorkingHoursArrangementListResponse,
        )


class AsyncWorkingHoursArrangementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkingHoursArrangementsResourceWithRawResponse:
        return AsyncWorkingHoursArrangementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkingHoursArrangementsResourceWithStreamingResponse:
        return AsyncWorkingHoursArrangementsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str],
        external_id: Optional[str],
        internal_id: str,
        name: str,
        status: Literal["active", "archived"],
        working_hours_per_week: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkingHoursArrangementCreateResponse:
        """
        Create working hours arrangement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/working-hours-arrangements",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "name": name,
                    "status": status,
                    "working_hours_per_week": working_hours_per_week,
                },
                working_hours_arrangement_create_params.WorkingHoursArrangementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkingHoursArrangementCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkingHoursArrangementRetrieveResponse:
        """
        Get working hours arrangement by identifier.

        Args:
          external: Param determines if `id` is external (`externalId`) or internal (`id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/personnel/working-hours-arrangements/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external},
                    working_hours_arrangement_retrieve_params.WorkingHoursArrangementRetrieveParams,
                ),
            ),
            cast_to=WorkingHoursArrangementRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived"] | NotGiven = NOT_GIVEN,
        working_hours_per_week: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkingHoursArrangementUpdateResponse:
        """
        Edit part of working hours arrangement.

        Args:
          external: Param determines if `id` is external (`externalId`) or internal (`id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/personnel/working-hours-arrangements/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "name": name,
                    "status": status,
                    "working_hours_per_week": working_hours_per_week,
                },
                working_hours_arrangement_update_params.WorkingHoursArrangementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, working_hours_arrangement_update_params.WorkingHoursArrangementUpdateParams
                ),
            ),
            cast_to=WorkingHoursArrangementUpdateResponse,
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
    ) -> WorkingHoursArrangementListResponse:
        """
        Get working hours arrangements list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/working-hours-arrangements",
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
                    working_hours_arrangement_list_params.WorkingHoursArrangementListParams,
                ),
            ),
            cast_to=WorkingHoursArrangementListResponse,
        )


class WorkingHoursArrangementsResourceWithRawResponse:
    def __init__(self, working_hours_arrangements: WorkingHoursArrangementsResource) -> None:
        self._working_hours_arrangements = working_hours_arrangements

        self.create = to_raw_response_wrapper(
            working_hours_arrangements.create,
        )
        self.retrieve = to_raw_response_wrapper(
            working_hours_arrangements.retrieve,
        )
        self.update = to_raw_response_wrapper(
            working_hours_arrangements.update,
        )
        self.list = to_raw_response_wrapper(
            working_hours_arrangements.list,
        )


class AsyncWorkingHoursArrangementsResourceWithRawResponse:
    def __init__(self, working_hours_arrangements: AsyncWorkingHoursArrangementsResource) -> None:
        self._working_hours_arrangements = working_hours_arrangements

        self.create = async_to_raw_response_wrapper(
            working_hours_arrangements.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            working_hours_arrangements.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            working_hours_arrangements.update,
        )
        self.list = async_to_raw_response_wrapper(
            working_hours_arrangements.list,
        )


class WorkingHoursArrangementsResourceWithStreamingResponse:
    def __init__(self, working_hours_arrangements: WorkingHoursArrangementsResource) -> None:
        self._working_hours_arrangements = working_hours_arrangements

        self.create = to_streamed_response_wrapper(
            working_hours_arrangements.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            working_hours_arrangements.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            working_hours_arrangements.update,
        )
        self.list = to_streamed_response_wrapper(
            working_hours_arrangements.list,
        )


class AsyncWorkingHoursArrangementsResourceWithStreamingResponse:
    def __init__(self, working_hours_arrangements: AsyncWorkingHoursArrangementsResource) -> None:
        self._working_hours_arrangements = working_hours_arrangements

        self.create = async_to_streamed_response_wrapper(
            working_hours_arrangements.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            working_hours_arrangements.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            working_hours_arrangements.update,
        )
        self.list = async_to_streamed_response_wrapper(
            working_hours_arrangements.list,
        )
