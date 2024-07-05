# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import SalaryRegulationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSalaryRegulations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        salary_regulation = client.personnel.salary_regulations.list()
        assert_matches_type(SalaryRegulationListResponse, salary_regulation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        salary_regulation = client.personnel.salary_regulations.list(
            limit=0,
            page=0,
            reference_id="string",
        )
        assert_matches_type(SalaryRegulationListResponse, salary_regulation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.personnel.salary_regulations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        salary_regulation = response.parse()
        assert_matches_type(SalaryRegulationListResponse, salary_regulation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.personnel.salary_regulations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            salary_regulation = response.parse()
            assert_matches_type(SalaryRegulationListResponse, salary_regulation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSalaryRegulations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        salary_regulation = await async_client.personnel.salary_regulations.list()
        assert_matches_type(SalaryRegulationListResponse, salary_regulation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        salary_regulation = await async_client.personnel.salary_regulations.list(
            limit=0,
            page=0,
            reference_id="string",
        )
        assert_matches_type(SalaryRegulationListResponse, salary_regulation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.salary_regulations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        salary_regulation = await response.parse()
        assert_matches_type(SalaryRegulationListResponse, salary_regulation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.salary_regulations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            salary_regulation = await response.parse()
            assert_matches_type(SalaryRegulationListResponse, salary_regulation, path=["response"])

        assert cast(Any, response.is_closed) is True
