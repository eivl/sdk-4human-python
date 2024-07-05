# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.personnel import job_category_list_params, job_category_create_params
from ...types.personnel.job_category_list_response import JobCategoryListResponse
from ...types.personnel.job_category_create_response import JobCategoryCreateResponse

__all__ = ["JobCategoriesResource", "AsyncJobCategoriesResource"]


class JobCategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobCategoriesResourceWithRawResponse:
        return JobCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobCategoriesResourceWithStreamingResponse:
        return JobCategoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str],
        external_id: Optional[str],
        internal_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCategoryCreateResponse:
        """
        This endpoint allows to create a new category to group jobs.

        Args:
          description: Job category additional description

          external_id: External ID, allowing to store the ID of the client's system

          internal_id: Internal ID provided, must be unique

          name: Job category name, must be unique

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/job-categories",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "name": name,
                },
                job_category_create_params.JobCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCategoryCreateResponse,
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
    ) -> JobCategoryListResponse:
        """
        This endpoint allows to get the paginated job categories list.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/job-categories",
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
                    job_category_list_params.JobCategoryListParams,
                ),
            ),
            cast_to=JobCategoryListResponse,
        )


class AsyncJobCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobCategoriesResourceWithRawResponse:
        return AsyncJobCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobCategoriesResourceWithStreamingResponse:
        return AsyncJobCategoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str],
        external_id: Optional[str],
        internal_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCategoryCreateResponse:
        """
        This endpoint allows to create a new category to group jobs.

        Args:
          description: Job category additional description

          external_id: External ID, allowing to store the ID of the client's system

          internal_id: Internal ID provided, must be unique

          name: Job category name, must be unique

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/job-categories",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "name": name,
                },
                job_category_create_params.JobCategoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCategoryCreateResponse,
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
    ) -> JobCategoryListResponse:
        """
        This endpoint allows to get the paginated job categories list.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/job-categories",
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
                    job_category_list_params.JobCategoryListParams,
                ),
            ),
            cast_to=JobCategoryListResponse,
        )


class JobCategoriesResourceWithRawResponse:
    def __init__(self, job_categories: JobCategoriesResource) -> None:
        self._job_categories = job_categories

        self.create = to_raw_response_wrapper(
            job_categories.create,
        )
        self.list = to_raw_response_wrapper(
            job_categories.list,
        )


class AsyncJobCategoriesResourceWithRawResponse:
    def __init__(self, job_categories: AsyncJobCategoriesResource) -> None:
        self._job_categories = job_categories

        self.create = async_to_raw_response_wrapper(
            job_categories.create,
        )
        self.list = async_to_raw_response_wrapper(
            job_categories.list,
        )


class JobCategoriesResourceWithStreamingResponse:
    def __init__(self, job_categories: JobCategoriesResource) -> None:
        self._job_categories = job_categories

        self.create = to_streamed_response_wrapper(
            job_categories.create,
        )
        self.list = to_streamed_response_wrapper(
            job_categories.list,
        )


class AsyncJobCategoriesResourceWithStreamingResponse:
    def __init__(self, job_categories: AsyncJobCategoriesResource) -> None:
        self._job_categories = job_categories

        self.create = async_to_streamed_response_wrapper(
            job_categories.create,
        )
        self.list = async_to_streamed_response_wrapper(
            job_categories.list,
        )
