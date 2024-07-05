# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import employee_type_list_params, employee_type_create_params, employee_type_update_params
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
from ..types.employee_type_list_response import EmployeeTypeListResponse
from ..types.employee_type_create_response import EmployeeTypeCreateResponse
from ..types.employee_type_update_response import EmployeeTypeUpdateResponse
from ..types.employee_type_retrieve_response import EmployeeTypeRetrieveResponse

__all__ = ["EmployeeTypesResource", "AsyncEmployeeTypesResource"]


class EmployeeTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmployeeTypesResourceWithRawResponse:
        return EmployeeTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeeTypesResourceWithStreamingResponse:
        return EmployeeTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        employee_type: str,
        employment_type_id: str,
        type_id: str,
        reason: bool | NotGiven = NOT_GIVEN,
        substitute: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeTypeCreateResponse:
        """
        This endpoint allows to create new employee type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/employee-types",
            body=maybe_transform(
                {
                    "employee_type": employee_type,
                    "employment_type_id": employment_type_id,
                    "type_id": type_id,
                    "reason": reason,
                    "substitute": substitute,
                },
                employee_type_create_params.EmployeeTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeTypeCreateResponse,
        )

    def retrieve(
        self,
        employee_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeTypeRetrieveResponse:
        """
        Get employee type by given employeeTypeId.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_type_id:
            raise ValueError(f"Expected a non-empty value for `employee_type_id` but received {employee_type_id!r}")
        return self._get(
            f"/personnel/employee-types/{employee_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeTypeRetrieveResponse,
        )

    def update(
        self,
        employee_type_id: str,
        *,
        employee_type: str | NotGiven = NOT_GIVEN,
        employment_type_id: str | NotGiven = NOT_GIVEN,
        reason: bool | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived"] | NotGiven = NOT_GIVEN,
        substitute: bool | NotGiven = NOT_GIVEN,
        type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeTypeUpdateResponse:
        """
        Edit field in employee type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_type_id:
            raise ValueError(f"Expected a non-empty value for `employee_type_id` but received {employee_type_id!r}")
        return self._patch(
            f"/personnel/employee-types/{employee_type_id}",
            body=maybe_transform(
                {
                    "employee_type": employee_type,
                    "employment_type_id": employment_type_id,
                    "reason": reason,
                    "status": status,
                    "substitute": substitute,
                    "type_id": type_id,
                },
                employee_type_update_params.EmployeeTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeTypeUpdateResponse,
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
    ) -> EmployeeTypeListResponse:
        """This endpoint allows to get list of existing employee types.

        In Application
        employee types may be found at: Settings > Code list > Employee types.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/employee-types",
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
                    employee_type_list_params.EmployeeTypeListParams,
                ),
            ),
            cast_to=EmployeeTypeListResponse,
        )


class AsyncEmployeeTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmployeeTypesResourceWithRawResponse:
        return AsyncEmployeeTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeeTypesResourceWithStreamingResponse:
        return AsyncEmployeeTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        employee_type: str,
        employment_type_id: str,
        type_id: str,
        reason: bool | NotGiven = NOT_GIVEN,
        substitute: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeTypeCreateResponse:
        """
        This endpoint allows to create new employee type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/employee-types",
            body=await async_maybe_transform(
                {
                    "employee_type": employee_type,
                    "employment_type_id": employment_type_id,
                    "type_id": type_id,
                    "reason": reason,
                    "substitute": substitute,
                },
                employee_type_create_params.EmployeeTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeTypeCreateResponse,
        )

    async def retrieve(
        self,
        employee_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeTypeRetrieveResponse:
        """
        Get employee type by given employeeTypeId.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_type_id:
            raise ValueError(f"Expected a non-empty value for `employee_type_id` but received {employee_type_id!r}")
        return await self._get(
            f"/personnel/employee-types/{employee_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeTypeRetrieveResponse,
        )

    async def update(
        self,
        employee_type_id: str,
        *,
        employee_type: str | NotGiven = NOT_GIVEN,
        employment_type_id: str | NotGiven = NOT_GIVEN,
        reason: bool | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived"] | NotGiven = NOT_GIVEN,
        substitute: bool | NotGiven = NOT_GIVEN,
        type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeTypeUpdateResponse:
        """
        Edit field in employee type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_type_id:
            raise ValueError(f"Expected a non-empty value for `employee_type_id` but received {employee_type_id!r}")
        return await self._patch(
            f"/personnel/employee-types/{employee_type_id}",
            body=await async_maybe_transform(
                {
                    "employee_type": employee_type,
                    "employment_type_id": employment_type_id,
                    "reason": reason,
                    "status": status,
                    "substitute": substitute,
                    "type_id": type_id,
                },
                employee_type_update_params.EmployeeTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeTypeUpdateResponse,
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
    ) -> EmployeeTypeListResponse:
        """This endpoint allows to get list of existing employee types.

        In Application
        employee types may be found at: Settings > Code list > Employee types.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/employee-types",
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
                    employee_type_list_params.EmployeeTypeListParams,
                ),
            ),
            cast_to=EmployeeTypeListResponse,
        )


class EmployeeTypesResourceWithRawResponse:
    def __init__(self, employee_types: EmployeeTypesResource) -> None:
        self._employee_types = employee_types

        self.create = to_raw_response_wrapper(
            employee_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            employee_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employee_types.update,
        )
        self.list = to_raw_response_wrapper(
            employee_types.list,
        )


class AsyncEmployeeTypesResourceWithRawResponse:
    def __init__(self, employee_types: AsyncEmployeeTypesResource) -> None:
        self._employee_types = employee_types

        self.create = async_to_raw_response_wrapper(
            employee_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            employee_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employee_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            employee_types.list,
        )


class EmployeeTypesResourceWithStreamingResponse:
    def __init__(self, employee_types: EmployeeTypesResource) -> None:
        self._employee_types = employee_types

        self.create = to_streamed_response_wrapper(
            employee_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            employee_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employee_types.update,
        )
        self.list = to_streamed_response_wrapper(
            employee_types.list,
        )


class AsyncEmployeeTypesResourceWithStreamingResponse:
    def __init__(self, employee_types: AsyncEmployeeTypesResource) -> None:
        self._employee_types = employee_types

        self.create = async_to_streamed_response_wrapper(
            employee_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            employee_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employee_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            employee_types.list,
        )
