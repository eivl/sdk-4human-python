# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import (
    SkillListResponse,
    SkillCreateResponse,
    SkillUpdateResponse,
    SkillRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        skill = client.skills.create(
            company_id=2,
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            parent_id=None,
            privacy="public",
            skill_type_id="95058825-a8e1-11eb-866b-0242ac130011",
            status="approved",
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        )
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        skill = client.skills.create(
            company_id=2,
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            parent_id=None,
            privacy="public",
            skill_type_id="95058825-a8e1-11eb-866b-0242ac130011",
            status="approved",
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
            employee_id="333",
            organization_number="982247500",
        )
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.skills.with_raw_response.create(
            company_id=2,
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            parent_id=None,
            privacy="public",
            skill_type_id="95058825-a8e1-11eb-866b-0242ac130011",
            status="approved",
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.skills.with_streaming_response.create(
            company_id=2,
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            parent_id=None,
            privacy="public",
            skill_type_id="95058825-a8e1-11eb-866b-0242ac130011",
            status="approved",
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillCreateResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        skill = client.skills.retrieve(
            "string",
        )
        assert_matches_type(SkillRetrieveResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.skills.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillRetrieveResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.skills.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillRetrieveResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.skills.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        skill = client.skills.update(
            "string",
        )
        assert_matches_type(SkillUpdateResponse, skill, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        skill = client.skills.update(
            "string",
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            privacy="public",
            status="approved",
        )
        assert_matches_type(SkillUpdateResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.skills.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillUpdateResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.skills.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillUpdateResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.skills.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        skill = client.skills.list()
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        skill = client.skills.list(
            limit=0,
            page=0,
        )
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.skills.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.skills.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillListResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSkills:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        skill = await async_client.skills.create(
            company_id=2,
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            parent_id=None,
            privacy="public",
            skill_type_id="95058825-a8e1-11eb-866b-0242ac130011",
            status="approved",
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        )
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        skill = await async_client.skills.create(
            company_id=2,
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            parent_id=None,
            privacy="public",
            skill_type_id="95058825-a8e1-11eb-866b-0242ac130011",
            status="approved",
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
            employee_id="333",
            organization_number="982247500",
        )
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skills.with_raw_response.create(
            company_id=2,
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            parent_id=None,
            privacy="public",
            skill_type_id="95058825-a8e1-11eb-866b-0242ac130011",
            status="approved",
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skills.with_streaming_response.create(
            company_id=2,
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            parent_id=None,
            privacy="public",
            skill_type_id="95058825-a8e1-11eb-866b-0242ac130011",
            status="approved",
            user_id="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillCreateResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        skill = await async_client.skills.retrieve(
            "string",
        )
        assert_matches_type(SkillRetrieveResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skills.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillRetrieveResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skills.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillRetrieveResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.skills.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        skill = await async_client.skills.update(
            "string",
        )
        assert_matches_type(SkillUpdateResponse, skill, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        skill = await async_client.skills.update(
            "string",
            employment_id=123,
            fields=[
                {
                    "id": "skillTitle",
                    "data": "PHP",
                },
                {
                    "id": "startedDate",
                    "data": "2021-03-01T00:00:00+00:00",
                },
                {
                    "id": "completedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "comment",
                    "data": "PHP for beginners.",
                },
                {
                    "id": "lengthOfExperience",
                    "data": "1m",
                },
                {
                    "id": "educationalLevel",
                    "data": 2,
                },
                {
                    "id": "writtenLanguageSkillLevel",
                    "data": 1,
                },
                {
                    "id": "oralLanguageSkillLevel",
                    "data": 2,
                },
                {
                    "id": "documents",
                    "data": [
                        {"id": "5ccb543e-b98c-43b0-8cdf-829bb710b6d5"},
                        {"id": "d32a45d6-40fb-4c7c-9964-65c5a4d25c71"},
                    ],
                },
                {
                    "id": "customUrl",
                    "data": "http://php.net",
                },
                {
                    "id": "internalExternal",
                    "data": 1,
                },
                {
                    "id": "nameOfProvider",
                    "data": "PHP University",
                },
                {
                    "id": "countryOfProvider",
                    "data": "pol",
                },
                {
                    "id": "providerPlace",
                    "data": None,
                },
                {
                    "id": "targetScore",
                    "data": 3,
                },
                {
                    "id": "currentScore",
                    "data": 1,
                },
                {
                    "id": "expiryDate",
                    "data": "2021-07-09T00:00:00+00:00",
                },
                {
                    "id": "plannedCompletedDate",
                    "data": "2021-03-31T00:00:00+00:00",
                },
                {
                    "id": "userDefinedNotificationDate",
                    "data": None,
                },
                {
                    "id": "requirement",
                    "data": 1,
                },
                {
                    "id": "criticality",
                    "data": 1,
                },
            ],
            privacy="public",
            status="approved",
        )
        assert_matches_type(SkillUpdateResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skills.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillUpdateResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skills.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillUpdateResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.skills.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        skill = await async_client.skills.list()
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        skill = await async_client.skills.list(
            limit=0,
            page=0,
        )
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.skills.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.skills.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillListResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True
