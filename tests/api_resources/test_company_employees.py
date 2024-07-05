# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import (
    CompanyEmployeeListResponse,
    CompanyEmployeeUpdateResponse,
    CompanyEmployeeRetrieveResponse,
    CompanyEmployeeUpdatePartialResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanyEmployees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        company_employee = client.company_employees.retrieve(
            "string",
        )
        assert_matches_type(CompanyEmployeeRetrieveResponse, company_employee, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        company_employee = client.company_employees.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(CompanyEmployeeRetrieveResponse, company_employee, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.company_employees.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_employee = response.parse()
        assert_matches_type(CompanyEmployeeRetrieveResponse, company_employee, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.company_employees.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_employee = response.parse()
            assert_matches_type(CompanyEmployeeRetrieveResponse, company_employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_employee_id` but received ''"):
            client.company_employees.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        company_employee = client.company_employees.update(
            0,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={},
            industry_ids=[
                {
                    "industry_branch_id": 1,
                    "card_number": "123456",
                    "country_issue": "NOR",
                    "issue_date": "2021-10-10T00:00:00+0000",
                    "expiry_date": "2023-10-10T00:00:00+0000",
                    "additional_info": "Industry information",
                    "file": {
                        "id": "string",
                        "original_name": "x",
                    },
                }
            ],
            main_employer=False,
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={},
            resource_type=1,
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={},
            work_status="WORK_STATUS_ACTIVE",
        )
        assert_matches_type(CompanyEmployeeUpdateResponse, company_employee, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        company_employee = client.company_employees.update(
            0,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": None,
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={
                "from": "2021-02-15T00:00:00+0000",
                "to": "2021-02-15T00:00:00+0000",
            },
            industry_ids=[
                {
                    "id": 1,
                    "industry_branch_id": 1,
                    "card_number": "123456",
                    "country_issue": "NOR",
                    "issue_date": "2021-10-10T00:00:00+0000",
                    "expiry_date": "2023-10-10T00:00:00+0000",
                    "additional_info": "Industry information",
                    "file": {
                        "id": "string",
                        "original_name": "x",
                    },
                }
            ],
            main_employer=False,
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={
                "from": "2021-02-15T00:00:00+0000",
                "to": None,
            },
            resource_type=1,
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={
                "from": "2021-02-15T00:00:00+0000",
                "to": "2021-02-15T00:00:00+0000",
            },
            work_status="WORK_STATUS_ACTIVE",
            external=True,
            force_no_approval_policy=True,
            max_date_follow_up_sickness="2022-10-30T00:00:00+0000",
            max_date_sickness_refund="2022-10-30T00:00:00+0000",
            retirement_date="2022-10-30T00:00:00+0000",
        )
        assert_matches_type(CompanyEmployeeUpdateResponse, company_employee, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.company_employees.with_raw_response.update(
            0,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={},
            industry_ids=[
                {
                    "industry_branch_id": 1,
                    "card_number": "123456",
                    "country_issue": "NOR",
                    "issue_date": "2021-10-10T00:00:00+0000",
                    "expiry_date": "2023-10-10T00:00:00+0000",
                    "additional_info": "Industry information",
                    "file": {
                        "id": "string",
                        "original_name": "x",
                    },
                }
            ],
            main_employer=False,
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={},
            resource_type=1,
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={},
            work_status="WORK_STATUS_ACTIVE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_employee = response.parse()
        assert_matches_type(CompanyEmployeeUpdateResponse, company_employee, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.company_employees.with_streaming_response.update(
            0,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={},
            industry_ids=[
                {
                    "industry_branch_id": 1,
                    "card_number": "123456",
                    "country_issue": "NOR",
                    "issue_date": "2021-10-10T00:00:00+0000",
                    "expiry_date": "2023-10-10T00:00:00+0000",
                    "additional_info": "Industry information",
                    "file": {
                        "id": "string",
                        "original_name": "x",
                    },
                }
            ],
            main_employer=False,
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={},
            resource_type=1,
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={},
            work_status="WORK_STATUS_ACTIVE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_employee = response.parse()
            assert_matches_type(CompanyEmployeeUpdateResponse, company_employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        company_employee = client.company_employees.list()
        assert_matches_type(CompanyEmployeeListResponse, company_employee, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        company_employee = client.company_employees.list(
            company_id=0,
            employee_id="string",
            employment_id="string",
            external=True,
            limit=0,
            page=0,
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyEmployeeListResponse, company_employee, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.company_employees.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_employee = response.parse()
        assert_matches_type(CompanyEmployeeListResponse, company_employee, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.company_employees.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_employee = response.parse()
            assert_matches_type(CompanyEmployeeListResponse, company_employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_partial(self, client: SDK4human) -> None:
        company_employee = client.company_employees.update_partial(
            "string",
        )
        assert_matches_type(CompanyEmployeeUpdatePartialResponse, company_employee, path=["response"])

    @parametrize
    def test_method_update_partial_with_all_params(self, client: SDK4human) -> None:
        company_employee = client.company_employees.update_partial(
            "string",
            external=True,
            force_no_approval_policy=True,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": None,
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={
                "from": "2021-02-15T00:00:00+0000",
                "to": "2021-02-15T00:00:00+0000",
            },
            main_employer=False,
            max_date_follow_up_sickness="2022-10-30T00:00:00+0000",
            max_date_sickness_refund="2022-10-30T00:00:00+0000",
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={
                "from": "2021-02-15T00:00:00+0000",
                "to": None,
            },
            resource_type=1,
            retirement_date="2022-10-30T00:00:00+0000",
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={
                "from": "2021-02-15T00:00:00+0000",
                "to": "2021-02-15T00:00:00+0000",
            },
            work_status="WORK_STATUS_ACTIVE",
        )
        assert_matches_type(CompanyEmployeeUpdatePartialResponse, company_employee, path=["response"])

    @parametrize
    def test_raw_response_update_partial(self, client: SDK4human) -> None:
        response = client.company_employees.with_raw_response.update_partial(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_employee = response.parse()
        assert_matches_type(CompanyEmployeeUpdatePartialResponse, company_employee, path=["response"])

    @parametrize
    def test_streaming_response_update_partial(self, client: SDK4human) -> None:
        with client.company_employees.with_streaming_response.update_partial(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_employee = response.parse()
            assert_matches_type(CompanyEmployeeUpdatePartialResponse, company_employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_partial(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_employee_id` but received ''"):
            client.company_employees.with_raw_response.update_partial(
                "",
            )


class TestAsyncCompanyEmployees:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        company_employee = await async_client.company_employees.retrieve(
            "string",
        )
        assert_matches_type(CompanyEmployeeRetrieveResponse, company_employee, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        company_employee = await async_client.company_employees.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(CompanyEmployeeRetrieveResponse, company_employee, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.company_employees.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_employee = await response.parse()
        assert_matches_type(CompanyEmployeeRetrieveResponse, company_employee, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.company_employees.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_employee = await response.parse()
            assert_matches_type(CompanyEmployeeRetrieveResponse, company_employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_employee_id` but received ''"):
            await async_client.company_employees.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        company_employee = await async_client.company_employees.update(
            0,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={},
            industry_ids=[
                {
                    "industry_branch_id": 1,
                    "card_number": "123456",
                    "country_issue": "NOR",
                    "issue_date": "2021-10-10T00:00:00+0000",
                    "expiry_date": "2023-10-10T00:00:00+0000",
                    "additional_info": "Industry information",
                    "file": {
                        "id": "string",
                        "original_name": "x",
                    },
                }
            ],
            main_employer=False,
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={},
            resource_type=1,
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={},
            work_status="WORK_STATUS_ACTIVE",
        )
        assert_matches_type(CompanyEmployeeUpdateResponse, company_employee, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        company_employee = await async_client.company_employees.update(
            0,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": None,
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={
                "from": "2021-02-15T00:00:00+0000",
                "to": "2021-02-15T00:00:00+0000",
            },
            industry_ids=[
                {
                    "id": 1,
                    "industry_branch_id": 1,
                    "card_number": "123456",
                    "country_issue": "NOR",
                    "issue_date": "2021-10-10T00:00:00+0000",
                    "expiry_date": "2023-10-10T00:00:00+0000",
                    "additional_info": "Industry information",
                    "file": {
                        "id": "string",
                        "original_name": "x",
                    },
                }
            ],
            main_employer=False,
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={
                "from": "2021-02-15T00:00:00+0000",
                "to": None,
            },
            resource_type=1,
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={
                "from": "2021-02-15T00:00:00+0000",
                "to": "2021-02-15T00:00:00+0000",
            },
            work_status="WORK_STATUS_ACTIVE",
            external=True,
            force_no_approval_policy=True,
            max_date_follow_up_sickness="2022-10-30T00:00:00+0000",
            max_date_sickness_refund="2022-10-30T00:00:00+0000",
            retirement_date="2022-10-30T00:00:00+0000",
        )
        assert_matches_type(CompanyEmployeeUpdateResponse, company_employee, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.company_employees.with_raw_response.update(
            0,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={},
            industry_ids=[
                {
                    "industry_branch_id": 1,
                    "card_number": "123456",
                    "country_issue": "NOR",
                    "issue_date": "2021-10-10T00:00:00+0000",
                    "expiry_date": "2023-10-10T00:00:00+0000",
                    "additional_info": "Industry information",
                    "file": {
                        "id": "string",
                        "original_name": "x",
                    },
                }
            ],
            main_employer=False,
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={},
            resource_type=1,
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={},
            work_status="WORK_STATUS_ACTIVE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_employee = await response.parse()
        assert_matches_type(CompanyEmployeeUpdateResponse, company_employee, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.company_employees.with_streaming_response.update(
            0,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={},
            industry_ids=[
                {
                    "industry_branch_id": 1,
                    "card_number": "123456",
                    "country_issue": "NOR",
                    "issue_date": "2021-10-10T00:00:00+0000",
                    "expiry_date": "2023-10-10T00:00:00+0000",
                    "additional_info": "Industry information",
                    "file": {
                        "id": "string",
                        "original_name": "x",
                    },
                }
            ],
            main_employer=False,
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={},
            resource_type=1,
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={},
            work_status="WORK_STATUS_ACTIVE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_employee = await response.parse()
            assert_matches_type(CompanyEmployeeUpdateResponse, company_employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        company_employee = await async_client.company_employees.list()
        assert_matches_type(CompanyEmployeeListResponse, company_employee, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        company_employee = await async_client.company_employees.list(
            company_id=0,
            employee_id="string",
            employment_id="string",
            external=True,
            limit=0,
            page=0,
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyEmployeeListResponse, company_employee, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.company_employees.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_employee = await response.parse()
        assert_matches_type(CompanyEmployeeListResponse, company_employee, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.company_employees.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_employee = await response.parse()
            assert_matches_type(CompanyEmployeeListResponse, company_employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_partial(self, async_client: AsyncSDK4human) -> None:
        company_employee = await async_client.company_employees.update_partial(
            "string",
        )
        assert_matches_type(CompanyEmployeeUpdatePartialResponse, company_employee, path=["response"])

    @parametrize
    async def test_method_update_partial_with_all_params(self, async_client: AsyncSDK4human) -> None:
        company_employee = await async_client.company_employees.update_partial(
            "string",
            external=True,
            force_no_approval_policy=True,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": None,
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_id="66",
            free_employer={
                "from": "2021-02-15T00:00:00+0000",
                "to": "2021-02-15T00:00:00+0000",
            },
            main_employer=False,
            max_date_follow_up_sickness="2022-10-30T00:00:00+0000",
            max_date_sickness_refund="2022-10-30T00:00:00+0000",
            primary_employment_id=28,
            ready_for_payment=False,
            residence_permit={
                "from": "2021-02-15T00:00:00+0000",
                "to": None,
            },
            resource_type=1,
            retirement_date="2022-10-30T00:00:00+0000",
            salary_number="SAL-01A",
            self_sickness="2019-07-30T00:00:00+0000",
            seniority_date="2019-08-29T00:00:00+0000",
            termination_seniority_date="2019-08-29T00:00:00+0000",
            work_permit={
                "from": "2021-02-15T00:00:00+0000",
                "to": "2021-02-15T00:00:00+0000",
            },
            work_status="WORK_STATUS_ACTIVE",
        )
        assert_matches_type(CompanyEmployeeUpdatePartialResponse, company_employee, path=["response"])

    @parametrize
    async def test_raw_response_update_partial(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.company_employees.with_raw_response.update_partial(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_employee = await response.parse()
        assert_matches_type(CompanyEmployeeUpdatePartialResponse, company_employee, path=["response"])

    @parametrize
    async def test_streaming_response_update_partial(self, async_client: AsyncSDK4human) -> None:
        async with async_client.company_employees.with_streaming_response.update_partial(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_employee = await response.parse()
            assert_matches_type(CompanyEmployeeUpdatePartialResponse, company_employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_partial(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_employee_id` but received ''"):
            await async_client.company_employees.with_raw_response.update_partial(
                "",
            )
