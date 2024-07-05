# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import UserListResponse, UserCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        user = client.users.create(
            email="email@domain.com",
            first_name="John",
            language="en",
            last_name="Smith",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        user = client.users.create(
            email="email@domain.com",
            first_name="John",
            language="en",
            last_name="Smith",
            send_invitation=True,
            access_groups=["e8055e4c-ce96-11e7-ad6c-06063970b924", "98a10692-01f1-4199-80dd-399ce987eebc"],
            active_directory_user_name="John_Smith",
            login_method="ACTIVE_DIRECTORY",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.users.with_raw_response.create(
            email="email@domain.com",
            first_name="John",
            language="en",
            last_name="Smith",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.users.with_streaming_response.create(
            email="email@domain.com",
            first_name="John",
            language="en",
            last_name="Smith",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        user = client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        user = client.users.list(
            filter="all",
            limit=0,
            org_units="string",
            page=0,
            query="string",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: SDK4human) -> None:
        user = client.users.delete(
            "string",
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: SDK4human) -> None:
        response = client.users.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: SDK4human) -> None:
        with client.users.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        user = await async_client.users.create(
            email="email@domain.com",
            first_name="John",
            language="en",
            last_name="Smith",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        user = await async_client.users.create(
            email="email@domain.com",
            first_name="John",
            language="en",
            last_name="Smith",
            send_invitation=True,
            access_groups=["e8055e4c-ce96-11e7-ad6c-06063970b924", "98a10692-01f1-4199-80dd-399ce987eebc"],
            active_directory_user_name="John_Smith",
            login_method="ACTIVE_DIRECTORY",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.with_raw_response.create(
            email="email@domain.com",
            first_name="John",
            language="en",
            last_name="Smith",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.with_streaming_response.create(
            email="email@domain.com",
            first_name="John",
            language="en",
            last_name="Smith",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        user = await async_client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        user = await async_client.users.list(
            filter="all",
            limit=0,
            org_units="string",
            page=0,
            query="string",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSDK4human) -> None:
        user = await async_client.users.delete(
            "string",
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )
