# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .formers import (
    FormersResource,
    AsyncFormersResource,
    FormersResourceWithRawResponse,
    AsyncFormersResourceWithRawResponse,
    FormersResourceWithStreamingResponse,
    AsyncFormersResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .configuration import (
    ConfigurationResource,
    AsyncConfigurationResource,
    ConfigurationResourceWithRawResponse,
    AsyncConfigurationResourceWithRawResponse,
    ConfigurationResourceWithStreamingResponse,
    AsyncConfigurationResourceWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.personnel import (
    employment_list_params,
    employment_create_params,
    employment_update_params,
    employment_retrieve_params,
)
from ....types.personnel.employment_list_response import EmploymentListResponse
from ....types.personnel.employment_create_response import EmploymentCreateResponse
from ....types.personnel.employment_update_response import EmploymentUpdateResponse
from ....types.personnel.employment_retrieve_response import EmploymentRetrieveResponse

__all__ = ["EmploymentsResource", "AsyncEmploymentsResource"]


class EmploymentsResource(SyncAPIResource):
    @cached_property
    def formers(self) -> FormersResource:
        return FormersResource(self._client)

    @cached_property
    def configuration(self) -> ConfigurationResource:
        return ConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmploymentsResourceWithRawResponse:
        return EmploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmploymentsResourceWithStreamingResponse:
        return EmploymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        employment: employment_create_params.Employment,
        personal_identification: employment_create_params.PersonalIdentification,
        user: employment_create_params.User,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        send_invitation: bool | NotGiven = NOT_GIVEN,
        company_employee: Optional[employment_create_params.CompanyEmployee] | NotGiven = NOT_GIVEN,
        personal_greetings: str | NotGiven = NOT_GIVEN,
        program_template_id: Optional[int] | NotGiven = NOT_GIVEN,
        reference_date: Optional[str] | NotGiven = NOT_GIVEN,
        task_template_changes: Optional[Iterable[employment_create_params.TaskTemplateChange]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentCreateResponse:
        """
        This endpoint allows to onboard (create) an employment (personnel employment).

        In 4human's structure employment is the last level of employee data. The levels
        are as follows:

        - user - representing a user of the platform, with personal data

        - company employee - representing the employee working in a given company;
          company is an organization unit with a flag "company"

        - personnel employment (employment) - representing a single employee's contract
          in a given company.

        One user may have multiple company employees and one company employee may have
        multiple employments.

        This endpoint allows to create a one-to-one-to-one structure - which means one
        user with one company employee and one employment.

        Since it's an onboarding endpoint it also allows to set up personal greetings
        and assign an initial program.

        Args:
          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          send_invitation: Determines if invitation email should be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/personnel/employments",
            body=maybe_transform(
                {
                    "employment": employment,
                    "personal_identification": personal_identification,
                    "user": user,
                    "company_employee": company_employee,
                    "personal_greetings": personal_greetings,
                    "program_template_id": program_template_id,
                    "reference_date": reference_date,
                    "task_template_changes": task_template_changes,
                },
                employment_create_params.EmploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "force_no_approval_policy": force_no_approval_policy,
                        "send_invitation": send_invitation,
                    },
                    employment_create_params.EmploymentCreateParams,
                ),
            ),
            cast_to=EmploymentCreateResponse,
        )

    def retrieve(
        self,
        employment_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        on_given_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentRetrieveResponse:
        """This endpoint allows to get the single employment details.

        The employment data
        are complex and are also including the higher levels of the employment structure
        (user and company employee). This endpoint also exposes some additional
        configuration like manager data, job details and custom fields assigned to a
        given employment.

        Please note that the employment object represents a single contract of a given
        employee.

        Args:
          external: Param determines if "employmentId" is external (field called "number") or
              internal (field called "id")

          on_given_date: Param allows you to specify effective date of employment data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employment_id:
            raise ValueError(f"Expected a non-empty value for `employment_id` but received {employment_id!r}")
        return self._get(
            f"/personnel/employments/{employment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external": external,
                        "on_given_date": on_given_date,
                    },
                    employment_retrieve_params.EmploymentRetrieveParams,
                ),
            ),
            cast_to=EmploymentRetrieveResponse,
        )

    def update(
        self,
        employment_id: str,
        *,
        comment: Optional[str],
        cost_place: Optional[str],
        custom_fields: Iterable[employment_update_params.CustomField],
        effective_dates: employment_update_params.EffectiveDates,
        employee_type_id: Optional[str],
        end_date: Optional[str],
        external_id: Optional[str],
        first_working_day: Union[str, datetime, None],
        fte_factor: Optional[float],
        hr_role_id: str,
        job_id: int,
        last_working_day: Union[str, datetime, None],
        main_workplace_id: Optional[str],
        manager_id: Optional[int],
        notice_period: Optional[str],
        number: str,
        occupational_code: Optional[str],
        org_unit_id: int,
        personal_job_description: Optional[str],
        position_title: Optional[str],
        present_fte_factor: Optional[float],
        probation_period: Optional[str],
        salary_seniority_date: Union[str, datetime, None],
        salary_type: Optional[str],
        start_date: str,
        working_hours_arrangement: Optional[str],
        working_hours_per_week: Optional[float],
        work_relation_type: Optional[str],
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        additional_salaries: Iterable[employment_update_params.AdditionalSalary] | NotGiven = NOT_GIVEN,
        benefits: Iterable[employment_update_params.Benefit] | NotGiven = NOT_GIVEN,
        deductions: Iterable[employment_update_params.Deduction] | NotGiven = NOT_GIVEN,
        main_salary: employment_update_params.MainSalary | NotGiven = NOT_GIVEN,
        overtime_allowance: Optional[Literal["FIELD_OVERTIME_ALLOWANCE_YES", "FIELD_OVERTIME_ALLOWANCE_NO"]]
        | NotGiven = NOT_GIVEN,
        reason_for_employment: Optional[str] | NotGiven = NOT_GIVEN,
        substitute_for_employment: Optional[Iterable[employment_update_params.SubstituteForEmployment]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentUpdateResponse:
        """Only available fields will be updated.

        If the field is hidden in an employee
        profile, it will be omitted.

        Args:
          fte_factor: Decimal precision 0.00001

          job_id: database internal id of job.

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          notice_period: concatenation of value + measurement unit units are first letter of time range
              (d - days, w -weeks, m - months, y - years) example value `2w` - two weeks

          number: The employment number serves as an external ID for employment (flag
              isExternal=true) and is used for lookups.

          occupational_code: Use code only without name

          org_unit_id: database id of employment organisation unit.

          present_fte_factor: Decimal precision 0.00001

          probation_period: concatenation of value + measurement unit units are first letter of time range
              (d - days, w -weeks, m - months, y - years) example value `2w` - two weeks

          external: Param determines if "employmentId" is external (field called "number") or
              internal (field called "id")

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employment_id:
            raise ValueError(f"Expected a non-empty value for `employment_id` but received {employment_id!r}")
        return self._put(
            f"/personnel/employments/{employment_id}",
            body=maybe_transform(
                {
                    "comment": comment,
                    "cost_place": cost_place,
                    "custom_fields": custom_fields,
                    "effective_dates": effective_dates,
                    "employee_type_id": employee_type_id,
                    "end_date": end_date,
                    "external_id": external_id,
                    "first_working_day": first_working_day,
                    "fte_factor": fte_factor,
                    "hr_role_id": hr_role_id,
                    "job_id": job_id,
                    "last_working_day": last_working_day,
                    "main_workplace_id": main_workplace_id,
                    "manager_id": manager_id,
                    "notice_period": notice_period,
                    "number": number,
                    "occupational_code": occupational_code,
                    "org_unit_id": org_unit_id,
                    "personal_job_description": personal_job_description,
                    "position_title": position_title,
                    "present_fte_factor": present_fte_factor,
                    "probation_period": probation_period,
                    "salary_seniority_date": salary_seniority_date,
                    "salary_type": salary_type,
                    "start_date": start_date,
                    "working_hours_arrangement": working_hours_arrangement,
                    "working_hours_per_week": working_hours_per_week,
                    "work_relation_type": work_relation_type,
                    "additional_salaries": additional_salaries,
                    "benefits": benefits,
                    "deductions": deductions,
                    "main_salary": main_salary,
                    "overtime_allowance": overtime_allowance,
                    "reason_for_employment": reason_for_employment,
                    "substitute_for_employment": substitute_for_employment,
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

    def list(
        self,
        *,
        employee_id: str | NotGiven = NOT_GIVEN,
        employment_id: str | NotGiven = NOT_GIVEN,
        external: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        organisation_number: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentListResponse:
        """
        This endpoints allows to get the full list of employments (personnel
        employments), paginated and filtered by employment ID (internal or external) or
        employee ID (company employee external ID - which means employeeID field in
        company employee object)

        Args:
          employee_id: This is an external identifier of a company employee ("employeeId" field in
              company employee object)

          employment_id: Employment ID which may be interpreted as internal ID (if external=false) or
              "number" field (if external=true)

          external: Param determines if "employmentId" is external (field called "number") or
              internal (field called "id")

          limit: Number of records returned in one request

          organisation_number: ID of the company fetched from [brreg.no](https://www.brreg.no) for norway or
              custom one for other countries

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/personnel/employments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "employee_id": employee_id,
                        "employment_id": employment_id,
                        "external": external,
                        "limit": limit,
                        "organisation_number": organisation_number,
                        "page": page,
                    },
                    employment_list_params.EmploymentListParams,
                ),
            ),
            cast_to=EmploymentListResponse,
        )


class AsyncEmploymentsResource(AsyncAPIResource):
    @cached_property
    def formers(self) -> AsyncFormersResource:
        return AsyncFormersResource(self._client)

    @cached_property
    def configuration(self) -> AsyncConfigurationResource:
        return AsyncConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmploymentsResourceWithRawResponse:
        return AsyncEmploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmploymentsResourceWithStreamingResponse:
        return AsyncEmploymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        employment: employment_create_params.Employment,
        personal_identification: employment_create_params.PersonalIdentification,
        user: employment_create_params.User,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        send_invitation: bool | NotGiven = NOT_GIVEN,
        company_employee: Optional[employment_create_params.CompanyEmployee] | NotGiven = NOT_GIVEN,
        personal_greetings: str | NotGiven = NOT_GIVEN,
        program_template_id: Optional[int] | NotGiven = NOT_GIVEN,
        reference_date: Optional[str] | NotGiven = NOT_GIVEN,
        task_template_changes: Optional[Iterable[employment_create_params.TaskTemplateChange]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentCreateResponse:
        """
        This endpoint allows to onboard (create) an employment (personnel employment).

        In 4human's structure employment is the last level of employee data. The levels
        are as follows:

        - user - representing a user of the platform, with personal data

        - company employee - representing the employee working in a given company;
          company is an organization unit with a flag "company"

        - personnel employment (employment) - representing a single employee's contract
          in a given company.

        One user may have multiple company employees and one company employee may have
        multiple employments.

        This endpoint allows to create a one-to-one-to-one structure - which means one
        user with one company employee and one employment.

        Since it's an onboarding endpoint it also allows to set up personal greetings
        and assign an initial program.

        Args:
          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          send_invitation: Determines if invitation email should be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/personnel/employments",
            body=await async_maybe_transform(
                {
                    "employment": employment,
                    "personal_identification": personal_identification,
                    "user": user,
                    "company_employee": company_employee,
                    "personal_greetings": personal_greetings,
                    "program_template_id": program_template_id,
                    "reference_date": reference_date,
                    "task_template_changes": task_template_changes,
                },
                employment_create_params.EmploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "force_no_approval_policy": force_no_approval_policy,
                        "send_invitation": send_invitation,
                    },
                    employment_create_params.EmploymentCreateParams,
                ),
            ),
            cast_to=EmploymentCreateResponse,
        )

    async def retrieve(
        self,
        employment_id: str,
        *,
        external: bool | NotGiven = NOT_GIVEN,
        on_given_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentRetrieveResponse:
        """This endpoint allows to get the single employment details.

        The employment data
        are complex and are also including the higher levels of the employment structure
        (user and company employee). This endpoint also exposes some additional
        configuration like manager data, job details and custom fields assigned to a
        given employment.

        Please note that the employment object represents a single contract of a given
        employee.

        Args:
          external: Param determines if "employmentId" is external (field called "number") or
              internal (field called "id")

          on_given_date: Param allows you to specify effective date of employment data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employment_id:
            raise ValueError(f"Expected a non-empty value for `employment_id` but received {employment_id!r}")
        return await self._get(
            f"/personnel/employments/{employment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external": external,
                        "on_given_date": on_given_date,
                    },
                    employment_retrieve_params.EmploymentRetrieveParams,
                ),
            ),
            cast_to=EmploymentRetrieveResponse,
        )

    async def update(
        self,
        employment_id: str,
        *,
        comment: Optional[str],
        cost_place: Optional[str],
        custom_fields: Iterable[employment_update_params.CustomField],
        effective_dates: employment_update_params.EffectiveDates,
        employee_type_id: Optional[str],
        end_date: Optional[str],
        external_id: Optional[str],
        first_working_day: Union[str, datetime, None],
        fte_factor: Optional[float],
        hr_role_id: str,
        job_id: int,
        last_working_day: Union[str, datetime, None],
        main_workplace_id: Optional[str],
        manager_id: Optional[int],
        notice_period: Optional[str],
        number: str,
        occupational_code: Optional[str],
        org_unit_id: int,
        personal_job_description: Optional[str],
        position_title: Optional[str],
        present_fte_factor: Optional[float],
        probation_period: Optional[str],
        salary_seniority_date: Union[str, datetime, None],
        salary_type: Optional[str],
        start_date: str,
        working_hours_arrangement: Optional[str],
        working_hours_per_week: Optional[float],
        work_relation_type: Optional[str],
        external: bool | NotGiven = NOT_GIVEN,
        force_no_approval_policy: bool | NotGiven = NOT_GIVEN,
        additional_salaries: Iterable[employment_update_params.AdditionalSalary] | NotGiven = NOT_GIVEN,
        benefits: Iterable[employment_update_params.Benefit] | NotGiven = NOT_GIVEN,
        deductions: Iterable[employment_update_params.Deduction] | NotGiven = NOT_GIVEN,
        main_salary: employment_update_params.MainSalary | NotGiven = NOT_GIVEN,
        overtime_allowance: Optional[Literal["FIELD_OVERTIME_ALLOWANCE_YES", "FIELD_OVERTIME_ALLOWANCE_NO"]]
        | NotGiven = NOT_GIVEN,
        reason_for_employment: Optional[str] | NotGiven = NOT_GIVEN,
        substitute_for_employment: Optional[Iterable[employment_update_params.SubstituteForEmployment]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentUpdateResponse:
        """Only available fields will be updated.

        If the field is hidden in an employee
        profile, it will be omitted.

        Args:
          fte_factor: Decimal precision 0.00001

          job_id: database internal id of job.

          manager_id: Manager ID which is in fact an employment ID (personnel employment ID)

          notice_period: concatenation of value + measurement unit units are first letter of time range
              (d - days, w -weeks, m - months, y - years) example value `2w` - two weeks

          number: The employment number serves as an external ID for employment (flag
              isExternal=true) and is used for lookups.

          occupational_code: Use code only without name

          org_unit_id: database id of employment organisation unit.

          present_fte_factor: Decimal precision 0.00001

          probation_period: concatenation of value + measurement unit units are first letter of time range
              (d - days, w -weeks, m - months, y - years) example value `2w` - two weeks

          external: Param determines if "employmentId" is external (field called "number") or
              internal (field called "id")

          force_no_approval_policy: Determines if changes should be made without approval (no confirmation snapshots
              will be created).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employment_id:
            raise ValueError(f"Expected a non-empty value for `employment_id` but received {employment_id!r}")
        return await self._put(
            f"/personnel/employments/{employment_id}",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "cost_place": cost_place,
                    "custom_fields": custom_fields,
                    "effective_dates": effective_dates,
                    "employee_type_id": employee_type_id,
                    "end_date": end_date,
                    "external_id": external_id,
                    "first_working_day": first_working_day,
                    "fte_factor": fte_factor,
                    "hr_role_id": hr_role_id,
                    "job_id": job_id,
                    "last_working_day": last_working_day,
                    "main_workplace_id": main_workplace_id,
                    "manager_id": manager_id,
                    "notice_period": notice_period,
                    "number": number,
                    "occupational_code": occupational_code,
                    "org_unit_id": org_unit_id,
                    "personal_job_description": personal_job_description,
                    "position_title": position_title,
                    "present_fte_factor": present_fte_factor,
                    "probation_period": probation_period,
                    "salary_seniority_date": salary_seniority_date,
                    "salary_type": salary_type,
                    "start_date": start_date,
                    "working_hours_arrangement": working_hours_arrangement,
                    "working_hours_per_week": working_hours_per_week,
                    "work_relation_type": work_relation_type,
                    "additional_salaries": additional_salaries,
                    "benefits": benefits,
                    "deductions": deductions,
                    "main_salary": main_salary,
                    "overtime_allowance": overtime_allowance,
                    "reason_for_employment": reason_for_employment,
                    "substitute_for_employment": substitute_for_employment,
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

    async def list(
        self,
        *,
        employee_id: str | NotGiven = NOT_GIVEN,
        employment_id: str | NotGiven = NOT_GIVEN,
        external: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        organisation_number: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentListResponse:
        """
        This endpoints allows to get the full list of employments (personnel
        employments), paginated and filtered by employment ID (internal or external) or
        employee ID (company employee external ID - which means employeeID field in
        company employee object)

        Args:
          employee_id: This is an external identifier of a company employee ("employeeId" field in
              company employee object)

          employment_id: Employment ID which may be interpreted as internal ID (if external=false) or
              "number" field (if external=true)

          external: Param determines if "employmentId" is external (field called "number") or
              internal (field called "id")

          limit: Number of records returned in one request

          organisation_number: ID of the company fetched from [brreg.no](https://www.brreg.no) for norway or
              custom one for other countries

          page: Number of returned page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/personnel/employments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "employee_id": employee_id,
                        "employment_id": employment_id,
                        "external": external,
                        "limit": limit,
                        "organisation_number": organisation_number,
                        "page": page,
                    },
                    employment_list_params.EmploymentListParams,
                ),
            ),
            cast_to=EmploymentListResponse,
        )


class EmploymentsResourceWithRawResponse:
    def __init__(self, employments: EmploymentsResource) -> None:
        self._employments = employments

        self.create = to_raw_response_wrapper(
            employments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            employments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employments.update,
        )
        self.list = to_raw_response_wrapper(
            employments.list,
        )

    @cached_property
    def formers(self) -> FormersResourceWithRawResponse:
        return FormersResourceWithRawResponse(self._employments.formers)

    @cached_property
    def configuration(self) -> ConfigurationResourceWithRawResponse:
        return ConfigurationResourceWithRawResponse(self._employments.configuration)


class AsyncEmploymentsResourceWithRawResponse:
    def __init__(self, employments: AsyncEmploymentsResource) -> None:
        self._employments = employments

        self.create = async_to_raw_response_wrapper(
            employments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            employments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employments.update,
        )
        self.list = async_to_raw_response_wrapper(
            employments.list,
        )

    @cached_property
    def formers(self) -> AsyncFormersResourceWithRawResponse:
        return AsyncFormersResourceWithRawResponse(self._employments.formers)

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithRawResponse:
        return AsyncConfigurationResourceWithRawResponse(self._employments.configuration)


class EmploymentsResourceWithStreamingResponse:
    def __init__(self, employments: EmploymentsResource) -> None:
        self._employments = employments

        self.create = to_streamed_response_wrapper(
            employments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            employments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employments.update,
        )
        self.list = to_streamed_response_wrapper(
            employments.list,
        )

    @cached_property
    def formers(self) -> FormersResourceWithStreamingResponse:
        return FormersResourceWithStreamingResponse(self._employments.formers)

    @cached_property
    def configuration(self) -> ConfigurationResourceWithStreamingResponse:
        return ConfigurationResourceWithStreamingResponse(self._employments.configuration)


class AsyncEmploymentsResourceWithStreamingResponse:
    def __init__(self, employments: AsyncEmploymentsResource) -> None:
        self._employments = employments

        self.create = async_to_streamed_response_wrapper(
            employments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            employments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            employments.list,
        )

    @cached_property
    def formers(self) -> AsyncFormersResourceWithStreamingResponse:
        return AsyncFormersResourceWithStreamingResponse(self._employments.formers)

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithStreamingResponse:
        return AsyncConfigurationResourceWithStreamingResponse(self._employments.configuration)
