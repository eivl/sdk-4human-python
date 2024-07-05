# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel.salary.elements import (
    DeductionListResponse,
    DeductionCreateResponse,
    DeductionUpdateResponse,
    DeductionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeductions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        deduction = client.personnel.salary.elements.deductions.create(
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
        )
        assert_matches_type(DeductionCreateResponse, deduction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        deduction = client.personnel.salary.elements.deductions.create(
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
            additional_main_salary=False,
        )
        assert_matches_type(DeductionCreateResponse, deduction, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.salary.elements.deductions.with_raw_response.create(
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deduction = response.parse()
        assert_matches_type(DeductionCreateResponse, deduction, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.salary.elements.deductions.with_streaming_response.create(
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deduction = response.parse()
            assert_matches_type(DeductionCreateResponse, deduction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        deduction = client.personnel.salary.elements.deductions.retrieve(
            0,
        )
        assert_matches_type(DeductionRetrieveResponse, deduction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.personnel.salary.elements.deductions.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deduction = response.parse()
        assert_matches_type(DeductionRetrieveResponse, deduction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.personnel.salary.elements.deductions.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deduction = response.parse()
            assert_matches_type(DeductionRetrieveResponse, deduction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        deduction = client.personnel.salary.elements.deductions.update(
            0,
        )
        assert_matches_type(DeductionUpdateResponse, deduction, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        deduction = client.personnel.salary.elements.deductions.update(
            0,
            additional_main_salary=False,
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
        )
        assert_matches_type(DeductionUpdateResponse, deduction, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.salary.elements.deductions.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deduction = response.parse()
        assert_matches_type(DeductionUpdateResponse, deduction, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.salary.elements.deductions.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deduction = response.parse()
            assert_matches_type(DeductionUpdateResponse, deduction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        deduction = client.personnel.salary.elements.deductions.list()
        assert_matches_type(DeductionListResponse, deduction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        deduction = client.personnel.salary.elements.deductions.list(
            limit=0,
            page=0,
        )
        assert_matches_type(DeductionListResponse, deduction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.personnel.salary.elements.deductions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deduction = response.parse()
        assert_matches_type(DeductionListResponse, deduction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.personnel.salary.elements.deductions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deduction = response.parse()
            assert_matches_type(DeductionListResponse, deduction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeductions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        deduction = await async_client.personnel.salary.elements.deductions.create(
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
        )
        assert_matches_type(DeductionCreateResponse, deduction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        deduction = await async_client.personnel.salary.elements.deductions.create(
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
            additional_main_salary=False,
        )
        assert_matches_type(DeductionCreateResponse, deduction, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.salary.elements.deductions.with_raw_response.create(
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deduction = await response.parse()
        assert_matches_type(DeductionCreateResponse, deduction, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.salary.elements.deductions.with_streaming_response.create(
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deduction = await response.parse()
            assert_matches_type(DeductionCreateResponse, deduction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        deduction = await async_client.personnel.salary.elements.deductions.retrieve(
            0,
        )
        assert_matches_type(DeductionRetrieveResponse, deduction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.salary.elements.deductions.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deduction = await response.parse()
        assert_matches_type(DeductionRetrieveResponse, deduction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.salary.elements.deductions.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deduction = await response.parse()
            assert_matches_type(DeductionRetrieveResponse, deduction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        deduction = await async_client.personnel.salary.elements.deductions.update(
            0,
        )
        assert_matches_type(DeductionUpdateResponse, deduction, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        deduction = await async_client.personnel.salary.elements.deductions.update(
            0,
            additional_main_salary=False,
            amount="50.2",
            currency="NOK",
            description="Hourly salary",
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            external_id="ext-22",
            include_to_contract=False,
            individual=False,
            internal_id="int-22",
            job_ids=[7],
            mandatory=False,
            name="Salary-1",
            org_unit_ids=[0, 0, 0],
            period="SALARY_PERIOD_HOUR",
            show_in_profile=False,
            status="active",
            type="rate",
        )
        assert_matches_type(DeductionUpdateResponse, deduction, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.salary.elements.deductions.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deduction = await response.parse()
        assert_matches_type(DeductionUpdateResponse, deduction, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.salary.elements.deductions.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deduction = await response.parse()
            assert_matches_type(DeductionUpdateResponse, deduction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        deduction = await async_client.personnel.salary.elements.deductions.list()
        assert_matches_type(DeductionListResponse, deduction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        deduction = await async_client.personnel.salary.elements.deductions.list(
            limit=0,
            page=0,
        )
        assert_matches_type(DeductionListResponse, deduction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.salary.elements.deductions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deduction = await response.parse()
        assert_matches_type(DeductionListResponse, deduction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.salary.elements.deductions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deduction = await response.parse()
            assert_matches_type(DeductionListResponse, deduction, path=["response"])

        assert cast(Any, response.is_closed) is True
