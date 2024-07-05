# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import (
    SkillTypeCreateResponse,
    SkillTypeStatusResponse,
    SkillTypeUpdateResponse,
    SkillTypeRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkillTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        skill_type = client.skill_types.create(
            categories=["7aa384cc-b007-4537-9fb7-d985b54fbb2f", "fe6b2a07-eddf-11ea-a2e3-022ed6ba66f8"],
            cv_categories=["94c7599e-bd9c-453c-9d2d-a3a9d0037db7", "eb62b316-d588-4a2f-9e37-68d4ee09dc45"],
            default_skill_status="approved",
            description="Petal to the metal.",
            meta_fields=[
                {
                    "id": "administrator",
                    "visibility": "visible",
                    "value": "1",
                },
                {
                    "id": "tags",
                    "visibility": "visible",
                    "value": ["yamaha", "honda", "kawasaki", "suzuki"],
                },
            ],
            name="Industrial flower arrangement",
            number="123",
            privacy="public",
            sections=[
                {
                    "id": "details",
                    "fields": [
                        {
                            "id": "startedDate",
                            "visibility": "mandatory",
                        },
                        {
                            "id": "completedDate",
                            "visibility": "visible",
                        },
                        {
                            "id": "comment",
                            "visibility": "visible",
                        },
                        {
                            "id": "lengthOfExperience",
                            "visibility": "visible",
                        },
                    ],
                }
            ],
        )
        assert_matches_type(SkillTypeCreateResponse, skill_type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.skill_types.with_raw_response.create(
            categories=["7aa384cc-b007-4537-9fb7-d985b54fbb2f", "fe6b2a07-eddf-11ea-a2e3-022ed6ba66f8"],
            cv_categories=["94c7599e-bd9c-453c-9d2d-a3a9d0037db7", "eb62b316-d588-4a2f-9e37-68d4ee09dc45"],
            default_skill_status="approved",
            description="Petal to the metal.",
            meta_fields=[
                {
                    "id": "administrator",
                    "visibility": "visible",
                    "value": "1",
                },
                {
                    "id": "tags",
                    "visibility": "visible",
                    "value": ["yamaha", "honda", "kawasaki", "suzuki"],
                },
            ],
            name="Industrial flower arrangement",
            number="123",
            privacy="public",
            sections=[
                {
                    "id": "details",
                    "fields": [
                        {
                            "id": "startedDate",
                            "visibility": "mandatory",
                        },
                        {
                            "id": "completedDate",
                            "visibility": "visible",
                        },
                        {
                            "id": "comment",
                            "visibility": "visible",
                        },
                        {
                            "id": "lengthOfExperience",
                            "visibility": "visible",
                        },
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type = response.parse()
        assert_matches_type(SkillTypeCreateResponse, skill_type, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.skill_types.with_streaming_response.create(
            categories=["7aa384cc-b007-4537-9fb7-d985b54fbb2f", "fe6b2a07-eddf-11ea-a2e3-022ed6ba66f8"],
            cv_categories=["94c7599e-bd9c-453c-9d2d-a3a9d0037db7", "eb62b316-d588-4a2f-9e37-68d4ee09dc45"],
            default_skill_status="approved",
            description="Petal to the metal.",
            meta_fields=[
                {
                    "id": "administrator",
                    "visibility": "visible",
                    "value": "1",
                },
                {
                    "id": "tags",
                    "visibility": "visible",
                    "value": ["yamaha", "honda", "kawasaki", "suzuki"],
                },
            ],
            name="Industrial flower arrangement",
            number="123",
            privacy="public",
            sections=[
                {
                    "id": "details",
                    "fields": [
                        {
                            "id": "startedDate",
                            "visibility": "mandatory",
                        },
                        {
                            "id": "completedDate",
                            "visibility": "visible",
                        },
                        {
                            "id": "comment",
                            "visibility": "visible",
                        },
                        {
                            "id": "lengthOfExperience",
                            "visibility": "visible",
                        },
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type = response.parse()
            assert_matches_type(SkillTypeCreateResponse, skill_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        skill_type = client.skill_types.retrieve(
            "string",
        )
        assert_matches_type(SkillTypeRetrieveResponse, skill_type, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        skill_type = client.skill_types.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(SkillTypeRetrieveResponse, skill_type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.skill_types.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type = response.parse()
        assert_matches_type(SkillTypeRetrieveResponse, skill_type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.skill_types.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type = response.parse()
            assert_matches_type(SkillTypeRetrieveResponse, skill_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.skill_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        skill_type = client.skill_types.update(
            "string",
        )
        assert_matches_type(SkillTypeUpdateResponse, skill_type, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        skill_type = client.skill_types.update(
            "string",
            external=True,
            categories=["7aa384cc-b007-4537-9fb7-d985b54fbb2f", "fe6b2a07-eddf-11ea-a2e3-022ed6ba66f8"],
            cv_categories=["94c7599e-bd9c-453c-9d2d-a3a9d0037db7", "eb62b316-d588-4a2f-9e37-68d4ee09dc45"],
            default_skill_status="approved",
            description="Petal to the metal.",
            meta_fields=[
                {
                    "id": "administrator",
                    "visibility": "visible",
                    "value": "1",
                },
                {
                    "id": "tags",
                    "visibility": "visible",
                    "value": ["yamaha", "honda", "kawasaki", "suzuki"],
                },
            ],
            name="Industrial flower arrangement",
            number="123",
            privacy="public",
            sections=[
                {
                    "id": "details",
                    "fields": [
                        {
                            "id": "startedDate",
                            "visibility": "mandatory",
                            "value": 0,
                        },
                        {
                            "id": "completedDate",
                            "visibility": "visible",
                            "value": 0,
                        },
                        {
                            "id": "comment",
                            "visibility": "visible",
                            "value": 0,
                        },
                        {
                            "id": "lengthOfExperience",
                            "visibility": "visible",
                            "value": 0,
                        },
                    ],
                }
            ],
        )
        assert_matches_type(SkillTypeUpdateResponse, skill_type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.skill_types.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type = response.parse()
        assert_matches_type(SkillTypeUpdateResponse, skill_type, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.skill_types.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type = response.parse()
            assert_matches_type(SkillTypeUpdateResponse, skill_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.skill_types.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_status(self, client: SDK4human) -> None:
        skill_type = client.skill_types.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="active",
        )
        assert_matches_type(SkillTypeStatusResponse, skill_type, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: SDK4human) -> None:
        response = client.skill_types.with_raw_response.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type = response.parse()
        assert_matches_type(SkillTypeStatusResponse, skill_type, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: SDK4human) -> None:
        with client.skill_types.with_streaming_response.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type = response.parse()
            assert_matches_type(SkillTypeStatusResponse, skill_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.skill_types.with_raw_response.status(
                "",
                status="active",
            )


class TestAsyncSkillTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        skill_type = await async_client.skill_types.create(
            categories=["7aa384cc-b007-4537-9fb7-d985b54fbb2f", "fe6b2a07-eddf-11ea-a2e3-022ed6ba66f8"],
            cv_categories=["94c7599e-bd9c-453c-9d2d-a3a9d0037db7", "eb62b316-d588-4a2f-9e37-68d4ee09dc45"],
            default_skill_status="approved",
            description="Petal to the metal.",
            meta_fields=[
                {
                    "id": "administrator",
                    "visibility": "visible",
                    "value": "1",
                },
                {
                    "id": "tags",
                    "visibility": "visible",
                    "value": ["yamaha", "honda", "kawasaki", "suzuki"],
                },
            ],
            name="Industrial flower arrangement",
            number="123",
            privacy="public",
            sections=[
                {
                    "id": "details",
                    "fields": [
                        {
                            "id": "startedDate",
                            "visibility": "mandatory",
                        },
                        {
                            "id": "completedDate",
                            "visibility": "visible",
                        },
                        {
                            "id": "comment",
                            "visibility": "visible",
                        },
                        {
                            "id": "lengthOfExperience",
                            "visibility": "visible",
                        },
                    ],
                }
            ],
        )
        assert_matches_type(SkillTypeCreateResponse, skill_type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skill_types.with_raw_response.create(
            categories=["7aa384cc-b007-4537-9fb7-d985b54fbb2f", "fe6b2a07-eddf-11ea-a2e3-022ed6ba66f8"],
            cv_categories=["94c7599e-bd9c-453c-9d2d-a3a9d0037db7", "eb62b316-d588-4a2f-9e37-68d4ee09dc45"],
            default_skill_status="approved",
            description="Petal to the metal.",
            meta_fields=[
                {
                    "id": "administrator",
                    "visibility": "visible",
                    "value": "1",
                },
                {
                    "id": "tags",
                    "visibility": "visible",
                    "value": ["yamaha", "honda", "kawasaki", "suzuki"],
                },
            ],
            name="Industrial flower arrangement",
            number="123",
            privacy="public",
            sections=[
                {
                    "id": "details",
                    "fields": [
                        {
                            "id": "startedDate",
                            "visibility": "mandatory",
                        },
                        {
                            "id": "completedDate",
                            "visibility": "visible",
                        },
                        {
                            "id": "comment",
                            "visibility": "visible",
                        },
                        {
                            "id": "lengthOfExperience",
                            "visibility": "visible",
                        },
                    ],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type = await response.parse()
        assert_matches_type(SkillTypeCreateResponse, skill_type, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skill_types.with_streaming_response.create(
            categories=["7aa384cc-b007-4537-9fb7-d985b54fbb2f", "fe6b2a07-eddf-11ea-a2e3-022ed6ba66f8"],
            cv_categories=["94c7599e-bd9c-453c-9d2d-a3a9d0037db7", "eb62b316-d588-4a2f-9e37-68d4ee09dc45"],
            default_skill_status="approved",
            description="Petal to the metal.",
            meta_fields=[
                {
                    "id": "administrator",
                    "visibility": "visible",
                    "value": "1",
                },
                {
                    "id": "tags",
                    "visibility": "visible",
                    "value": ["yamaha", "honda", "kawasaki", "suzuki"],
                },
            ],
            name="Industrial flower arrangement",
            number="123",
            privacy="public",
            sections=[
                {
                    "id": "details",
                    "fields": [
                        {
                            "id": "startedDate",
                            "visibility": "mandatory",
                        },
                        {
                            "id": "completedDate",
                            "visibility": "visible",
                        },
                        {
                            "id": "comment",
                            "visibility": "visible",
                        },
                        {
                            "id": "lengthOfExperience",
                            "visibility": "visible",
                        },
                    ],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type = await response.parse()
            assert_matches_type(SkillTypeCreateResponse, skill_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        skill_type = await async_client.skill_types.retrieve(
            "string",
        )
        assert_matches_type(SkillTypeRetrieveResponse, skill_type, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        skill_type = await async_client.skill_types.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(SkillTypeRetrieveResponse, skill_type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skill_types.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type = await response.parse()
        assert_matches_type(SkillTypeRetrieveResponse, skill_type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skill_types.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type = await response.parse()
            assert_matches_type(SkillTypeRetrieveResponse, skill_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.skill_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        skill_type = await async_client.skill_types.update(
            "string",
        )
        assert_matches_type(SkillTypeUpdateResponse, skill_type, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        skill_type = await async_client.skill_types.update(
            "string",
            external=True,
            categories=["7aa384cc-b007-4537-9fb7-d985b54fbb2f", "fe6b2a07-eddf-11ea-a2e3-022ed6ba66f8"],
            cv_categories=["94c7599e-bd9c-453c-9d2d-a3a9d0037db7", "eb62b316-d588-4a2f-9e37-68d4ee09dc45"],
            default_skill_status="approved",
            description="Petal to the metal.",
            meta_fields=[
                {
                    "id": "administrator",
                    "visibility": "visible",
                    "value": "1",
                },
                {
                    "id": "tags",
                    "visibility": "visible",
                    "value": ["yamaha", "honda", "kawasaki", "suzuki"],
                },
            ],
            name="Industrial flower arrangement",
            number="123",
            privacy="public",
            sections=[
                {
                    "id": "details",
                    "fields": [
                        {
                            "id": "startedDate",
                            "visibility": "mandatory",
                            "value": 0,
                        },
                        {
                            "id": "completedDate",
                            "visibility": "visible",
                            "value": 0,
                        },
                        {
                            "id": "comment",
                            "visibility": "visible",
                            "value": 0,
                        },
                        {
                            "id": "lengthOfExperience",
                            "visibility": "visible",
                            "value": 0,
                        },
                    ],
                }
            ],
        )
        assert_matches_type(SkillTypeUpdateResponse, skill_type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skill_types.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type = await response.parse()
        assert_matches_type(SkillTypeUpdateResponse, skill_type, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skill_types.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type = await response.parse()
            assert_matches_type(SkillTypeUpdateResponse, skill_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.skill_types.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncSDK4human) -> None:
        skill_type = await async_client.skill_types.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="active",
        )
        assert_matches_type(SkillTypeStatusResponse, skill_type, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skill_types.with_raw_response.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_type = await response.parse()
        assert_matches_type(SkillTypeStatusResponse, skill_type, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skill_types.with_streaming_response.status(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_type = await response.parse()
            assert_matches_type(SkillTypeStatusResponse, skill_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.skill_types.with_raw_response.status(
                "",
                status="active",
            )
