# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import CustomFieldChangeStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_change_status(self, client: SDK4human) -> None:
        custom_field = client.personnel.custom_fields.change_status(
            path_id="string",
        )
        assert_matches_type(CustomFieldChangeStatusResponse, custom_field, path=["response"])

    @parametrize
    def test_method_change_status_with_all_params(self, client: SDK4human) -> None:
        custom_field = client.personnel.custom_fields.change_status(
            path_id="string",
            body_id="ACTIVE",
        )
        assert_matches_type(CustomFieldChangeStatusResponse, custom_field, path=["response"])

    @parametrize
    def test_raw_response_change_status(self, client: SDK4human) -> None:
        response = client.personnel.custom_fields.with_raw_response.change_status(
            path_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert_matches_type(CustomFieldChangeStatusResponse, custom_field, path=["response"])

    @parametrize
    def test_streaming_response_change_status(self, client: SDK4human) -> None:
        with client.personnel.custom_fields.with_streaming_response.change_status(
            path_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert_matches_type(CustomFieldChangeStatusResponse, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_change_status(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.personnel.custom_fields.with_raw_response.change_status(
                path_id="",
                body_id="",
            )


class TestAsyncCustomFields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_change_status(self, async_client: AsyncSDK4human) -> None:
        custom_field = await async_client.personnel.custom_fields.change_status(
            path_id="string",
        )
        assert_matches_type(CustomFieldChangeStatusResponse, custom_field, path=["response"])

    @parametrize
    async def test_method_change_status_with_all_params(self, async_client: AsyncSDK4human) -> None:
        custom_field = await async_client.personnel.custom_fields.change_status(
            path_id="string",
            body_id="ACTIVE",
        )
        assert_matches_type(CustomFieldChangeStatusResponse, custom_field, path=["response"])

    @parametrize
    async def test_raw_response_change_status(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.custom_fields.with_raw_response.change_status(
            path_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert_matches_type(CustomFieldChangeStatusResponse, custom_field, path=["response"])

    @parametrize
    async def test_streaming_response_change_status(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.custom_fields.with_streaming_response.change_status(
            path_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert_matches_type(CustomFieldChangeStatusResponse, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_change_status(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.personnel.custom_fields.with_raw_response.change_status(
                path_id="",
                body_id="",
            )
