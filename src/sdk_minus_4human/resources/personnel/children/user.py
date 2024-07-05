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
from ....types.personnel.children import user_create_params
from ....types.personnel.children.user_create_response import UserCreateResponse
from ....types.personnel.children.user_retrieve_response import UserRetrieveResponse

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
        birth_date: str,
        chronically_sick: user_create_params.ChronicallySick,
        do_i_have_care: bool,
        firstname: str,
        phone_number: Optional[str],
        single_parent: bool,
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
        Create child for user.

        Args:
          external_id: To post externalId use additional parameter forceExternalId otherwise field will
              be ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/personnel/children/user/{user_id}",
            body=maybe_transform(
                {
                    "birth_date": birth_date,
                    "chronically_sick": chronically_sick,
                    "do_i_have_care": do_i_have_care,
                    "firstname": firstname,
                    "phone_number": phone_number,
                    "single_parent": single_parent,
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

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveResponse:
        """
        Get list of children by user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/personnel/children/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
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
        birth_date: str,
        chronically_sick: user_create_params.ChronicallySick,
        do_i_have_care: bool,
        firstname: str,
        phone_number: Optional[str],
        single_parent: bool,
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
        Create child for user.

        Args:
          external_id: To post externalId use additional parameter forceExternalId otherwise field will
              be ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/personnel/children/user/{user_id}",
            body=await async_maybe_transform(
                {
                    "birth_date": birth_date,
                    "chronically_sick": chronically_sick,
                    "do_i_have_care": do_i_have_care,
                    "firstname": firstname,
                    "phone_number": phone_number,
                    "single_parent": single_parent,
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

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveResponse:
        """
        Get list of children by user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/personnel/children/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_raw_response_wrapper(
            user.create,
        )
        self.retrieve = to_raw_response_wrapper(
            user.retrieve,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_raw_response_wrapper(
            user.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            user.retrieve,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_streamed_response_wrapper(
            user.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            user.retrieve,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_streamed_response_wrapper(
            user.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            user.retrieve,
        )
