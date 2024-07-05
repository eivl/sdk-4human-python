# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from .changes import (
    ChangesResource,
    AsyncChangesResource,
    ChangesResourceWithRawResponse,
    AsyncChangesResourceWithRawResponse,
    ChangesResourceWithStreamingResponse,
    AsyncChangesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .custom_fields import (
    CustomFieldsResource,
    AsyncCustomFieldsResource,
    CustomFieldsResourceWithRawResponse,
    AsyncCustomFieldsResourceWithRawResponse,
    CustomFieldsResourceWithStreamingResponse,
    AsyncCustomFieldsResourceWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.orgstructure import (
    company_create_params,
    company_update_params,
    company_retrieve_params,
    company_update_field_params,
    company_update_locations_params,
)
from .custom_fields.custom_fields import CustomFieldsResource, AsyncCustomFieldsResource
from ....types.orgstructure.company_create_response import CompanyCreateResponse
from ....types.orgstructure.company_update_response import CompanyUpdateResponse
from ....types.orgstructure.company_retrieve_response import CompanyRetrieveResponse
from ....types.orgstructure.company_update_field_response import CompanyUpdateFieldResponse
from ....types.orgstructure.company_update_locations_response import CompanyUpdateLocationsResponse

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def custom_fields(self) -> CustomFieldsResource:
        return CustomFieldsResource(self._client)

    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_country: str,
        manager_id: int,
        organization_number: str,
        unit_type_id: str,
        approval_policy: Literal["noPolicy", "confirmation", "approvalAndConfirmation"] | NotGiven = NOT_GIVEN,
        candidate_approval_policy: Literal["none", "candidateApproval", "candidateWithoutApproval"]
        | NotGiven = NOT_GIVEN,
        company_logo_url: Optional[str] | NotGiven = NOT_GIVEN,
        locations: Optional[Iterable[company_create_params.Location]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        post_address: Optional[company_create_params.PostAddress] | NotGiven = NOT_GIVEN,
        salary_system_company_id: Optional[str] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        unit_id: Optional[str] | NotGiven = NOT_GIVEN,
        visit_address: company_create_params.VisitAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyCreateResponse:
        """
        Adding organization unit type company.

        Args:
          company_country: ISO 3166-1 alpha-3 country code

          manager_id: database id of unit manager.

          organization_number: For NOR country passing organizationNumber is not allowed as its fetched from
              Brreg

          locations: For NOR country locations is not allowed as they are fetched from Brreg and
              should be null.

          name: For NOR country passing name is not allowed as its fetched from Brreg

          post_address: For NOR country postAddress is not allowed as is fetched from Brreg and should
              be null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/orgstructure/companies",
            body=maybe_transform(
                {
                    "company_country": company_country,
                    "manager_id": manager_id,
                    "organization_number": organization_number,
                    "unit_type_id": unit_type_id,
                    "approval_policy": approval_policy,
                    "candidate_approval_policy": candidate_approval_policy,
                    "company_logo_url": company_logo_url,
                    "locations": locations,
                    "name": name,
                    "parent_id": parent_id,
                    "post_address": post_address,
                    "salary_system_company_id": salary_system_company_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "unit_id": unit_id,
                    "visit_address": visit_address,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyCreateResponse,
        )

    def retrieve(
        self,
        company_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        on_given_date: str | NotGiven = NOT_GIVEN,
        with_soft_deleted: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRetrieveResponse:
        """
        Get details about organization unit type company based on company id.

        Args:
          external: Param determines if id of unit is external (unitId) or internal (id)

          on_given_date: Param allows you to specify effective date of company employee data.

          with_soft_deleted: Param determines if deleted company should be fetched

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/orgstructure/companies/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external": external,
                        "on_given_date": on_given_date,
                        "with_soft_deleted": with_soft_deleted,
                    },
                    company_retrieve_params.CompanyRetrieveParams,
                ),
            ),
            cast_to=CompanyRetrieveResponse,
        )

    def update(
        self,
        company_id: str,
        *,
        manager_id: int,
        organization_number: str,
        unit_id: str,
        unit_type_id: str,
        external: bool | NotGiven = NOT_GIVEN,
        approval_policy: Literal["noPolicy", "confirmation", "approvalAndConfirmation"] | NotGiven = NOT_GIVEN,
        candidate_approval_policy: Literal["none", "candidateApproval", "candidateWithoutApproval"]
        | NotGiven = NOT_GIVEN,
        company_logo_url: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[company_update_params.CustomField] | NotGiven = NOT_GIVEN,
        locations: Optional[Iterable[company_update_params.Location]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        post_address: Optional[company_update_params.PostAddress] | NotGiven = NOT_GIVEN,
        ready_for_payment_message: Optional[str] | NotGiven = NOT_GIVEN,
        salary_system_company_id: Optional[str] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        visit_address: Optional[company_update_params.VisitAddress] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyUpdateResponse:
        """
        Endpoint for editing company data by company id.

        Args:
          external: Param determines if id of unit is external (unitId) or internal (id)

          locations: For NOR country passing locations is not allowed as they are fetched from Brreg.

          name: For NOR country passing name is not allowed as its fetched from Brreg

          post_address: For NOR country passing pody is not allowed as they are fetched from Brreg.

          visit_address: For NOR country visitAddress is not allowed as is fetched from Brreg and should
              be null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._put(
            f"/orgstructure/companies/{company_id}",
            body=maybe_transform(
                {
                    "manager_id": manager_id,
                    "organization_number": organization_number,
                    "unit_id": unit_id,
                    "unit_type_id": unit_type_id,
                    "approval_policy": approval_policy,
                    "candidate_approval_policy": candidate_approval_policy,
                    "company_logo_url": company_logo_url,
                    "custom_fields": custom_fields,
                    "locations": locations,
                    "name": name,
                    "parent_id": parent_id,
                    "post_address": post_address,
                    "ready_for_payment_message": ready_for_payment_message,
                    "salary_system_company_id": salary_system_company_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "visit_address": visit_address,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"external": external}, company_update_params.CompanyUpdateParams),
            ),
            cast_to=CompanyUpdateResponse,
        )

    def update_field(
        self,
        company_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        company_logo_url: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[company_update_field_params.CustomField] | NotGiven = NOT_GIVEN,
        locations: Optional[Iterable[company_update_field_params.Location]] | NotGiven = NOT_GIVEN,
        manager_id: int | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        organization_number: str | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        post_address: Optional[company_update_field_params.PostAddress] | NotGiven = NOT_GIVEN,
        ready_for_payment_message: Optional[str] | NotGiven = NOT_GIVEN,
        salary_system_company_id: Optional[str] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        unit_id: str | NotGiven = NOT_GIVEN,
        unit_type_id: str | NotGiven = NOT_GIVEN,
        visit_address: Optional[company_update_field_params.VisitAddress] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyUpdateFieldResponse:
        """
        Update only single field of company base on company id

        Args:
          external: Param determines if id of unit is external (unitId) or internal (id)

          locations: For NOR country passing locations is not allowed as they are fetched from Brreg.

          name: For NOR country passing name is not allowed as its fetched from Brreg

          post_address: For NOR country passing postAddress is not allowed as is fetched from Brreg.

          visit_address: For NOR country visitAddress is not allowed as is fetched from Brreg and should
              be null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._patch(
            f"/orgstructure/companies/{company_id}",
            body=maybe_transform(
                {
                    "company_logo_url": company_logo_url,
                    "custom_fields": custom_fields,
                    "locations": locations,
                    "manager_id": manager_id,
                    "name": name,
                    "organization_number": organization_number,
                    "parent_id": parent_id,
                    "post_address": post_address,
                    "ready_for_payment_message": ready_for_payment_message,
                    "salary_system_company_id": salary_system_company_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "unit_id": unit_id,
                    "unit_type_id": unit_type_id,
                    "visit_address": visit_address,
                },
                company_update_field_params.CompanyUpdateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"external": external}, company_update_field_params.CompanyUpdateFieldParams),
            ),
            cast_to=CompanyUpdateFieldResponse,
        )

    def update_locations(
        self,
        company_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyUpdateLocationsResponse:
        """
        Updating company location data from Brreg based on company id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._patch(
            f"/orgstructure/companies/{company_id}/update-locations",
            body=maybe_transform(body, company_update_locations_params.CompanyUpdateLocationsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyUpdateLocationsResponse,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResource:
        return AsyncCustomFieldsResource(self._client)

    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_country: str,
        manager_id: int,
        organization_number: str,
        unit_type_id: str,
        approval_policy: Literal["noPolicy", "confirmation", "approvalAndConfirmation"] | NotGiven = NOT_GIVEN,
        candidate_approval_policy: Literal["none", "candidateApproval", "candidateWithoutApproval"]
        | NotGiven = NOT_GIVEN,
        company_logo_url: Optional[str] | NotGiven = NOT_GIVEN,
        locations: Optional[Iterable[company_create_params.Location]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        post_address: Optional[company_create_params.PostAddress] | NotGiven = NOT_GIVEN,
        salary_system_company_id: Optional[str] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        unit_id: Optional[str] | NotGiven = NOT_GIVEN,
        visit_address: company_create_params.VisitAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyCreateResponse:
        """
        Adding organization unit type company.

        Args:
          company_country: ISO 3166-1 alpha-3 country code

          manager_id: database id of unit manager.

          organization_number: For NOR country passing organizationNumber is not allowed as its fetched from
              Brreg

          locations: For NOR country locations is not allowed as they are fetched from Brreg and
              should be null.

          name: For NOR country passing name is not allowed as its fetched from Brreg

          post_address: For NOR country postAddress is not allowed as is fetched from Brreg and should
              be null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/orgstructure/companies",
            body=await async_maybe_transform(
                {
                    "company_country": company_country,
                    "manager_id": manager_id,
                    "organization_number": organization_number,
                    "unit_type_id": unit_type_id,
                    "approval_policy": approval_policy,
                    "candidate_approval_policy": candidate_approval_policy,
                    "company_logo_url": company_logo_url,
                    "locations": locations,
                    "name": name,
                    "parent_id": parent_id,
                    "post_address": post_address,
                    "salary_system_company_id": salary_system_company_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "unit_id": unit_id,
                    "visit_address": visit_address,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyCreateResponse,
        )

    async def retrieve(
        self,
        company_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        on_given_date: str | NotGiven = NOT_GIVEN,
        with_soft_deleted: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRetrieveResponse:
        """
        Get details about organization unit type company based on company id.

        Args:
          external: Param determines if id of unit is external (unitId) or internal (id)

          on_given_date: Param allows you to specify effective date of company employee data.

          with_soft_deleted: Param determines if deleted company should be fetched

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/orgstructure/companies/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external": external,
                        "on_given_date": on_given_date,
                        "with_soft_deleted": with_soft_deleted,
                    },
                    company_retrieve_params.CompanyRetrieveParams,
                ),
            ),
            cast_to=CompanyRetrieveResponse,
        )

    async def update(
        self,
        company_id: str,
        *,
        manager_id: int,
        organization_number: str,
        unit_id: str,
        unit_type_id: str,
        external: bool | NotGiven = NOT_GIVEN,
        approval_policy: Literal["noPolicy", "confirmation", "approvalAndConfirmation"] | NotGiven = NOT_GIVEN,
        candidate_approval_policy: Literal["none", "candidateApproval", "candidateWithoutApproval"]
        | NotGiven = NOT_GIVEN,
        company_logo_url: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[company_update_params.CustomField] | NotGiven = NOT_GIVEN,
        locations: Optional[Iterable[company_update_params.Location]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        post_address: Optional[company_update_params.PostAddress] | NotGiven = NOT_GIVEN,
        ready_for_payment_message: Optional[str] | NotGiven = NOT_GIVEN,
        salary_system_company_id: Optional[str] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        visit_address: Optional[company_update_params.VisitAddress] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyUpdateResponse:
        """
        Endpoint for editing company data by company id.

        Args:
          external: Param determines if id of unit is external (unitId) or internal (id)

          locations: For NOR country passing locations is not allowed as they are fetched from Brreg.

          name: For NOR country passing name is not allowed as its fetched from Brreg

          post_address: For NOR country passing pody is not allowed as they are fetched from Brreg.

          visit_address: For NOR country visitAddress is not allowed as is fetched from Brreg and should
              be null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._put(
            f"/orgstructure/companies/{company_id}",
            body=await async_maybe_transform(
                {
                    "manager_id": manager_id,
                    "organization_number": organization_number,
                    "unit_id": unit_id,
                    "unit_type_id": unit_type_id,
                    "approval_policy": approval_policy,
                    "candidate_approval_policy": candidate_approval_policy,
                    "company_logo_url": company_logo_url,
                    "custom_fields": custom_fields,
                    "locations": locations,
                    "name": name,
                    "parent_id": parent_id,
                    "post_address": post_address,
                    "ready_for_payment_message": ready_for_payment_message,
                    "salary_system_company_id": salary_system_company_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "visit_address": visit_address,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"external": external}, company_update_params.CompanyUpdateParams),
            ),
            cast_to=CompanyUpdateResponse,
        )

    async def update_field(
        self,
        company_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        company_logo_url: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[company_update_field_params.CustomField] | NotGiven = NOT_GIVEN,
        locations: Optional[Iterable[company_update_field_params.Location]] | NotGiven = NOT_GIVEN,
        manager_id: int | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        organization_number: str | NotGiven = NOT_GIVEN,
        parent_id: Optional[int] | NotGiven = NOT_GIVEN,
        post_address: Optional[company_update_field_params.PostAddress] | NotGiven = NOT_GIVEN,
        ready_for_payment_message: Optional[str] | NotGiven = NOT_GIVEN,
        salary_system_company_id: Optional[str] | NotGiven = NOT_GIVEN,
        selected_company_number: Optional[str] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        unit_id: str | NotGiven = NOT_GIVEN,
        unit_type_id: str | NotGiven = NOT_GIVEN,
        visit_address: Optional[company_update_field_params.VisitAddress] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyUpdateFieldResponse:
        """
        Update only single field of company base on company id

        Args:
          external: Param determines if id of unit is external (unitId) or internal (id)

          locations: For NOR country passing locations is not allowed as they are fetched from Brreg.

          name: For NOR country passing name is not allowed as its fetched from Brreg

          post_address: For NOR country passing postAddress is not allowed as is fetched from Brreg.

          visit_address: For NOR country visitAddress is not allowed as is fetched from Brreg and should
              be null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._patch(
            f"/orgstructure/companies/{company_id}",
            body=await async_maybe_transform(
                {
                    "company_logo_url": company_logo_url,
                    "custom_fields": custom_fields,
                    "locations": locations,
                    "manager_id": manager_id,
                    "name": name,
                    "organization_number": organization_number,
                    "parent_id": parent_id,
                    "post_address": post_address,
                    "ready_for_payment_message": ready_for_payment_message,
                    "salary_system_company_id": salary_system_company_id,
                    "selected_company_number": selected_company_number,
                    "status": status,
                    "unit_id": unit_id,
                    "unit_type_id": unit_type_id,
                    "visit_address": visit_address,
                },
                company_update_field_params.CompanyUpdateFieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"external": external}, company_update_field_params.CompanyUpdateFieldParams
                ),
            ),
            cast_to=CompanyUpdateFieldResponse,
        )

    async def update_locations(
        self,
        company_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyUpdateLocationsResponse:
        """
        Updating company location data from Brreg based on company id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._patch(
            f"/orgstructure/companies/{company_id}/update-locations",
            body=await async_maybe_transform(body, company_update_locations_params.CompanyUpdateLocationsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyUpdateLocationsResponse,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            companies.update,
        )
        self.update_field = to_raw_response_wrapper(
            companies.update_field,
        )
        self.update_locations = to_raw_response_wrapper(
            companies.update_locations,
        )

    @cached_property
    def custom_fields(self) -> CustomFieldsResourceWithRawResponse:
        return CustomFieldsResourceWithRawResponse(self._companies.custom_fields)

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._companies.locations)

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._companies.changes)


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            companies.update,
        )
        self.update_field = async_to_raw_response_wrapper(
            companies.update_field,
        )
        self.update_locations = async_to_raw_response_wrapper(
            companies.update_locations,
        )

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResourceWithRawResponse:
        return AsyncCustomFieldsResourceWithRawResponse(self._companies.custom_fields)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._companies.locations)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._companies.changes)


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            companies.update,
        )
        self.update_field = to_streamed_response_wrapper(
            companies.update_field,
        )
        self.update_locations = to_streamed_response_wrapper(
            companies.update_locations,
        )

    @cached_property
    def custom_fields(self) -> CustomFieldsResourceWithStreamingResponse:
        return CustomFieldsResourceWithStreamingResponse(self._companies.custom_fields)

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._companies.locations)

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._companies.changes)


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            companies.update,
        )
        self.update_field = async_to_streamed_response_wrapper(
            companies.update_field,
        )
        self.update_locations = async_to_streamed_response_wrapper(
            companies.update_locations,
        )

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResourceWithStreamingResponse:
        return AsyncCustomFieldsResourceWithStreamingResponse(self._companies.custom_fields)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._companies.locations)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._companies.changes)
