# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel.custom_fields.fields import (
    DimensionCreateResponse,
    DimensionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDimensions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        dimension = client.personnel.custom_fields.fields.dimensions.create(
            "string",
            external_id="dimension_001_external",
            external_name="Main Office - external",
            internal_id="dimension_001",
            name="Main Office",
        )
        assert_matches_type(DimensionCreateResponse, dimension, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.custom_fields.fields.dimensions.with_raw_response.create(
            "string",
            external_id="dimension_001_external",
            external_name="Main Office - external",
            internal_id="dimension_001",
            name="Main Office",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimension = response.parse()
        assert_matches_type(DimensionCreateResponse, dimension, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.custom_fields.fields.dimensions.with_streaming_response.create(
            "string",
            external_id="dimension_001_external",
            external_name="Main Office - external",
            internal_id="dimension_001",
            name="Main Office",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimension = response.parse()
            assert_matches_type(DimensionCreateResponse, dimension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            client.personnel.custom_fields.fields.dimensions.with_raw_response.create(
                "",
                external_id="dimension_001_external",
                external_name="Main Office - external",
                internal_id="dimension_001",
                name="Main Office",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        dimension = client.personnel.custom_fields.fields.dimensions.update(
            "string",
        )
        assert_matches_type(DimensionUpdateResponse, dimension, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        dimension = client.personnel.custom_fields.fields.dimensions.update(
            "string",
            external_id="dimension_001_external",
            external_name="Main Office - external",
            internal_id="dimension_001",
            name="Main Office",
        )
        assert_matches_type(DimensionUpdateResponse, dimension, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.custom_fields.fields.dimensions.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimension = response.parse()
        assert_matches_type(DimensionUpdateResponse, dimension, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.custom_fields.fields.dimensions.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimension = response.parse()
            assert_matches_type(DimensionUpdateResponse, dimension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dimension_id` but received ''"):
            client.personnel.custom_fields.fields.dimensions.with_raw_response.update(
                "",
            )


class TestAsyncDimensions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        dimension = await async_client.personnel.custom_fields.fields.dimensions.create(
            "string",
            external_id="dimension_001_external",
            external_name="Main Office - external",
            internal_id="dimension_001",
            name="Main Office",
        )
        assert_matches_type(DimensionCreateResponse, dimension, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.custom_fields.fields.dimensions.with_raw_response.create(
            "string",
            external_id="dimension_001_external",
            external_name="Main Office - external",
            internal_id="dimension_001",
            name="Main Office",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimension = await response.parse()
        assert_matches_type(DimensionCreateResponse, dimension, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.custom_fields.fields.dimensions.with_streaming_response.create(
            "string",
            external_id="dimension_001_external",
            external_name="Main Office - external",
            internal_id="dimension_001",
            name="Main Office",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimension = await response.parse()
            assert_matches_type(DimensionCreateResponse, dimension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            await async_client.personnel.custom_fields.fields.dimensions.with_raw_response.create(
                "",
                external_id="dimension_001_external",
                external_name="Main Office - external",
                internal_id="dimension_001",
                name="Main Office",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        dimension = await async_client.personnel.custom_fields.fields.dimensions.update(
            "string",
        )
        assert_matches_type(DimensionUpdateResponse, dimension, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        dimension = await async_client.personnel.custom_fields.fields.dimensions.update(
            "string",
            external_id="dimension_001_external",
            external_name="Main Office - external",
            internal_id="dimension_001",
            name="Main Office",
        )
        assert_matches_type(DimensionUpdateResponse, dimension, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.custom_fields.fields.dimensions.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimension = await response.parse()
        assert_matches_type(DimensionUpdateResponse, dimension, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.custom_fields.fields.dimensions.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimension = await response.parse()
            assert_matches_type(DimensionUpdateResponse, dimension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dimension_id` but received ''"):
            await async_client.personnel.custom_fields.fields.dimensions.with_raw_response.update(
                "",
            )
