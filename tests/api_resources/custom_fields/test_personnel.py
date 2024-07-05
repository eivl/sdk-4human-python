# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.custom_fields import (
    PersonnelUpdateResponse,
    PersonnelUpdateByNameResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPersonnel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        personnel = client.custom_fields.personnel.update(
            "string",
        )
        assert_matches_type(PersonnelUpdateResponse, personnel, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        personnel = client.custom_fields.personnel.update(
            "string",
            force_no_approval_policy=True,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": None,
                }
            ],
        )
        assert_matches_type(PersonnelUpdateResponse, personnel, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.custom_fields.personnel.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnel = response.parse()
        assert_matches_type(PersonnelUpdateResponse, personnel, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.custom_fields.personnel.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnel = response.parse()
            assert_matches_type(PersonnelUpdateResponse, personnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.custom_fields.personnel.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_update_by_name(self, client: SDK4human) -> None:
        personnel = client.custom_fields.personnel.update_by_name(
            "string",
        )
        assert_matches_type(PersonnelUpdateByNameResponse, personnel, path=["response"])

    @parametrize
    def test_method_update_by_name_with_all_params(self, client: SDK4human) -> None:
        personnel = client.custom_fields.personnel.update_by_name(
            "string",
            force_no_approval_policy=True,
            custom_fields=[
                {
                    "field_external_id": "salary",
                    "field_external_name": "string",
                    "value_external_id": "bigValue",
                    "value_external_name": "string",
                    "value": "string",
                },
                {
                    "field_external_id": "string",
                    "field_external_name": "salaryExternalName",
                    "value_external_id": "string",
                    "value_external_name": "bigExternalValue",
                    "value": "string",
                },
                {
                    "field_external_id": "email",
                    "field_external_name": "string",
                    "value_external_id": "string",
                    "value_external_name": "string",
                    "value": "user@example.com",
                },
            ],
        )
        assert_matches_type(PersonnelUpdateByNameResponse, personnel, path=["response"])

    @parametrize
    def test_raw_response_update_by_name(self, client: SDK4human) -> None:
        response = client.custom_fields.personnel.with_raw_response.update_by_name(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnel = response.parse()
        assert_matches_type(PersonnelUpdateByNameResponse, personnel, path=["response"])

    @parametrize
    def test_streaming_response_update_by_name(self, client: SDK4human) -> None:
        with client.custom_fields.personnel.with_streaming_response.update_by_name(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnel = response.parse()
            assert_matches_type(PersonnelUpdateByNameResponse, personnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_name(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.custom_fields.personnel.with_raw_response.update_by_name(
                "",
            )


class TestAsyncPersonnel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        personnel = await async_client.custom_fields.personnel.update(
            "string",
        )
        assert_matches_type(PersonnelUpdateResponse, personnel, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        personnel = await async_client.custom_fields.personnel.update(
            "string",
            force_no_approval_policy=True,
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": None,
                }
            ],
        )
        assert_matches_type(PersonnelUpdateResponse, personnel, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.personnel.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnel = await response.parse()
        assert_matches_type(PersonnelUpdateResponse, personnel, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.personnel.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnel = await response.parse()
            assert_matches_type(PersonnelUpdateResponse, personnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.custom_fields.personnel.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_update_by_name(self, async_client: AsyncSDK4human) -> None:
        personnel = await async_client.custom_fields.personnel.update_by_name(
            "string",
        )
        assert_matches_type(PersonnelUpdateByNameResponse, personnel, path=["response"])

    @parametrize
    async def test_method_update_by_name_with_all_params(self, async_client: AsyncSDK4human) -> None:
        personnel = await async_client.custom_fields.personnel.update_by_name(
            "string",
            force_no_approval_policy=True,
            custom_fields=[
                {
                    "field_external_id": "salary",
                    "field_external_name": "string",
                    "value_external_id": "bigValue",
                    "value_external_name": "string",
                    "value": "string",
                },
                {
                    "field_external_id": "string",
                    "field_external_name": "salaryExternalName",
                    "value_external_id": "string",
                    "value_external_name": "bigExternalValue",
                    "value": "string",
                },
                {
                    "field_external_id": "email",
                    "field_external_name": "string",
                    "value_external_id": "string",
                    "value_external_name": "string",
                    "value": "user@example.com",
                },
            ],
        )
        assert_matches_type(PersonnelUpdateByNameResponse, personnel, path=["response"])

    @parametrize
    async def test_raw_response_update_by_name(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.personnel.with_raw_response.update_by_name(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personnel = await response.parse()
        assert_matches_type(PersonnelUpdateByNameResponse, personnel, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_name(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.personnel.with_streaming_response.update_by_name(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personnel = await response.parse()
            assert_matches_type(PersonnelUpdateByNameResponse, personnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_name(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.custom_fields.personnel.with_raw_response.update_by_name(
                "",
            )
