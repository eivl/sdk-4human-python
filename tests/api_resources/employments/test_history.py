# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.employments import HistoryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        history = client.employments.history.retrieve(
            0,
        )
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        history = client.employments.history.retrieve(
            0,
            changes_from=0,
            changes_to=0,
            effective_statuses="string",
            external=True,
            limit=0,
            page=0,
            valid_from=0,
            valid_to=0,
        )
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.employments.history.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.employments.history.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        history = await async_client.employments.history.retrieve(
            0,
        )
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        history = await async_client.employments.history.retrieve(
            0,
            changes_from=0,
            changes_to=0,
            effective_statuses="string",
            external=True,
            limit=0,
            page=0,
            valid_from=0,
            valid_to=0,
        )
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.employments.history.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.employments.history.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True
