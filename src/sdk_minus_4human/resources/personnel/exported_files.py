# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["ExportedFilesResource", "AsyncExportedFilesResource"]


class ExportedFilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportedFilesResourceWithRawResponse:
        return ExportedFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportedFilesResourceWithStreamingResponse:
        return ExportedFilesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        date: str,
        *,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """This endpoint allows to obtain file exported from external integration.

        For
        example SDWorx export generates dump of custom fields. Contact integration team
        to enable nightly export for given instance. Files wil be exported in CSV format
        in asynchronous nightly job (they must be generated before can be downloaded).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_name:
            raise ValueError(f"Expected a non-empty value for `file_name` but received {file_name!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            f"/personnel/exported-files/{file_name}/{date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncExportedFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportedFilesResourceWithRawResponse:
        return AsyncExportedFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportedFilesResourceWithStreamingResponse:
        return AsyncExportedFilesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        date: str,
        *,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """This endpoint allows to obtain file exported from external integration.

        For
        example SDWorx export generates dump of custom fields. Contact integration team
        to enable nightly export for given instance. Files wil be exported in CSV format
        in asynchronous nightly job (they must be generated before can be downloaded).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_name:
            raise ValueError(f"Expected a non-empty value for `file_name` but received {file_name!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            f"/personnel/exported-files/{file_name}/{date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ExportedFilesResourceWithRawResponse:
    def __init__(self, exported_files: ExportedFilesResource) -> None:
        self._exported_files = exported_files

        self.retrieve = to_raw_response_wrapper(
            exported_files.retrieve,
        )


class AsyncExportedFilesResourceWithRawResponse:
    def __init__(self, exported_files: AsyncExportedFilesResource) -> None:
        self._exported_files = exported_files

        self.retrieve = async_to_raw_response_wrapper(
            exported_files.retrieve,
        )


class ExportedFilesResourceWithStreamingResponse:
    def __init__(self, exported_files: ExportedFilesResource) -> None:
        self._exported_files = exported_files

        self.retrieve = to_streamed_response_wrapper(
            exported_files.retrieve,
        )


class AsyncExportedFilesResourceWithStreamingResponse:
    def __init__(self, exported_files: AsyncExportedFilesResource) -> None:
        self._exported_files = exported_files

        self.retrieve = async_to_streamed_response_wrapper(
            exported_files.retrieve,
        )
