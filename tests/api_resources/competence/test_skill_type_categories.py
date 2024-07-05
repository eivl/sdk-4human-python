# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.competence import (
    SkillTypeCategoryListResponse,
    SkillTypeCategoryCreateResponse,
    SkillTypeCategoryUpdateResponse,
    SkillTypeCategoryRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkillTypeCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        skill_type_category = client.competence.skill_type_categories.create(
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
        )
        assert_matches_type(SkillTypeCategoryCreateResponse, skill_type_category, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        skill_type_category = client.competence.skill_type_categories.create(
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
            icon={
                "prefix": "fab",
                "icon_name": "award",
            },
        )
        assert_matches_type(SkillTypeCategoryCreateResponse, skill_type_category, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.competence.skill_type_categories.with_raw_response.create(
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type_category = response.parse()
        assert_matches_type(SkillTypeCategoryCreateResponse, skill_type_category, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.competence.skill_type_categories.with_streaming_response.create(
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type_category = response.parse()
            assert_matches_type(SkillTypeCategoryCreateResponse, skill_type_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        skill_type_category = client.competence.skill_type_categories.retrieve(
            "string",
        )
        assert_matches_type(SkillTypeCategoryRetrieveResponse, skill_type_category, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        skill_type_category = client.competence.skill_type_categories.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(SkillTypeCategoryRetrieveResponse, skill_type_category, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.competence.skill_type_categories.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type_category = response.parse()
        assert_matches_type(SkillTypeCategoryRetrieveResponse, skill_type_category, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.competence.skill_type_categories.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type_category = response.parse()
            assert_matches_type(SkillTypeCategoryRetrieveResponse, skill_type_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.competence.skill_type_categories.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        skill_type_category = client.competence.skill_type_categories.update(
            "string",
        )
        assert_matches_type(SkillTypeCategoryUpdateResponse, skill_type_category, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        skill_type_category = client.competence.skill_type_categories.update(
            "string",
            external=True,
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            icon={
                "prefix": "fab",
                "icon_name": "award",
            },
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
        )
        assert_matches_type(SkillTypeCategoryUpdateResponse, skill_type_category, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.competence.skill_type_categories.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type_category = response.parse()
        assert_matches_type(SkillTypeCategoryUpdateResponse, skill_type_category, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.competence.skill_type_categories.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type_category = response.parse()
            assert_matches_type(SkillTypeCategoryUpdateResponse, skill_type_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.competence.skill_type_categories.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        skill_type_category = client.competence.skill_type_categories.list()
        assert_matches_type(SkillTypeCategoryListResponse, skill_type_category, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.competence.skill_type_categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type_category = response.parse()
        assert_matches_type(SkillTypeCategoryListResponse, skill_type_category, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.competence.skill_type_categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type_category = response.parse()
            assert_matches_type(SkillTypeCategoryListResponse, skill_type_category, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSkillTypeCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        skill_type_category = await async_client.competence.skill_type_categories.create(
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
        )
        assert_matches_type(SkillTypeCategoryCreateResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        skill_type_category = await async_client.competence.skill_type_categories.create(
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
            icon={
                "prefix": "fab",
                "icon_name": "award",
            },
        )
        assert_matches_type(SkillTypeCategoryCreateResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.competence.skill_type_categories.with_raw_response.create(
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type_category = await response.parse()
        assert_matches_type(SkillTypeCategoryCreateResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.competence.skill_type_categories.with_streaming_response.create(
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type_category = await response.parse()
            assert_matches_type(SkillTypeCategoryCreateResponse, skill_type_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        skill_type_category = await async_client.competence.skill_type_categories.retrieve(
            "string",
        )
        assert_matches_type(SkillTypeCategoryRetrieveResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        skill_type_category = await async_client.competence.skill_type_categories.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(SkillTypeCategoryRetrieveResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.competence.skill_type_categories.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type_category = await response.parse()
        assert_matches_type(SkillTypeCategoryRetrieveResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.competence.skill_type_categories.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type_category = await response.parse()
            assert_matches_type(SkillTypeCategoryRetrieveResponse, skill_type_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.competence.skill_type_categories.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        skill_type_category = await async_client.competence.skill_type_categories.update(
            "string",
        )
        assert_matches_type(SkillTypeCategoryUpdateResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        skill_type_category = await async_client.competence.skill_type_categories.update(
            "string",
            external=True,
            color="#191970",
            description="Responsible for implementations and maintenance cloud infrastructures.",
            icon={
                "prefix": "fab",
                "icon_name": "award",
            },
            name="Cloud Developer",
            number="D0001",
            parent_id="f866acc7-ed9e-4eef-8a45-95f1c7ae29aa",
        )
        assert_matches_type(SkillTypeCategoryUpdateResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.competence.skill_type_categories.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type_category = await response.parse()
        assert_matches_type(SkillTypeCategoryUpdateResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.competence.skill_type_categories.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type_category = await response.parse()
            assert_matches_type(SkillTypeCategoryUpdateResponse, skill_type_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.competence.skill_type_categories.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        skill_type_category = await async_client.competence.skill_type_categories.list()
        assert_matches_type(SkillTypeCategoryListResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.competence.skill_type_categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type_category = await response.parse()
        assert_matches_type(SkillTypeCategoryListResponse, skill_type_category, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.competence.skill_type_categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type_category = await response.parse()
            assert_matches_type(SkillTypeCategoryListResponse, skill_type_category, path=["response"])

        assert cast(Any, response.is_closed) is True
