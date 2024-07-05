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
from ....types.personnel import child_update_params
from ....types.personnel.child_update_response import ChildUpdateResponse

__all__ = ["ChildrenResource", "AsyncChildrenResource"]


class ChildrenResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChildrenResourceWithRawResponse:
        return ChildrenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChildrenResourceWithStreamingResponse:
        return ChildrenResourceWithStreamingResponse(self)

    def update(
        self,
        child_id: str,
        *,
        birth_date: str | NotGiven = NOT_GIVEN,
        chronically_sick: child_update_params.ChronicallySick | NotGiven = NOT_GIVEN,
        do_i_have_care: bool | NotGiven = NOT_GIVEN,
        firstname: str | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["-", "M", "F"]] | NotGiven = NOT_GIVEN,
        phone_number: Optional[str] | NotGiven = NOT_GIVEN,
        single_parent: bool | NotGiven = NOT_GIVEN,
        surname: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildUpdateResponse:
        """
        Edit single field of child.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not child_id:
            raise ValueError(f"Expected a non-empty value for `child_id` but received {child_id!r}")
        return self._patch(
            f"/personnel/children/{child_id}",
            body=maybe_transform(
                {
                    "birth_date": birth_date,
                    "chronically_sick": chronically_sick,
                    "do_i_have_care": do_i_have_care,
                    "firstname": firstname,
                    "gender": gender,
                    "phone_number": phone_number,
                    "single_parent": single_parent,
                    "surname": surname,
                },
                child_update_params.ChildUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildUpdateResponse,
        )


class AsyncChildrenResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChildrenResourceWithRawResponse:
        return AsyncChildrenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChildrenResourceWithStreamingResponse:
        return AsyncChildrenResourceWithStreamingResponse(self)

    async def update(
        self,
        child_id: str,
        *,
        birth_date: str | NotGiven = NOT_GIVEN,
        chronically_sick: child_update_params.ChronicallySick | NotGiven = NOT_GIVEN,
        do_i_have_care: bool | NotGiven = NOT_GIVEN,
        firstname: str | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["-", "M", "F"]] | NotGiven = NOT_GIVEN,
        phone_number: Optional[str] | NotGiven = NOT_GIVEN,
        single_parent: bool | NotGiven = NOT_GIVEN,
        surname: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChildUpdateResponse:
        """
        Edit single field of child.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not child_id:
            raise ValueError(f"Expected a non-empty value for `child_id` but received {child_id!r}")
        return await self._patch(
            f"/personnel/children/{child_id}",
            body=await async_maybe_transform(
                {
                    "birth_date": birth_date,
                    "chronically_sick": chronically_sick,
                    "do_i_have_care": do_i_have_care,
                    "firstname": firstname,
                    "gender": gender,
                    "phone_number": phone_number,
                    "single_parent": single_parent,
                    "surname": surname,
                },
                child_update_params.ChildUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChildUpdateResponse,
        )


class ChildrenResourceWithRawResponse:
    def __init__(self, children: ChildrenResource) -> None:
        self._children = children

        self.update = to_raw_response_wrapper(
            children.update,
        )

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._children.user)


class AsyncChildrenResourceWithRawResponse:
    def __init__(self, children: AsyncChildrenResource) -> None:
        self._children = children

        self.update = async_to_raw_response_wrapper(
            children.update,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._children.user)


class ChildrenResourceWithStreamingResponse:
    def __init__(self, children: ChildrenResource) -> None:
        self._children = children

        self.update = to_streamed_response_wrapper(
            children.update,
        )

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._children.user)


class AsyncChildrenResourceWithStreamingResponse:
    def __init__(self, children: AsyncChildrenResource) -> None:
        self._children = children

        self.update = async_to_streamed_response_wrapper(
            children.update,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._children.user)
