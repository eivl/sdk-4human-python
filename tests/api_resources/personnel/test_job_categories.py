# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import (
    JobCategoryListResponse,
    JobCategoryCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        job_category = client.personnel.job_categories.create(
            description="Description of the first category.",
            external_id="001",
            internal_id="001",
            name="First category",
        )
        assert_matches_type(JobCategoryCreateResponse, job_category, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.job_categories.with_raw_response.create(
            description="Description of the first category.",
            external_id="001",
            internal_id="001",
            name="First category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = response.parse()
        assert_matches_type(JobCategoryCreateResponse, job_category, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.job_categories.with_streaming_response.create(
            description="Description of the first category.",
            external_id="001",
            internal_id="001",
            name="First category",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = response.parse()
            assert_matches_type(JobCategoryCreateResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        job_category = client.personnel.job_categories.list()
        assert_matches_type(JobCategoryListResponse, job_category, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        job_category = client.personnel.job_categories.list(
            limit=0,
            page=0,
        )
        assert_matches_type(JobCategoryListResponse, job_category, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.personnel.job_categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = response.parse()
        assert_matches_type(JobCategoryListResponse, job_category, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.personnel.job_categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = response.parse()
            assert_matches_type(JobCategoryListResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        job_category = await async_client.personnel.job_categories.create(
            description="Description of the first category.",
            external_id="001",
            internal_id="001",
            name="First category",
        )
        assert_matches_type(JobCategoryCreateResponse, job_category, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.job_categories.with_raw_response.create(
            description="Description of the first category.",
            external_id="001",
            internal_id="001",
            name="First category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = await response.parse()
        assert_matches_type(JobCategoryCreateResponse, job_category, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.job_categories.with_streaming_response.create(
            description="Description of the first category.",
            external_id="001",
            internal_id="001",
            name="First category",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = await response.parse()
            assert_matches_type(JobCategoryCreateResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        job_category = await async_client.personnel.job_categories.list()
        assert_matches_type(JobCategoryListResponse, job_category, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        job_category = await async_client.personnel.job_categories.list(
            limit=0,
            page=0,
        )
        assert_matches_type(JobCategoryListResponse, job_category, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.job_categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = await response.parse()
        assert_matches_type(JobCategoryListResponse, job_category, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.job_categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = await response.parse()
            assert_matches_type(JobCategoryListResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True
