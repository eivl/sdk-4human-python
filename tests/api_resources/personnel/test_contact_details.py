# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import ContactDetailUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContactDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        contact_detail = client.personnel.contact_details.update(
            "string",
        )
        assert_matches_type(ContactDetailUpdateResponse, contact_detail, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        contact_detail = client.personnel.contact_details.update(
            "string",
            force_no_approval_policy=True,
            address="Sverres Gate 73",
            building_entrance=None,
            city="Oslo",
            country="NOR",
            municipality="Oslo",
            private_email="private@email.com",
            private_mobile_phone="100100100",
            private_phone="200200200",
            work_email="work@email.com",
            work_mobile_phone="900900900",
            work_phone="800800800",
            zip_code="0652",
        )
        assert_matches_type(ContactDetailUpdateResponse, contact_detail, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.contact_details.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_detail = response.parse()
        assert_matches_type(ContactDetailUpdateResponse, contact_detail, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.contact_details.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_detail = response.parse()
            assert_matches_type(ContactDetailUpdateResponse, contact_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.personnel.contact_details.with_raw_response.update(
                "",
            )


class TestAsyncContactDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        contact_detail = await async_client.personnel.contact_details.update(
            "string",
        )
        assert_matches_type(ContactDetailUpdateResponse, contact_detail, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        contact_detail = await async_client.personnel.contact_details.update(
            "string",
            force_no_approval_policy=True,
            address="Sverres Gate 73",
            building_entrance=None,
            city="Oslo",
            country="NOR",
            municipality="Oslo",
            private_email="private@email.com",
            private_mobile_phone="100100100",
            private_phone="200200200",
            work_email="work@email.com",
            work_mobile_phone="900900900",
            work_phone="800800800",
            zip_code="0652",
        )
        assert_matches_type(ContactDetailUpdateResponse, contact_detail, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.contact_details.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_detail = await response.parse()
        assert_matches_type(ContactDetailUpdateResponse, contact_detail, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.contact_details.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_detail = await response.parse()
            assert_matches_type(ContactDetailUpdateResponse, contact_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.personnel.contact_details.with_raw_response.update(
                "",
            )
