# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.personnel.employments import former_create_params
from ....types.personnel.employments.former_create_response import FormerCreateResponse

__all__ = ["FormersResource", "AsyncFormersResource"]


class FormersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FormersResourceWithRawResponse:
        return FormersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormersResourceWithStreamingResponse:
        return FormersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_employee: Optional[former_create_params.CompanyEmployee],
        employment: former_create_params.Employment,
        internal_termination_reason_id: str,
        personal_identification: former_create_params.PersonalIdentification,
        termination_reason_id: str,
        user: former_create_params.User,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormerCreateResponse:
        """
        This endpoint allows to onboard (create) a former employment (personnel
        employment).

        In 4human's structure employment is the last level of employee data. The levels
        are as follows:

        - user - representing a user of the platform, with personal data

        - company employee - representing the employee working in a given company;
          company is an organization unit with a flag "company"

        - personnel employment (employment) - representing a single employee's contract
          in a given company.

        One user may have multiple company employees and one company employee may have
        multiple employments.

        This endpoint allows to create a one-to-one-to-one structure - which means one
        user with one company employee and one employment.

        This endpoint does not send invitations to former employments.

        Args:
          internal_termination_reason_id: Internal termination reason ID, from instance section settings > termination
              reasons

          termination_reason_id: Termination reason ID, from master management Terminate Reasons (id)

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/employments/formers",
            body=maybe_transform(
                {
                    "company_employee": company_employee,
                    "employment": employment,
                    "internal_termination_reason_id": internal_termination_reason_id,
                    "personal_identification": personal_identification,
                    "termination_reason_id": termination_reason_id,
                    "user": user,
                },
                former_create_params.FormerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy}, former_create_params.FormerCreateParams
                ),
            ),
            cast_to=FormerCreateResponse,
        )


class AsyncFormersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFormersResourceWithRawResponse:
        return AsyncFormersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormersResourceWithStreamingResponse:
        return AsyncFormersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_employee: Optional[former_create_params.CompanyEmployee],
        employment: former_create_params.Employment,
        internal_termination_reason_id: str,
        personal_identification: former_create_params.PersonalIdentification,
        termination_reason_id: str,
        user: former_create_params.User,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormerCreateResponse:
        """
        This endpoint allows to onboard (create) a former employment (personnel
        employment).

        In 4human's structure employment is the last level of employee data. The levels
        are as follows:

        - user - representing a user of the platform, with personal data

        - company employee - representing the employee working in a given company;
          company is an organization unit with a flag "company"

        - personnel employment (employment) - representing a single employee's contract
          in a given company.

        One user may have multiple company employees and one company employee may have
        multiple employments.

        This endpoint allows to create a one-to-one-to-one structure - which means one
        user with one company employee and one employment.

        This endpoint does not send invitations to former employments.

        Args:
          internal_termination_reason_id: Internal termination reason ID, from instance section settings > termination
              reasons

          termination_reason_id: Termination reason ID, from master management Terminate Reasons (id)

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/employments/formers",
            body=await async_maybe_transform(
                {
                    "company_employee": company_employee,
                    "employment": employment,
                    "internal_termination_reason_id": internal_termination_reason_id,
                    "personal_identification": personal_identification,
                    "termination_reason_id": termination_reason_id,
                    "user": user,
                },
                former_create_params.FormerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_no_approval_policy": force_no_approval_policy}, former_create_params.FormerCreateParams
                ),
            ),
            cast_to=FormerCreateResponse,
        )


class FormersResourceWithRawResponse:
    def __init__(self, formers: FormersResource) -> None:
        self._formers = formers

        self.create = to_raw_response_wrapper(
            formers.create,
        )


class AsyncFormersResourceWithRawResponse:
    def __init__(self, formers: AsyncFormersResource) -> None:
        self._formers = formers

        self.create = async_to_raw_response_wrapper(
            formers.create,
        )


class FormersResourceWithStreamingResponse:
    def __init__(self, formers: FormersResource) -> None:
        self._formers = formers

        self.create = to_streamed_response_wrapper(
            formers.create,
        )


class AsyncFormersResourceWithStreamingResponse:
    def __init__(self, formers: AsyncFormersResource) -> None:
        self._formers = formers

        self.create = async_to_streamed_response_wrapper(
            formers.create,
        )
