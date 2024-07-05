# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import AuthenticationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthentications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        authentication = client.authentications.create(
            client_id="string",
            client_secret="string",
            grant_type="client_credentials",
        )
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.authentications.with_raw_response.create(
            client_id="string",
            client_secret="string",
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.authentications.with_streaming_response.create(
            client_id="string",
            client_secret="string",
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthentications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        authentication = await async_client.authentications.create(
            client_id="string",
            client_secret="string",
            grant_type="client_credentials",
        )
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.authentications.with_raw_response.create(
            client_id="string",
            client_secret="string",
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.authentications.with_streaming_response.create(
            client_id="string",
            client_secret="string",
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True
