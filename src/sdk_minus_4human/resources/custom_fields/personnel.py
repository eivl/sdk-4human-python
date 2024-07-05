# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.custom_fields import personnel_update_params, personnel_update_by_name_params
from ...types.custom_fields.personnel_update_response import PersonnelUpdateResponse
from ...types.custom_fields.personnel_update_by_name_response import PersonnelUpdateByNameResponse

__all__ = ["PersonnelResource", "AsyncPersonnelResource"]


class PersonnelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersonnelResourceWithRawResponse:
        return PersonnelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonnelResourceWithStreamingResponse:
        return PersonnelResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[personnel_update_params.CustomField] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonnelUpdateResponse:
        """This endpoint allows to edit custom fields for personnel.

        Custom fields assigned
        to personnel has no inheritance. Personal custom fields not supports effective
        dates.

        Args:
          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/personnel/custom-fields/{user_id}",
            body=maybe_transform({"custom_fields": custom_fields}, personnel_update_params.PersonnelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personnel_update_params.PersonnelUpdateParams,
                ),
            ),
            cast_to=PersonnelUpdateResponse,
        )

    def update_by_name(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[personnel_update_by_name_params.CustomField] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonnelUpdateByNameResponse:
        """This endpoint allows to edit custom fields for personnel.

        Custom fields assigned
        to personnel has no inheritance. Personal custom fields not supports effective
        dates. In this endpoint you can assign custom fields by using their name,
        external name and internal or external ids.

        Args:
          user_id: User UUID

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/personnel/custom-fields-by-name/{user_id}",
            body=maybe_transform(
                {"custom_fields": custom_fields}, personnel_update_by_name_params.PersonnelUpdateByNameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personnel_update_by_name_params.PersonnelUpdateByNameParams,
                ),
            ),
            cast_to=PersonnelUpdateByNameResponse,
        )


class AsyncPersonnelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersonnelResourceWithRawResponse:
        return AsyncPersonnelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonnelResourceWithStreamingResponse:
        return AsyncPersonnelResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[personnel_update_params.CustomField] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonnelUpdateResponse:
        """This endpoint allows to edit custom fields for personnel.

        Custom fields assigned
        to personnel has no inheritance. Personal custom fields not supports effective
        dates.

        Args:
          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/personnel/custom-fields/{user_id}",
            body=await async_maybe_transform(
                {"custom_fields": custom_fields}, personnel_update_params.PersonnelUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personnel_update_params.PersonnelUpdateParams,
                ),
            ),
            cast_to=PersonnelUpdateResponse,
        )

    async def update_by_name(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[personnel_update_by_name_params.CustomField] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonnelUpdateByNameResponse:
        """This endpoint allows to edit custom fields for personnel.

        Custom fields assigned
        to personnel has no inheritance. Personal custom fields not supports effective
        dates. In this endpoint you can assign custom fields by using their name,
        external name and internal or external ids.

        Args:
          user_id: User UUID

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/personnel/custom-fields-by-name/{user_id}",
            body=await async_maybe_transform(
                {"custom_fields": custom_fields}, personnel_update_by_name_params.PersonnelUpdateByNameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personnel_update_by_name_params.PersonnelUpdateByNameParams,
                ),
            ),
            cast_to=PersonnelUpdateByNameResponse,
        )


class PersonnelResourceWithRawResponse:
    def __init__(self, personnel: PersonnelResource) -> None:
        self._personnel = personnel

        self.update = to_raw_response_wrapper(
            personnel.update,
        )
        self.update_by_name = to_raw_response_wrapper(
            personnel.update_by_name,
        )


class AsyncPersonnelResourceWithRawResponse:
    def __init__(self, personnel: AsyncPersonnelResource) -> None:
        self._personnel = personnel

        self.update = async_to_raw_response_wrapper(
            personnel.update,
        )
        self.update_by_name = async_to_raw_response_wrapper(
            personnel.update_by_name,
        )


class PersonnelResourceWithStreamingResponse:
    def __init__(self, personnel: PersonnelResource) -> None:
        self._personnel = personnel

        self.update = to_streamed_response_wrapper(
            personnel.update,
        )
        self.update_by_name = to_streamed_response_wrapper(
            personnel.update_by_name,
        )


class AsyncPersonnelResourceWithStreamingResponse:
    def __init__(self, personnel: AsyncPersonnelResource) -> None:
        self._personnel = personnel

        self.update = async_to_streamed_response_wrapper(
            personnel.update,
        )
        self.update_by_name = async_to_streamed_response_wrapper(
            personnel.update_by_name,
        )
