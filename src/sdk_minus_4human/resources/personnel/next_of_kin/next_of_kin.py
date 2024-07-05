# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
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
from ....types.personnel import next_of_kin_update_params
from ....types.personnel.next_of_kin_update_response import NextOfKinUpdateResponse

__all__ = ["NextOfKinResource", "AsyncNextOfKinResource"]


class NextOfKinResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> NextOfKinResourceWithRawResponse:
        return NextOfKinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NextOfKinResourceWithStreamingResponse:
        return NextOfKinResourceWithStreamingResponse(self)

    def update(
        self,
        next_of_kin_id: str,
        *,
        address: next_of_kin_update_params.Address | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        firstname: str | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["-", "M", "F"]] | NotGiven = NOT_GIVEN,
        relationship_type: Literal[
            "notDefined",
            "children",
            "parent",
            "partner",
            "family",
            "friend",
            "other",
            "cohabitant",
            "mother",
            "father",
            "married",
        ]
        | NotGiven = NOT_GIVEN,
        surname: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NextOfKinUpdateResponse:
        """
        Edit single field of next of kin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not next_of_kin_id:
            raise ValueError(f"Expected a non-empty value for `next_of_kin_id` but received {next_of_kin_id!r}")
        return self._patch(
            f"/personnel/next-of-kin/{next_of_kin_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "comment": comment,
                    "firstname": firstname,
                    "gender": gender,
                    "relationship_type": relationship_type,
                    "surname": surname,
                },
                next_of_kin_update_params.NextOfKinUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NextOfKinUpdateResponse,
        )


class AsyncNextOfKinResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNextOfKinResourceWithRawResponse:
        return AsyncNextOfKinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNextOfKinResourceWithStreamingResponse:
        return AsyncNextOfKinResourceWithStreamingResponse(self)

    async def update(
        self,
        next_of_kin_id: str,
        *,
        address: next_of_kin_update_params.Address | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        firstname: str | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["-", "M", "F"]] | NotGiven = NOT_GIVEN,
        relationship_type: Literal[
            "notDefined",
            "children",
            "parent",
            "partner",
            "family",
            "friend",
            "other",
            "cohabitant",
            "mother",
            "father",
            "married",
        ]
        | NotGiven = NOT_GIVEN,
        surname: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NextOfKinUpdateResponse:
        """
        Edit single field of next of kin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not next_of_kin_id:
            raise ValueError(f"Expected a non-empty value for `next_of_kin_id` but received {next_of_kin_id!r}")
        return await self._patch(
            f"/personnel/next-of-kin/{next_of_kin_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "comment": comment,
                    "firstname": firstname,
                    "gender": gender,
                    "relationship_type": relationship_type,
                    "surname": surname,
                },
                next_of_kin_update_params.NextOfKinUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NextOfKinUpdateResponse,
        )


class NextOfKinResourceWithRawResponse:
    def __init__(self, next_of_kin: NextOfKinResource) -> None:
        self._next_of_kin = next_of_kin

        self.update = to_raw_response_wrapper(
            next_of_kin.update,
        )

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._next_of_kin.user)


class AsyncNextOfKinResourceWithRawResponse:
    def __init__(self, next_of_kin: AsyncNextOfKinResource) -> None:
        self._next_of_kin = next_of_kin

        self.update = async_to_raw_response_wrapper(
            next_of_kin.update,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._next_of_kin.user)


class NextOfKinResourceWithStreamingResponse:
    def __init__(self, next_of_kin: NextOfKinResource) -> None:
        self._next_of_kin = next_of_kin

        self.update = to_streamed_response_wrapper(
            next_of_kin.update,
        )

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._next_of_kin.user)


class AsyncNextOfKinResourceWithStreamingResponse:
    def __init__(self, next_of_kin: AsyncNextOfKinResource) -> None:
        self._next_of_kin = next_of_kin

        self.update = async_to_streamed_response_wrapper(
            next_of_kin.update,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._next_of_kin.user)
