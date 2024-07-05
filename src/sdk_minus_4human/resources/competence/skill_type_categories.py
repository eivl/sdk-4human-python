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
from ..._base_client import (
    make_request_options,
)
from ...types.competence import (
    skill_type_category_create_params,
    skill_type_category_update_params,
    skill_type_category_retrieve_params,
)
from ...types.competence.skill_type_category_list_response import SkillTypeCategoryListResponse
from ...types.competence.skill_type_category_create_response import SkillTypeCategoryCreateResponse
from ...types.competence.skill_type_category_update_response import SkillTypeCategoryUpdateResponse
from ...types.competence.skill_type_category_retrieve_response import SkillTypeCategoryRetrieveResponse

__all__ = ["SkillTypeCategoriesResource", "AsyncSkillTypeCategoriesResource"]


class SkillTypeCategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SkillTypeCategoriesResourceWithRawResponse:
        return SkillTypeCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillTypeCategoriesResourceWithStreamingResponse:
        return SkillTypeCategoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        color: Optional[
            Literal[
                "#191970",
                "#4169E1",
                "#4682B4",
                "#52BFFF",
                "#4ED1CC",
                "#008080",
                "#298652",
                "#5E8115",
                "#4B0082",
                "#800080",
                "#C71585",
                "#8562CD",
                "#AF4AC8",
                "#F084F0",
                "#E0330D",
                "#FF8B6F",
                "#C35252",
                "#696969",
                "#A52A2A",
                "#EA977B",
                "#DAA51F",
                "#F4A503",
            ]
        ],
        description: Optional[str],
        name: str,
        number: str,
        parent_id: Optional[str],
        icon: Optional[skill_type_category_create_params.Icon] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeCategoryCreateResponse:
        """
        Create skill type category.

        Args:
          color: Color of icon skill type category (hexadecimal color value)

          description: Description of skill type category

          name: Name of skill type category

          number: Number of skill type category

          parent_id: ID of parent skill type category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/competence/skill-type-categories",
            body=maybe_transform(
                {
                    "color": color,
                    "description": description,
                    "name": name,
                    "number": number,
                    "parent_id": parent_id,
                    "icon": icon,
                },
                skill_type_category_create_params.SkillTypeCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillTypeCategoryCreateResponse,
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
    ) -> SkillTypeCategoryRetrieveResponse:
        """
        Get skill type category with given id.

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
            f"/competence/skill-type-categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external": external}, skill_type_category_retrieve_params.SkillTypeCategoryRetrieveParams
                ),
            ),
            cast_to=SkillTypeCategoryRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        color: Optional[
            Literal[
                "#191970",
                "#4169E1",
                "#4682B4",
                "#52BFFF",
                "#4ED1CC",
                "#008080",
                "#298652",
                "#5E8115",
                "#4B0082",
                "#800080",
                "#C71585",
                "#8562CD",
                "#AF4AC8",
                "#F084F0",
                "#E0330D",
                "#FF8B6F",
                "#C35252",
                "#696969",
                "#A52A2A",
                "#EA977B",
                "#DAA51F",
                "#F4A503",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        icon: Optional[skill_type_category_update_params.Icon] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        parent_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeCategoryUpdateResponse:
        """
        Edit single field of skill type category with given id.

        Args:
          external: Param determines if `id` is external (`number`) or internal (`id`)

          color: Color of icon skill type category (hexadecimal color value)

          description: Description of skill type category

          name: Name of skill type category

          number: Number of skill type category

          parent_id: ID of parent skill type category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/competence/skill-type-categories/{id}",
            body=maybe_transform(
                {
                    "color": color,
                    "description": description,
                    "icon": icon,
                    "name": name,
                    "number": number,
                    "parent_id": parent_id,
                },
                skill_type_category_update_params.SkillTypeCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"external": external}, skill_type_category_update_params.SkillTypeCategoryUpdateParams
                ),
            ),
            cast_to=SkillTypeCategoryUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeCategoryListResponse:
        """Get list of skill type categories."""
        return self._get(
            "/competence/skill-type-categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillTypeCategoryListResponse,
        )


class AsyncSkillTypeCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSkillTypeCategoriesResourceWithRawResponse:
        return AsyncSkillTypeCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillTypeCategoriesResourceWithStreamingResponse:
        return AsyncSkillTypeCategoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        color: Optional[
            Literal[
                "#191970",
                "#4169E1",
                "#4682B4",
                "#52BFFF",
                "#4ED1CC",
                "#008080",
                "#298652",
                "#5E8115",
                "#4B0082",
                "#800080",
                "#C71585",
                "#8562CD",
                "#AF4AC8",
                "#F084F0",
                "#E0330D",
                "#FF8B6F",
                "#C35252",
                "#696969",
                "#A52A2A",
                "#EA977B",
                "#DAA51F",
                "#F4A503",
            ]
        ],
        description: Optional[str],
        name: str,
        number: str,
        parent_id: Optional[str],
        icon: Optional[skill_type_category_create_params.Icon] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeCategoryCreateResponse:
        """
        Create skill type category.

        Args:
          color: Color of icon skill type category (hexadecimal color value)

          description: Description of skill type category

          name: Name of skill type category

          number: Number of skill type category

          parent_id: ID of parent skill type category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/competence/skill-type-categories",
            body=await async_maybe_transform(
                {
                    "color": color,
                    "description": description,
                    "name": name,
                    "number": number,
                    "parent_id": parent_id,
                    "icon": icon,
                },
                skill_type_category_create_params.SkillTypeCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillTypeCategoryCreateResponse,
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
    ) -> SkillTypeCategoryRetrieveResponse:
        """
        Get skill type category with given id.

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
            f"/competence/skill-type-categories/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, skill_type_category_retrieve_params.SkillTypeCategoryRetrieveParams
                ),
            ),
            cast_to=SkillTypeCategoryRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        color: Optional[
            Literal[
                "#191970",
                "#4169E1",
                "#4682B4",
                "#52BFFF",
                "#4ED1CC",
                "#008080",
                "#298652",
                "#5E8115",
                "#4B0082",
                "#800080",
                "#C71585",
                "#8562CD",
                "#AF4AC8",
                "#F084F0",
                "#E0330D",
                "#FF8B6F",
                "#C35252",
                "#696969",
                "#A52A2A",
                "#EA977B",
                "#DAA51F",
                "#F4A503",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        icon: Optional[skill_type_category_update_params.Icon] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        parent_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeCategoryUpdateResponse:
        """
        Edit single field of skill type category with given id.

        Args:
          external: Param determines if `id` is external (`number`) or internal (`id`)

          color: Color of icon skill type category (hexadecimal color value)

          description: Description of skill type category

          name: Name of skill type category

          number: Number of skill type category

          parent_id: ID of parent skill type category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/competence/skill-type-categories/{id}",
            body=await async_maybe_transform(
                {
                    "color": color,
                    "description": description,
                    "icon": icon,
                    "name": name,
                    "number": number,
                    "parent_id": parent_id,
                },
                skill_type_category_update_params.SkillTypeCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, skill_type_category_update_params.SkillTypeCategoryUpdateParams
                ),
            ),
            cast_to=SkillTypeCategoryUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillTypeCategoryListResponse:
        """Get list of skill type categories."""
        return await self._get(
            "/competence/skill-type-categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillTypeCategoryListResponse,
        )


class SkillTypeCategoriesResourceWithRawResponse:
    def __init__(self, skill_type_categories: SkillTypeCategoriesResource) -> None:
        self._skill_type_categories = skill_type_categories

        self.create = to_raw_response_wrapper(
            skill_type_categories.create,
        )
        self.retrieve = to_raw_response_wrapper(
            skill_type_categories.retrieve,
        )
        self.update = to_raw_response_wrapper(
            skill_type_categories.update,
        )
        self.list = to_raw_response_wrapper(
            skill_type_categories.list,
        )


class AsyncSkillTypeCategoriesResourceWithRawResponse:
    def __init__(self, skill_type_categories: AsyncSkillTypeCategoriesResource) -> None:
        self._skill_type_categories = skill_type_categories

        self.create = async_to_raw_response_wrapper(
            skill_type_categories.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            skill_type_categories.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            skill_type_categories.update,
        )
        self.list = async_to_raw_response_wrapper(
            skill_type_categories.list,
        )


class SkillTypeCategoriesResourceWithStreamingResponse:
    def __init__(self, skill_type_categories: SkillTypeCategoriesResource) -> None:
        self._skill_type_categories = skill_type_categories

        self.create = to_streamed_response_wrapper(
            skill_type_categories.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            skill_type_categories.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            skill_type_categories.update,
        )
        self.list = to_streamed_response_wrapper(
            skill_type_categories.list,
        )


class AsyncSkillTypeCategoriesResourceWithStreamingResponse:
    def __init__(self, skill_type_categories: AsyncSkillTypeCategoriesResource) -> None:
        self._skill_type_categories = skill_type_categories

        self.create = async_to_streamed_response_wrapper(
            skill_type_categories.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            skill_type_categories.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            skill_type_categories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            skill_type_categories.list,
        )
