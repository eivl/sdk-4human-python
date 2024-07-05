# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.users import send_invitation_update_params
from ..._base_client import (
    make_request_options,
)
from ...types.users.send_invitation_update_response import SendInvitationUpdateResponse

__all__ = ["SendInvitationResource", "AsyncSendInvitationResource"]


class SendInvitationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendInvitationResourceWithRawResponse:
        return SendInvitationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendInvitationResourceWithStreamingResponse:
        return SendInvitationResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SendInvitationUpdateResponse:
        """
        Send invitation link to existing user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/users/send-invitation/{user_id}",
            body=maybe_transform(body, send_invitation_update_params.SendInvitationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendInvitationUpdateResponse,
        )


class AsyncSendInvitationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendInvitationResourceWithRawResponse:
        return AsyncSendInvitationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendInvitationResourceWithStreamingResponse:
        return AsyncSendInvitationResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SendInvitationUpdateResponse:
        """
        Send invitation link to existing user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/users/send-invitation/{user_id}",
            body=await async_maybe_transform(body, send_invitation_update_params.SendInvitationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendInvitationUpdateResponse,
        )


class SendInvitationResourceWithRawResponse:
    def __init__(self, send_invitation: SendInvitationResource) -> None:
        self._send_invitation = send_invitation

        self.update = to_raw_response_wrapper(
            send_invitation.update,
        )


class AsyncSendInvitationResourceWithRawResponse:
    def __init__(self, send_invitation: AsyncSendInvitationResource) -> None:
        self._send_invitation = send_invitation

        self.update = async_to_raw_response_wrapper(
            send_invitation.update,
        )


class SendInvitationResourceWithStreamingResponse:
    def __init__(self, send_invitation: SendInvitationResource) -> None:
        self._send_invitation = send_invitation

        self.update = to_streamed_response_wrapper(
            send_invitation.update,
        )


class AsyncSendInvitationResourceWithStreamingResponse:
    def __init__(self, send_invitation: AsyncSendInvitationResource) -> None:
        self._send_invitation = send_invitation

        self.update = async_to_streamed_response_wrapper(
            send_invitation.update,
        )
