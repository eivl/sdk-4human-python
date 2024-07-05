# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import (
    JobCategoryStatusResponse,
    JobCategoryUpdateResponse,
    JobCategoryRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        job_category = client.job_categories.retrieve(
            "string",
        )
        assert_matches_type(JobCategoryRetrieveResponse, job_category, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.job_categories.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = response.parse()
        assert_matches_type(JobCategoryRetrieveResponse, job_category, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.job_categories.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = response.parse()
            assert_matches_type(JobCategoryRetrieveResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_category_id` but received ''"):
            client.job_categories.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        job_category = client.job_categories.update(
            "string",
        )
        assert_matches_type(JobCategoryUpdateResponse, job_category, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        job_category = client.job_categories.update(
            "string",
            description="Description of the first category.",
            external_id="001",
            internal_id="001",
            name="First category",
        )
        assert_matches_type(JobCategoryUpdateResponse, job_category, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.job_categories.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = response.parse()
        assert_matches_type(JobCategoryUpdateResponse, job_category, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.job_categories.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = response.parse()
            assert_matches_type(JobCategoryUpdateResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_category_id` but received ''"):
            client.job_categories.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_status(self, client: SDK4human) -> None:
        job_category = client.job_categories.status(
            "string",
            status="active",
        )
        assert_matches_type(JobCategoryStatusResponse, job_category, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: SDK4human) -> None:
        response = client.job_categories.with_raw_response.status(
            "string",
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = response.parse()
        assert_matches_type(JobCategoryStatusResponse, job_category, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: SDK4human) -> None:
        with client.job_categories.with_streaming_response.status(
            "string",
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = response.parse()
            assert_matches_type(JobCategoryStatusResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_category_id` but received ''"):
            client.job_categories.with_raw_response.status(
                "",
                status="active",
            )


class TestAsyncJobCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        job_category = await async_client.job_categories.retrieve(
            "string",
        )
        assert_matches_type(JobCategoryRetrieveResponse, job_category, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.job_categories.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = await response.parse()
        assert_matches_type(JobCategoryRetrieveResponse, job_category, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.job_categories.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = await response.parse()
            assert_matches_type(JobCategoryRetrieveResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_category_id` but received ''"):
            await async_client.job_categories.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        job_category = await async_client.job_categories.update(
            "string",
        )
        assert_matches_type(JobCategoryUpdateResponse, job_category, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        job_category = await async_client.job_categories.update(
            "string",
            description="Description of the first category.",
            external_id="001",
            internal_id="001",
            name="First category",
        )
        assert_matches_type(JobCategoryUpdateResponse, job_category, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.job_categories.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = await response.parse()
        assert_matches_type(JobCategoryUpdateResponse, job_category, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.job_categories.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = await response.parse()
            assert_matches_type(JobCategoryUpdateResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_category_id` but received ''"):
            await async_client.job_categories.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncSDK4human) -> None:
        job_category = await async_client.job_categories.status(
            "string",
            status="active",
        )
        assert_matches_type(JobCategoryStatusResponse, job_category, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.job_categories.with_raw_response.status(
            "string",
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_category = await response.parse()
        assert_matches_type(JobCategoryStatusResponse, job_category, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncSDK4human) -> None:
        async with async_client.job_categories.with_streaming_response.status(
            "string",
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_category = await response.parse()
            assert_matches_type(JobCategoryStatusResponse, job_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_category_id` but received ''"):
            await async_client.job_categories.with_raw_response.status(
                "",
                status="active",
            )
