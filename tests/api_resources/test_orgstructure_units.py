# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import (
    OrgstructureUnitCreateResponse,
    OrgstructureUnitUpdateResponse,
    OrgstructureUnitRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrgstructureUnits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        orgstructure_unit = client.orgstructure_units.create(
            name="4Human",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(OrgstructureUnitCreateResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        orgstructure_unit = client.orgstructure_units.create(
            name="4Human",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            manager_id=1,
            parent_id=1,
            selected_company_number="string",
            status="ACTIVE",
            unit_id="unit005",
        )
        assert_matches_type(OrgstructureUnitCreateResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.orgstructure_units.with_raw_response.create(
            name="4Human",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orgstructure_unit = response.parse()
        assert_matches_type(OrgstructureUnitCreateResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.orgstructure_units.with_streaming_response.create(
            name="4Human",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orgstructure_unit = response.parse()
            assert_matches_type(OrgstructureUnitCreateResponse, orgstructure_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        orgstructure_unit = client.orgstructure_units.retrieve(
            "string",
        )
        assert_matches_type(OrgstructureUnitRetrieveResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        orgstructure_unit = client.orgstructure_units.retrieve(
            "string",
            external=True,
            with_soft_deleted=True,
        )
        assert_matches_type(OrgstructureUnitRetrieveResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.orgstructure_units.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orgstructure_unit = response.parse()
        assert_matches_type(OrgstructureUnitRetrieveResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.orgstructure_units.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orgstructure_unit = response.parse()
            assert_matches_type(OrgstructureUnitRetrieveResponse, orgstructure_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_unit_id` but received ''"):
            client.orgstructure_units.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        orgstructure_unit = client.orgstructure_units.update(
            "string",
            name="Main Unit",
            unit_id="unit002",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(OrgstructureUnitUpdateResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        orgstructure_unit = client.orgstructure_units.update(
            "string",
            name="Main Unit",
            unit_id="unit002",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            external=True,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            manager_id=1,
            parent_id=1,
            status="ACTIVE",
        )
        assert_matches_type(OrgstructureUnitUpdateResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.orgstructure_units.with_raw_response.update(
            "string",
            name="Main Unit",
            unit_id="unit002",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orgstructure_unit = response.parse()
        assert_matches_type(OrgstructureUnitUpdateResponse, orgstructure_unit, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.orgstructure_units.with_streaming_response.update(
            "string",
            name="Main Unit",
            unit_id="unit002",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orgstructure_unit = response.parse()
            assert_matches_type(OrgstructureUnitUpdateResponse, orgstructure_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_unit_id` but received ''"):
            client.orgstructure_units.with_raw_response.update(
                "",
                name="Main Unit",
                unit_id="unit002",
                unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            )


class TestAsyncOrgstructureUnits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        orgstructure_unit = await async_client.orgstructure_units.create(
            name="4Human",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(OrgstructureUnitCreateResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        orgstructure_unit = await async_client.orgstructure_units.create(
            name="4Human",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            manager_id=1,
            parent_id=1,
            selected_company_number="string",
            status="ACTIVE",
            unit_id="unit005",
        )
        assert_matches_type(OrgstructureUnitCreateResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure_units.with_raw_response.create(
            name="4Human",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orgstructure_unit = await response.parse()
        assert_matches_type(OrgstructureUnitCreateResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure_units.with_streaming_response.create(
            name="4Human",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orgstructure_unit = await response.parse()
            assert_matches_type(OrgstructureUnitCreateResponse, orgstructure_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        orgstructure_unit = await async_client.orgstructure_units.retrieve(
            "string",
        )
        assert_matches_type(OrgstructureUnitRetrieveResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        orgstructure_unit = await async_client.orgstructure_units.retrieve(
            "string",
            external=True,
            with_soft_deleted=True,
        )
        assert_matches_type(OrgstructureUnitRetrieveResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure_units.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orgstructure_unit = await response.parse()
        assert_matches_type(OrgstructureUnitRetrieveResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure_units.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orgstructure_unit = await response.parse()
            assert_matches_type(OrgstructureUnitRetrieveResponse, orgstructure_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_unit_id` but received ''"):
            await async_client.orgstructure_units.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        orgstructure_unit = await async_client.orgstructure_units.update(
            "string",
            name="Main Unit",
            unit_id="unit002",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(OrgstructureUnitUpdateResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        orgstructure_unit = await async_client.orgstructure_units.update(
            "string",
            name="Main Unit",
            unit_id="unit002",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            external=True,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            manager_id=1,
            parent_id=1,
            status="ACTIVE",
        )
        assert_matches_type(OrgstructureUnitUpdateResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure_units.with_raw_response.update(
            "string",
            name="Main Unit",
            unit_id="unit002",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orgstructure_unit = await response.parse()
        assert_matches_type(OrgstructureUnitUpdateResponse, orgstructure_unit, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure_units.with_streaming_response.update(
            "string",
            name="Main Unit",
            unit_id="unit002",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orgstructure_unit = await response.parse()
            assert_matches_type(OrgstructureUnitUpdateResponse, orgstructure_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_unit_id` but received ''"):
            await async_client.orgstructure_units.with_raw_response.update(
                "",
                name="Main Unit",
                unit_id="unit002",
                unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            )
