# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.orgstructure.companies.custom_fields import (
    TemplateListResponse,
    TemplateCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        template = client.orgstructure.companies.custom_fields.templates.create(
            company_id=1,
            template_id="9355ae32-ae3d-11eb-807e-0242ac120007",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.orgstructure.companies.custom_fields.templates.with_raw_response.create(
            company_id=1,
            template_id="9355ae32-ae3d-11eb-807e-0242ac120007",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.orgstructure.companies.custom_fields.templates.with_streaming_response.create(
            company_id=1,
            template_id="9355ae32-ae3d-11eb-807e-0242ac120007",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        template = client.orgstructure.companies.custom_fields.templates.list()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        template = client.orgstructure.companies.custom_fields.templates.list(
            sort_by="companyId",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.orgstructure.companies.custom_fields.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.orgstructure.companies.custom_fields.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        template = await async_client.orgstructure.companies.custom_fields.templates.create(
            company_id=1,
            template_id="9355ae32-ae3d-11eb-807e-0242ac120007",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.companies.custom_fields.templates.with_raw_response.create(
            company_id=1,
            template_id="9355ae32-ae3d-11eb-807e-0242ac120007",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.companies.custom_fields.templates.with_streaming_response.create(
            company_id=1,
            template_id="9355ae32-ae3d-11eb-807e-0242ac120007",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        template = await async_client.orgstructure.companies.custom_fields.templates.list()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        template = await async_client.orgstructure.companies.custom_fields.templates.list(
            sort_by="companyId",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.companies.custom_fields.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.companies.custom_fields.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True
