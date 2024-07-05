# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...types import user_list_params, user_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .by_login import (
    ByLoginResource,
    AsyncByLoginResource,
    ByLoginResourceWithRawResponse,
    AsyncByLoginResourceWithRawResponse,
    ByLoginResourceWithStreamingResponse,
    AsyncByLoginResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .logged_user import (
    LoggedUserResource,
    AsyncLoggedUserResource,
    LoggedUserResourceWithRawResponse,
    AsyncLoggedUserResourceWithRawResponse,
    LoggedUserResourceWithStreamingResponse,
    AsyncLoggedUserResourceWithStreamingResponse,
)
from .personal_id import (
    PersonalIDResource,
    AsyncPersonalIDResource,
    PersonalIDResourceWithRawResponse,
    AsyncPersonalIDResourceWithRawResponse,
    PersonalIDResourceWithStreamingResponse,
    AsyncPersonalIDResourceWithStreamingResponse,
)
from .login_method import (
    LoginMethodResource,
    AsyncLoginMethodResource,
    LoginMethodResourceWithRawResponse,
    AsyncLoginMethodResourceWithRawResponse,
    LoginMethodResourceWithStreamingResponse,
    AsyncLoginMethodResourceWithStreamingResponse,
)
from .access_groups import (
    AccessGroupsResource,
    AsyncAccessGroupsResource,
    AccessGroupsResourceWithRawResponse,
    AsyncAccessGroupsResourceWithRawResponse,
    AccessGroupsResourceWithStreamingResponse,
    AsyncAccessGroupsResourceWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from .send_invitation import (
    SendInvitationResource,
    AsyncSendInvitationResource,
    SendInvitationResourceWithRawResponse,
    AsyncSendInvitationResourceWithRawResponse,
    SendInvitationResourceWithStreamingResponse,
    AsyncSendInvitationResourceWithStreamingResponse,
)
from .personal_details import (
    PersonalDetailsResource,
    AsyncPersonalDetailsResource,
    PersonalDetailsResourceWithRawResponse,
    AsyncPersonalDetailsResourceWithRawResponse,
    PersonalDetailsResourceWithStreamingResponse,
    AsyncPersonalDetailsResourceWithStreamingResponse,
)
from .payment_details_data import (
    PaymentDetailsDataResource,
    AsyncPaymentDetailsDataResource,
    PaymentDetailsDataResourceWithRawResponse,
    AsyncPaymentDetailsDataResourceWithRawResponse,
    PaymentDetailsDataResourceWithStreamingResponse,
    AsyncPaymentDetailsDataResourceWithStreamingResponse,
)
from .active_directory_data import (
    ActiveDirectoryDataResource,
    AsyncActiveDirectoryDataResource,
    ActiveDirectoryDataResourceWithRawResponse,
    AsyncActiveDirectoryDataResourceWithRawResponse,
    ActiveDirectoryDataResourceWithStreamingResponse,
    AsyncActiveDirectoryDataResourceWithStreamingResponse,
)
from .logged_user.logged_user import LoggedUserResource, AsyncLoggedUserResource
from ...types.user_list_response import UserListResponse
from .access_groups.access_groups import AccessGroupsResource, AsyncAccessGroupsResource
from ...types.user_create_response import UserCreateResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def logged_user(self) -> LoggedUserResource:
        return LoggedUserResource(self._client)

    @cached_property
    def by_login(self) -> ByLoginResource:
        return ByLoginResource(self._client)

    @cached_property
    def active_directory_data(self) -> ActiveDirectoryDataResource:
        return ActiveDirectoryDataResource(self._client)

    @cached_property
    def login_method(self) -> LoginMethodResource:
        return LoginMethodResource(self._client)

    @cached_property
    def personal_details(self) -> PersonalDetailsResource:
        return PersonalDetailsResource(self._client)

    @cached_property
    def personal_id(self) -> PersonalIDResource:
        return PersonalIDResource(self._client)

    @cached_property
    def payment_details_data(self) -> PaymentDetailsDataResource:
        return PaymentDetailsDataResource(self._client)

    @cached_property
    def send_invitation(self) -> SendInvitationResource:
        return SendInvitationResource(self._client)

    @cached_property
    def access_groups(self) -> AccessGroupsResource:
        return AccessGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        first_name: Optional[str],
        language: Literal["en", "no"],
        last_name: Optional[str],
        send_invitation: bool | NotGiven = NOT_GIVEN,
        access_groups: List[str] | NotGiven = NOT_GIVEN,
        active_directory_user_name: Optional[str] | NotGiven = NOT_GIVEN,
        login_method: Literal["ACTIVE_DIRECTORY", "AUTH0"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserCreateResponse:
        """
        Creating user.

        Args:
          send_invitation: Param determines if the email notification should be sent for created user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users",
            body=maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "language": language,
                    "last_name": last_name,
                    "access_groups": access_groups,
                    "active_directory_user_name": active_directory_user_name,
                    "login_method": login_method,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"send_invitation": send_invitation}, user_create_params.UserCreateParams),
            ),
            cast_to=UserCreateResponse,
        )

    def list(
        self,
        *,
        filter: Literal["all", "offboarding", "invited", "uninvited", "expired", "inactive"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_units: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        Get users.

        Args:
          filter: filter users by given status

          limit: Number of records returned in one request

          org_units: comma separated list of orgUnits

          page: Number of returned page

          query: filter users by name, work email, job type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "org_units": org_units,
                        "page": page,
                        "query": query,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def logged_user(self) -> AsyncLoggedUserResource:
        return AsyncLoggedUserResource(self._client)

    @cached_property
    def by_login(self) -> AsyncByLoginResource:
        return AsyncByLoginResource(self._client)

    @cached_property
    def active_directory_data(self) -> AsyncActiveDirectoryDataResource:
        return AsyncActiveDirectoryDataResource(self._client)

    @cached_property
    def login_method(self) -> AsyncLoginMethodResource:
        return AsyncLoginMethodResource(self._client)

    @cached_property
    def personal_details(self) -> AsyncPersonalDetailsResource:
        return AsyncPersonalDetailsResource(self._client)

    @cached_property
    def personal_id(self) -> AsyncPersonalIDResource:
        return AsyncPersonalIDResource(self._client)

    @cached_property
    def payment_details_data(self) -> AsyncPaymentDetailsDataResource:
        return AsyncPaymentDetailsDataResource(self._client)

    @cached_property
    def send_invitation(self) -> AsyncSendInvitationResource:
        return AsyncSendInvitationResource(self._client)

    @cached_property
    def access_groups(self) -> AsyncAccessGroupsResource:
        return AsyncAccessGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        first_name: Optional[str],
        language: Literal["en", "no"],
        last_name: Optional[str],
        send_invitation: bool | NotGiven = NOT_GIVEN,
        access_groups: List[str] | NotGiven = NOT_GIVEN,
        active_directory_user_name: Optional[str] | NotGiven = NOT_GIVEN,
        login_method: Literal["ACTIVE_DIRECTORY", "AUTH0"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserCreateResponse:
        """
        Creating user.

        Args:
          send_invitation: Param determines if the email notification should be sent for created user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "language": language,
                    "last_name": last_name,
                    "access_groups": access_groups,
                    "active_directory_user_name": active_directory_user_name,
                    "login_method": login_method,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"send_invitation": send_invitation}, user_create_params.UserCreateParams
                ),
            ),
            cast_to=UserCreateResponse,
        )

    async def list(
        self,
        *,
        filter: Literal["all", "offboarding", "invited", "uninvited", "expired", "inactive"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_units: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        Get users.

        Args:
          filter: filter users by given status

          limit: Number of records returned in one request

          org_units: comma separated list of orgUnits

          page: Number of returned page

          query: filter users by name, work email, job type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "org_units": org_units,
                        "page": page,
                        "query": query,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    async def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )

    @cached_property
    def logged_user(self) -> LoggedUserResourceWithRawResponse:
        return LoggedUserResourceWithRawResponse(self._users.logged_user)

    @cached_property
    def by_login(self) -> ByLoginResourceWithRawResponse:
        return ByLoginResourceWithRawResponse(self._users.by_login)

    @cached_property
    def active_directory_data(self) -> ActiveDirectoryDataResourceWithRawResponse:
        return ActiveDirectoryDataResourceWithRawResponse(self._users.active_directory_data)

    @cached_property
    def login_method(self) -> LoginMethodResourceWithRawResponse:
        return LoginMethodResourceWithRawResponse(self._users.login_method)

    @cached_property
    def personal_details(self) -> PersonalDetailsResourceWithRawResponse:
        return PersonalDetailsResourceWithRawResponse(self._users.personal_details)

    @cached_property
    def personal_id(self) -> PersonalIDResourceWithRawResponse:
        return PersonalIDResourceWithRawResponse(self._users.personal_id)

    @cached_property
    def payment_details_data(self) -> PaymentDetailsDataResourceWithRawResponse:
        return PaymentDetailsDataResourceWithRawResponse(self._users.payment_details_data)

    @cached_property
    def send_invitation(self) -> SendInvitationResourceWithRawResponse:
        return SendInvitationResourceWithRawResponse(self._users.send_invitation)

    @cached_property
    def access_groups(self) -> AccessGroupsResourceWithRawResponse:
        return AccessGroupsResourceWithRawResponse(self._users.access_groups)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )

    @cached_property
    def logged_user(self) -> AsyncLoggedUserResourceWithRawResponse:
        return AsyncLoggedUserResourceWithRawResponse(self._users.logged_user)

    @cached_property
    def by_login(self) -> AsyncByLoginResourceWithRawResponse:
        return AsyncByLoginResourceWithRawResponse(self._users.by_login)

    @cached_property
    def active_directory_data(self) -> AsyncActiveDirectoryDataResourceWithRawResponse:
        return AsyncActiveDirectoryDataResourceWithRawResponse(self._users.active_directory_data)

    @cached_property
    def login_method(self) -> AsyncLoginMethodResourceWithRawResponse:
        return AsyncLoginMethodResourceWithRawResponse(self._users.login_method)

    @cached_property
    def personal_details(self) -> AsyncPersonalDetailsResourceWithRawResponse:
        return AsyncPersonalDetailsResourceWithRawResponse(self._users.personal_details)

    @cached_property
    def personal_id(self) -> AsyncPersonalIDResourceWithRawResponse:
        return AsyncPersonalIDResourceWithRawResponse(self._users.personal_id)

    @cached_property
    def payment_details_data(self) -> AsyncPaymentDetailsDataResourceWithRawResponse:
        return AsyncPaymentDetailsDataResourceWithRawResponse(self._users.payment_details_data)

    @cached_property
    def send_invitation(self) -> AsyncSendInvitationResourceWithRawResponse:
        return AsyncSendInvitationResourceWithRawResponse(self._users.send_invitation)

    @cached_property
    def access_groups(self) -> AsyncAccessGroupsResourceWithRawResponse:
        return AsyncAccessGroupsResourceWithRawResponse(self._users.access_groups)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )

    @cached_property
    def logged_user(self) -> LoggedUserResourceWithStreamingResponse:
        return LoggedUserResourceWithStreamingResponse(self._users.logged_user)

    @cached_property
    def by_login(self) -> ByLoginResourceWithStreamingResponse:
        return ByLoginResourceWithStreamingResponse(self._users.by_login)

    @cached_property
    def active_directory_data(self) -> ActiveDirectoryDataResourceWithStreamingResponse:
        return ActiveDirectoryDataResourceWithStreamingResponse(self._users.active_directory_data)

    @cached_property
    def login_method(self) -> LoginMethodResourceWithStreamingResponse:
        return LoginMethodResourceWithStreamingResponse(self._users.login_method)

    @cached_property
    def personal_details(self) -> PersonalDetailsResourceWithStreamingResponse:
        return PersonalDetailsResourceWithStreamingResponse(self._users.personal_details)

    @cached_property
    def personal_id(self) -> PersonalIDResourceWithStreamingResponse:
        return PersonalIDResourceWithStreamingResponse(self._users.personal_id)

    @cached_property
    def payment_details_data(self) -> PaymentDetailsDataResourceWithStreamingResponse:
        return PaymentDetailsDataResourceWithStreamingResponse(self._users.payment_details_data)

    @cached_property
    def send_invitation(self) -> SendInvitationResourceWithStreamingResponse:
        return SendInvitationResourceWithStreamingResponse(self._users.send_invitation)

    @cached_property
    def access_groups(self) -> AccessGroupsResourceWithStreamingResponse:
        return AccessGroupsResourceWithStreamingResponse(self._users.access_groups)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )

    @cached_property
    def logged_user(self) -> AsyncLoggedUserResourceWithStreamingResponse:
        return AsyncLoggedUserResourceWithStreamingResponse(self._users.logged_user)

    @cached_property
    def by_login(self) -> AsyncByLoginResourceWithStreamingResponse:
        return AsyncByLoginResourceWithStreamingResponse(self._users.by_login)

    @cached_property
    def active_directory_data(self) -> AsyncActiveDirectoryDataResourceWithStreamingResponse:
        return AsyncActiveDirectoryDataResourceWithStreamingResponse(self._users.active_directory_data)

    @cached_property
    def login_method(self) -> AsyncLoginMethodResourceWithStreamingResponse:
        return AsyncLoginMethodResourceWithStreamingResponse(self._users.login_method)

    @cached_property
    def personal_details(self) -> AsyncPersonalDetailsResourceWithStreamingResponse:
        return AsyncPersonalDetailsResourceWithStreamingResponse(self._users.personal_details)

    @cached_property
    def personal_id(self) -> AsyncPersonalIDResourceWithStreamingResponse:
        return AsyncPersonalIDResourceWithStreamingResponse(self._users.personal_id)

    @cached_property
    def payment_details_data(self) -> AsyncPaymentDetailsDataResourceWithStreamingResponse:
        return AsyncPaymentDetailsDataResourceWithStreamingResponse(self._users.payment_details_data)

    @cached_property
    def send_invitation(self) -> AsyncSendInvitationResourceWithStreamingResponse:
        return AsyncSendInvitationResourceWithStreamingResponse(self._users.send_invitation)

    @cached_property
    def access_groups(self) -> AsyncAccessGroupsResourceWithStreamingResponse:
        return AsyncAccessGroupsResourceWithStreamingResponse(self._users.access_groups)
