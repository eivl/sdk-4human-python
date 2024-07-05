# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    skill_type_create_params,
    skill_type_status_params,
    skill_type_update_params,
    skill_type_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.skill_type_create_response import SkillTypeCreateResponse
from ..types.skill_type_status_response import SkillTypeStatusResponse
from ..types.skill_type_update_response import SkillTypeUpdateResponse
from ..types.skill_type_retrieve_response import SkillTypeRetrieveResponse

__all__ = ["SkillTypesResource", "AsyncSkillTypesResource"]


class SkillTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SkillTypesResourceWithRawResponse:
        return SkillTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillTypesResourceWithStreamingResponse:
        return SkillTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        categories: List[str],
        cv_categories: List[str],
        default_skill_status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved"],
        description: Optional[str],
        meta_fields: Iterable[skill_type_create_params.MetaField],
        name: str,
        number: str,
        privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"],
        sections: Iterable[skill_type_create_params.Section],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeCreateResponse:
        """
        Create competence skill type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/competence/skill-types",
            body=maybe_transform(
                {
                    "categories": categories,
                    "cv_categories": cv_categories,
                    "default_skill_status": default_skill_status,
                    "description": description,
                    "meta_fields": meta_fields,
                    "name": name,
                    "number": number,
                    "privacy": privacy,
                    "sections": sections,
                },
                skill_type_create_params.SkillTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillTypeCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeRetrieveResponse:
        """
        Get one Skill Type with all its definition, fields etc by given id.

        Args:
          external: Param determines if `id` is external (`number`) or internal (`id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/competence/skill-types/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"external": external}, skill_type_retrieve_params.SkillTypeRetrieveParams),
            ),
            cast_to=SkillTypeRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        categories: List[str] | NotGiven = NOT_GIVEN,
        cv_categories: List[str] | NotGiven = NOT_GIVEN,
        default_skill_status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved"]
        | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        meta_fields: Iterable[skill_type_update_params.MetaField] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"] | NotGiven = NOT_GIVEN,
        sections: Iterable[skill_type_update_params.Section] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeUpdateResponse:
        """
        Edit single field of Skill Type with given id.

        Args:
          external: Param determines if `id` is external (`number`) or internal (`id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/competence/skill-types/{id}",
            body=maybe_transform(
                {
                    "categories": categories,
                    "cv_categories": cv_categories,
                    "default_skill_status": default_skill_status,
                    "description": description,
                    "meta_fields": meta_fields,
                    "name": name,
                    "number": number,
                    "privacy": privacy,
                    "sections": sections,
                },
                skill_type_update_params.SkillTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"external": external}, skill_type_update_params.SkillTypeUpdateParams),
            ),
            cast_to=SkillTypeUpdateResponse,
        )

    def status(
        self,
        id: str,
        *,
        status: Literal["active", "draft", "archived"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeStatusResponse:
        """
        Change status of Skill Type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/competence/skill-types/{id}/status",
            body=maybe_transform({"status": status}, skill_type_status_params.SkillTypeStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillTypeStatusResponse,
        )


class AsyncSkillTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSkillTypesResourceWithRawResponse:
        return AsyncSkillTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillTypesResourceWithStreamingResponse:
        return AsyncSkillTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        categories: List[str],
        cv_categories: List[str],
        default_skill_status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved"],
        description: Optional[str],
        meta_fields: Iterable[skill_type_create_params.MetaField],
        name: str,
        number: str,
        privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"],
        sections: Iterable[skill_type_create_params.Section],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeCreateResponse:
        """
        Create competence skill type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/competence/skill-types",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "cv_categories": cv_categories,
                    "default_skill_status": default_skill_status,
                    "description": description,
                    "meta_fields": meta_fields,
                    "name": name,
                    "number": number,
                    "privacy": privacy,
                    "sections": sections,
                },
                skill_type_create_params.SkillTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillTypeCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeRetrieveResponse:
        """
        Get one Skill Type with all its definition, fields etc by given id.

        Args:
          external: Param determines if `id` is external (`number`) or internal (`id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/competence/skill-types/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, skill_type_retrieve_params.SkillTypeRetrieveParams
                ),
            ),
            cast_to=SkillTypeRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        categories: List[str] | NotGiven = NOT_GIVEN,
        cv_categories: List[str] | NotGiven = NOT_GIVEN,
        default_skill_status: Literal["toBePlanned", "planned", "started", "toBeApproved", "approved"]
        | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        meta_fields: Iterable[skill_type_update_params.MetaField] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        privacy: Literal["public", "myOrganization", "myManagers", "onlyMe"] | NotGiven = NOT_GIVEN,
        sections: Iterable[skill_type_update_params.Section] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeUpdateResponse:
        """
        Edit single field of Skill Type with given id.

        Args:
          external: Param determines if `id` is external (`number`) or internal (`id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/competence/skill-types/{id}",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "cv_categories": cv_categories,
                    "default_skill_status": default_skill_status,
                    "description": description,
                    "meta_fields": meta_fields,
                    "name": name,
                    "number": number,
                    "privacy": privacy,
                    "sections": sections,
                },
                skill_type_update_params.SkillTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, skill_type_update_params.SkillTypeUpdateParams
                ),
            ),
            cast_to=SkillTypeUpdateResponse,
        )

    async def status(
        self,
        id: str,
        *,
        status: Literal["active", "draft", "archived"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeStatusResponse:
        """
        Change status of Skill Type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/competence/skill-types/{id}/status",
            body=await async_maybe_transform({"status": status}, skill_type_status_params.SkillTypeStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillTypeStatusResponse,
        )


class SkillTypesResourceWithRawResponse:
    def __init__(self, skill_types: SkillTypesResource) -> None:
        self._skill_types = skill_types

        self.create = to_raw_response_wrapper(
            skill_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            skill_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            skill_types.update,
        )
        self.status = to_raw_response_wrapper(
            skill_types.status,
        )


class AsyncSkillTypesResourceWithRawResponse:
    def __init__(self, skill_types: AsyncSkillTypesResource) -> None:
        self._skill_types = skill_types

        self.create = async_to_raw_response_wrapper(
            skill_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            skill_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            skill_types.update,
        )
        self.status = async_to_raw_response_wrapper(
            skill_types.status,
        )


class SkillTypesResourceWithStreamingResponse:
    def __init__(self, skill_types: SkillTypesResource) -> None:
        self._skill_types = skill_types

        self.create = to_streamed_response_wrapper(
            skill_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            skill_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            skill_types.update,
        )
        self.status = to_streamed_response_wrapper(
            skill_types.status,
        )


class AsyncSkillTypesResourceWithStreamingResponse:
    def __init__(self, skill_types: AsyncSkillTypesResource) -> None:
        self._skill_types = skill_types

        self.create = async_to_streamed_response_wrapper(
            skill_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            skill_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            skill_types.update,
        )
        self.status = async_to_streamed_response_wrapper(
            skill_types.status,
        )
