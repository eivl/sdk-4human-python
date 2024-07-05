# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import ExternalIntegrationRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run(self, client: SDK4human) -> None:
        external_integration = client.external_integrations.run(
            feature_name="Visma",
        )
        assert_matches_type(ExternalIntegrationRunResponse, external_integration, path=["response"])

    @parametrize
    def test_method_run_with_all_params(self, client: SDK4human) -> None:
        external_integration = client.external_integrations.run(
            feature_name="Visma",
            cron_expression="*/5 * * * *",
            run_hours=["01", "12", "23"],
        )
        assert_matches_type(ExternalIntegrationRunResponse, external_integration, path=["response"])

    @parametrize
    def test_raw_response_run(self, client: SDK4human) -> None:
        response = client.external_integrations.with_raw_response.run(
            feature_name="Visma",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_integration = response.parse()
        assert_matches_type(ExternalIntegrationRunResponse, external_integration, path=["response"])

    @parametrize
    def test_streaming_response_run(self, client: SDK4human) -> None:
        with client.external_integrations.with_streaming_response.run(
            feature_name="Visma",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_integration = response.parse()
            assert_matches_type(ExternalIntegrationRunResponse, external_integration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExternalIntegrations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_run(self, async_client: AsyncSDK4human) -> None:
        external_integration = await async_client.external_integrations.run(
            feature_name="Visma",
        )
        assert_matches_type(ExternalIntegrationRunResponse, external_integration, path=["response"])

    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncSDK4human) -> None:
        external_integration = await async_client.external_integrations.run(
            feature_name="Visma",
            cron_expression="*/5 * * * *",
            run_hours=["01", "12", "23"],
        )
        assert_matches_type(ExternalIntegrationRunResponse, external_integration, path=["response"])

    @parametrize
    async def test_raw_response_run(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.external_integrations.with_raw_response.run(
            feature_name="Visma",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_integration = await response.parse()
        assert_matches_type(ExternalIntegrationRunResponse, external_integration, path=["response"])

    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncSDK4human) -> None:
        async with async_client.external_integrations.with_streaming_response.run(
            feature_name="Visma",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_integration = await response.parse()
            assert_matches_type(ExternalIntegrationRunResponse, external_integration, path=["response"])

        assert cast(Any, response.is_closed) is True
