# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.orgstructure import (
    UnitTypeListResponse,
    UnitTypeCreateResponse,
    UnitTypeUpdateResponse,
    UnitTypeRetrieveResponse,
    UnitTypeUpdateFieldResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUnitTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        unit_type = client.orgstructure.unit_types.create(
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )
        assert_matches_type(UnitTypeCreateResponse, unit_type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.orgstructure.unit_types.with_raw_response.create(
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = response.parse()
        assert_matches_type(UnitTypeCreateResponse, unit_type, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.orgstructure.unit_types.with_streaming_response.create(
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = response.parse()
            assert_matches_type(UnitTypeCreateResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        unit_type = client.orgstructure.unit_types.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UnitTypeRetrieveResponse, unit_type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.orgstructure.unit_types.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = response.parse()
        assert_matches_type(UnitTypeRetrieveResponse, unit_type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.orgstructure.unit_types.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = response.parse()
            assert_matches_type(UnitTypeRetrieveResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unit_type_id` but received ''"):
            client.orgstructure.unit_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        unit_type = client.orgstructure.unit_types.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )
        assert_matches_type(UnitTypeUpdateResponse, unit_type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.orgstructure.unit_types.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = response.parse()
        assert_matches_type(UnitTypeUpdateResponse, unit_type, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.orgstructure.unit_types.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = response.parse()
            assert_matches_type(UnitTypeUpdateResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unit_type_id` but received ''"):
            client.orgstructure.unit_types.with_raw_response.update(
                "",
                description="Typically when a large corporate is split into geographical units like North/South etc.",
                external_id="region_external_id",
                name="Region",
                status="active",
                type_id="REGION",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        unit_type = client.orgstructure.unit_types.list()
        assert_matches_type(UnitTypeListResponse, unit_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        unit_type = client.orgstructure.unit_types.list(
            limit=0,
            page=0,
        )
        assert_matches_type(UnitTypeListResponse, unit_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.orgstructure.unit_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = response.parse()
        assert_matches_type(UnitTypeListResponse, unit_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.orgstructure.unit_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = response.parse()
            assert_matches_type(UnitTypeListResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_field(self, client: SDK4human) -> None:
        unit_type = client.orgstructure.unit_types.update_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UnitTypeUpdateFieldResponse, unit_type, path=["response"])

    @parametrize
    def test_method_update_field_with_all_params(self, client: SDK4human) -> None:
        unit_type = client.orgstructure.unit_types.update_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )
        assert_matches_type(UnitTypeUpdateFieldResponse, unit_type, path=["response"])

    @parametrize
    def test_raw_response_update_field(self, client: SDK4human) -> None:
        response = client.orgstructure.unit_types.with_raw_response.update_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = response.parse()
        assert_matches_type(UnitTypeUpdateFieldResponse, unit_type, path=["response"])

    @parametrize
    def test_streaming_response_update_field(self, client: SDK4human) -> None:
        with client.orgstructure.unit_types.with_streaming_response.update_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = response.parse()
            assert_matches_type(UnitTypeUpdateFieldResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_field(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unit_type_id` but received ''"):
            client.orgstructure.unit_types.with_raw_response.update_field(
                "",
            )


class TestAsyncUnitTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        unit_type = await async_client.orgstructure.unit_types.create(
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )
        assert_matches_type(UnitTypeCreateResponse, unit_type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.unit_types.with_raw_response.create(
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = await response.parse()
        assert_matches_type(UnitTypeCreateResponse, unit_type, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.unit_types.with_streaming_response.create(
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = await response.parse()
            assert_matches_type(UnitTypeCreateResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        unit_type = await async_client.orgstructure.unit_types.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UnitTypeRetrieveResponse, unit_type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.unit_types.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = await response.parse()
        assert_matches_type(UnitTypeRetrieveResponse, unit_type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.unit_types.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = await response.parse()
            assert_matches_type(UnitTypeRetrieveResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unit_type_id` but received ''"):
            await async_client.orgstructure.unit_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        unit_type = await async_client.orgstructure.unit_types.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )
        assert_matches_type(UnitTypeUpdateResponse, unit_type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.unit_types.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = await response.parse()
        assert_matches_type(UnitTypeUpdateResponse, unit_type, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.unit_types.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = await response.parse()
            assert_matches_type(UnitTypeUpdateResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unit_type_id` but received ''"):
            await async_client.orgstructure.unit_types.with_raw_response.update(
                "",
                description="Typically when a large corporate is split into geographical units like North/South etc.",
                external_id="region_external_id",
                name="Region",
                status="active",
                type_id="REGION",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        unit_type = await async_client.orgstructure.unit_types.list()
        assert_matches_type(UnitTypeListResponse, unit_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        unit_type = await async_client.orgstructure.unit_types.list(
            limit=0,
            page=0,
        )
        assert_matches_type(UnitTypeListResponse, unit_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.unit_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = await response.parse()
        assert_matches_type(UnitTypeListResponse, unit_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.unit_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = await response.parse()
            assert_matches_type(UnitTypeListResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_field(self, async_client: AsyncSDK4human) -> None:
        unit_type = await async_client.orgstructure.unit_types.update_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UnitTypeUpdateFieldResponse, unit_type, path=["response"])

    @parametrize
    async def test_method_update_field_with_all_params(self, async_client: AsyncSDK4human) -> None:
        unit_type = await async_client.orgstructure.unit_types.update_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="Typically when a large corporate is split into geographical units like North/South etc.",
            external_id="region_external_id",
            name="Region",
            status="active",
            type_id="REGION",
        )
        assert_matches_type(UnitTypeUpdateFieldResponse, unit_type, path=["response"])

    @parametrize
    async def test_raw_response_update_field(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.unit_types.with_raw_response.update_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_type = await response.parse()
        assert_matches_type(UnitTypeUpdateFieldResponse, unit_type, path=["response"])

    @parametrize
    async def test_streaming_response_update_field(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.unit_types.with_streaming_response.update_field(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_type = await response.parse()
            assert_matches_type(UnitTypeUpdateFieldResponse, unit_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_field(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unit_type_id` but received ''"):
            await async_client.orgstructure.unit_types.with_raw_response.update_field(
                "",
            )
