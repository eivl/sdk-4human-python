# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel.custom_fields.templates import (
    FieldCreateResponse,
    FieldUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        field = client.personnel.custom_fields.templates.fields.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="CustomFieldName",
        )
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        field = client.personnel.custom_fields.templates.fields.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="CustomFieldName",
            children=[
                {
                    "name": "Dimension one",
                    "externalName": "Dimension one - External",
                    "internalId": "2",
                    "externalId": "Ex2",
                    "children": [
                        {
                            "name": "Dimension three",
                            "externalName": "Dimension two - External",
                            "internalId": "3",
                            "externalId": "Ex3",
                            "children": [
                                {
                                    "name": "Dimension three",
                                    "externalName": "Dimension three - External",
                                    "internalId": "4",
                                    "externalId": "Ex4",
                                }
                            ],
                        }
                    ],
                }
            ],
            field_type="structure",
            placing={
                "context": "employment",
                "section": "details",
            },
            validators=["short"],
        )
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.custom_fields.templates.fields.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="CustomFieldName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.custom_fields.templates.fields.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="CustomFieldName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldCreateResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.personnel.custom_fields.templates.fields.with_raw_response.create(
                "",
                external_id="Ex1",
                external_name="4Human.hrm - External",
                internal_id="1",
                name="CustomFieldName",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        field = client.personnel.custom_fields.templates.fields.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="4Human.hrm",
        )
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        field = client.personnel.custom_fields.templates.fields.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="4Human.hrm",
            placing={
                "context": "employment",
                "section": "details",
            },
            validators=["string", "string", "string"],
        )
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.custom_fields.templates.fields.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="4Human.hrm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.custom_fields.templates.fields.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="4Human.hrm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldUpdateResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.personnel.custom_fields.templates.fields.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                template_id="",
                external_id="Ex1",
                external_name="4Human.hrm - External",
                internal_id="1",
                name="4Human.hrm",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            client.personnel.custom_fields.templates.fields.with_raw_response.update(
                "",
                template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                external_id="Ex1",
                external_name="4Human.hrm - External",
                internal_id="1",
                name="4Human.hrm",
            )


class TestAsyncFields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        field = await async_client.personnel.custom_fields.templates.fields.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="CustomFieldName",
        )
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        field = await async_client.personnel.custom_fields.templates.fields.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="CustomFieldName",
            children=[
                {
                    "name": "Dimension one",
                    "externalName": "Dimension one - External",
                    "internalId": "2",
                    "externalId": "Ex2",
                    "children": [
                        {
                            "name": "Dimension three",
                            "externalName": "Dimension two - External",
                            "internalId": "3",
                            "externalId": "Ex3",
                            "children": [
                                {
                                    "name": "Dimension three",
                                    "externalName": "Dimension three - External",
                                    "internalId": "4",
                                    "externalId": "Ex4",
                                }
                            ],
                        }
                    ],
                }
            ],
            field_type="structure",
            placing={
                "context": "employment",
                "section": "details",
            },
            validators=["short"],
        )
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.custom_fields.templates.fields.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="CustomFieldName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldCreateResponse, field, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.custom_fields.templates.fields.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="CustomFieldName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldCreateResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.personnel.custom_fields.templates.fields.with_raw_response.create(
                "",
                external_id="Ex1",
                external_name="4Human.hrm - External",
                internal_id="1",
                name="CustomFieldName",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        field = await async_client.personnel.custom_fields.templates.fields.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="4Human.hrm",
        )
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        field = await async_client.personnel.custom_fields.templates.fields.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="4Human.hrm",
            placing={
                "context": "employment",
                "section": "details",
            },
            validators=["string", "string", "string"],
        )
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.custom_fields.templates.fields.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="4Human.hrm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.custom_fields.templates.fields.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_id="Ex1",
            external_name="4Human.hrm - External",
            internal_id="1",
            name="4Human.hrm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldUpdateResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.personnel.custom_fields.templates.fields.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                template_id="",
                external_id="Ex1",
                external_name="4Human.hrm - External",
                internal_id="1",
                name="4Human.hrm",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            await async_client.personnel.custom_fields.templates.fields.with_raw_response.update(
                "",
                template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                external_id="Ex1",
                external_name="4Human.hrm - External",
                internal_id="1",
                name="4Human.hrm",
            )
