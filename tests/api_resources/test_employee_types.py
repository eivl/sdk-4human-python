# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import (
    EmployeeTypeListResponse,
    EmployeeTypeCreateResponse,
    EmployeeTypeUpdateResponse,
    EmployeeTypeRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployeeTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        employee_type = client.employee_types.create(
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            type_id="O",
        )
        assert_matches_type(EmployeeTypeCreateResponse, employee_type, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        employee_type = client.employee_types.create(
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            type_id="O",
            reason=True,
            substitute=False,
        )
        assert_matches_type(EmployeeTypeCreateResponse, employee_type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.employee_types.with_raw_response.create(
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            type_id="O",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee_type = response.parse()
        assert_matches_type(EmployeeTypeCreateResponse, employee_type, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.employee_types.with_streaming_response.create(
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            type_id="O",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee_type = response.parse()
            assert_matches_type(EmployeeTypeCreateResponse, employee_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        employee_type = client.employee_types.retrieve(
            "string",
        )
        assert_matches_type(EmployeeTypeRetrieveResponse, employee_type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.employee_types.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee_type = response.parse()
        assert_matches_type(EmployeeTypeRetrieveResponse, employee_type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.employee_types.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee_type = response.parse()
            assert_matches_type(EmployeeTypeRetrieveResponse, employee_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employee_type_id` but received ''"):
            client.employee_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        employee_type = client.employee_types.update(
            "string",
        )
        assert_matches_type(EmployeeTypeUpdateResponse, employee_type, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        employee_type = client.employee_types.update(
            "string",
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            reason=True,
            status="active",
            substitute=False,
            type_id="O",
        )
        assert_matches_type(EmployeeTypeUpdateResponse, employee_type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.employee_types.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee_type = response.parse()
        assert_matches_type(EmployeeTypeUpdateResponse, employee_type, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.employee_types.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee_type = response.parse()
            assert_matches_type(EmployeeTypeUpdateResponse, employee_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employee_type_id` but received ''"):
            client.employee_types.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        employee_type = client.employee_types.list()
        assert_matches_type(EmployeeTypeListResponse, employee_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        employee_type = client.employee_types.list(
            limit=0,
            page=0,
        )
        assert_matches_type(EmployeeTypeListResponse, employee_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.employee_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee_type = response.parse()
        assert_matches_type(EmployeeTypeListResponse, employee_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.employee_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee_type = response.parse()
            assert_matches_type(EmployeeTypeListResponse, employee_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmployeeTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        employee_type = await async_client.employee_types.create(
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            type_id="O",
        )
        assert_matches_type(EmployeeTypeCreateResponse, employee_type, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        employee_type = await async_client.employee_types.create(
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            type_id="O",
            reason=True,
            substitute=False,
        )
        assert_matches_type(EmployeeTypeCreateResponse, employee_type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.employee_types.with_raw_response.create(
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            type_id="O",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee_type = await response.parse()
        assert_matches_type(EmployeeTypeCreateResponse, employee_type, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.employee_types.with_streaming_response.create(
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            type_id="O",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee_type = await response.parse()
            assert_matches_type(EmployeeTypeCreateResponse, employee_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        employee_type = await async_client.employee_types.retrieve(
            "string",
        )
        assert_matches_type(EmployeeTypeRetrieveResponse, employee_type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.employee_types.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee_type = await response.parse()
        assert_matches_type(EmployeeTypeRetrieveResponse, employee_type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.employee_types.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee_type = await response.parse()
            assert_matches_type(EmployeeTypeRetrieveResponse, employee_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employee_type_id` but received ''"):
            await async_client.employee_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        employee_type = await async_client.employee_types.update(
            "string",
        )
        assert_matches_type(EmployeeTypeUpdateResponse, employee_type, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        employee_type = await async_client.employee_types.update(
            "string",
            employee_type="WORKER_NONEMPLOYEE",
            employment_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            reason=True,
            status="active",
            substitute=False,
            type_id="O",
        )
        assert_matches_type(EmployeeTypeUpdateResponse, employee_type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.employee_types.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee_type = await response.parse()
        assert_matches_type(EmployeeTypeUpdateResponse, employee_type, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.employee_types.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee_type = await response.parse()
            assert_matches_type(EmployeeTypeUpdateResponse, employee_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employee_type_id` but received ''"):
            await async_client.employee_types.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        employee_type = await async_client.employee_types.list()
        assert_matches_type(EmployeeTypeListResponse, employee_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        employee_type = await async_client.employee_types.list(
            limit=0,
            page=0,
        )
        assert_matches_type(EmployeeTypeListResponse, employee_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.employee_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee_type = await response.parse()
        assert_matches_type(EmployeeTypeListResponse, employee_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.employee_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee_type = await response.parse()
            assert_matches_type(EmployeeTypeListResponse, employee_type, path=["response"])

        assert cast(Any, response.is_closed) is True
