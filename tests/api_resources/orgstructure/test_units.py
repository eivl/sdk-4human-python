# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.orgstructure import UnitUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUnits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        unit = client.orgstructure.units.update(
            "string",
            name="4Human Hrm",
            unit_id="D0001",
        )
        assert_matches_type(UnitUpdateResponse, unit, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        unit = client.orgstructure.units.update(
            "string",
            name="4Human Hrm",
            unit_id="D0001",
            external=True,
            custom_fields=[
                {
                    "field_id": "c799e3d9-e3b8-11eb-a317-0242ac12001f",
                    "value_id": "5adfe243-e3ba-11eb-a317-0242ac12001f",
                },
                {
                    "field_id": "ae94511b-a391-11ec-b67d-02012b4602c5",
                    "value_id": None,
                },
            ],
            manager_id=1,
            parent_id=1,
            selected_company_number="007",
            status="ACTIVE",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(UnitUpdateResponse, unit, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.orgstructure.units.with_raw_response.update(
            "string",
            name="4Human Hrm",
            unit_id="D0001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit = response.parse()
        assert_matches_type(UnitUpdateResponse, unit, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.orgstructure.units.with_streaming_response.update(
            "string",
            name="4Human Hrm",
            unit_id="D0001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit = response.parse()
            assert_matches_type(UnitUpdateResponse, unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_unit_id` but received ''"):
            client.orgstructure.units.with_raw_response.update(
                "",
                name="4Human Hrm",
                unit_id="D0001",
            )


class TestAsyncUnits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        unit = await async_client.orgstructure.units.update(
            "string",
            name="4Human Hrm",
            unit_id="D0001",
        )
        assert_matches_type(UnitUpdateResponse, unit, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        unit = await async_client.orgstructure.units.update(
            "string",
            name="4Human Hrm",
            unit_id="D0001",
            external=True,
            custom_fields=[
                {
                    "field_id": "c799e3d9-e3b8-11eb-a317-0242ac12001f",
                    "value_id": "5adfe243-e3ba-11eb-a317-0242ac12001f",
                },
                {
                    "field_id": "ae94511b-a391-11ec-b67d-02012b4602c5",
                    "value_id": None,
                },
            ],
            manager_id=1,
            parent_id=1,
            selected_company_number="007",
            status="ACTIVE",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(UnitUpdateResponse, unit, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.units.with_raw_response.update(
            "string",
            name="4Human Hrm",
            unit_id="D0001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit = await response.parse()
        assert_matches_type(UnitUpdateResponse, unit, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.units.with_streaming_response.update(
            "string",
            name="4Human Hrm",
            unit_id="D0001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit = await response.parse()
            assert_matches_type(UnitUpdateResponse, unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_unit_id` but received ''"):
            await async_client.orgstructure.units.with_raw_response.update(
                "",
                name="4Human Hrm",
                unit_id="D0001",
            )
