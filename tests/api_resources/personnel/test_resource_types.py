# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import (
    ResourceTypeCreateResponse,
    ResourceTypeUpdateResponse,
    ResourceTypeRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResourceTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        resource_type = client.personnel.resource_types.create(
            description="BACKEND_DEFAULT_DESCRIPTION_RESOURCE_TYPE_F",
            name="BACKEND_DEFAULT_NAME_RESOURCE_TYPE_F",
            type_id="F",
        )
        assert_matches_type(ResourceTypeCreateResponse, resource_type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.resource_types.with_raw_response.create(
            description="BACKEND_DEFAULT_DESCRIPTION_RESOURCE_TYPE_F",
            name="BACKEND_DEFAULT_NAME_RESOURCE_TYPE_F",
            type_id="F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_type = response.parse()
        assert_matches_type(ResourceTypeCreateResponse, resource_type, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.resource_types.with_streaming_response.create(
            description="BACKEND_DEFAULT_DESCRIPTION_RESOURCE_TYPE_F",
            name="BACKEND_DEFAULT_NAME_RESOURCE_TYPE_F",
            type_id="F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_type = response.parse()
            assert_matches_type(ResourceTypeCreateResponse, resource_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        resource_type = client.personnel.resource_types.retrieve(
            "string",
        )
        assert_matches_type(ResourceTypeRetrieveResponse, resource_type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.personnel.resource_types.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_type = response.parse()
        assert_matches_type(ResourceTypeRetrieveResponse, resource_type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.personnel.resource_types.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_type = response.parse()
            assert_matches_type(ResourceTypeRetrieveResponse, resource_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_type_id` but received ''"):
            client.personnel.resource_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        resource_type = client.personnel.resource_types.update(
            "string",
        )
        assert_matches_type(ResourceTypeUpdateResponse, resource_type, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        resource_type = client.personnel.resource_types.update(
            "string",
            description="BACKEND_DEFAULT_DESCRIPTION_RESOURCE_TYPE_F",
            name="BACKEND_DEFAULT_NAME_RESOURCE_TYPE_F",
            status="active",
            type_id="F",
        )
        assert_matches_type(ResourceTypeUpdateResponse, resource_type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.resource_types.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_type = response.parse()
        assert_matches_type(ResourceTypeUpdateResponse, resource_type, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.resource_types.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_type = response.parse()
            assert_matches_type(ResourceTypeUpdateResponse, resource_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_type_id` but received ''"):
            client.personnel.resource_types.with_raw_response.update(
                "",
            )


class TestAsyncResourceTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        resource_type = await async_client.personnel.resource_types.create(
            description="BACKEND_DEFAULT_DESCRIPTION_RESOURCE_TYPE_F",
            name="BACKEND_DEFAULT_NAME_RESOURCE_TYPE_F",
            type_id="F",
        )
        assert_matches_type(ResourceTypeCreateResponse, resource_type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.resource_types.with_raw_response.create(
            description="BACKEND_DEFAULT_DESCRIPTION_RESOURCE_TYPE_F",
            name="BACKEND_DEFAULT_NAME_RESOURCE_TYPE_F",
            type_id="F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_type = await response.parse()
        assert_matches_type(ResourceTypeCreateResponse, resource_type, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.resource_types.with_streaming_response.create(
            description="BACKEND_DEFAULT_DESCRIPTION_RESOURCE_TYPE_F",
            name="BACKEND_DEFAULT_NAME_RESOURCE_TYPE_F",
            type_id="F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_type = await response.parse()
            assert_matches_type(ResourceTypeCreateResponse, resource_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        resource_type = await async_client.personnel.resource_types.retrieve(
            "string",
        )
        assert_matches_type(ResourceTypeRetrieveResponse, resource_type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.resource_types.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_type = await response.parse()
        assert_matches_type(ResourceTypeRetrieveResponse, resource_type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.resource_types.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_type = await response.parse()
            assert_matches_type(ResourceTypeRetrieveResponse, resource_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_type_id` but received ''"):
            await async_client.personnel.resource_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        resource_type = await async_client.personnel.resource_types.update(
            "string",
        )
        assert_matches_type(ResourceTypeUpdateResponse, resource_type, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        resource_type = await async_client.personnel.resource_types.update(
            "string",
            description="BACKEND_DEFAULT_DESCRIPTION_RESOURCE_TYPE_F",
            name="BACKEND_DEFAULT_NAME_RESOURCE_TYPE_F",
            status="active",
            type_id="F",
        )
        assert_matches_type(ResourceTypeUpdateResponse, resource_type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.resource_types.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_type = await response.parse()
        assert_matches_type(ResourceTypeUpdateResponse, resource_type, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.resource_types.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_type = await response.parse()
            assert_matches_type(ResourceTypeUpdateResponse, resource_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_type_id` but received ''"):
            await async_client.personnel.resource_types.with_raw_response.update(
                "",
            )
