# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.custom_fields import (
    TemplateListResponse,
    TemplateCreateResponse,
    TemplateUpdateResponse,
    TemplateRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        template = client.custom_fields.templates.create(
            description="template",
            external_id="template_001",
            name="Place",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.custom_fields.templates.with_raw_response.create(
            description="template",
            external_id="template_001",
            name="Place",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.custom_fields.templates.with_streaming_response.create(
            description="template",
            external_id="template_001",
            name="Place",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        template = client.custom_fields.templates.retrieve(
            0,
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.custom_fields.templates.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.custom_fields.templates.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        template = client.custom_fields.templates.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="template",
            external_id="template_001",
            name="Place",
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.custom_fields.templates.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="template",
            external_id="template_001",
            name="Place",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.custom_fields.templates.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="template",
            external_id="template_001",
            name="Place",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateUpdateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.custom_fields.templates.with_raw_response.update(
                "",
                description="template",
                external_id="template_001",
                name="Place",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        template = client.custom_fields.templates.list()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.custom_fields.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.custom_fields.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        template = await async_client.custom_fields.templates.create(
            description="template",
            external_id="template_001",
            name="Place",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.templates.with_raw_response.create(
            description="template",
            external_id="template_001",
            name="Place",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.templates.with_streaming_response.create(
            description="template",
            external_id="template_001",
            name="Place",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        template = await async_client.custom_fields.templates.retrieve(
            0,
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.templates.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.templates.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        template = await async_client.custom_fields.templates.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="template",
            external_id="template_001",
            name="Place",
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.templates.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="template",
            external_id="template_001",
            name="Place",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.templates.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="template",
            external_id="template_001",
            name="Place",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateUpdateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.custom_fields.templates.with_raw_response.update(
                "",
                description="template",
                external_id="template_001",
                name="Place",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        template = await async_client.custom_fields.templates.list()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.custom_fields.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.custom_fields.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True
