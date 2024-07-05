# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import (
    make_request_options,
)
from ...types.skills import user_skill_update_params
from ...types.skills.user_skill_update_response import UserSkillUpdateResponse

__all__ = ["UserSkillResource", "AsyncUserSkillResource"]


class UserSkillResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserSkillResourceWithRawResponse:
        return UserSkillResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserSkillResourceWithStreamingResponse:
        return UserSkillResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        mode: Literal["READ_ONLY", "EDIT", "CREATE"] | NotGiven = NOT_GIVEN,
        company: user_skill_update_params.Company | NotGiven = NOT_GIVEN,
        company_employee: user_skill_update_params.CompanyEmployee | NotGiven = NOT_GIVEN,
        instance_user: user_skill_update_params.InstanceUser | NotGiven = NOT_GIVEN,
        skill: user_skill_update_params.Skill | NotGiven = NOT_GIVEN,
        skill_type: user_skill_update_params.SkillType | NotGiven = NOT_GIVEN,
        skill_type_category: user_skill_update_params.SkillTypeCategory | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSkillUpdateResponse:
        """
        Create skill or skill type for given user/ update skill status if exists.

        Args:
          mode: `CREATE` - create skill type if skill type not exists, otherwise update skill
              type name `EDIT` - update skill type name if skill type exists, otherwise do not
              create skill type `READ_ONLY` - do not create skill type and do not edit skill
              type name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/competence/import/user-skill",
            body=maybe_transform(
                {
                    "company": company,
                    "company_employee": company_employee,
                    "instance_user": instance_user,
                    "skill": skill,
                    "skill_type": skill_type,
                    "skill_type_category": skill_type_category,
                },
                user_skill_update_params.UserSkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"mode": mode}, user_skill_update_params.UserSkillUpdateParams),
            ),
            cast_to=UserSkillUpdateResponse,
        )


class AsyncUserSkillResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserSkillResourceWithRawResponse:
        return AsyncUserSkillResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserSkillResourceWithStreamingResponse:
        return AsyncUserSkillResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        mode: Literal["READ_ONLY", "EDIT", "CREATE"] | NotGiven = NOT_GIVEN,
        company: user_skill_update_params.Company | NotGiven = NOT_GIVEN,
        company_employee: user_skill_update_params.CompanyEmployee | NotGiven = NOT_GIVEN,
        instance_user: user_skill_update_params.InstanceUser | NotGiven = NOT_GIVEN,
        skill: user_skill_update_params.Skill | NotGiven = NOT_GIVEN,
        skill_type: user_skill_update_params.SkillType | NotGiven = NOT_GIVEN,
        skill_type_category: user_skill_update_params.SkillTypeCategory | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSkillUpdateResponse:
        """
        Create skill or skill type for given user/ update skill status if exists.

        Args:
          mode: `CREATE` - create skill type if skill type not exists, otherwise update skill
              type name `EDIT` - update skill type name if skill type exists, otherwise do not
              create skill type `READ_ONLY` - do not create skill type and do not edit skill
              type name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/competence/import/user-skill",
            body=await async_maybe_transform(
                {
                    "company": company,
                    "company_employee": company_employee,
                    "instance_user": instance_user,
                    "skill": skill,
                    "skill_type": skill_type,
                    "skill_type_category": skill_type_category,
                },
                user_skill_update_params.UserSkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"mode": mode}, user_skill_update_params.UserSkillUpdateParams),
            ),
            cast_to=UserSkillUpdateResponse,
        )


class UserSkillResourceWithRawResponse:
    def __init__(self, user_skill: UserSkillResource) -> None:
        self._user_skill = user_skill

        self.update = to_raw_response_wrapper(
            user_skill.update,
        )


class AsyncUserSkillResourceWithRawResponse:
    def __init__(self, user_skill: AsyncUserSkillResource) -> None:
        self._user_skill = user_skill

        self.update = async_to_raw_response_wrapper(
            user_skill.update,
        )


class UserSkillResourceWithStreamingResponse:
    def __init__(self, user_skill: UserSkillResource) -> None:
        self._user_skill = user_skill

        self.update = to_streamed_response_wrapper(
            user_skill.update,
        )


class AsyncUserSkillResourceWithStreamingResponse:
    def __init__(self, user_skill: AsyncUserSkillResource) -> None:
        self._user_skill = user_skill

        self.update = async_to_streamed_response_wrapper(
            user_skill.update,
        )
