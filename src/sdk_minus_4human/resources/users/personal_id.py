# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ...types.users import (
    personal_id_create_params,
    personal_id_delete_params,
    personal_id_import_params,
    personal_id_update_params,
)
from ..._base_client import (
    make_request_options,
)
from ...types.users.personal_id_create_response import PersonalIDCreateResponse
from ...types.users.personal_id_delete_response import PersonalIDDeleteResponse
from ...types.users.personal_id_import_response import PersonalIDImportResponse
from ...types.users.personal_id_update_response import PersonalIDUpdateResponse

__all__ = ["PersonalIDResource", "AsyncPersonalIDResource"]


class PersonalIDResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersonalIDResourceWithRawResponse:
        return PersonalIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonalIDResourceWithStreamingResponse:
        return PersonalIDResourceWithStreamingResponse(self)

    def create(
        self,
        user_id: str,
        *,
        id_country: Optional[str],
        id_number: Optional[str],
        id_type: Optional[Literal["none", "alternative_id", "ssn", "passport"]],
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalIDCreateResponse:
        """
        Create user personal id.

        Args:
          id_country: Country of document

          id_number: Document number

          id_type: Type of document

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/users/personal-id/{user_id}",
            body=maybe_transform(
                {
                    "id_country": id_country,
                    "id_number": id_number,
                    "id_type": id_type,
                },
                personal_id_create_params.PersonalIDCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_id_create_params.PersonalIDCreateParams,
                ),
            ),
            cast_to=PersonalIDCreateResponse,
        )

    def update(
        self,
        id: int,
        *,
        user_id: str,
        id_country: Optional[str],
        id_number: Optional[str],
        id_type: Optional[Literal["none", "alternative_id", "ssn", "passport"]],
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalIDUpdateResponse:
        """
        Edit user personal id.

        Args:
          id_country: Country of document

          id_number: Document number

          id_type: Type of document

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
            f"/users/personal-id/{user_id}/{id}",
            body=maybe_transform(
                {
                    "id_country": id_country,
                    "id_number": id_number,
                    "id_type": id_type,
                },
                personal_id_update_params.PersonalIDUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_id_update_params.PersonalIDUpdateParams,
                ),
            ),
            cast_to=PersonalIDUpdateResponse,
        )

    def delete(
        self,
        id: int,
        *,
        user_id: str,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalIDDeleteResponse:
        """
        Delete user personal id.

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
        return self._delete(
            f"/users/personal-id/{user_id}/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_id_delete_params.PersonalIDDeleteParams,
                ),
            ),
            cast_to=PersonalIDDeleteResponse,
        )

    def import_(
        self,
        user_id: str,
        *,
        id_country: Optional[str],
        id_number: Optional[str],
        id_type: Optional[Literal["none", "alternative_id", "ssn"]],
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        passport_country: Optional[str] | NotGiven = NOT_GIVEN,
        passport_number: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalIDImportResponse:
        """Import personal id.

        It uses a deprecated way to update personal id. Update
        idNumber when find idType and idCountry in current data or add as new ones

        Args:
          id_country: Country of document

          id_number: Document number

          id_type: Type of document

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          passport_country: Country of passport

          passport_number: Passport number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/users/personal-id/{user_id}/import",
            body=maybe_transform(
                {
                    "id_country": id_country,
                    "id_number": id_number,
                    "id_type": id_type,
                    "passport_country": passport_country,
                    "passport_number": passport_number,
                },
                personal_id_import_params.PersonalIDImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_id_import_params.PersonalIDImportParams,
                ),
            ),
            cast_to=PersonalIDImportResponse,
        )


class AsyncPersonalIDResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersonalIDResourceWithRawResponse:
        return AsyncPersonalIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonalIDResourceWithStreamingResponse:
        return AsyncPersonalIDResourceWithStreamingResponse(self)

    async def create(
        self,
        user_id: str,
        *,
        id_country: Optional[str],
        id_number: Optional[str],
        id_type: Optional[Literal["none", "alternative_id", "ssn", "passport"]],
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalIDCreateResponse:
        """
        Create user personal id.

        Args:
          id_country: Country of document

          id_number: Document number

          id_type: Type of document

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/users/personal-id/{user_id}",
            body=await async_maybe_transform(
                {
                    "id_country": id_country,
                    "id_number": id_number,
                    "id_type": id_type,
                },
                personal_id_create_params.PersonalIDCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_id_create_params.PersonalIDCreateParams,
                ),
            ),
            cast_to=PersonalIDCreateResponse,
        )

    async def update(
        self,
        id: int,
        *,
        user_id: str,
        id_country: Optional[str],
        id_number: Optional[str],
        id_type: Optional[Literal["none", "alternative_id", "ssn", "passport"]],
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalIDUpdateResponse:
        """
        Edit user personal id.

        Args:
          id_country: Country of document

          id_number: Document number

          id_type: Type of document

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
            f"/users/personal-id/{user_id}/{id}",
            body=await async_maybe_transform(
                {
                    "id_country": id_country,
                    "id_number": id_number,
                    "id_type": id_type,
                },
                personal_id_update_params.PersonalIDUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_id_update_params.PersonalIDUpdateParams,
                ),
            ),
            cast_to=PersonalIDUpdateResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        user_id: str,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalIDDeleteResponse:
        """
        Delete user personal id.

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
        return await self._delete(
            f"/users/personal-id/{user_id}/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_id_delete_params.PersonalIDDeleteParams,
                ),
            ),
            cast_to=PersonalIDDeleteResponse,
        )

    async def import_(
        self,
        user_id: str,
        *,
        id_country: Optional[str],
        id_number: Optional[str],
        id_type: Optional[Literal["none", "alternative_id", "ssn"]],
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        passport_country: Optional[str] | NotGiven = NOT_GIVEN,
        passport_number: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalIDImportResponse:
        """Import personal id.

        It uses a deprecated way to update personal id. Update
        idNumber when find idType and idCountry in current data or add as new ones

        Args:
          id_country: Country of document

          id_number: Document number

          id_type: Type of document

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          passport_country: Country of passport

          passport_number: Passport number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/users/personal-id/{user_id}/import",
            body=await async_maybe_transform(
                {
                    "id_country": id_country,
                    "id_number": id_number,
                    "id_type": id_type,
                    "passport_country": passport_country,
                    "passport_number": passport_number,
                },
                personal_id_import_params.PersonalIDImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy},
                    personal_id_import_params.PersonalIDImportParams,
                ),
            ),
            cast_to=PersonalIDImportResponse,
        )


class PersonalIDResourceWithRawResponse:
    def __init__(self, personal_id: PersonalIDResource) -> None:
        self._personal_id = personal_id

        self.create = to_raw_response_wrapper(
            personal_id.create,
        )
        self.update = to_raw_response_wrapper(
            personal_id.update,
        )
        self.delete = to_raw_response_wrapper(
            personal_id.delete,
        )
        self.import_ = to_raw_response_wrapper(
            personal_id.import_,
        )


class AsyncPersonalIDResourceWithRawResponse:
    def __init__(self, personal_id: AsyncPersonalIDResource) -> None:
        self._personal_id = personal_id

        self.create = async_to_raw_response_wrapper(
            personal_id.create,
        )
        self.update = async_to_raw_response_wrapper(
            personal_id.update,
        )
        self.delete = async_to_raw_response_wrapper(
            personal_id.delete,
        )
        self.import_ = async_to_raw_response_wrapper(
            personal_id.import_,
        )


class PersonalIDResourceWithStreamingResponse:
    def __init__(self, personal_id: PersonalIDResource) -> None:
        self._personal_id = personal_id

        self.create = to_streamed_response_wrapper(
            personal_id.create,
        )
        self.update = to_streamed_response_wrapper(
            personal_id.update,
        )
        self.delete = to_streamed_response_wrapper(
            personal_id.delete,
        )
        self.import_ = to_streamed_response_wrapper(
            personal_id.import_,
        )


class AsyncPersonalIDResourceWithStreamingResponse:
    def __init__(self, personal_id: AsyncPersonalIDResource) -> None:
        self._personal_id = personal_id

        self.create = async_to_streamed_response_wrapper(
            personal_id.create,
        )
        self.update = async_to_streamed_response_wrapper(
            personal_id.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            personal_id.delete,
        )
        self.import_ = async_to_streamed_response_wrapper(
            personal_id.import_,
        )
