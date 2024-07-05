# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
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
from ...types.personnel import (
    job_list_params,
    job_create_params,
    job_update_params,
    job_retrieve_params,
    job_update_fields_params,
)
from ...types.personnel.job_list_response import JobListResponse
from ...types.personnel.job_create_response import JobCreateResponse
from ...types.personnel.job_update_response import JobUpdateResponse
from ...types.personnel.job_retrieve_response import JobRetrieveResponse
from ...types.personnel.job_update_fields_response import JobUpdateFieldsResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        acl: Iterable[job_create_params.ACL],
        number: str,
        title: str,
        category_id: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        occupational_codes: Iterable[job_create_params.OccupationalCode] | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCreateResponse:
        """
        This endpoint allows to create a new job.<br /> The job can be assigned to job
        category. You can also define the permissions for which organization unit can be
        used and also define the occupational codes.

        Args:
          acl: Permissions definition

          number: Editable, unique external ID, allowing to store the ID of the client's system

          title: Job name

          category_id: Internal 4human's ID of job category to which job will be assigned

          description: Additional job description

          occupational_codes: The list of occupational codes. Occupational code consists of country code,
              numerical code and name. In this field only country and code are necessary, the
              name will be automatically fetch from occupational code catalog available under
              this link
              <a href="https://data.ssb.no/api/klass/v1/versions/683" target="_blank">https://data.ssb.no/api/klass/v1/versions/683</a>

          status: Job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/jobs",
            body=maybe_transform(
                {
                    "acl": acl,
                    "number": number,
                    "title": title,
                    "category_id": category_id,
                    "description": description,
                    "occupational_codes": occupational_codes,
                    "status": status,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCreateResponse,
        )

    def retrieve(
        self,
        job_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobRetrieveResponse:
        """
        This endpoint allows to get a single job by its internal 4human's ID or external
        ID.

        Args:
          external: Param determines if `jobId` parameter is provided as external ID (field called
              `number`) or internal 4human's ID (field called `id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/personnel/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"external": external}, job_retrieve_params.JobRetrieveParams),
            ),
            cast_to=JobRetrieveResponse,
        )

    def update(
        self,
        job_id: str,
        *,
        acl: Iterable[job_update_params.ACL],
        number: str,
        title: str,
        external: bool | NotGiven = NOT_GIVEN,
        category_id: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        occupational_codes: Iterable[job_update_params.OccupationalCode] | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobUpdateResponse:
        """
        This endpoint allows to update a whole object of single job by its internal
        4human's ID or external ID.

        Args:
          acl: Permissions definition

          number: Editable, unique external ID, allowing to store the ID of the client's system

          title: Job name

          external: Param determines if `jobId` parameter is provided as external ID (field called
              `number`) or internal 4human's ID (field called `id`)

          category_id: Internal 4human's ID of job category to which job will be assigned

          description: Additional job description

          occupational_codes: The list of occupational codes. Occupational code consists of country code,
              numerical code and name. In this field only country and code are necessary, the
              name will be automatically fetch from occupational code catalog available under
              this link
              <a href="https://data.ssb.no/api/klass/v1/versions/683" target="_blank">https://data.ssb.no/api/klass/v1/versions/683</a>

          status: Job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._put(
            f"/personnel/jobs/{job_id}",
            body=maybe_transform(
                {
                    "acl": acl,
                    "number": number,
                    "title": title,
                    "category_id": category_id,
                    "description": description,
                    "occupational_codes": occupational_codes,
                    "status": status,
                },
                job_update_params.JobUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"external": external}, job_update_params.JobUpdateParams),
            ),
            cast_to=JobUpdateResponse,
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
    ) -> JobListResponse:
        """
        This endpoint allows to get the paginated jobs list.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/jobs",
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
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    def update_fields(
        self,
        job_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        acl: Iterable[job_update_fields_params.ACL] | NotGiven = NOT_GIVEN,
        category_id: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        occupational_codes: Iterable[job_update_fields_params.OccupationalCode] | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobUpdateFieldsResponse:
        """
        This endpoint allows to update a particular fields of job object by its internal
        4human's ID or external ID.

        Args:
          external: Param determines if `jobId` parameter is provided as external ID (field called
              `number`) or internal 4human's ID (field called `id`)

          acl: Permissions definition

          category_id: Internal 4human's ID of job category to which job will be assigned

          description: Additional job description

          number: Editable, unique external ID, allowing to store the ID of the client's system

          occupational_codes: The list of occupational codes. Occupational code consists of country code,
              numerical code and name. In this field only country and code are necessary, the
              name will be automatically fetch from occupational code catalog available under
              this link
              <a href="https://data.ssb.no/api/klass/v1/versions/683" target="_blank">https://data.ssb.no/api/klass/v1/versions/683</a>

          status: Job status

          title: Job name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._patch(
            f"/personnel/jobs/{job_id}",
            body=maybe_transform(
                {
                    "acl": acl,
                    "category_id": category_id,
                    "description": description,
                    "number": number,
                    "occupational_codes": occupational_codes,
                    "status": status,
                    "title": title,
                },
                job_update_fields_params.JobUpdateFieldsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"external": external}, job_update_fields_params.JobUpdateFieldsParams),
            ),
            cast_to=JobUpdateFieldsResponse,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        acl: Iterable[job_create_params.ACL],
        number: str,
        title: str,
        category_id: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        occupational_codes: Iterable[job_create_params.OccupationalCode] | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCreateResponse:
        """
        This endpoint allows to create a new job.<br /> The job can be assigned to job
        category. You can also define the permissions for which organization unit can be
        used and also define the occupational codes.

        Args:
          acl: Permissions definition

          number: Editable, unique external ID, allowing to store the ID of the client's system

          title: Job name

          category_id: Internal 4human's ID of job category to which job will be assigned

          description: Additional job description

          occupational_codes: The list of occupational codes. Occupational code consists of country code,
              numerical code and name. In this field only country and code are necessary, the
              name will be automatically fetch from occupational code catalog available under
              this link
              <a href="https://data.ssb.no/api/klass/v1/versions/683" target="_blank">https://data.ssb.no/api/klass/v1/versions/683</a>

          status: Job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/jobs",
            body=await async_maybe_transform(
                {
                    "acl": acl,
                    "number": number,
                    "title": title,
                    "category_id": category_id,
                    "description": description,
                    "occupational_codes": occupational_codes,
                    "status": status,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCreateResponse,
        )

    async def retrieve(
        self,
        job_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobRetrieveResponse:
        """
        This endpoint allows to get a single job by its internal 4human's ID or external
        ID.

        Args:
          external: Param determines if `jobId` parameter is provided as external ID (field called
              `number`) or internal 4human's ID (field called `id`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/personnel/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"external": external}, job_retrieve_params.JobRetrieveParams),
            ),
            cast_to=JobRetrieveResponse,
        )

    async def update(
        self,
        job_id: str,
        *,
        acl: Iterable[job_update_params.ACL],
        number: str,
        title: str,
        external: bool | NotGiven = NOT_GIVEN,
        category_id: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        occupational_codes: Iterable[job_update_params.OccupationalCode] | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobUpdateResponse:
        """
        This endpoint allows to update a whole object of single job by its internal
        4human's ID or external ID.

        Args:
          acl: Permissions definition

          number: Editable, unique external ID, allowing to store the ID of the client's system

          title: Job name

          external: Param determines if `jobId` parameter is provided as external ID (field called
              `number`) or internal 4human's ID (field called `id`)

          category_id: Internal 4human's ID of job category to which job will be assigned

          description: Additional job description

          occupational_codes: The list of occupational codes. Occupational code consists of country code,
              numerical code and name. In this field only country and code are necessary, the
              name will be automatically fetch from occupational code catalog available under
              this link
              <a href="https://data.ssb.no/api/klass/v1/versions/683" target="_blank">https://data.ssb.no/api/klass/v1/versions/683</a>

          status: Job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._put(
            f"/personnel/jobs/{job_id}",
            body=await async_maybe_transform(
                {
                    "acl": acl,
                    "number": number,
                    "title": title,
                    "category_id": category_id,
                    "description": description,
                    "occupational_codes": occupational_codes,
                    "status": status,
                },
                job_update_params.JobUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"external": external}, job_update_params.JobUpdateParams),
            ),
            cast_to=JobUpdateResponse,
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
    ) -> JobListResponse:
        """
        This endpoint allows to get the paginated jobs list.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/jobs",
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
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    async def update_fields(
        self,
        job_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        acl: Iterable[job_update_fields_params.ACL] | NotGiven = NOT_GIVEN,
        category_id: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        occupational_codes: Iterable[job_update_fields_params.OccupationalCode] | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobUpdateFieldsResponse:
        """
        This endpoint allows to update a particular fields of job object by its internal
        4human's ID or external ID.

        Args:
          external: Param determines if `jobId` parameter is provided as external ID (field called
              `number`) or internal 4human's ID (field called `id`)

          acl: Permissions definition

          category_id: Internal 4human's ID of job category to which job will be assigned

          description: Additional job description

          number: Editable, unique external ID, allowing to store the ID of the client's system

          occupational_codes: The list of occupational codes. Occupational code consists of country code,
              numerical code and name. In this field only country and code are necessary, the
              name will be automatically fetch from occupational code catalog available under
              this link
              <a href="https://data.ssb.no/api/klass/v1/versions/683" target="_blank">https://data.ssb.no/api/klass/v1/versions/683</a>

          status: Job status

          title: Job name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._patch(
            f"/personnel/jobs/{job_id}",
            body=await async_maybe_transform(
                {
                    "acl": acl,
                    "category_id": category_id,
                    "description": description,
                    "number": number,
                    "occupational_codes": occupational_codes,
                    "status": status,
                    "title": title,
                },
                job_update_fields_params.JobUpdateFieldsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, job_update_fields_params.JobUpdateFieldsParams
                ),
            ),
            cast_to=JobUpdateFieldsResponse,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            jobs.update,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.update_fields = to_raw_response_wrapper(
            jobs.update_fields,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            jobs.update,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.update_fields = async_to_raw_response_wrapper(
            jobs.update_fields,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            jobs.update,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.update_fields = to_streamed_response_wrapper(
            jobs.update_fields,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            jobs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.update_fields = async_to_streamed_response_wrapper(
            jobs.update_fields,
        )
