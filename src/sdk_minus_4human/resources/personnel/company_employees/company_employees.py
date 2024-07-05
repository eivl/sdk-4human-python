# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .custom_fields_by_name import (
    CustomFieldsByNameResource,
    AsyncCustomFieldsByNameResource,
    CustomFieldsByNameResourceWithRawResponse,
    AsyncCustomFieldsByNameResourceWithRawResponse,
    CustomFieldsByNameResourceWithStreamingResponse,
    AsyncCustomFieldsByNameResourceWithStreamingResponse,
)

__all__ = ["CompanyEmployeesResource", "AsyncCompanyEmployeesResource"]


class CompanyEmployeesResource(SyncAPIResource):
    @cached_property
    def custom_fields_by_name(self) -> CustomFieldsByNameResource:
        return CustomFieldsByNameResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompanyEmployeesResourceWithRawResponse:
        return CompanyEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyEmployeesResourceWithStreamingResponse:
        return CompanyEmployeesResourceWithStreamingResponse(self)


class AsyncCompanyEmployeesResource(AsyncAPIResource):
    @cached_property
    def custom_fields_by_name(self) -> AsyncCustomFieldsByNameResource:
        return AsyncCustomFieldsByNameResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompanyEmployeesResourceWithRawResponse:
        return AsyncCompanyEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyEmployeesResourceWithStreamingResponse:
        return AsyncCompanyEmployeesResourceWithStreamingResponse(self)


class CompanyEmployeesResourceWithRawResponse:
    def __init__(self, company_employees: CompanyEmployeesResource) -> None:
        self._company_employees = company_employees

    @cached_property
    def custom_fields_by_name(self) -> CustomFieldsByNameResourceWithRawResponse:
        return CustomFieldsByNameResourceWithRawResponse(self._company_employees.custom_fields_by_name)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._company_employees.history)


class AsyncCompanyEmployeesResourceWithRawResponse:
    def __init__(self, company_employees: AsyncCompanyEmployeesResource) -> None:
        self._company_employees = company_employees

    @cached_property
    def custom_fields_by_name(self) -> AsyncCustomFieldsByNameResourceWithRawResponse:
        return AsyncCustomFieldsByNameResourceWithRawResponse(self._company_employees.custom_fields_by_name)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._company_employees.history)


class CompanyEmployeesResourceWithStreamingResponse:
    def __init__(self, company_employees: CompanyEmployeesResource) -> None:
        self._company_employees = company_employees

    @cached_property
    def custom_fields_by_name(self) -> CustomFieldsByNameResourceWithStreamingResponse:
        return CustomFieldsByNameResourceWithStreamingResponse(self._company_employees.custom_fields_by_name)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._company_employees.history)


class AsyncCompanyEmployeesResourceWithStreamingResponse:
    def __init__(self, company_employees: AsyncCompanyEmployeesResource) -> None:
        self._company_employees = company_employees

    @cached_property
    def custom_fields_by_name(self) -> AsyncCustomFieldsByNameResourceWithStreamingResponse:
        return AsyncCustomFieldsByNameResourceWithStreamingResponse(self._company_employees.custom_fields_by_name)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._company_employees.history)
