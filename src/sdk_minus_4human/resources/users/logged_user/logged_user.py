# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .details import (
    DetailsResource,
    AsyncDetailsResource,
    DetailsResourceWithRawResponse,
    AsyncDetailsResourceWithRawResponse,
    DetailsResourceWithStreamingResponse,
    AsyncDetailsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LoggedUserResource", "AsyncLoggedUserResource"]


class LoggedUserResource(SyncAPIResource):
    @cached_property
    def details(self) -> DetailsResource:
        return DetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LoggedUserResourceWithRawResponse:
        return LoggedUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoggedUserResourceWithStreamingResponse:
        return LoggedUserResourceWithStreamingResponse(self)


class AsyncLoggedUserResource(AsyncAPIResource):
    @cached_property
    def details(self) -> AsyncDetailsResource:
        return AsyncDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoggedUserResourceWithRawResponse:
        return AsyncLoggedUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoggedUserResourceWithStreamingResponse:
        return AsyncLoggedUserResourceWithStreamingResponse(self)


class LoggedUserResourceWithRawResponse:
    def __init__(self, logged_user: LoggedUserResource) -> None:
        self._logged_user = logged_user

    @cached_property
    def details(self) -> DetailsResourceWithRawResponse:
        return DetailsResourceWithRawResponse(self._logged_user.details)


class AsyncLoggedUserResourceWithRawResponse:
    def __init__(self, logged_user: AsyncLoggedUserResource) -> None:
        self._logged_user = logged_user

    @cached_property
    def details(self) -> AsyncDetailsResourceWithRawResponse:
        return AsyncDetailsResourceWithRawResponse(self._logged_user.details)


class LoggedUserResourceWithStreamingResponse:
    def __init__(self, logged_user: LoggedUserResource) -> None:
        self._logged_user = logged_user

    @cached_property
    def details(self) -> DetailsResourceWithStreamingResponse:
        return DetailsResourceWithStreamingResponse(self._logged_user.details)


class AsyncLoggedUserResourceWithStreamingResponse:
    def __init__(self, logged_user: AsyncLoggedUserResource) -> None:
        self._logged_user = logged_user

    @cached_property
    def details(self) -> AsyncDetailsResourceWithStreamingResponse:
        return AsyncDetailsResourceWithStreamingResponse(self._logged_user.details)
