# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.users import (
    PersonalIDCreateResponse,
    PersonalIDDeleteResponse,
    PersonalIDImportResponse,
    PersonalIDUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPersonalID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        personal_id = client.users.personal_id.create(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        )
        assert_matches_type(PersonalIDCreateResponse, personal_id, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        personal_id = client.users.personal_id.create(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
            force_no_approval_policy=True,
        )
        assert_matches_type(PersonalIDCreateResponse, personal_id, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.users.personal_id.with_raw_response.create(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_id = response.parse()
        assert_matches_type(PersonalIDCreateResponse, personal_id, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.users.personal_id.with_streaming_response.create(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_id = response.parse()
            assert_matches_type(PersonalIDCreateResponse, personal_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.personal_id.with_raw_response.create(
                "",
                id_country=None,
                id_number=None,
                id_type="none",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        personal_id = client.users.personal_id.update(
            0,
            user_id="string",
            id_country=None,
            id_number=None,
            id_type="none",
        )
        assert_matches_type(PersonalIDUpdateResponse, personal_id, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        personal_id = client.users.personal_id.update(
            0,
            user_id="string",
            id_country=None,
            id_number=None,
            id_type="none",
            force_no_approval_policy=True,
        )
        assert_matches_type(PersonalIDUpdateResponse, personal_id, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.users.personal_id.with_raw_response.update(
            0,
            user_id="string",
            id_country=None,
            id_number=None,
            id_type="none",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_id = response.parse()
        assert_matches_type(PersonalIDUpdateResponse, personal_id, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.users.personal_id.with_streaming_response.update(
            0,
            user_id="string",
            id_country=None,
            id_number=None,
            id_type="none",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_id = response.parse()
            assert_matches_type(PersonalIDUpdateResponse, personal_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.personal_id.with_raw_response.update(
                0,
                user_id="",
                id_country=None,
                id_number=None,
                id_type="none",
            )

    @parametrize
    def test_method_delete(self, client: SDK4human) -> None:
        personal_id = client.users.personal_id.delete(
            0,
            user_id="string",
        )
        assert_matches_type(PersonalIDDeleteResponse, personal_id, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: SDK4human) -> None:
        personal_id = client.users.personal_id.delete(
            0,
            user_id="string",
            force_no_approval_policy=True,
        )
        assert_matches_type(PersonalIDDeleteResponse, personal_id, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: SDK4human) -> None:
        response = client.users.personal_id.with_raw_response.delete(
            0,
            user_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_id = response.parse()
        assert_matches_type(PersonalIDDeleteResponse, personal_id, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: SDK4human) -> None:
        with client.users.personal_id.with_streaming_response.delete(
            0,
            user_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_id = response.parse()
            assert_matches_type(PersonalIDDeleteResponse, personal_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.personal_id.with_raw_response.delete(
                0,
                user_id="",
            )

    @parametrize
    def test_method_import(self, client: SDK4human) -> None:
        personal_id = client.users.personal_id.import_(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        )
        assert_matches_type(PersonalIDImportResponse, personal_id, path=["response"])

    @parametrize
    def test_method_import_with_all_params(self, client: SDK4human) -> None:
        personal_id = client.users.personal_id.import_(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
            force_no_approval_policy=True,
            passport_country="NOR",
            passport_number="987654321",
        )
        assert_matches_type(PersonalIDImportResponse, personal_id, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: SDK4human) -> None:
        response = client.users.personal_id.with_raw_response.import_(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_id = response.parse()
        assert_matches_type(PersonalIDImportResponse, personal_id, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: SDK4human) -> None:
        with client.users.personal_id.with_streaming_response.import_(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_id = response.parse()
            assert_matches_type(PersonalIDImportResponse, personal_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_import(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.personal_id.with_raw_response.import_(
                "",
                id_country=None,
                id_number=None,
                id_type="none",
            )


class TestAsyncPersonalID:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        personal_id = await async_client.users.personal_id.create(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        )
        assert_matches_type(PersonalIDCreateResponse, personal_id, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        personal_id = await async_client.users.personal_id.create(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
            force_no_approval_policy=True,
        )
        assert_matches_type(PersonalIDCreateResponse, personal_id, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.personal_id.with_raw_response.create(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_id = await response.parse()
        assert_matches_type(PersonalIDCreateResponse, personal_id, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.personal_id.with_streaming_response.create(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_id = await response.parse()
            assert_matches_type(PersonalIDCreateResponse, personal_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.personal_id.with_raw_response.create(
                "",
                id_country=None,
                id_number=None,
                id_type="none",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        personal_id = await async_client.users.personal_id.update(
            0,
            user_id="string",
            id_country=None,
            id_number=None,
            id_type="none",
        )
        assert_matches_type(PersonalIDUpdateResponse, personal_id, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        personal_id = await async_client.users.personal_id.update(
            0,
            user_id="string",
            id_country=None,
            id_number=None,
            id_type="none",
            force_no_approval_policy=True,
        )
        assert_matches_type(PersonalIDUpdateResponse, personal_id, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.personal_id.with_raw_response.update(
            0,
            user_id="string",
            id_country=None,
            id_number=None,
            id_type="none",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_id = await response.parse()
        assert_matches_type(PersonalIDUpdateResponse, personal_id, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.personal_id.with_streaming_response.update(
            0,
            user_id="string",
            id_country=None,
            id_number=None,
            id_type="none",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_id = await response.parse()
            assert_matches_type(PersonalIDUpdateResponse, personal_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.personal_id.with_raw_response.update(
                0,
                user_id="",
                id_country=None,
                id_number=None,
                id_type="none",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSDK4human) -> None:
        personal_id = await async_client.users.personal_id.delete(
            0,
            user_id="string",
        )
        assert_matches_type(PersonalIDDeleteResponse, personal_id, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSDK4human) -> None:
        personal_id = await async_client.users.personal_id.delete(
            0,
            user_id="string",
            force_no_approval_policy=True,
        )
        assert_matches_type(PersonalIDDeleteResponse, personal_id, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.personal_id.with_raw_response.delete(
            0,
            user_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_id = await response.parse()
        assert_matches_type(PersonalIDDeleteResponse, personal_id, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.personal_id.with_streaming_response.delete(
            0,
            user_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_id = await response.parse()
            assert_matches_type(PersonalIDDeleteResponse, personal_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.personal_id.with_raw_response.delete(
                0,
                user_id="",
            )

    @parametrize
    async def test_method_import(self, async_client: AsyncSDK4human) -> None:
        personal_id = await async_client.users.personal_id.import_(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        )
        assert_matches_type(PersonalIDImportResponse, personal_id, path=["response"])

    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncSDK4human) -> None:
        personal_id = await async_client.users.personal_id.import_(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
            force_no_approval_policy=True,
            passport_country="NOR",
            passport_number="987654321",
        )
        assert_matches_type(PersonalIDImportResponse, personal_id, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.users.personal_id.with_raw_response.import_(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        personal_id = await response.parse()
        assert_matches_type(PersonalIDImportResponse, personal_id, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncSDK4human) -> None:
        async with async_client.users.personal_id.with_streaming_response.import_(
            "string",
            id_country=None,
            id_number=None,
            id_type="none",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            personal_id = await response.parse()
            assert_matches_type(PersonalIDImportResponse, personal_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_import(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.personal_id.with_raw_response.import_(
                "",
                id_country=None,
                id_number=None,
                id_type="none",
            )
