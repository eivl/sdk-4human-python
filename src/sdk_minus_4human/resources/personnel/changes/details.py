# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ....types.personnel.changes import (
    detail_retrieve_user_changes_params,
    detail_retrieve_employment_changes_params,
    detail_list_company_employee_changes_params,
)
from ....types.personnel.changes.detail_retrieve_user_changes_response import DetailRetrieveUserChangesResponse
from ....types.personnel.changes.detail_retrieve_employment_changes_response import (
    DetailRetrieveEmploymentChangesResponse,
)
from ....types.personnel.changes.detail_list_company_employee_changes_response import (
    DetailListCompanyEmployeeChangesResponse,
)

__all__ = ["DetailsResource", "AsyncDetailsResource"]


class DetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsResourceWithRawResponse:
        return DetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsResourceWithStreamingResponse:
        return DetailsResourceWithStreamingResponse(self)

    def list_company_employee_changes(
        self,
        *,
        from_: Union[int, str],
        to: Union[int, str],
        company_id: str | NotGiven = NOT_GIVEN,
        database_id: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        employment_id: str | NotGiven = NOT_GIVEN,
        format: Literal["timestamp", "date", "dateTime"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        organization_number: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        response_as_objects: bool | NotGiven = NOT_GIVEN,
        salary_system_company_id: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["createdAt", "-createdAt", "validFrom", "-validFrom"] | NotGiven = NOT_GIVEN,
        unit_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        with_custom_fields_tree: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailListCompanyEmployeeChangesResponse:
        """
        This endpoint allows to get the history changes details.

        Args:
          from_: Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
              ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`. Filter `from` and `to`
              searches data (in the selected period) using updated/created dates of snapshots.

          to: Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
              selected `format`

          company_id: Company ID parameter

          database_id: Employee ID parameter

          employee_id: Employee ID parameter

          employment_id: External Employment ID

          format: Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
              8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters

          organization_number: Organization Number parameter

          response_as_objects: Determine the format of the response for relatedChanges key.

          salary_system_company_id: Salary System Company ID parameter

          sort_by: Direction of sort

          unit_id: Unit ID parameter

          user_id: User ID parameter

          with_custom_fields_tree: Determine if structure of custom fields should be returned (resource demanding
              operation).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/changes/details/companyEmployee",
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
                        "database_id": database_id,
                        "employee_id": employee_id,
                        "employment_id": employment_id,
                        "format": format,
                        "limit": limit,
                        "organization_number": organization_number,
                        "page": page,
                        "response_as_objects": response_as_objects,
                        "salary_system_company_id": salary_system_company_id,
                        "sort_by": sort_by,
                        "unit_id": unit_id,
                        "user_id": user_id,
                        "with_custom_fields_tree": with_custom_fields_tree,
                    },
                    detail_list_company_employee_changes_params.DetailListCompanyEmployeeChangesParams,
                ),
            ),
            cast_to=DetailListCompanyEmployeeChangesResponse,
        )

    def retrieve_employment_changes(
        self,
        employment_id: str,
        *,
        from_: Union[int, str],
        to: Union[int, str],
        format: Literal["timestamp", "date", "dateTime"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        response_as_objects: bool | NotGiven = NOT_GIVEN,
        sort_by: Literal["createdAt", "-createdAt", "validFrom", "-validFrom"] | NotGiven = NOT_GIVEN,
        with_custom_fields_tree: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRetrieveEmploymentChangesResponse:
        """
        This endpoint allows to get the single employment history changes details.
        Please note that the employment object represents a single contract of a given
        employee.

        Args:
          from_: Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
              ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`. Filter `from` and `to`
              searches data (in the selected period) using updated/created dates of snapshots.

          to: Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
              selected `format`

          format: Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
              8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters

          response_as_objects: Determine the format of the response for relatedChanges key.

          sort_by: Direction of sort

          with_custom_fields_tree: Determine if structure of custom fields should be returned (resource demanding
              operation).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employment_id:
            raise ValueError(f"Expected a non-empty value for `employment_id` but received {employment_id!r}")
        return self._get(
            f"/personnel/changes/details/employment/{employment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "format": format,
                        "limit": limit,
                        "page": page,
                        "response_as_objects": response_as_objects,
                        "sort_by": sort_by,
                        "with_custom_fields_tree": with_custom_fields_tree,
                    },
                    detail_retrieve_employment_changes_params.DetailRetrieveEmploymentChangesParams,
                ),
            ),
            cast_to=DetailRetrieveEmploymentChangesResponse,
        )

    def retrieve_user_changes(
        self,
        user_id: str,
        *,
        from_: Union[int, str],
        to: Union[int, str],
        format: Literal["timestamp", "date", "dateTime"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        response_as_objects: bool | NotGiven = NOT_GIVEN,
        sort_by: Literal["createdAt", "-createdAt", "validFrom", "-validFrom"] | NotGiven = NOT_GIVEN,
        with_custom_fields_tree: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRetrieveUserChangesResponse:
        """
        This endpoint allows to get the history changes details for user.

        Args:
          from_: Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
              ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`. Filter `from` and `to`
              searches data (in the selected period) using updated/created dates of snapshots.

          to: Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
              selected `format`

          format: Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
              8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters

          limit: Number of records returned in one request

          page: Number of returned page

          response_as_objects: Determine the format of the response for relatedChanges key.

          sort_by: Direction of sort

          with_custom_fields_tree: Determine if structure of custom fields should be returned (resource demanding
              operation).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/personnel/changes/details/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "format": format,
                        "limit": limit,
                        "page": page,
                        "response_as_objects": response_as_objects,
                        "sort_by": sort_by,
                        "with_custom_fields_tree": with_custom_fields_tree,
                    },
                    detail_retrieve_user_changes_params.DetailRetrieveUserChangesParams,
                ),
            ),
            cast_to=DetailRetrieveUserChangesResponse,
        )


class AsyncDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsResourceWithRawResponse:
        return AsyncDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsResourceWithStreamingResponse:
        return AsyncDetailsResourceWithStreamingResponse(self)

    async def list_company_employee_changes(
        self,
        *,
        from_: Union[int, str],
        to: Union[int, str],
        company_id: str | NotGiven = NOT_GIVEN,
        database_id: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        employment_id: str | NotGiven = NOT_GIVEN,
        format: Literal["timestamp", "date", "dateTime"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        organization_number: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        response_as_objects: bool | NotGiven = NOT_GIVEN,
        salary_system_company_id: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["createdAt", "-createdAt", "validFrom", "-validFrom"] | NotGiven = NOT_GIVEN,
        unit_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        with_custom_fields_tree: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailListCompanyEmployeeChangesResponse:
        """
        This endpoint allows to get the history changes details.

        Args:
          from_: Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
              ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`. Filter `from` and `to`
              searches data (in the selected period) using updated/created dates of snapshots.

          to: Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
              selected `format`

          company_id: Company ID parameter

          database_id: Employee ID parameter

          employee_id: Employee ID parameter

          employment_id: External Employment ID

          format: Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
              8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters

          organization_number: Organization Number parameter

          response_as_objects: Determine the format of the response for relatedChanges key.

          salary_system_company_id: Salary System Company ID parameter

          sort_by: Direction of sort

          unit_id: Unit ID parameter

          user_id: User ID parameter

          with_custom_fields_tree: Determine if structure of custom fields should be returned (resource demanding
              operation).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/changes/details/companyEmployee",
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
                        "database_id": database_id,
                        "employee_id": employee_id,
                        "employment_id": employment_id,
                        "format": format,
                        "limit": limit,
                        "organization_number": organization_number,
                        "page": page,
                        "response_as_objects": response_as_objects,
                        "salary_system_company_id": salary_system_company_id,
                        "sort_by": sort_by,
                        "unit_id": unit_id,
                        "user_id": user_id,
                        "with_custom_fields_tree": with_custom_fields_tree,
                    },
                    detail_list_company_employee_changes_params.DetailListCompanyEmployeeChangesParams,
                ),
            ),
            cast_to=DetailListCompanyEmployeeChangesResponse,
        )

    async def retrieve_employment_changes(
        self,
        employment_id: str,
        *,
        from_: Union[int, str],
        to: Union[int, str],
        format: Literal["timestamp", "date", "dateTime"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        response_as_objects: bool | NotGiven = NOT_GIVEN,
        sort_by: Literal["createdAt", "-createdAt", "validFrom", "-validFrom"] | NotGiven = NOT_GIVEN,
        with_custom_fields_tree: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRetrieveEmploymentChangesResponse:
        """
        This endpoint allows to get the single employment history changes details.
        Please note that the employment object represents a single contract of a given
        employee.

        Args:
          from_: Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
              ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`. Filter `from` and `to`
              searches data (in the selected period) using updated/created dates of snapshots.

          to: Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
              selected `format`

          format: Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
              8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters

          response_as_objects: Determine the format of the response for relatedChanges key.

          sort_by: Direction of sort

          with_custom_fields_tree: Determine if structure of custom fields should be returned (resource demanding
              operation).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employment_id:
            raise ValueError(f"Expected a non-empty value for `employment_id` but received {employment_id!r}")
        return await self._get(
            f"/personnel/changes/details/employment/{employment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "format": format,
                        "limit": limit,
                        "page": page,
                        "response_as_objects": response_as_objects,
                        "sort_by": sort_by,
                        "with_custom_fields_tree": with_custom_fields_tree,
                    },
                    detail_retrieve_employment_changes_params.DetailRetrieveEmploymentChangesParams,
                ),
            ),
            cast_to=DetailRetrieveEmploymentChangesResponse,
        )

    async def retrieve_user_changes(
        self,
        user_id: str,
        *,
        from_: Union[int, str],
        to: Union[int, str],
        format: Literal["timestamp", "date", "dateTime"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        response_as_objects: bool | NotGiven = NOT_GIVEN,
        sort_by: Literal["createdAt", "-createdAt", "validFrom", "-validFrom"] | NotGiven = NOT_GIVEN,
        with_custom_fields_tree: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRetrieveUserChangesResponse:
        """
        This endpoint allows to get the history changes details for user.

        Args:
          from_: Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
              ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`. Filter `from` and `to`
              searches data (in the selected period) using updated/created dates of snapshots.

          to: Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
              selected `format`

          format: Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
              8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters

          limit: Number of records returned in one request

          page: Number of returned page

          response_as_objects: Determine the format of the response for relatedChanges key.

          sort_by: Direction of sort

          with_custom_fields_tree: Determine if structure of custom fields should be returned (resource demanding
              operation).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/personnel/changes/details/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "format": format,
                        "limit": limit,
                        "page": page,
                        "response_as_objects": response_as_objects,
                        "sort_by": sort_by,
                        "with_custom_fields_tree": with_custom_fields_tree,
                    },
                    detail_retrieve_user_changes_params.DetailRetrieveUserChangesParams,
                ),
            ),
            cast_to=DetailRetrieveUserChangesResponse,
        )


class DetailsResourceWithRawResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.list_company_employee_changes = to_raw_response_wrapper(
            details.list_company_employee_changes,
        )
        self.retrieve_employment_changes = to_raw_response_wrapper(
            details.retrieve_employment_changes,
        )
        self.retrieve_user_changes = to_raw_response_wrapper(
            details.retrieve_user_changes,
        )


class AsyncDetailsResourceWithRawResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.list_company_employee_changes = async_to_raw_response_wrapper(
            details.list_company_employee_changes,
        )
        self.retrieve_employment_changes = async_to_raw_response_wrapper(
            details.retrieve_employment_changes,
        )
        self.retrieve_user_changes = async_to_raw_response_wrapper(
            details.retrieve_user_changes,
        )


class DetailsResourceWithStreamingResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.list_company_employee_changes = to_streamed_response_wrapper(
            details.list_company_employee_changes,
        )
        self.retrieve_employment_changes = to_streamed_response_wrapper(
            details.retrieve_employment_changes,
        )
        self.retrieve_user_changes = to_streamed_response_wrapper(
            details.retrieve_user_changes,
        )


class AsyncDetailsResourceWithStreamingResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.list_company_employee_changes = async_to_streamed_response_wrapper(
            details.list_company_employee_changes,
        )
        self.retrieve_employment_changes = async_to_streamed_response_wrapper(
            details.retrieve_employment_changes,
        )
        self.retrieve_user_changes = async_to_streamed_response_wrapper(
            details.retrieve_user_changes,
        )
