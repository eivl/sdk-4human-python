# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.skills import UserSkillUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserSkill:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        user_skill = client.skills.user_skill.update()
        assert_matches_type(UserSkillUpdateResponse, user_skill, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        user_skill = client.skills.user_skill.update(
            mode="READ_ONLY",
            company={
                "unit_id": "unit123",
                "organization_number": "org123",
            },
            company_employee={"employee_id": "123"},
            instance_user={"email": "string"},
            skill={
                "status": "approved",
                "fields": [
                    {
                        "id": "skillTitle",
                        "data": "PHP",
                    },
                    {
                        "id": "startedDate",
                        "data": "2021-03-01T00:00:00+00:00",
                    },
                ],
            },
            skill_type={
                "number": "123",
                "name": "Industrial flower arrangement",
            },
            skill_type_category={"name": "categoryName"},
        )
        assert_matches_type(UserSkillUpdateResponse, user_skill, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.skills.user_skill.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_skill = response.parse()
        assert_matches_type(UserSkillUpdateResponse, user_skill, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.skills.user_skill.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_skill = response.parse()
            assert_matches_type(UserSkillUpdateResponse, user_skill, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserSkill:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        user_skill = await async_client.skills.user_skill.update()
        assert_matches_type(UserSkillUpdateResponse, user_skill, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        user_skill = await async_client.skills.user_skill.update(
            mode="READ_ONLY",
            company={
                "unit_id": "unit123",
                "organization_number": "org123",
            },
            company_employee={"employee_id": "123"},
            instance_user={"email": "string"},
            skill={
                "status": "approved",
                "fields": [
                    {
                        "id": "skillTitle",
                        "data": "PHP",
                    },
                    {
                        "id": "startedDate",
                        "data": "2021-03-01T00:00:00+00:00",
                    },
                ],
            },
            skill_type={
                "number": "123",
                "name": "Industrial flower arrangement",
            },
            skill_type_category={"name": "categoryName"},
        )
        assert_matches_type(UserSkillUpdateResponse, user_skill, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skills.user_skill.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_skill = await response.parse()
        assert_matches_type(UserSkillUpdateResponse, user_skill, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skills.user_skill.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_skill = await response.parse()
            assert_matches_type(UserSkillUpdateResponse, user_skill, path=["response"])

        assert cast(Any, response.is_closed) is True
