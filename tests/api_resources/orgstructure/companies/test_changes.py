# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.orgstructure.companies import ChangeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        change = client.orgstructure.companies.changes.list(
            from_=0,
            to=0,
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        change = client.orgstructure.companies.changes.list(
            from_=0,
            to=0,
            external=True,
            format="timestamp",
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.orgstructure.companies.changes.with_raw_response.list(
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change = response.parse()
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.orgstructure.companies.changes.with_streaming_response.list(
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change = response.parse()
            assert_matches_type(ChangeListResponse, change, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChanges:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        change = await async_client.orgstructure.companies.changes.list(
            from_=0,
            to=0,
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        change = await async_client.orgstructure.companies.changes.list(
            from_=0,
            to=0,
            external=True,
            format="timestamp",
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.companies.changes.with_raw_response.list(
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change = await response.parse()
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.companies.changes.with_streaming_response.list(
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change = await response.parse()
            assert_matches_type(ChangeListResponse, change, path=["response"])

        assert cast(Any, response.is_closed) is True
