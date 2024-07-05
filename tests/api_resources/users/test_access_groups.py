# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.users import AccessGroupListResponse, AccessGroupAssignResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        access_group = client.users.access_groups.list()
        assert_matches_type(AccessGroupListResponse, access_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.users.access_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_group = response.parse()
        assert_matches_type(AccessGroupListResponse, access_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.users.access_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_group = response.parse()
            assert_matches_type(AccessGroupListResponse, access_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_assign(self, client: SDK4human) -> None:
        access_group = client.users.access_groups.assign(
            group_ids=["dd63031d-ce96-11e7-ad6c-06063970b924", "dd73031d-cf96-11e7-ad6c-06063970b994"],
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        )
        assert_matches_type(AccessGroupAssignResponse, access_group, path=["response"])

    @parametrize
    def test_raw_response_assign(self, client: SDK4human) -> None:
        response = client.users.access_groups.with_raw_response.assign(
            group_ids=["dd63031d-ce96-11e7-ad6c-06063970b924", "dd73031d-cf96-11e7-ad6c-06063970b994"],
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_group = response.parse()
        assert_matches_type(AccessGroupAssignResponse, access_group, path=["response"])

    @parametrize
    def test_streaming_response_assign(self, client: SDK4human) -> None:
        with client.users.access_groups.with_streaming_response.assign(
            group_ids=["dd63031d-ce96-11e7-ad6c-06063970b924", "dd73031d-cf96-11e7-ad6c-06063970b994"],
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_group = response.parse()
            assert_matches_type(AccessGroupAssignResponse, access_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccessGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        access_group = await async_client.users.access_groups.list()
        assert_matches_type(AccessGroupListResponse, access_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.access_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_group = await response.parse()
        assert_matches_type(AccessGroupListResponse, access_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.access_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_group = await response.parse()
            assert_matches_type(AccessGroupListResponse, access_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_assign(self, async_client: AsyncSDK4human) -> None:
        access_group = await async_client.users.access_groups.assign(
            group_ids=["dd63031d-ce96-11e7-ad6c-06063970b924", "dd73031d-cf96-11e7-ad6c-06063970b994"],
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        )
        assert_matches_type(AccessGroupAssignResponse, access_group, path=["response"])

    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.access_groups.with_raw_response.assign(
            group_ids=["dd63031d-ce96-11e7-ad6c-06063970b924", "dd73031d-cf96-11e7-ad6c-06063970b994"],
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_group = await response.parse()
        assert_matches_type(AccessGroupAssignResponse, access_group, path=["response"])

    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.access_groups.with_streaming_response.assign(
            group_ids=["dd63031d-ce96-11e7-ad6c-06063970b924", "dd73031d-cf96-11e7-ad6c-06063970b994"],
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_group = await response.parse()
            assert_matches_type(AccessGroupAssignResponse, access_group, path=["response"])

        assert cast(Any, response.is_closed) is True
