# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.custom_fields import (
    ValueCreateResponse,
    ValueUpdateResponse,
    ValueChangeStatusResponse,
    ValueUpdatePartialResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        value = client.custom_fields.values.create(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )
        assert_matches_type(ValueCreateResponse, value, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        value = client.custom_fields.values.create(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
            return_single_item=True,
        )
        assert_matches_type(ValueCreateResponse, value, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.custom_fields.values.with_raw_response.create(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(ValueCreateResponse, value, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.custom_fields.values.with_streaming_response.create(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(ValueCreateResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value_id` but received ''"):
            client.custom_fields.values.with_raw_response.create(
                "",
                external_id="main_office_city_001_external",
                external_name="Oslo - external",
                internal_id="main_office_city_001",
                name="Oslo",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        value = client.custom_fields.values.update(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        value = client.custom_fields.values.update(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
            return_single_item=True,
        )
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.custom_fields.values.with_raw_response.update(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.custom_fields.values.with_streaming_response.update(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(ValueUpdateResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value_id` but received ''"):
            client.custom_fields.values.with_raw_response.update(
                "",
                external_id="main_office_city_001_external",
                external_name="Oslo - external",
                internal_id="main_office_city_001",
                name="Oslo",
            )

    @parametrize
    def test_method_change_status(self, client: SDK4human) -> None:
        value = client.custom_fields.values.change_status(
            "string",
        )
        assert_matches_type(ValueChangeStatusResponse, value, path=["response"])

    @parametrize
    def test_method_change_status_with_all_params(self, client: SDK4human) -> None:
        value = client.custom_fields.values.change_status(
            "string",
            return_single_item=True,
            id="ACTIVE",
        )
        assert_matches_type(ValueChangeStatusResponse, value, path=["response"])

    @parametrize
    def test_raw_response_change_status(self, client: SDK4human) -> None:
        response = client.custom_fields.values.with_raw_response.change_status(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(ValueChangeStatusResponse, value, path=["response"])

    @parametrize
    def test_streaming_response_change_status(self, client: SDK4human) -> None:
        with client.custom_fields.values.with_streaming_response.change_status(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(ValueChangeStatusResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_change_status(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value_id` but received ''"):
            client.custom_fields.values.with_raw_response.change_status(
                "",
            )

    @parametrize
    def test_method_update_partial(self, client: SDK4human) -> None:
        value = client.custom_fields.values.update_partial(
            "string",
        )
        assert_matches_type(ValueUpdatePartialResponse, value, path=["response"])

    @parametrize
    def test_method_update_partial_with_all_params(self, client: SDK4human) -> None:
        value = client.custom_fields.values.update_partial(
            "string",
            return_single_item=True,
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )
        assert_matches_type(ValueUpdatePartialResponse, value, path=["response"])

    @parametrize
    def test_raw_response_update_partial(self, client: SDK4human) -> None:
        response = client.custom_fields.values.with_raw_response.update_partial(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(ValueUpdatePartialResponse, value, path=["response"])

    @parametrize
    def test_streaming_response_update_partial(self, client: SDK4human) -> None:
        with client.custom_fields.values.with_streaming_response.update_partial(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(ValueUpdatePartialResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_partial(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value_id` but received ''"):
            client.custom_fields.values.with_raw_response.update_partial(
                "",
            )


class TestAsyncValues:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        value = await async_client.custom_fields.values.create(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )
        assert_matches_type(ValueCreateResponse, value, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        value = await async_client.custom_fields.values.create(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
            return_single_item=True,
        )
        assert_matches_type(ValueCreateResponse, value, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.values.with_raw_response.create(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(ValueCreateResponse, value, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.values.with_streaming_response.create(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(ValueCreateResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value_id` but received ''"):
            await async_client.custom_fields.values.with_raw_response.create(
                "",
                external_id="main_office_city_001_external",
                external_name="Oslo - external",
                internal_id="main_office_city_001",
                name="Oslo",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        value = await async_client.custom_fields.values.update(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        value = await async_client.custom_fields.values.update(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
            return_single_item=True,
        )
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.values.with_raw_response.update(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.values.with_streaming_response.update(
            "string",
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(ValueUpdateResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value_id` but received ''"):
            await async_client.custom_fields.values.with_raw_response.update(
                "",
                external_id="main_office_city_001_external",
                external_name="Oslo - external",
                internal_id="main_office_city_001",
                name="Oslo",
            )

    @parametrize
    async def test_method_change_status(self, async_client: AsyncSDK4human) -> None:
        value = await async_client.custom_fields.values.change_status(
            "string",
        )
        assert_matches_type(ValueChangeStatusResponse, value, path=["response"])

    @parametrize
    async def test_method_change_status_with_all_params(self, async_client: AsyncSDK4human) -> None:
        value = await async_client.custom_fields.values.change_status(
            "string",
            return_single_item=True,
            id="ACTIVE",
        )
        assert_matches_type(ValueChangeStatusResponse, value, path=["response"])

    @parametrize
    async def test_raw_response_change_status(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.values.with_raw_response.change_status(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(ValueChangeStatusResponse, value, path=["response"])

    @parametrize
    async def test_streaming_response_change_status(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.values.with_streaming_response.change_status(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(ValueChangeStatusResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_change_status(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value_id` but received ''"):
            await async_client.custom_fields.values.with_raw_response.change_status(
                "",
            )

    @parametrize
    async def test_method_update_partial(self, async_client: AsyncSDK4human) -> None:
        value = await async_client.custom_fields.values.update_partial(
            "string",
        )
        assert_matches_type(ValueUpdatePartialResponse, value, path=["response"])

    @parametrize
    async def test_method_update_partial_with_all_params(self, async_client: AsyncSDK4human) -> None:
        value = await async_client.custom_fields.values.update_partial(
            "string",
            return_single_item=True,
            external_id="main_office_city_001_external",
            external_name="Oslo - external",
            internal_id="main_office_city_001",
            name="Oslo",
        )
        assert_matches_type(ValueUpdatePartialResponse, value, path=["response"])

    @parametrize
    async def test_raw_response_update_partial(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.values.with_raw_response.update_partial(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(ValueUpdatePartialResponse, value, path=["response"])

    @parametrize
    async def test_streaming_response_update_partial(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.values.with_streaming_response.update_partial(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(ValueUpdatePartialResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_partial(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value_id` but received ''"):
            await async_client.custom_fields.values.with_raw_response.update_partial(
                "",
            )
