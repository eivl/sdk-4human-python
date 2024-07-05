# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import (
    WorkingHoursArrangementListResponse,
    WorkingHoursArrangementCreateResponse,
    WorkingHoursArrangementUpdateResponse,
    WorkingHoursArrangementRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkingHoursArrangements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        working_hours_arrangement = client.personnel.working_hours_arrangements.create(
            description=None,
            external_id="externalId",
            internal_id="id",
            name="name",
            status="active",
            working_hours_per_week=12,
        )
        assert_matches_type(WorkingHoursArrangementCreateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.working_hours_arrangements.with_raw_response.create(
            description=None,
            external_id="externalId",
            internal_id="id",
            name="name",
            status="active",
            working_hours_per_week=12,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        working_hours_arrangement = response.parse()
        assert_matches_type(WorkingHoursArrangementCreateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.working_hours_arrangements.with_streaming_response.create(
            description=None,
            external_id="externalId",
            internal_id="id",
            name="name",
            status="active",
            working_hours_per_week=12,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            working_hours_arrangement = response.parse()
            assert_matches_type(WorkingHoursArrangementCreateResponse, working_hours_arrangement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        working_hours_arrangement = client.personnel.working_hours_arrangements.retrieve(
            "string",
        )
        assert_matches_type(WorkingHoursArrangementRetrieveResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        working_hours_arrangement = client.personnel.working_hours_arrangements.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(WorkingHoursArrangementRetrieveResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.personnel.working_hours_arrangements.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        working_hours_arrangement = response.parse()
        assert_matches_type(WorkingHoursArrangementRetrieveResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.personnel.working_hours_arrangements.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            working_hours_arrangement = response.parse()
            assert_matches_type(WorkingHoursArrangementRetrieveResponse, working_hours_arrangement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.personnel.working_hours_arrangements.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        working_hours_arrangement = client.personnel.working_hours_arrangements.update(
            "string",
        )
        assert_matches_type(WorkingHoursArrangementUpdateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        working_hours_arrangement = client.personnel.working_hours_arrangements.update(
            "string",
            external=True,
            description=None,
            external_id="externalId",
            internal_id="id",
            name="name",
            status="active",
            working_hours_per_week=12,
        )
        assert_matches_type(WorkingHoursArrangementUpdateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.working_hours_arrangements.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        working_hours_arrangement = response.parse()
        assert_matches_type(WorkingHoursArrangementUpdateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.working_hours_arrangements.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            working_hours_arrangement = response.parse()
            assert_matches_type(WorkingHoursArrangementUpdateResponse, working_hours_arrangement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.personnel.working_hours_arrangements.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        working_hours_arrangement = client.personnel.working_hours_arrangements.list()
        assert_matches_type(WorkingHoursArrangementListResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        working_hours_arrangement = client.personnel.working_hours_arrangements.list(
            limit=0,
            page=0,
        )
        assert_matches_type(WorkingHoursArrangementListResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.personnel.working_hours_arrangements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        working_hours_arrangement = response.parse()
        assert_matches_type(WorkingHoursArrangementListResponse, working_hours_arrangement, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.personnel.working_hours_arrangements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            working_hours_arrangement = response.parse()
            assert_matches_type(WorkingHoursArrangementListResponse, working_hours_arrangement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkingHoursArrangements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        working_hours_arrangement = await async_client.personnel.working_hours_arrangements.create(
            description=None,
            external_id="externalId",
            internal_id="id",
            name="name",
            status="active",
            working_hours_per_week=12,
        )
        assert_matches_type(WorkingHoursArrangementCreateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.working_hours_arrangements.with_raw_response.create(
            description=None,
            external_id="externalId",
            internal_id="id",
            name="name",
            status="active",
            working_hours_per_week=12,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        working_hours_arrangement = await response.parse()
        assert_matches_type(WorkingHoursArrangementCreateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.working_hours_arrangements.with_streaming_response.create(
            description=None,
            external_id="externalId",
            internal_id="id",
            name="name",
            status="active",
            working_hours_per_week=12,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            working_hours_arrangement = await response.parse()
            assert_matches_type(WorkingHoursArrangementCreateResponse, working_hours_arrangement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        working_hours_arrangement = await async_client.personnel.working_hours_arrangements.retrieve(
            "string",
        )
        assert_matches_type(WorkingHoursArrangementRetrieveResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        working_hours_arrangement = await async_client.personnel.working_hours_arrangements.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(WorkingHoursArrangementRetrieveResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.working_hours_arrangements.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        working_hours_arrangement = await response.parse()
        assert_matches_type(WorkingHoursArrangementRetrieveResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.working_hours_arrangements.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            working_hours_arrangement = await response.parse()
            assert_matches_type(WorkingHoursArrangementRetrieveResponse, working_hours_arrangement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.personnel.working_hours_arrangements.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        working_hours_arrangement = await async_client.personnel.working_hours_arrangements.update(
            "string",
        )
        assert_matches_type(WorkingHoursArrangementUpdateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        working_hours_arrangement = await async_client.personnel.working_hours_arrangements.update(
            "string",
            external=True,
            description=None,
            external_id="externalId",
            internal_id="id",
            name="name",
            status="active",
            working_hours_per_week=12,
        )
        assert_matches_type(WorkingHoursArrangementUpdateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.working_hours_arrangements.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        working_hours_arrangement = await response.parse()
        assert_matches_type(WorkingHoursArrangementUpdateResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.working_hours_arrangements.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            working_hours_arrangement = await response.parse()
            assert_matches_type(WorkingHoursArrangementUpdateResponse, working_hours_arrangement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.personnel.working_hours_arrangements.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        working_hours_arrangement = await async_client.personnel.working_hours_arrangements.list()
        assert_matches_type(WorkingHoursArrangementListResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        working_hours_arrangement = await async_client.personnel.working_hours_arrangements.list(
            limit=0,
            page=0,
        )
        assert_matches_type(WorkingHoursArrangementListResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.working_hours_arrangements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        working_hours_arrangement = await response.parse()
        assert_matches_type(WorkingHoursArrangementListResponse, working_hours_arrangement, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.working_hours_arrangements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            working_hours_arrangement = await response.parse()
            assert_matches_type(WorkingHoursArrangementListResponse, working_hours_arrangement, path=["response"])

        assert cast(Any, response.is_closed) is True
