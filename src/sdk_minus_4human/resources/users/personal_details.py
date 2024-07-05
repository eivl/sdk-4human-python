# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
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
from ...types.users import personal_detail_update_params
from ..._base_client import (
    make_request_options,
)
from ...types.users.personal_detail_update_response import PersonalDetailUpdateResponse

__all__ = ["PersonalDetailsResource", "AsyncPersonalDetailsResource"]


class PersonalDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersonalDetailsResourceWithRawResponse:
        return PersonalDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonalDetailsResourceWithStreamingResponse:
        return PersonalDetailsResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        alias: Optional[str] | NotGiven = NOT_GIVEN,
        country_of_origin: Optional[str] | NotGiven = NOT_GIVEN,
        date_of_birth: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["-", "M", "F"]] | NotGiven = NOT_GIVEN,
        initials: Optional[str] | NotGiven = NOT_GIVEN,
        marital_status: Optional[
            Literal[
                "unmarried",
                "married",
                "widowed",
                "divorced",
                "separated",
                "registeredPartner",
                "separatedPartner",
                "divorcedPartner",
                "survivingPartner",
                "cohabitant",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        nationality: Optional[str] | NotGiven = NOT_GIVEN,
        surname: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalDetailUpdateResponse:
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
            f"/users/personal-details/{user_id}",
            body=maybe_transform(
                {
                    "alias": alias,
                    "country_of_origin": country_of_origin,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "gender": gender,
                    "initials": initials,
                    "marital_status": marital_status,
                    "nationality": nationality,
                    "surname": surname,
                },
                personal_detail_update_params.PersonalDetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_detail_update_params.PersonalDetailUpdateParams,
                ),
            ),
            cast_to=PersonalDetailUpdateResponse,
        )


class AsyncPersonalDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersonalDetailsResourceWithRawResponse:
        return AsyncPersonalDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonalDetailsResourceWithStreamingResponse:
        return AsyncPersonalDetailsResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        alias: Optional[str] | NotGiven = NOT_GIVEN,
        country_of_origin: Optional[str] | NotGiven = NOT_GIVEN,
        date_of_birth: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["-", "M", "F"]] | NotGiven = NOT_GIVEN,
        initials: Optional[str] | NotGiven = NOT_GIVEN,
        marital_status: Optional[
            Literal[
                "unmarried",
                "married",
                "widowed",
                "divorced",
                "separated",
                "registeredPartner",
                "separatedPartner",
                "divorcedPartner",
                "survivingPartner",
                "cohabitant",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        nationality: Optional[str] | NotGiven = NOT_GIVEN,
        surname: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalDetailUpdateResponse:
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
            f"/users/personal-details/{user_id}",
            body=await async_maybe_transform(
                {
                    "alias": alias,
                    "country_of_origin": country_of_origin,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "gender": gender,
                    "initials": initials,
                    "marital_status": marital_status,
                    "nationality": nationality,
                    "surname": surname,
                },
                personal_detail_update_params.PersonalDetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_detail_update_params.PersonalDetailUpdateParams,
                ),
            ),
            cast_to=PersonalDetailUpdateResponse,
        )


class PersonalDetailsResourceWithRawResponse:
    def __init__(self, personal_details: PersonalDetailsResource) -> None:
        self._personal_details = personal_details

        self.update = to_raw_response_wrapper(
            personal_details.update,
        )


class AsyncPersonalDetailsResourceWithRawResponse:
    def __init__(self, personal_details: AsyncPersonalDetailsResource) -> None:
        self._personal_details = personal_details

        self.update = async_to_raw_response_wrapper(
            personal_details.update,
        )


class PersonalDetailsResourceWithStreamingResponse:
    def __init__(self, personal_details: PersonalDetailsResource) -> None:
        self._personal_details = personal_details

        self.update = to_streamed_response_wrapper(
            personal_details.update,
        )


class AsyncPersonalDetailsResourceWithStreamingResponse:
    def __init__(self, personal_details: AsyncPersonalDetailsResource) -> None:
        self._personal_details = personal_details

        self.update = async_to_streamed_response_wrapper(
            personal_details.update,
        )
