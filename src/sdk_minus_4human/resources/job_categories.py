# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import job_category_status_params, job_category_update_params
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
from ..types.job_category_status_response import JobCategoryStatusResponse
from ..types.job_category_update_response import JobCategoryUpdateResponse
from ..types.job_category_retrieve_response import JobCategoryRetrieveResponse

__all__ = ["JobCategoriesResource", "AsyncJobCategoriesResource"]


class JobCategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobCategoriesResourceWithRawResponse:
        return JobCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobCategoriesResourceWithStreamingResponse:
        return JobCategoriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        job_category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCategoryRetrieveResponse:
        """
        This endpoint allows to get a single job category by its internal 4human's ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_category_id:
            raise ValueError(f"Expected a non-empty value for `job_category_id` but received {job_category_id!r}")
        return self._get(
            f"/personnel/job-categories/{job_category_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCategoryRetrieveResponse,
        )

    def update(
        self,
        job_category_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCategoryUpdateResponse:
        """
        This endpoint allows to update a particular fields of job category object by its
        internal 4human's ID. In order to update `status` field please use the other
        PATCH endpoint dedicated for status field.

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
        if not job_category_id:
            raise ValueError(f"Expected a non-empty value for `job_category_id` but received {job_category_id!r}")
        return self._patch(
            f"/personnel/job-categories/{job_category_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "name": name,
                },
                job_category_update_params.JobCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCategoryUpdateResponse,
        )

    def status(
        self,
        job_category_id: str,
        *,
        status: Literal["active", "inactive", "archived"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCategoryStatusResponse:
        """
        This endpoint allows to update only `status` field of job category object by its
        internal 4human's ID.

        Args:
          status: Job category status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_category_id:
            raise ValueError(f"Expected a non-empty value for `job_category_id` but received {job_category_id!r}")
        return self._patch(
            f"/personnel/job-categories/{job_category_id}/status",
            body=maybe_transform({"status": status}, job_category_status_params.JobCategoryStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCategoryStatusResponse,
        )


class AsyncJobCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobCategoriesResourceWithRawResponse:
        return AsyncJobCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobCategoriesResourceWithStreamingResponse:
        return AsyncJobCategoriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        job_category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCategoryRetrieveResponse:
        """
        This endpoint allows to get a single job category by its internal 4human's ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_category_id:
            raise ValueError(f"Expected a non-empty value for `job_category_id` but received {job_category_id!r}")
        return await self._get(
            f"/personnel/job-categories/{job_category_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCategoryRetrieveResponse,
        )

    async def update(
        self,
        job_category_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        internal_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCategoryUpdateResponse:
        """
        This endpoint allows to update a particular fields of job category object by its
        internal 4human's ID. In order to update `status` field please use the other
        PATCH endpoint dedicated for status field.

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
        if not job_category_id:
            raise ValueError(f"Expected a non-empty value for `job_category_id` but received {job_category_id!r}")
        return await self._patch(
            f"/personnel/job-categories/{job_category_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "external_id": external_id,
                    "internal_id": internal_id,
                    "name": name,
                },
                job_category_update_params.JobCategoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCategoryUpdateResponse,
        )

    async def status(
        self,
        job_category_id: str,
        *,
        status: Literal["active", "inactive", "archived"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCategoryStatusResponse:
        """
        This endpoint allows to update only `status` field of job category object by its
        internal 4human's ID.

        Args:
          status: Job category status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_category_id:
            raise ValueError(f"Expected a non-empty value for `job_category_id` but received {job_category_id!r}")
        return await self._patch(
            f"/personnel/job-categories/{job_category_id}/status",
            body=await async_maybe_transform({"status": status}, job_category_status_params.JobCategoryStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCategoryStatusResponse,
        )


class JobCategoriesResourceWithRawResponse:
    def __init__(self, job_categories: JobCategoriesResource) -> None:
        self._job_categories = job_categories

        self.retrieve = to_raw_response_wrapper(
            job_categories.retrieve,
        )
        self.update = to_raw_response_wrapper(
            job_categories.update,
        )
        self.status = to_raw_response_wrapper(
            job_categories.status,
        )


class AsyncJobCategoriesResourceWithRawResponse:
    def __init__(self, job_categories: AsyncJobCategoriesResource) -> None:
        self._job_categories = job_categories

        self.retrieve = async_to_raw_response_wrapper(
            job_categories.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            job_categories.update,
        )
        self.status = async_to_raw_response_wrapper(
            job_categories.status,
        )


class JobCategoriesResourceWithStreamingResponse:
    def __init__(self, job_categories: JobCategoriesResource) -> None:
        self._job_categories = job_categories

        self.retrieve = to_streamed_response_wrapper(
            job_categories.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            job_categories.update,
        )
        self.status = to_streamed_response_wrapper(
            job_categories.status,
        )


class AsyncJobCategoriesResourceWithStreamingResponse:
    def __init__(self, job_categories: AsyncJobCategoriesResource) -> None:
        self._job_categories = job_categories

        self.retrieve = async_to_streamed_response_wrapper(
            job_categories.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            job_categories.update,
        )
        self.status = async_to_streamed_response_wrapper(
            job_categories.status,
        )
