# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import (
    WorkplanListResponse,
    WorkplanDeleteResponse,
)
from sdk_minus_4human._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkplans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        workplan = client.workplans.create(
            calendar_days=[
                {
                    "date": parse_date("2023-03-17"),
                    "number_of_hours": 8,
                },
                {
                    "date": parse_date("2023-03-18"),
                    "number_of_hours": 3.24,
                },
            ],
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        )
        assert workplan is None

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        workplan = client.workplans.create(
            calendar_days=[
                {
                    "date": parse_date("2023-03-17"),
                    "number_of_hours": 8,
                },
                {
                    "date": parse_date("2023-03-18"),
                    "number_of_hours": 3.24,
                },
            ],
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
            company_employee_ids=[2],
            company_id=2,
            employee_ids=["2"],
            employment_ids=[5, 6],
            source_system="Workplan-sys 2000",
            unit_id="unit",
        )
        assert workplan is None

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.workplans.with_raw_response.create(
            calendar_days=[
                {
                    "date": parse_date("2023-03-17"),
                    "number_of_hours": 8,
                },
                {
                    "date": parse_date("2023-03-18"),
                    "number_of_hours": 3.24,
                },
            ],
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workplan = response.parse()
        assert workplan is None

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.workplans.with_streaming_response.create(
            calendar_days=[
                {
                    "date": parse_date("2023-03-17"),
                    "number_of_hours": 8,
                },
                {
                    "date": parse_date("2023-03-18"),
                    "number_of_hours": 3.24,
                },
            ],
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workplan = response.parse()
            assert workplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        workplan = client.workplans.list(
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
        )
        assert_matches_type(WorkplanListResponse, workplan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        workplan = client.workplans.list(
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            company_employee_id="string",
            company_id=0,
            created_at_from=parse_date("2019-12-27"),
            created_at_to=parse_date("2019-12-27"),
            employee_id="string",
            employment_id=0,
            limit=0,
            origin="registered_by_api",
            page=0,
            source_system="string",
        )
        assert_matches_type(WorkplanListResponse, workplan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.workplans.with_raw_response.list(
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workplan = response.parse()
        assert_matches_type(WorkplanListResponse, workplan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.workplans.with_streaming_response.list(
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workplan = response.parse()
            assert_matches_type(WorkplanListResponse, workplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: SDK4human) -> None:
        workplan = client.workplans.delete(
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        )
        assert_matches_type(WorkplanDeleteResponse, workplan, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: SDK4human) -> None:
        workplan = client.workplans.delete(
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
            company_employee_id=4,
            company_id=2,
            employee_id="some random string",
            employment_id=5,
            unit_id="some random string",
        )
        assert_matches_type(WorkplanDeleteResponse, workplan, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: SDK4human) -> None:
        response = client.workplans.with_raw_response.delete(
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workplan = response.parse()
        assert_matches_type(WorkplanDeleteResponse, workplan, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: SDK4human) -> None:
        with client.workplans.with_streaming_response.delete(
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workplan = response.parse()
            assert_matches_type(WorkplanDeleteResponse, workplan, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkplans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        workplan = await async_client.workplans.create(
            calendar_days=[
                {
                    "date": parse_date("2023-03-17"),
                    "number_of_hours": 8,
                },
                {
                    "date": parse_date("2023-03-18"),
                    "number_of_hours": 3.24,
                },
            ],
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        )
        assert workplan is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        workplan = await async_client.workplans.create(
            calendar_days=[
                {
                    "date": parse_date("2023-03-17"),
                    "number_of_hours": 8,
                },
                {
                    "date": parse_date("2023-03-18"),
                    "number_of_hours": 3.24,
                },
            ],
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
            company_employee_ids=[2],
            company_id=2,
            employee_ids=["2"],
            employment_ids=[5, 6],
            source_system="Workplan-sys 2000",
            unit_id="unit",
        )
        assert workplan is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.workplans.with_raw_response.create(
            calendar_days=[
                {
                    "date": parse_date("2023-03-17"),
                    "number_of_hours": 8,
                },
                {
                    "date": parse_date("2023-03-18"),
                    "number_of_hours": 3.24,
                },
            ],
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workplan = await response.parse()
        assert workplan is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.workplans.with_streaming_response.create(
            calendar_days=[
                {
                    "date": parse_date("2023-03-17"),
                    "number_of_hours": 8,
                },
                {
                    "date": parse_date("2023-03-18"),
                    "number_of_hours": 3.24,
                },
            ],
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workplan = await response.parse()
            assert workplan is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        workplan = await async_client.workplans.list(
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
        )
        assert_matches_type(WorkplanListResponse, workplan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        workplan = await async_client.workplans.list(
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            company_employee_id="string",
            company_id=0,
            created_at_from=parse_date("2019-12-27"),
            created_at_to=parse_date("2019-12-27"),
            employee_id="string",
            employment_id=0,
            limit=0,
            origin="registered_by_api",
            page=0,
            source_system="string",
        )
        assert_matches_type(WorkplanListResponse, workplan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.workplans.with_raw_response.list(
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workplan = await response.parse()
        assert_matches_type(WorkplanListResponse, workplan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.workplans.with_streaming_response.list(
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workplan = await response.parse()
            assert_matches_type(WorkplanListResponse, workplan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSDK4human) -> None:
        workplan = await async_client.workplans.delete(
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        )
        assert_matches_type(WorkplanDeleteResponse, workplan, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSDK4human) -> None:
        workplan = await async_client.workplans.delete(
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
            company_employee_id=4,
            company_id=2,
            employee_id="some random string",
            employment_id=5,
            unit_id="some random string",
        )
        assert_matches_type(WorkplanDeleteResponse, workplan, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.workplans.with_raw_response.delete(
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workplan = await response.parse()
        assert_matches_type(WorkplanDeleteResponse, workplan, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSDK4human) -> None:
        async with async_client.workplans.with_streaming_response.delete(
            date_from="2023-06-05T00:00:00+00:00",
            date_to="2023-06-05T00:00:00+00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workplan = await response.parse()
            assert_matches_type(WorkplanDeleteResponse, workplan, path=["response"])

        assert cast(Any, response.is_closed) is True
