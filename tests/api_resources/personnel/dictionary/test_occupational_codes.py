# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel.dictionary import OccupationalCodeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOccupationalCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        occupational_code = client.personnel.dictionary.occupational_codes.list(
            country="string",
            query="string",
        )
        assert_matches_type(OccupationalCodeListResponse, occupational_code, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.personnel.dictionary.occupational_codes.with_raw_response.list(
            country="string",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        occupational_code = response.parse()
        assert_matches_type(OccupationalCodeListResponse, occupational_code, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.personnel.dictionary.occupational_codes.with_streaming_response.list(
            country="string",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            occupational_code = response.parse()
            assert_matches_type(OccupationalCodeListResponse, occupational_code, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOccupationalCodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        occupational_code = await async_client.personnel.dictionary.occupational_codes.list(
            country="string",
            query="string",
        )
        assert_matches_type(OccupationalCodeListResponse, occupational_code, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.dictionary.occupational_codes.with_raw_response.list(
            country="string",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        occupational_code = await response.parse()
        assert_matches_type(OccupationalCodeListResponse, occupational_code, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.dictionary.occupational_codes.with_streaming_response.list(
            country="string",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            occupational_code = await response.parse()
            assert_matches_type(OccupationalCodeListResponse, occupational_code, path=["response"])

        assert cast(Any, response.is_closed) is True
