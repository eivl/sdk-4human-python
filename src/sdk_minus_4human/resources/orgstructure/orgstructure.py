# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .units import (
    UnitsResource,
    AsyncUnitsResource,
    UnitsResourceWithRawResponse,
    AsyncUnitsResourceWithRawResponse,
    UnitsResourceWithStreamingResponse,
    AsyncUnitsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .companies import (
    CompaniesResource,
    AsyncCompaniesResource,
    CompaniesResourceWithRawResponse,
    AsyncCompaniesResourceWithRawResponse,
    CompaniesResourceWithStreamingResponse,
    AsyncCompaniesResourceWithStreamingResponse,
)
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from .unit_types import (
    UnitTypesResource,
    AsyncUnitTypesResource,
    UnitTypesResourceWithRawResponse,
    AsyncUnitTypesResourceWithRawResponse,
    UnitTypesResourceWithStreamingResponse,
    AsyncUnitTypesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .units.units import UnitsResource, AsyncUnitsResource
from ..._base_client import (
    make_request_options,
)
from .companies.companies import CompaniesResource, AsyncCompaniesResource
from ...types.orgstructure_list_response import OrgstructureListResponse

__all__ = ["OrgstructureResource", "AsyncOrgstructureResource"]


class OrgstructureResource(SyncAPIResource):
    @cached_property
    def units(self) -> UnitsResource:
        return UnitsResource(self._client)

    @cached_property
    def companies(self) -> CompaniesResource:
        return CompaniesResource(self._client)

    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def unit_types(self) -> UnitTypesResource:
        return UnitTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgstructureResourceWithRawResponse:
        return OrgstructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgstructureResourceWithStreamingResponse:
        return OrgstructureResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgstructureListResponse:
        """Displays organization structure with all units and companies."""
        return self._get(
            "/orgstructure",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgstructureListResponse,
        )


class AsyncOrgstructureResource(AsyncAPIResource):
    @cached_property
    def units(self) -> AsyncUnitsResource:
        return AsyncUnitsResource(self._client)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        return AsyncCompaniesResource(self._client)

    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def unit_types(self) -> AsyncUnitTypesResource:
        return AsyncUnitTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgstructureResourceWithRawResponse:
        return AsyncOrgstructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgstructureResourceWithStreamingResponse:
        return AsyncOrgstructureResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgstructureListResponse:
        """Displays organization structure with all units and companies."""
        return await self._get(
            "/orgstructure",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgstructureListResponse,
        )


class OrgstructureResourceWithRawResponse:
    def __init__(self, orgstructure: OrgstructureResource) -> None:
        self._orgstructure = orgstructure

        self.list = to_raw_response_wrapper(
            orgstructure.list,
        )

    @cached_property
    def units(self) -> UnitsResourceWithRawResponse:
        return UnitsResourceWithRawResponse(self._orgstructure.units)

    @cached_property
    def companies(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self._orgstructure.companies)

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._orgstructure.locations)

    @cached_property
    def unit_types(self) -> UnitTypesResourceWithRawResponse:
        return UnitTypesResourceWithRawResponse(self._orgstructure.unit_types)


class AsyncOrgstructureResourceWithRawResponse:
    def __init__(self, orgstructure: AsyncOrgstructureResource) -> None:
        self._orgstructure = orgstructure

        self.list = async_to_raw_response_wrapper(
            orgstructure.list,
        )

    @cached_property
    def units(self) -> AsyncUnitsResourceWithRawResponse:
        return AsyncUnitsResourceWithRawResponse(self._orgstructure.units)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self._orgstructure.companies)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._orgstructure.locations)

    @cached_property
    def unit_types(self) -> AsyncUnitTypesResourceWithRawResponse:
        return AsyncUnitTypesResourceWithRawResponse(self._orgstructure.unit_types)


class OrgstructureResourceWithStreamingResponse:
    def __init__(self, orgstructure: OrgstructureResource) -> None:
        self._orgstructure = orgstructure

        self.list = to_streamed_response_wrapper(
            orgstructure.list,
        )

    @cached_property
    def units(self) -> UnitsResourceWithStreamingResponse:
        return UnitsResourceWithStreamingResponse(self._orgstructure.units)

    @cached_property
    def companies(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self._orgstructure.companies)

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._orgstructure.locations)

    @cached_property
    def unit_types(self) -> UnitTypesResourceWithStreamingResponse:
        return UnitTypesResourceWithStreamingResponse(self._orgstructure.unit_types)


class AsyncOrgstructureResourceWithStreamingResponse:
    def __init__(self, orgstructure: AsyncOrgstructureResource) -> None:
        self._orgstructure = orgstructure

        self.list = async_to_streamed_response_wrapper(
            orgstructure.list,
        )

    @cached_property
    def units(self) -> AsyncUnitsResourceWithStreamingResponse:
        return AsyncUnitsResourceWithStreamingResponse(self._orgstructure.units)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self._orgstructure.companies)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._orgstructure.locations)

    @cached_property
    def unit_types(self) -> AsyncUnitTypesResourceWithStreamingResponse:
        return AsyncUnitTypesResourceWithStreamingResponse(self._orgstructure.unit_types)
