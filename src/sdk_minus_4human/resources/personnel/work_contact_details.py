# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ...types.personnel import work_contact_detail_update_params
from ...types.personnel.work_contact_detail_update_response import WorkContactDetailUpdateResponse

__all__ = ["WorkContactDetailsResource", "AsyncWorkContactDetailsResource"]


class WorkContactDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkContactDetailsResourceWithRawResponse:
        return WorkContactDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkContactDetailsResourceWithStreamingResponse:
        return WorkContactDetailsResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        address_info: Iterable[work_contact_detail_update_params.AddressInfo] | NotGiven = NOT_GIVEN,
        contact_info: Optional[work_contact_detail_update_params.ContactInfo] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkContactDetailUpdateResponse:
        """
        Edit Employee Work Contact Details

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
            f"/personnel/work-contact-details/{user_id}",
            body=maybe_transform(
                {
                    "address_info": address_info,
                    "contact_info": contact_info,
                },
                work_contact_detail_update_params.WorkContactDetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    work_contact_detail_update_params.WorkContactDetailUpdateParams,
                ),
            ),
            cast_to=WorkContactDetailUpdateResponse,
        )


class AsyncWorkContactDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkContactDetailsResourceWithRawResponse:
        return AsyncWorkContactDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkContactDetailsResourceWithStreamingResponse:
        return AsyncWorkContactDetailsResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        address_info: Iterable[work_contact_detail_update_params.AddressInfo] | NotGiven = NOT_GIVEN,
        contact_info: Optional[work_contact_detail_update_params.ContactInfo] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkContactDetailUpdateResponse:
        """
        Edit Employee Work Contact Details

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
            f"/personnel/work-contact-details/{user_id}",
            body=await async_maybe_transform(
                {
                    "address_info": address_info,
                    "contact_info": contact_info,
                },
                work_contact_detail_update_params.WorkContactDetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    work_contact_detail_update_params.WorkContactDetailUpdateParams,
                ),
            ),
            cast_to=WorkContactDetailUpdateResponse,
        )


class WorkContactDetailsResourceWithRawResponse:
    def __init__(self, work_contact_details: WorkContactDetailsResource) -> None:
        self._work_contact_details = work_contact_details

        self.update = to_raw_response_wrapper(
            work_contact_details.update,
        )


class AsyncWorkContactDetailsResourceWithRawResponse:
    def __init__(self, work_contact_details: AsyncWorkContactDetailsResource) -> None:
        self._work_contact_details = work_contact_details

        self.update = async_to_raw_response_wrapper(
            work_contact_details.update,
        )


class WorkContactDetailsResourceWithStreamingResponse:
    def __init__(self, work_contact_details: WorkContactDetailsResource) -> None:
        self._work_contact_details = work_contact_details

        self.update = to_streamed_response_wrapper(
            work_contact_details.update,
        )


class AsyncWorkContactDetailsResourceWithStreamingResponse:
    def __init__(self, work_contact_details: AsyncWorkContactDetailsResource) -> None:
        self._work_contact_details = work_contact_details

        self.update = async_to_streamed_response_wrapper(
            work_contact_details.update,
        )
