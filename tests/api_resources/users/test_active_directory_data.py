# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.users import ActiveDirectoryDataUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActiveDirectoryData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        active_directory_data = client.users.active_directory_data.update(
            "string",
        )
        assert_matches_type(ActiveDirectoryDataUpdateResponse, active_directory_data, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        active_directory_data = client.users.active_directory_data.update(
            "string",
            active_directory_username="ad-user",
            email="example@email.com",
        )
        assert_matches_type(ActiveDirectoryDataUpdateResponse, active_directory_data, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.users.active_directory_data.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_directory_data = response.parse()
        assert_matches_type(ActiveDirectoryDataUpdateResponse, active_directory_data, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.users.active_directory_data.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_directory_data = response.parse()
            assert_matches_type(ActiveDirectoryDataUpdateResponse, active_directory_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.active_directory_data.with_raw_response.update(
                "",
            )


class TestAsyncActiveDirectoryData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        active_directory_data = await async_client.users.active_directory_data.update(
            "string",
        )
        assert_matches_type(ActiveDirectoryDataUpdateResponse, active_directory_data, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        active_directory_data = await async_client.users.active_directory_data.update(
            "string",
            active_directory_username="ad-user",
            email="example@email.com",
        )
        assert_matches_type(ActiveDirectoryDataUpdateResponse, active_directory_data, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.active_directory_data.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_directory_data = await response.parse()
        assert_matches_type(ActiveDirectoryDataUpdateResponse, active_directory_data, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.active_directory_data.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_directory_data = await response.parse()
            assert_matches_type(ActiveDirectoryDataUpdateResponse, active_directory_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.active_directory_data.with_raw_response.update(
                "",
            )
