# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human._utils import parse_datetime
from sdk_minus_4human.types.users import PersonalDetailUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPersonalDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        personal_detail = client.users.personal_details.update(
            "string",
        )
        assert_matches_type(PersonalDetailUpdateResponse, personal_detail, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        personal_detail = client.users.personal_details.update(
            "string",
            force_no_approval_policy=True,
            alias="Grand Master",
            country_of_origin="NOR",
            date_of_birth=parse_datetime("1980-01-16T00:00:00Z"),
            first_name="John",
            gender="M",
            initials="JD",
            marital_status="unmarried",
            nationality="NOR",
            surname="Doe",
        )
        assert_matches_type(PersonalDetailUpdateResponse, personal_detail, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.users.personal_details.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_detail = response.parse()
        assert_matches_type(PersonalDetailUpdateResponse, personal_detail, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.users.personal_details.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_detail = response.parse()
            assert_matches_type(PersonalDetailUpdateResponse, personal_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.personal_details.with_raw_response.update(
                "",
            )


class TestAsyncPersonalDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        personal_detail = await async_client.users.personal_details.update(
            "string",
        )
        assert_matches_type(PersonalDetailUpdateResponse, personal_detail, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        personal_detail = await async_client.users.personal_details.update(
            "string",
            force_no_approval_policy=True,
            alias="Grand Master",
            country_of_origin="NOR",
            date_of_birth=parse_datetime("1980-01-16T00:00:00Z"),
            first_name="John",
            gender="M",
            initials="JD",
            marital_status="unmarried",
            nationality="NOR",
            surname="Doe",
        )
        assert_matches_type(PersonalDetailUpdateResponse, personal_detail, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.personal_details.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_detail = await response.parse()
        assert_matches_type(PersonalDetailUpdateResponse, personal_detail, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.personal_details.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_detail = await response.parse()
            assert_matches_type(PersonalDetailUpdateResponse, personal_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.personal_details.with_raw_response.update(
                "",
            )
