# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import skill_list_params, skill_create_params, skill_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .user_skill import (
    UserSkillResource,
    AsyncUserSkillResource,
    UserSkillResourceWithRawResponse,
    AsyncUserSkillResourceWithRawResponse,
    UserSkillResourceWithStreamingResponse,
    AsyncUserSkillResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.skill_list_response import SkillListResponse
from ...types.skill_create_response import SkillCreateResponse
from ...types.skill_update_response import SkillUpdateResponse
from ...types.skill_retrieve_response import SkillRetrieveResponse

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    @cached_property
    def user_skill(self) -> UserSkillResource:
        return UserSkillResource(self._client)

    @cached_property
    def with_raw_response(self) -> SkillsResourceWithRawResponse:
        return SkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillsResourceWithStreamingResponse:
        return SkillsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: int,
        employment_id: Optional[int],
        fields: Iterable[skill_create_params.Field],
        parent_id: Optional[int],
        privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"],
        skill_type_id: str,
        status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved", "notApplicable"],
        user_id: str,
        employee_id: Optional[str] | NotGiven = NOT_GIVEN,
        organization_number: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillCreateResponse:
        """
        Create skill.

        Args:
          parent_id: Id of parent skill used in renewed process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/competence/skills",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "employment_id": employment_id,
                    "fields": fields,
                    "parent_id": parent_id,
                    "privacy": privacy,
                    "skill_type_id": skill_type_id,
                    "status": status,
                    "user_id": user_id,
                    "employee_id": employee_id,
                    "organization_number": organization_number,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillCreateResponse,
        )

    def retrieve(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillRetrieveResponse:
        """
        Get skill details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._get(
            f"/competence/skills/{skill_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillRetrieveResponse,
        )

    def update(
        self,
        skill_id: str,
        *,
        employment_id: Optional[int] | NotGiven = NOT_GIVEN,
        fields: Iterable[skill_update_params.Field] | NotGiven = NOT_GIVEN,
        privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"] | NotGiven = NOT_GIVEN,
        status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved", "notApplicable"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillUpdateResponse:
        """
        Edit field in skill details.

        Args:
          fields: - Fields set as not visible in the skill type configuration will be omitted and
                not updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._patch(
            f"/competence/skills/{skill_id}",
            body=maybe_transform(
                {
                    "employment_id": employment_id,
                    "fields": fields,
                    "privacy": privacy,
                    "status": status,
                },
                skill_update_params.SkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillListResponse:
        """
        Get list of competence skills.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/competence/skills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    skill_list_params.SkillListParams,
                ),
            ),
            cast_to=SkillListResponse,
        )


class AsyncSkillsResource(AsyncAPIResource):
    @cached_property
    def user_skill(self) -> AsyncUserSkillResource:
        return AsyncUserSkillResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSkillsResourceWithRawResponse:
        return AsyncSkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillsResourceWithStreamingResponse:
        return AsyncSkillsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: int,
        employment_id: Optional[int],
        fields: Iterable[skill_create_params.Field],
        parent_id: Optional[int],
        privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"],
        skill_type_id: str,
        status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved", "notApplicable"],
        user_id: str,
        employee_id: Optional[str] | NotGiven = NOT_GIVEN,
        organization_number: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillCreateResponse:
        """
        Create skill.

        Args:
          parent_id: Id of parent skill used in renewed process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/competence/skills",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "employment_id": employment_id,
                    "fields": fields,
                    "parent_id": parent_id,
                    "privacy": privacy,
                    "skill_type_id": skill_type_id,
                    "status": status,
                    "user_id": user_id,
                    "employee_id": employee_id,
                    "organization_number": organization_number,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillCreateResponse,
        )

    async def retrieve(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillRetrieveResponse:
        """
        Get skill details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._get(
            f"/competence/skills/{skill_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillRetrieveResponse,
        )

    async def update(
        self,
        skill_id: str,
        *,
        employment_id: Optional[int] | NotGiven = NOT_GIVEN,
        fields: Iterable[skill_update_params.Field] | NotGiven = NOT_GIVEN,
        privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"] | NotGiven = NOT_GIVEN,
        status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved", "notApplicable"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillUpdateResponse:
        """
        Edit field in skill details.

        Args:
          fields: - Fields set as not visible in the skill type configuration will be omitted and
                not updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._patch(
            f"/competence/skills/{skill_id}",
            body=await async_maybe_transform(
                {
                    "employment_id": employment_id,
                    "fields": fields,
                    "privacy": privacy,
                    "status": status,
                },
                skill_update_params.SkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillListResponse:
        """
        Get list of competence skills.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/competence/skills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    skill_list_params.SkillListParams,
                ),
            ),
            cast_to=SkillListResponse,
        )


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_raw_response_wrapper(
            skills.create,
        )
        self.retrieve = to_raw_response_wrapper(
            skills.retrieve,
        )
        self.update = to_raw_response_wrapper(
            skills.update,
        )
        self.list = to_raw_response_wrapper(
            skills.list,
        )

    @cached_property
    def user_skill(self) -> UserSkillResourceWithRawResponse:
        return UserSkillResourceWithRawResponse(self._skills.user_skill)


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_raw_response_wrapper(
            skills.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            skills.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            skills.update,
        )
        self.list = async_to_raw_response_wrapper(
            skills.list,
        )

    @cached_property
    def user_skill(self) -> AsyncUserSkillResourceWithRawResponse:
        return AsyncUserSkillResourceWithRawResponse(self._skills.user_skill)


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_streamed_response_wrapper(
            skills.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            skills.update,
        )
        self.list = to_streamed_response_wrapper(
            skills.list,
        )

    @cached_property
    def user_skill(self) -> UserSkillResourceWithStreamingResponse:
        return UserSkillResourceWithStreamingResponse(self._skills.user_skill)


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_streamed_response_wrapper(
            skills.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            skills.update,
        )
        self.list = async_to_streamed_response_wrapper(
            skills.list,
        )

    @cached_property
    def user_skill(self) -> AsyncUserSkillResourceWithStreamingResponse:
        return AsyncUserSkillResourceWithStreamingResponse(self._skills.user_skill)
