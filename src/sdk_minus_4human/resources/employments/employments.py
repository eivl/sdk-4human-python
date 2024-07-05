# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import employment_update_params
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .elements import (
    ElementsResource,
    AsyncElementsResource,
    ElementsResourceWithRawResponse,
    AsyncElementsResourceWithRawResponse,
    ElementsResourceWithStreamingResponse,
    AsyncElementsResourceWithStreamingResponse,
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
from .salary_elements import (
    SalaryElementsResource,
    AsyncSalaryElementsResource,
    SalaryElementsResourceWithRawResponse,
    AsyncSalaryElementsResourceWithRawResponse,
    SalaryElementsResourceWithStreamingResponse,
    AsyncSalaryElementsResourceWithStreamingResponse,
)
from .custom_fields_by_name import (
    CustomFieldsByNameResource,
    AsyncCustomFieldsByNameResource,
    CustomFieldsByNameResourceWithRawResponse,
    AsyncCustomFieldsByNameResourceWithRawResponse,
    CustomFieldsByNameResourceWithStreamingResponse,
    AsyncCustomFieldsByNameResourceWithStreamingResponse,
)
from .salary_elements.salary_elements import SalaryElementsResource, AsyncSalaryElementsResource
from ...types.employment_update_response import EmploymentUpdateResponse

__all__ = ["EmploymentsResource", "AsyncEmploymentsResource"]


class EmploymentsResource(SyncAPIResource):
    @cached_property
    def custom_fields_by_name(self) -> CustomFieldsByNameResource:
        return CustomFieldsByNameResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def elements(self) -> ElementsResource:
        return ElementsResource(self._client)

    @cached_property
    def salary_elements(self) -> SalaryElementsResource:
        return SalaryElementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmploymentsResourceWithRawResponse:
        return EmploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmploymentsResourceWithStreamingResponse:
        return EmploymentsResourceWithStreamingResponse(self)

    def update(
        self,
        employment_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        additional_salaries: Iterable[employment_update_params.AdditionalSalary] | NotGiven = NOT_GIVEN,
        benefits: Iterable[employment_update_params.Benefit] | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        cost_place: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[employment_update_params.CustomField] | NotGiven = NOT_GIVEN,
        deductions: Iterable[employment_update_params.Deduction] | NotGiven = NOT_GIVEN,
        effective_dates: employment_update_params.EffectiveDates | NotGiven = NOT_GIVEN,
        employee_type_id: Optional[str] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        first_working_day: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        fte_factor: Optional[float] | NotGiven = NOT_GIVEN,
        hr_role_id: str | NotGiven = NOT_GIVEN,
        job_id: int | NotGiven = NOT_GIVEN,
        last_working_day: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        location: Optional[str] | NotGiven = NOT_GIVEN,
        main_salary: employment_update_params.MainSalary | NotGiven = NOT_GIVEN,
        main_workplace_id: Optional[str] | NotGiven = NOT_GIVEN,
        manager_id: Optional[int] | NotGiven = NOT_GIVEN,
        notice_period: Optional[str] | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        occupational_code: Optional[str] | NotGiven = NOT_GIVEN,
        org_unit_id: int | NotGiven = NOT_GIVEN,
        org_units_with_advanced_access: Iterable[int] | NotGiven = NOT_GIVEN,
        overtime_allowance: Optional[Literal["FIELD_OVERTIME_ALLOWANCE_YES", "FIELD_OVERTIME_ALLOWANCE_NO"]]
        | NotGiven = NOT_GIVEN,
        personal_job_description: Optional[str] | NotGiven = NOT_GIVEN,
        position_title: Optional[str] | NotGiven = NOT_GIVEN,
        present_fte_factor: Optional[float] | NotGiven = NOT_GIVEN,
        probation_period: Optional[str] | NotGiven = NOT_GIVEN,
        reason_for_employment: Optional[str] | NotGiven = NOT_GIVEN,
        salary_type: Optional[str] | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        substitute_for_employment: Optional[Iterable[employment_update_params.SubstituteForEmployment]]
        | NotGiven = NOT_GIVEN,
        working_hours_arrangement: Optional[str] | NotGiven = NOT_GIVEN,
        working_hours_per_week: Optional[float] | NotGiven = NOT_GIVEN,
        work_relation_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentUpdateResponse:
        """Only visible fields configured by field templates can be updated.

        Trying to
        update the not visible field will response with an error.<br /><br /> How to
        work with nested fields:

        - Main salary - `"mainSalary"`:
          - only provided fields will be updated
          - `"mainSalary: null"` - will set all nested fields to null (delete whole main
            salary)
        - Salary elements - `"additionalSalaries"`, `"benefits"`, `"deductions"`:
          - `"id": ...` - will update (or create if not exists) particular salary
            element
          - only provided fields will be updated
          - not listed salary element will not be deleted/updated (there is no possible
            to delete one item)
          - `"additionalSalaries: null"` - will delete all additional salaries
        - Custom fields - `"customFields"`:
          - `"fieldId": ...` - will update particular custom field
          - `"fieldId": ...` with `"valueId": null"` - will delete local value and start
            inheritance from company
          - not listed custom field will not be deleted/updated

        Args:
          external: Param determines if "employmentId" is external (field called "number") or
              internal (field called "id")

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          effective_dates: If effectiveDates are not provided, the changes will be immediate

          employee_type_id: database UUID for employee type

          end_date: If endDate field is provided, the startDate field must also be provided

          fte_factor: Decimal precision 0.00001

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          occupational_code: Use code only without name

          org_unit_id: database id of employment organisation unit.

          present_fte_factor: Decimal precision 0.00001

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employment_id:
            raise ValueError(f"Expected a non-empty value for `employment_id` but received {employment_id!r}")
        return self._patch(
            f"/personnel/employments/{employment_id}",
            body=maybe_transform(
                {
                    "additional_salaries": additional_salaries,
                    "benefits": benefits,
                    "comment": comment,
                    "cost_place": cost_place,
                    "custom_fields": custom_fields,
                    "deductions": deductions,
                    "effective_dates": effective_dates,
                    "employee_type_id": employee_type_id,
                    "end_date": end_date,
                    "external_id": external_id,
                    "first_working_day": first_working_day,
                    "fte_factor": fte_factor,
                    "hr_role_id": hr_role_id,
                    "job_id": job_id,
                    "last_working_day": last_working_day,
                    "location": location,
                    "main_salary": main_salary,
                    "main_workplace_id": main_workplace_id,
                    "manager_id": manager_id,
                    "notice_period": notice_period,
                    "number": number,
                    "occupational_code": occupational_code,
                    "org_unit_id": org_unit_id,
                    "org_units_with_advanced_access": org_units_with_advanced_access,
                    "overtime_allowance": overtime_allowance,
                    "personal_job_description": personal_job_description,
                    "position_title": position_title,
                    "present_fte_factor": present_fte_factor,
                    "probation_period": probation_period,
                    "reason_for_employment": reason_for_employment,
                    "salary_type": salary_type,
                    "start_date": start_date,
                    "substitute_for_employment": substitute_for_employment,
                    "working_hours_arrangement": working_hours_arrangement,
                    "working_hours_per_week": working_hours_per_week,
                    "work_relation_type": work_relation_type,
                },
                employment_update_params.EmploymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external": external,
                        "force_no_approval_policy": force_no_approval_policy,
                    },
                    employment_update_params.EmploymentUpdateParams,
                ),
            ),
            cast_to=EmploymentUpdateResponse,
        )


class AsyncEmploymentsResource(AsyncAPIResource):
    @cached_property
    def custom_fields_by_name(self) -> AsyncCustomFieldsByNameResource:
        return AsyncCustomFieldsByNameResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def elements(self) -> AsyncElementsResource:
        return AsyncElementsResource(self._client)

    @cached_property
    def salary_elements(self) -> AsyncSalaryElementsResource:
        return AsyncSalaryElementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmploymentsResourceWithRawResponse:
        return AsyncEmploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmploymentsResourceWithStreamingResponse:
        return AsyncEmploymentsResourceWithStreamingResponse(self)

    async def update(
        self,
        employment_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        additional_salaries: Iterable[employment_update_params.AdditionalSalary] | NotGiven = NOT_GIVEN,
        benefits: Iterable[employment_update_params.Benefit] | NotGiven = NOT_GIVEN,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        cost_place: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[employment_update_params.CustomField] | NotGiven = NOT_GIVEN,
        deductions: Iterable[employment_update_params.Deduction] | NotGiven = NOT_GIVEN,
        effective_dates: employment_update_params.EffectiveDates | NotGiven = NOT_GIVEN,
        employee_type_id: Optional[str] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        first_working_day: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        fte_factor: Optional[float] | NotGiven = NOT_GIVEN,
        hr_role_id: str | NotGiven = NOT_GIVEN,
        job_id: int | NotGiven = NOT_GIVEN,
        last_working_day: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        location: Optional[str] | NotGiven = NOT_GIVEN,
        main_salary: employment_update_params.MainSalary | NotGiven = NOT_GIVEN,
        main_workplace_id: Optional[str] | NotGiven = NOT_GIVEN,
        manager_id: Optional[int] | NotGiven = NOT_GIVEN,
        notice_period: Optional[str] | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        occupational_code: Optional[str] | NotGiven = NOT_GIVEN,
        org_unit_id: int | NotGiven = NOT_GIVEN,
        org_units_with_advanced_access: Iterable[int] | NotGiven = NOT_GIVEN,
        overtime_allowance: Optional[Literal["FIELD_OVERTIME_ALLOWANCE_YES", "FIELD_OVERTIME_ALLOWANCE_NO"]]
        | NotGiven = NOT_GIVEN,
        personal_job_description: Optional[str] | NotGiven = NOT_GIVEN,
        position_title: Optional[str] | NotGiven = NOT_GIVEN,
        present_fte_factor: Optional[float] | NotGiven = NOT_GIVEN,
        probation_period: Optional[str] | NotGiven = NOT_GIVEN,
        reason_for_employment: Optional[str] | NotGiven = NOT_GIVEN,
        salary_type: Optional[str] | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        substitute_for_employment: Optional[Iterable[employment_update_params.SubstituteForEmployment]]
        | NotGiven = NOT_GIVEN,
        working_hours_arrangement: Optional[str] | NotGiven = NOT_GIVEN,
        working_hours_per_week: Optional[float] | NotGiven = NOT_GIVEN,
        work_relation_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentUpdateResponse:
        """Only visible fields configured by field templates can be updated.

        Trying to
        update the not visible field will response with an error.<br /><br /> How to
        work with nested fields:

        - Main salary - `"mainSalary"`:
          - only provided fields will be updated
          - `"mainSalary: null"` - will set all nested fields to null (delete whole main
            salary)
        - Salary elements - `"additionalSalaries"`, `"benefits"`, `"deductions"`:
          - `"id": ...` - will update (or create if not exists) particular salary
            element
          - only provided fields will be updated
          - not listed salary element will not be deleted/updated (there is no possible
            to delete one item)
          - `"additionalSalaries: null"` - will delete all additional salaries
        - Custom fields - `"customFields"`:
          - `"fieldId": ...` - will update particular custom field
          - `"fieldId": ...` with `"valueId": null"` - will delete local value and start
            inheritance from company
          - not listed custom field will not be deleted/updated

        Args:
          external: Param determines if "employmentId" is external (field called "number") or
              internal (field called "id")

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          effective_dates: If effectiveDates are not provided, the changes will be immediate

          employee_type_id: database UUID for employee type

          end_date: If endDate field is provided, the startDate field must also be provided

          fte_factor: Decimal precision 0.00001

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          occupational_code: Use code only without name

          org_unit_id: database id of employment organisation unit.

          present_fte_factor: Decimal precision 0.00001

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employment_id:
            raise ValueError(f"Expected a non-empty value for `employment_id` but received {employment_id!r}")
        return await self._patch(
            f"/personnel/employments/{employment_id}",
            body=await async_maybe_transform(
                {
                    "additional_salaries": additional_salaries,
                    "benefits": benefits,
                    "comment": comment,
                    "cost_place": cost_place,
                    "custom_fields": custom_fields,
                    "deductions": deductions,
                    "effective_dates": effective_dates,
                    "employee_type_id": employee_type_id,
                    "end_date": end_date,
                    "external_id": external_id,
                    "first_working_day": first_working_day,
                    "fte_factor": fte_factor,
                    "hr_role_id": hr_role_id,
                    "job_id": job_id,
                    "last_working_day": last_working_day,
                    "location": location,
                    "main_salary": main_salary,
                    "main_workplace_id": main_workplace_id,
                    "manager_id": manager_id,
                    "notice_period": notice_period,
                    "number": number,
                    "occupational_code": occupational_code,
                    "org_unit_id": org_unit_id,
                    "org_units_with_advanced_access": org_units_with_advanced_access,
                    "overtime_allowance": overtime_allowance,
                    "personal_job_description": personal_job_description,
                    "position_title": position_title,
                    "present_fte_factor": present_fte_factor,
                    "probation_period": probation_period,
                    "reason_for_employment": reason_for_employment,
                    "salary_type": salary_type,
                    "start_date": start_date,
                    "substitute_for_employment": substitute_for_employment,
                    "working_hours_arrangement": working_hours_arrangement,
                    "working_hours_per_week": working_hours_per_week,
                    "work_relation_type": work_relation_type,
                },
                employment_update_params.EmploymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external": external,
                        "force_no_approval_policy": force_no_approval_policy,
                    },
                    employment_update_params.EmploymentUpdateParams,
                ),
            ),
            cast_to=EmploymentUpdateResponse,
        )


class EmploymentsResourceWithRawResponse:
    def __init__(self, employments: EmploymentsResource) -> None:
        self._employments = employments

        self.update = to_raw_response_wrapper(
            employments.update,
        )

    @cached_property
    def custom_fields_by_name(self) -> CustomFieldsByNameResourceWithRawResponse:
        return CustomFieldsByNameResourceWithRawResponse(self._employments.custom_fields_by_name)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._employments.history)

    @cached_property
    def elements(self) -> ElementsResourceWithRawResponse:
        return ElementsResourceWithRawResponse(self._employments.elements)

    @cached_property
    def salary_elements(self) -> SalaryElementsResourceWithRawResponse:
        return SalaryElementsResourceWithRawResponse(self._employments.salary_elements)


class AsyncEmploymentsResourceWithRawResponse:
    def __init__(self, employments: AsyncEmploymentsResource) -> None:
        self._employments = employments

        self.update = async_to_raw_response_wrapper(
            employments.update,
        )

    @cached_property
    def custom_fields_by_name(self) -> AsyncCustomFieldsByNameResourceWithRawResponse:
        return AsyncCustomFieldsByNameResourceWithRawResponse(self._employments.custom_fields_by_name)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._employments.history)

    @cached_property
    def elements(self) -> AsyncElementsResourceWithRawResponse:
        return AsyncElementsResourceWithRawResponse(self._employments.elements)

    @cached_property
    def salary_elements(self) -> AsyncSalaryElementsResourceWithRawResponse:
        return AsyncSalaryElementsResourceWithRawResponse(self._employments.salary_elements)


class EmploymentsResourceWithStreamingResponse:
    def __init__(self, employments: EmploymentsResource) -> None:
        self._employments = employments

        self.update = to_streamed_response_wrapper(
            employments.update,
        )

    @cached_property
    def custom_fields_by_name(self) -> CustomFieldsByNameResourceWithStreamingResponse:
        return CustomFieldsByNameResourceWithStreamingResponse(self._employments.custom_fields_by_name)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._employments.history)

    @cached_property
    def elements(self) -> ElementsResourceWithStreamingResponse:
        return ElementsResourceWithStreamingResponse(self._employments.elements)

    @cached_property
    def salary_elements(self) -> SalaryElementsResourceWithStreamingResponse:
        return SalaryElementsResourceWithStreamingResponse(self._employments.salary_elements)


class AsyncEmploymentsResourceWithStreamingResponse:
    def __init__(self, employments: AsyncEmploymentsResource) -> None:
        self._employments = employments

        self.update = async_to_streamed_response_wrapper(
            employments.update,
        )

    @cached_property
    def custom_fields_by_name(self) -> AsyncCustomFieldsByNameResourceWithStreamingResponse:
        return AsyncCustomFieldsByNameResourceWithStreamingResponse(self._employments.custom_fields_by_name)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._employments.history)

    @cached_property
    def elements(self) -> AsyncElementsResourceWithStreamingResponse:
        return AsyncElementsResourceWithStreamingResponse(self._employments.elements)

    @cached_property
    def salary_elements(self) -> AsyncSalaryElementsResourceWithStreamingResponse:
        return AsyncSalaryElementsResourceWithStreamingResponse(self._employments.salary_elements)
