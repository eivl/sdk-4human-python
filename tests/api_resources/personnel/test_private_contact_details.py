# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import PrivateContactDetailUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrivateContactDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        private_contact_detail = client.personnel.private_contact_details.update(
            "string",
        )
        assert_matches_type(PrivateContactDetailUpdateResponse, private_contact_detail, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        private_contact_detail = client.personnel.private_contact_details.update(
            "string",
            force_no_approval_policy=True,
            address_info=[
                {
                    "id": 1,
                    "type": "primary",
                    "name": "Private address in Oslo",
                    "post_address": {
                        "address": "string",
                        "zip_code": "string",
                        "city": "string",
                        "municipality": "string",
                        "building_entrance": "string",
                        "country": "xxx",
                    },
                    "visit_address": {
                        "address": "Sverres Gate 73",
                        "zip_code": "0652",
                        "city": "Oslo",
                        "municipality": "Oslo",
                        "building_entrance": None,
                        "country": "NOR",
                    },
                },
                {
                    "id": None,
                    "type": "additional",
                    "name": "Private address in Trondheim",
                    "post_address": {
                        "address": "string",
                        "zip_code": "string",
                        "city": "string",
                        "municipality": "string",
                        "building_entrance": "string",
                        "country": "xxx",
                    },
                    "visit_address": {
                        "address": None,
                        "zip_code": "7068",
                        "city": "Trondheim",
                        "municipality": None,
                        "building_entrance": None,
                        "country": "NOR",
                    },
                },
            ],
            contact_info={
                "mobile_phone": "100100100",
                "phone": "200200200",
                "email": "private@email.com",
                "additional_contact": [
                    {
                        "name": "string",
                        "value": "string",
                    },
                    {
                        "name": "string",
                        "value": "string",
                    },
                    {
                        "name": "string",
                        "value": "string",
                    },
                ],
            },
        )
        assert_matches_type(PrivateContactDetailUpdateResponse, private_contact_detail, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.private_contact_details.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private_contact_detail = response.parse()
        assert_matches_type(PrivateContactDetailUpdateResponse, private_contact_detail, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.private_contact_details.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private_contact_detail = response.parse()
            assert_matches_type(PrivateContactDetailUpdateResponse, private_contact_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.personnel.private_contact_details.with_raw_response.update(
                "",
            )


class TestAsyncPrivateContactDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        private_contact_detail = await async_client.personnel.private_contact_details.update(
            "string",
        )
        assert_matches_type(PrivateContactDetailUpdateResponse, private_contact_detail, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        private_contact_detail = await async_client.personnel.private_contact_details.update(
            "string",
            force_no_approval_policy=True,
            address_info=[
                {
                    "id": 1,
                    "type": "primary",
                    "name": "Private address in Oslo",
                    "post_address": {
                        "address": "string",
                        "zip_code": "string",
                        "city": "string",
                        "municipality": "string",
                        "building_entrance": "string",
                        "country": "xxx",
                    },
                    "visit_address": {
                        "address": "Sverres Gate 73",
                        "zip_code": "0652",
                        "city": "Oslo",
                        "municipality": "Oslo",
                        "building_entrance": None,
                        "country": "NOR",
                    },
                },
                {
                    "id": None,
                    "type": "additional",
                    "name": "Private address in Trondheim",
                    "post_address": {
                        "address": "string",
                        "zip_code": "string",
                        "city": "string",
                        "municipality": "string",
                        "building_entrance": "string",
                        "country": "xxx",
                    },
                    "visit_address": {
                        "address": None,
                        "zip_code": "7068",
                        "city": "Trondheim",
                        "municipality": None,
                        "building_entrance": None,
                        "country": "NOR",
                    },
                },
            ],
            contact_info={
                "mobile_phone": "100100100",
                "phone": "200200200",
                "email": "private@email.com",
                "additional_contact": [
                    {
                        "name": "string",
                        "value": "string",
                    },
                    {
                        "name": "string",
                        "value": "string",
                    },
                    {
                        "name": "string",
                        "value": "string",
                    },
                ],
            },
        )
        assert_matches_type(PrivateContactDetailUpdateResponse, private_contact_detail, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.private_contact_details.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private_contact_detail = await response.parse()
        assert_matches_type(PrivateContactDetailUpdateResponse, private_contact_detail, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.private_contact_details.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private_contact_detail = await response.parse()
            assert_matches_type(PrivateContactDetailUpdateResponse, private_contact_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.personnel.private_contact_details.with_raw_response.update(
                "",
            )
