# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.external_integrations import FeatureStatusRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeatureStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        feature_status = client.external_integrations.feature_status.retrieve(
            "string",
        )
        assert_matches_type(FeatureStatusRetrieveResponse, feature_status, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.external_integrations.feature_status.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_status = response.parse()
        assert_matches_type(FeatureStatusRetrieveResponse, feature_status, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.external_integrations.feature_status.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_status = response.parse()
            assert_matches_type(FeatureStatusRetrieveResponse, feature_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_name` but received ''"):
            client.external_integrations.feature_status.with_raw_response.retrieve(
                "",
            )


class TestAsyncFeatureStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        feature_status = await async_client.external_integrations.feature_status.retrieve(
            "string",
        )
        assert_matches_type(FeatureStatusRetrieveResponse, feature_status, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.external_integrations.feature_status.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature_status = await response.parse()
        assert_matches_type(FeatureStatusRetrieveResponse, feature_status, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.external_integrations.feature_status.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature_status = await response.parse()
            assert_matches_type(FeatureStatusRetrieveResponse, feature_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_name` but received ''"):
            await async_client.external_integrations.feature_status.with_raw_response.retrieve(
                "",
            )
