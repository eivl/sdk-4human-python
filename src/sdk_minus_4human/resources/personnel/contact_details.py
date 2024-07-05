# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.personnel import contact_detail_update_params
from ...types.personnel.contact_detail_update_response import ContactDetailUpdateResponse

__all__ = ["ContactDetailsResource", "AsyncContactDetailsResource"]


class ContactDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactDetailsResourceWithRawResponse:
        return ContactDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactDetailsResourceWithStreamingResponse:
        return ContactDetailsResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        address: Optional[str] | NotGiven = NOT_GIVEN,
        building_entrance: Optional[str] | NotGiven = NOT_GIVEN,
        city: Optional[str] | NotGiven = NOT_GIVEN,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        municipality: Optional[str] | NotGiven = NOT_GIVEN,
        private_email: Optional[str] | NotGiven = NOT_GIVEN,
        private_mobile_phone: Optional[str] | NotGiven = NOT_GIVEN,
        private_phone: Optional[str] | NotGiven = NOT_GIVEN,
        work_email: Optional[str] | NotGiven = NOT_GIVEN,
        work_mobile_phone: Optional[str] | NotGiven = NOT_GIVEN,
        work_phone: Optional[str] | NotGiven = NOT_GIVEN,
        zip_code: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactDetailUpdateResponse:
        """Only visible fields configured by field templates can be updated.

        Trying to
        update the not visible field will response with an error.

        Args:
          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          address: Private primary address

          building_entrance: Private primary address

          city: Private primary address

          country: Private primary address

          municipality: Private primary address

          zip_code: Private primary address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/personnel/contact-details/{user_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "building_entrance": building_entrance,
                    "city": city,
                    "country": country,
                    "municipality": municipality,
                    "private_email": private_email,
                    "private_mobile_phone": private_mobile_phone,
                    "private_phone": private_phone,
                    "work_email": work_email,
                    "work_mobile_phone": work_mobile_phone,
                    "work_phone": work_phone,
                    "zip_code": zip_code,
                },
                contact_detail_update_params.ContactDetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    contact_detail_update_params.ContactDetailUpdateParams,
                ),
            ),
            cast_to=ContactDetailUpdateResponse,
        )


class AsyncContactDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactDetailsResourceWithRawResponse:
        return AsyncContactDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactDetailsResourceWithStreamingResponse:
        return AsyncContactDetailsResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        address: Optional[str] | NotGiven = NOT_GIVEN,
        building_entrance: Optional[str] | NotGiven = NOT_GIVEN,
        city: Optional[str] | NotGiven = NOT_GIVEN,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        municipality: Optional[str] | NotGiven = NOT_GIVEN,
        private_email: Optional[str] | NotGiven = NOT_GIVEN,
        private_mobile_phone: Optional[str] | NotGiven = NOT_GIVEN,
        private_phone: Optional[str] | NotGiven = NOT_GIVEN,
        work_email: Optional[str] | NotGiven = NOT_GIVEN,
        work_mobile_phone: Optional[str] | NotGiven = NOT_GIVEN,
        work_phone: Optional[str] | NotGiven = NOT_GIVEN,
        zip_code: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactDetailUpdateResponse:
        """Only visible fields configured by field templates can be updated.

        Trying to
        update the not visible field will response with an error.

        Args:
          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          address: Private primary address

          building_entrance: Private primary address

          city: Private primary address

          country: Private primary address

          municipality: Private primary address

          zip_code: Private primary address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/personnel/contact-details/{user_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "building_entrance": building_entrance,
                    "city": city,
                    "country": country,
                    "municipality": municipality,
                    "private_email": private_email,
                    "private_mobile_phone": private_mobile_phone,
                    "private_phone": private_phone,
                    "work_email": work_email,
                    "work_mobile_phone": work_mobile_phone,
                    "work_phone": work_phone,
                    "zip_code": zip_code,
                },
                contact_detail_update_params.ContactDetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    contact_detail_update_params.ContactDetailUpdateParams,
                ),
            ),
            cast_to=ContactDetailUpdateResponse,
        )


class ContactDetailsResourceWithRawResponse:
    def __init__(self, contact_details: ContactDetailsResource) -> None:
        self._contact_details = contact_details

        self.update = to_raw_response_wrapper(
            contact_details.update,
        )


class AsyncContactDetailsResourceWithRawResponse:
    def __init__(self, contact_details: AsyncContactDetailsResource) -> None:
        self._contact_details = contact_details

        self.update = async_to_raw_response_wrapper(
            contact_details.update,
        )


class ContactDetailsResourceWithStreamingResponse:
    def __init__(self, contact_details: ContactDetailsResource) -> None:
        self._contact_details = contact_details

        self.update = to_streamed_response_wrapper(
            contact_details.update,
        )


class AsyncContactDetailsResourceWithStreamingResponse:
    def __init__(self, contact_details: AsyncContactDetailsResource) -> None:
        self._contact_details = contact_details

        self.update = async_to_streamed_response_wrapper(
            contact_details.update,
        )
