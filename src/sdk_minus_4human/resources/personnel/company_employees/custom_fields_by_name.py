# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ....types.personnel.company_employees import custom_fields_by_name_update_params
from ....types.personnel.company_employees.custom_fields_by_name_update_response import CustomFieldsByNameUpdateResponse

__all__ = ["CustomFieldsByNameResource", "AsyncCustomFieldsByNameResource"]


class CustomFieldsByNameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomFieldsByNameResourceWithRawResponse:
        return CustomFieldsByNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomFieldsByNameResourceWithStreamingResponse:
        return CustomFieldsByNameResourceWithStreamingResponse(self)

    def update(
        self,
        company_employee_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[custom_fields_by_name_update_params.CustomField] | NotGiven = NOT_GIVEN,
        effective_dates: custom_fields_by_name_update_params.EffectiveDates | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomFieldsByNameUpdateResponse:
        """
        Only custom fields for company employee will be edited - endpoint NOT deletes
        not mentioned custom fields.

        Args:
          external: Param determines if id of employment is external (employeeId) or internal (id)

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
        return self._put(
            f"/personnel/company-employees/{company_employee_id}/custom-fields-by-name",
            body=maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "effective_dates": effective_dates,
                },
                custom_fields_by_name_update_params.CustomFieldsByNameUpdateParams,
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
                    custom_fields_by_name_update_params.CustomFieldsByNameUpdateParams,
                ),
            ),
            cast_to=CustomFieldsByNameUpdateResponse,
        )


class AsyncCustomFieldsByNameResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomFieldsByNameResourceWithRawResponse:
        return AsyncCustomFieldsByNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomFieldsByNameResourceWithStreamingResponse:
        return AsyncCustomFieldsByNameResourceWithStreamingResponse(self)

    async def update(
        self,
        company_employee_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[custom_fields_by_name_update_params.CustomField] | NotGiven = NOT_GIVEN,
        effective_dates: custom_fields_by_name_update_params.EffectiveDates | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomFieldsByNameUpdateResponse:
        """
        Only custom fields for company employee will be edited - endpoint NOT deletes
        not mentioned custom fields.

        Args:
          external: Param determines if id of employment is external (employeeId) or internal (id)

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
        return await self._put(
            f"/personnel/company-employees/{company_employee_id}/custom-fields-by-name",
            body=await async_maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "effective_dates": effective_dates,
                },
                custom_fields_by_name_update_params.CustomFieldsByNameUpdateParams,
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
                    custom_fields_by_name_update_params.CustomFieldsByNameUpdateParams,
                ),
            ),
            cast_to=CustomFieldsByNameUpdateResponse,
        )


class CustomFieldsByNameResourceWithRawResponse:
    def __init__(self, custom_fields_by_name: CustomFieldsByNameResource) -> None:
        self._custom_fields_by_name = custom_fields_by_name

        self.update = to_raw_response_wrapper(
            custom_fields_by_name.update,
        )


class AsyncCustomFieldsByNameResourceWithRawResponse:
    def __init__(self, custom_fields_by_name: AsyncCustomFieldsByNameResource) -> None:
        self._custom_fields_by_name = custom_fields_by_name

        self.update = async_to_raw_response_wrapper(
            custom_fields_by_name.update,
        )


class CustomFieldsByNameResourceWithStreamingResponse:
    def __init__(self, custom_fields_by_name: CustomFieldsByNameResource) -> None:
        self._custom_fields_by_name = custom_fields_by_name

        self.update = to_streamed_response_wrapper(
            custom_fields_by_name.update,
        )


class AsyncCustomFieldsByNameResourceWithStreamingResponse:
    def __init__(self, custom_fields_by_name: AsyncCustomFieldsByNameResource) -> None:
        self._custom_fields_by_name = custom_fields_by_name

        self.update = async_to_streamed_response_wrapper(
            custom_fields_by_name.update,
        )
