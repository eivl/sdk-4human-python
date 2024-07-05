# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import ChildUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChildren:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        child = client.personnel.children.update(
            "string",
        )
        assert_matches_type(ChildUpdateResponse, child, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        child = client.personnel.children.update(
            "string",
            birth_date="1980-01-01T00:00:00+00:00",
            chronically_sick={
                "from": "2010-01-16T00:00:00+0000",
                "to": "2020-01-16T00:00:00+0000",
            },
            do_i_have_care=True,
            firstname="Anne",
            gender="F",
            phone_number="800800801",
            single_parent=True,
            surname="Doe",
        )
        assert_matches_type(ChildUpdateResponse, child, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.children.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child = response.parse()
        assert_matches_type(ChildUpdateResponse, child, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.children.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child = response.parse()
            assert_matches_type(ChildUpdateResponse, child, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `child_id` but received ''"):
            client.personnel.children.with_raw_response.update(
                "",
            )


class TestAsyncChildren:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        child = await async_client.personnel.children.update(
            "string",
        )
        assert_matches_type(ChildUpdateResponse, child, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        child = await async_client.personnel.children.update(
            "string",
            birth_date="1980-01-01T00:00:00+00:00",
            chronically_sick={
                "from": "2010-01-16T00:00:00+0000",
                "to": "2020-01-16T00:00:00+0000",
            },
            do_i_have_care=True,
            firstname="Anne",
            gender="F",
            phone_number="800800801",
            single_parent=True,
            surname="Doe",
        )
        assert_matches_type(ChildUpdateResponse, child, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.children.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        child = await response.parse()
        assert_matches_type(ChildUpdateResponse, child, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.children.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            child = await response.parse()
            assert_matches_type(ChildUpdateResponse, child, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `child_id` but received ''"):
            await async_client.personnel.children.with_raw_response.update(
                "",
            )
