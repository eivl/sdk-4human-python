# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import OrgstructureListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrgstructure:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        orgstructure = client.orgstructure.list()
        assert_matches_type(OrgstructureListResponse, orgstructure, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.orgstructure.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orgstructure = response.parse()
        assert_matches_type(OrgstructureListResponse, orgstructure, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.orgstructure.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orgstructure = response.parse()
            assert_matches_type(OrgstructureListResponse, orgstructure, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrgstructure:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        orgstructure = await async_client.orgstructure.list()
        assert_matches_type(OrgstructureListResponse, orgstructure, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orgstructure = await response.parse()
        assert_matches_type(OrgstructureListResponse, orgstructure, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orgstructure = await response.parse()
            assert_matches_type(OrgstructureListResponse, orgstructure, path=["response"])

        assert cast(Any, response.is_closed) is True
