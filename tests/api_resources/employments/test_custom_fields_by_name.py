# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.employments import CustomFieldsByNameUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomFieldsByName:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        custom_fields_by_name = client.employments.custom_fields_by_name.update(
            "string",
        )
        assert_matches_type(CustomFieldsByNameUpdateResponse, custom_fields_by_name, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        custom_fields_by_name = client.employments.custom_fields_by_name.update(
            "string",
            external=True,
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
            effective_dates={
                "comment": None,
                "start_validity_date": "2023-09-02T00:00:00+00:00",
                "end_validity_date": "2023-10-01T00:00:00+00:00",
                "immediate": False,
            },
        )
        assert_matches_type(CustomFieldsByNameUpdateResponse, custom_fields_by_name, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.employments.custom_fields_by_name.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_fields_by_name = response.parse()
        assert_matches_type(CustomFieldsByNameUpdateResponse, custom_fields_by_name, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.employments.custom_fields_by_name.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_fields_by_name = response.parse()
            assert_matches_type(CustomFieldsByNameUpdateResponse, custom_fields_by_name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            client.employments.custom_fields_by_name.with_raw_response.update(
                "",
            )


class TestAsyncCustomFieldsByName:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        custom_fields_by_name = await async_client.employments.custom_fields_by_name.update(
            "string",
        )
        assert_matches_type(CustomFieldsByNameUpdateResponse, custom_fields_by_name, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        custom_fields_by_name = await async_client.employments.custom_fields_by_name.update(
            "string",
            external=True,
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
            effective_dates={
                "comment": None,
                "start_validity_date": "2023-09-02T00:00:00+00:00",
                "end_validity_date": "2023-10-01T00:00:00+00:00",
                "immediate": False,
            },
        )
        assert_matches_type(CustomFieldsByNameUpdateResponse, custom_fields_by_name, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.employments.custom_fields_by_name.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_fields_by_name = await response.parse()
        assert_matches_type(CustomFieldsByNameUpdateResponse, custom_fields_by_name, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.employments.custom_fields_by_name.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_fields_by_name = await response.parse()
            assert_matches_type(CustomFieldsByNameUpdateResponse, custom_fields_by_name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            await async_client.employments.custom_fields_by_name.with_raw_response.update(
                "",
            )
