# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ....types.personnel.next_of_kin import user_create_params
from ....types.personnel.next_of_kin.user_list_response import UserListResponse
from ....types.personnel.next_of_kin.user_create_response import UserCreateResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self)

    def create(
        self,
        user_id: str,
        *,
        address: user_create_params.Address,
        comment: Optional[str],
        firstname: str,
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
        ],
        surname: str,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        force_external_id: Optional[bool] | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["-", "M", "F"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserCreateResponse:
        """
        Create next of kin for user.

        Args:
          external_id: To post external id use additional parameter forceExternalId otherwise field
              will be ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/personnel/next-of-kin/user/{user_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "comment": comment,
                    "firstname": firstname,
                    "relationship_type": relationship_type,
                    "surname": surname,
                    "external_id": external_id,
                    "force_external_id": force_external_id,
                    "gender": gender,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateResponse,
        )

    def list(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        Get list of next of kin by user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/personnel/next-of-kin/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self)

    async def create(
        self,
        user_id: str,
        *,
        address: user_create_params.Address,
        comment: Optional[str],
        firstname: str,
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
        ],
        surname: str,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        force_external_id: Optional[bool] | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["-", "M", "F"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserCreateResponse:
        """
        Create next of kin for user.

        Args:
          external_id: To post external id use additional parameter forceExternalId otherwise field
              will be ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/personnel/next-of-kin/user/{user_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "comment": comment,
                    "firstname": firstname,
                    "relationship_type": relationship_type,
                    "surname": surname,
                    "external_id": external_id,
                    "force_external_id": force_external_id,
                    "gender": gender,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateResponse,
        )

    async def list(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        Get list of next of kin by user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/personnel/next-of-kin/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_raw_response_wrapper(
            user.create,
        )
        self.list = to_raw_response_wrapper(
            user.list,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_raw_response_wrapper(
            user.create,
        )
        self.list = async_to_raw_response_wrapper(
            user.list,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_streamed_response_wrapper(
            user.create,
        )
        self.list = to_streamed_response_wrapper(
            user.list,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_streamed_response_wrapper(
            user.create,
        )
        self.list = async_to_streamed_response_wrapper(
            user.list,
        )
