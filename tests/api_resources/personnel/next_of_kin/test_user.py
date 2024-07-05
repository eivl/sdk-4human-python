# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel.next_of_kin import UserListResponse, UserCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        user = client.personnel.next_of_kin.user.create(
            "string",
            address={
                "email": "example@email.com",
                "phone": "+48 888 999 888",
                "country": "PL",
                "city": "Warsaw",
                "address_line1": "ul. Dzielna 7B",
                "address_line2": None,
                "zip_code": "00-154",
            },
            comment="comment",
            firstname="John",
            relationship_type="partner",
            surname="Doe",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        user = client.personnel.next_of_kin.user.create(
            "string",
            address={
                "email": "example@email.com",
                "phone": "+48 888 999 888",
                "country": "PL",
                "city": "Warsaw",
                "address_line1": "ul. Dzielna 7B",
                "address_line2": None,
                "zip_code": "00-154",
            },
            comment="comment",
            firstname="John",
            relationship_type="partner",
            surname="Doe",
            external_id="next-01",
            force_external_id=True,
            gender="M",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.next_of_kin.user.with_raw_response.create(
            "string",
            address={
                "email": "example@email.com",
                "phone": "+48 888 999 888",
                "country": "PL",
                "city": "Warsaw",
                "address_line1": "ul. Dzielna 7B",
                "address_line2": None,
                "zip_code": "00-154",
            },
            comment="comment",
            firstname="John",
            relationship_type="partner",
            surname="Doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.next_of_kin.user.with_streaming_response.create(
            "string",
            address={
                "email": "example@email.com",
                "phone": "+48 888 999 888",
                "country": "PL",
                "city": "Warsaw",
                "address_line1": "ul. Dzielna 7B",
                "address_line2": None,
                "zip_code": "00-154",
            },
            comment="comment",
            firstname="John",
            relationship_type="partner",
            surname="Doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.personnel.next_of_kin.user.with_raw_response.create(
                "",
                address={
                    "email": "example@email.com",
                    "phone": "+48 888 999 888",
                    "country": "PL",
                    "city": "Warsaw",
                    "address_line1": "ul. Dzielna 7B",
                    "address_line2": None,
                    "zip_code": "00-154",
                },
                comment="comment",
                firstname="John",
                relationship_type="partner",
                surname="Doe",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        user = client.personnel.next_of_kin.user.list(
            "string",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.personnel.next_of_kin.user.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.personnel.next_of_kin.user.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.personnel.next_of_kin.user.with_raw_response.list(
                "",
            )


class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        user = await async_client.personnel.next_of_kin.user.create(
            "string",
            address={
                "email": "example@email.com",
                "phone": "+48 888 999 888",
                "country": "PL",
                "city": "Warsaw",
                "address_line1": "ul. Dzielna 7B",
                "address_line2": None,
                "zip_code": "00-154",
            },
            comment="comment",
            firstname="John",
            relationship_type="partner",
            surname="Doe",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        user = await async_client.personnel.next_of_kin.user.create(
            "string",
            address={
                "email": "example@email.com",
                "phone": "+48 888 999 888",
                "country": "PL",
                "city": "Warsaw",
                "address_line1": "ul. Dzielna 7B",
                "address_line2": None,
                "zip_code": "00-154",
            },
            comment="comment",
            firstname="John",
            relationship_type="partner",
            surname="Doe",
            external_id="next-01",
            force_external_id=True,
            gender="M",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.next_of_kin.user.with_raw_response.create(
            "string",
            address={
                "email": "example@email.com",
                "phone": "+48 888 999 888",
                "country": "PL",
                "city": "Warsaw",
                "address_line1": "ul. Dzielna 7B",
                "address_line2": None,
                "zip_code": "00-154",
            },
            comment="comment",
            firstname="John",
            relationship_type="partner",
            surname="Doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.next_of_kin.user.with_streaming_response.create(
            "string",
            address={
                "email": "example@email.com",
                "phone": "+48 888 999 888",
                "country": "PL",
                "city": "Warsaw",
                "address_line1": "ul. Dzielna 7B",
                "address_line2": None,
                "zip_code": "00-154",
            },
            comment="comment",
            firstname="John",
            relationship_type="partner",
            surname="Doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.personnel.next_of_kin.user.with_raw_response.create(
                "",
                address={
                    "email": "example@email.com",
                    "phone": "+48 888 999 888",
                    "country": "PL",
                    "city": "Warsaw",
                    "address_line1": "ul. Dzielna 7B",
                    "address_line2": None,
                    "zip_code": "00-154",
                },
                comment="comment",
                firstname="John",
                relationship_type="partner",
                surname="Doe",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        user = await async_client.personnel.next_of_kin.user.list(
            "string",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.next_of_kin.user.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.next_of_kin.user.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.personnel.next_of_kin.user.with_raw_response.list(
                "",
            )
