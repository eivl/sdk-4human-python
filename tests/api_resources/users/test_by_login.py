# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.users import ByLoginCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestByLogin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        by_login = client.users.by_login.create(
            body=["james@4human.hrm", "john@4human.hrm"],
        )
        assert_matches_type(ByLoginCreateResponse, by_login, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        by_login = client.users.by_login.create(
            body=["james@4human.hrm", "john@4human.hrm"],
            find_by="activeDirectoryUsername",
        )
        assert_matches_type(ByLoginCreateResponse, by_login, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.users.by_login.with_raw_response.create(
            body=["james@4human.hrm", "john@4human.hrm"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_login = response.parse()
        assert_matches_type(ByLoginCreateResponse, by_login, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.users.by_login.with_streaming_response.create(
            body=["james@4human.hrm", "john@4human.hrm"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_login = response.parse()
            assert_matches_type(ByLoginCreateResponse, by_login, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncByLogin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        by_login = await async_client.users.by_login.create(
            body=["james@4human.hrm", "john@4human.hrm"],
        )
        assert_matches_type(ByLoginCreateResponse, by_login, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        by_login = await async_client.users.by_login.create(
            body=["james@4human.hrm", "john@4human.hrm"],
            find_by="activeDirectoryUsername",
        )
        assert_matches_type(ByLoginCreateResponse, by_login, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.by_login.with_raw_response.create(
            body=["james@4human.hrm", "john@4human.hrm"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_login = await response.parse()
        assert_matches_type(ByLoginCreateResponse, by_login, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.by_login.with_streaming_response.create(
            body=["james@4human.hrm", "john@4human.hrm"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_login = await response.parse()
            assert_matches_type(ByLoginCreateResponse, by_login, path=["response"])

        assert cast(Any, response.is_closed) is True
