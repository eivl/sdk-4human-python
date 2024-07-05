# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExportedFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        exported_file = client.personnel.exported_files.retrieve(
            "string",
            file_name="string",
        )
        assert_matches_type(str, exported_file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.personnel.exported_files.with_raw_response.retrieve(
            "string",
            file_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exported_file = response.parse()
        assert_matches_type(str, exported_file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.personnel.exported_files.with_streaming_response.retrieve(
            "string",
            file_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exported_file = response.parse()
            assert_matches_type(str, exported_file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_name` but received ''"):
            client.personnel.exported_files.with_raw_response.retrieve(
                "string",
                file_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            client.personnel.exported_files.with_raw_response.retrieve(
                "",
                file_name="string",
            )


class TestAsyncExportedFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        exported_file = await async_client.personnel.exported_files.retrieve(
            "string",
            file_name="string",
        )
        assert_matches_type(str, exported_file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.exported_files.with_raw_response.retrieve(
            "string",
            file_name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exported_file = await response.parse()
        assert_matches_type(str, exported_file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.exported_files.with_streaming_response.retrieve(
            "string",
            file_name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exported_file = await response.parse()
            assert_matches_type(str, exported_file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_name` but received ''"):
            await async_client.personnel.exported_files.with_raw_response.retrieve(
                "string",
                file_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            await async_client.personnel.exported_files.with_raw_response.retrieve(
                "",
                file_name="string",
            )
