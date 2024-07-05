# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.orgstructure import location_list_params
from ...types.orgstructure.location_list_response import LocationListResponse

__all__ = ["LocationsResource", "AsyncLocationsResource"]


class LocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self)

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
    ) -> LocationListResponse:
        """Locations places connected with company.

        Places contains data like location
        name, company name, company country, company id. Each location have its own
        externalId. Locations for NOR country companies are fetched from
        [brreg.no](https://www.brreg.no). For non-norway companies you can define custom
        locations.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/orgstructure/locations",
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
                    location_list_params.LocationListParams,
                ),
            ),
            cast_to=LocationListResponse,
        )


class AsyncLocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self)

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
    ) -> LocationListResponse:
        """Locations places connected with company.

        Places contains data like location
        name, company name, company country, company id. Each location have its own
        externalId. Locations for NOR country companies are fetched from
        [brreg.no](https://www.brreg.no). For non-norway companies you can define custom
        locations.

        Args:
          limit: Number of records returned in one request

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/orgstructure/locations",
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
                    location_list_params.LocationListParams,
                ),
            ),
            cast_to=LocationListResponse,
        )


class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_raw_response_wrapper(
            locations.list,
        )


class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_raw_response_wrapper(
            locations.list,
        )


class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_streamed_response_wrapper(
            locations.list,
        )


class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_streamed_response_wrapper(
            locations.list,
        )
