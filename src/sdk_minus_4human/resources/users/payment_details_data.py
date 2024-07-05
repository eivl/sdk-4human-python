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
from ...types.users import payment_details_data_update_params
from ..._base_client import (
    make_request_options,
)
from ...types.users.payment_details_data_update_response import PaymentDetailsDataUpdateResponse

__all__ = ["PaymentDetailsDataResource", "AsyncPaymentDetailsDataResource"]


class PaymentDetailsDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentDetailsDataResourceWithRawResponse:
        return PaymentDetailsDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentDetailsDataResourceWithStreamingResponse:
        return PaymentDetailsDataResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        account_number: str,
        country_of_bank: str,
        iban: Optional[str],
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentDetailsDataUpdateResponse:
        """Only visible fields configured by field templates can be updated.

        Trying to
        update the not visible field will response with an error.

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
        return self._patch(
            f"/users/payment-details-data/{user_id}",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "country_of_bank": country_of_bank,
                    "iban": iban,
                },
                payment_details_data_update_params.PaymentDetailsDataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    payment_details_data_update_params.PaymentDetailsDataUpdateParams,
                ),
            ),
            cast_to=PaymentDetailsDataUpdateResponse,
        )


class AsyncPaymentDetailsDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentDetailsDataResourceWithRawResponse:
        return AsyncPaymentDetailsDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentDetailsDataResourceWithStreamingResponse:
        return AsyncPaymentDetailsDataResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        account_number: str,
        country_of_bank: str,
        iban: Optional[str],
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentDetailsDataUpdateResponse:
        """Only visible fields configured by field templates can be updated.

        Trying to
        update the not visible field will response with an error.

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
        return await self._patch(
            f"/users/payment-details-data/{user_id}",
            body=await async_maybe_transform(
                {
                    "account_number": account_number,
                    "country_of_bank": country_of_bank,
                    "iban": iban,
                },
                payment_details_data_update_params.PaymentDetailsDataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    payment_details_data_update_params.PaymentDetailsDataUpdateParams,
                ),
            ),
            cast_to=PaymentDetailsDataUpdateResponse,
        )


class PaymentDetailsDataResourceWithRawResponse:
    def __init__(self, payment_details_data: PaymentDetailsDataResource) -> None:
        self._payment_details_data = payment_details_data

        self.update = to_raw_response_wrapper(
            payment_details_data.update,
        )


class AsyncPaymentDetailsDataResourceWithRawResponse:
    def __init__(self, payment_details_data: AsyncPaymentDetailsDataResource) -> None:
        self._payment_details_data = payment_details_data

        self.update = async_to_raw_response_wrapper(
            payment_details_data.update,
        )


class PaymentDetailsDataResourceWithStreamingResponse:
    def __init__(self, payment_details_data: PaymentDetailsDataResource) -> None:
        self._payment_details_data = payment_details_data

        self.update = to_streamed_response_wrapper(
            payment_details_data.update,
        )


class AsyncPaymentDetailsDataResourceWithStreamingResponse:
    def __init__(self, payment_details_data: AsyncPaymentDetailsDataResource) -> None:
        self._payment_details_data = payment_details_data

        self.update = async_to_streamed_response_wrapper(
            payment_details_data.update,
        )
