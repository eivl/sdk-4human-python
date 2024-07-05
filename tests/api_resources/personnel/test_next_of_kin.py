# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import NextOfKinUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNextOfKin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        next_of_kin = client.personnel.next_of_kin.update(
            "string",
        )
        assert_matches_type(NextOfKinUpdateResponse, next_of_kin, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        next_of_kin = client.personnel.next_of_kin.update(
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
            gender="M",
            relationship_type="partner",
            surname="Doe",
        )
        assert_matches_type(NextOfKinUpdateResponse, next_of_kin, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.next_of_kin.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_of_kin = response.parse()
        assert_matches_type(NextOfKinUpdateResponse, next_of_kin, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.next_of_kin.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_of_kin = response.parse()
            assert_matches_type(NextOfKinUpdateResponse, next_of_kin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `next_of_kin_id` but received ''"):
            client.personnel.next_of_kin.with_raw_response.update(
                "",
            )


class TestAsyncNextOfKin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        next_of_kin = await async_client.personnel.next_of_kin.update(
            "string",
        )
        assert_matches_type(NextOfKinUpdateResponse, next_of_kin, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        next_of_kin = await async_client.personnel.next_of_kin.update(
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
            gender="M",
            relationship_type="partner",
            surname="Doe",
        )
        assert_matches_type(NextOfKinUpdateResponse, next_of_kin, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.next_of_kin.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        next_of_kin = await response.parse()
        assert_matches_type(NextOfKinUpdateResponse, next_of_kin, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.next_of_kin.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            next_of_kin = await response.parse()
            assert_matches_type(NextOfKinUpdateResponse, next_of_kin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `next_of_kin_id` but received ''"):
            await async_client.personnel.next_of_kin.with_raw_response.update(
                "",
            )
