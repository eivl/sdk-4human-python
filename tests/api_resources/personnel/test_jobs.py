# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel import (
    JobListResponse,
    JobCreateResponse,
    JobUpdateResponse,
    JobRetrieveResponse,
    JobUpdateFieldsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        job = client.personnel.jobs.create(
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        job = client.personnel.jobs.create(
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
            category_id="c4ecf795-8a87-4c35-927d-368c8cc9adec",
            description="Job Description",
            occupational_codes=[
                {
                    "country": "NOR",
                    "code": "0112102",
                }
            ],
            status="active",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.jobs.with_raw_response.create(
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.jobs.with_streaming_response.create(
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        job = client.personnel.jobs.retrieve(
            "string",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        job = client.personnel.jobs.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.personnel.jobs.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.personnel.jobs.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobRetrieveResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.personnel.jobs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        job = client.personnel.jobs.update(
            "string",
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        job = client.personnel.jobs.update(
            "string",
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
            external=True,
            category_id="c4ecf795-8a87-4c35-927d-368c8cc9adec",
            description="Job Description",
            occupational_codes=[
                {
                    "country": "NOR",
                    "code": "0112102",
                }
            ],
            status="active",
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.jobs.with_raw_response.update(
            "string",
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.jobs.with_streaming_response.update(
            "string",
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobUpdateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.personnel.jobs.with_raw_response.update(
                "",
                acl=[
                    {
                        "subject_type": "org_unit",
                        "subject_id": "8",
                        "setting": "allow",
                    },
                    {
                        "subject_type": "org_unit",
                        "subject_id": "4",
                        "setting": "allow",
                    },
                ],
                number="Unique job number which is string",
                title="Job title",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        job = client.personnel.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        job = client.personnel.jobs.list(
            limit=0,
            page=0,
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.personnel.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.personnel.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_fields(self, client: SDK4human) -> None:
        job = client.personnel.jobs.update_fields(
            "string",
        )
        assert_matches_type(JobUpdateFieldsResponse, job, path=["response"])

    @parametrize
    def test_method_update_fields_with_all_params(self, client: SDK4human) -> None:
        job = client.personnel.jobs.update_fields(
            "string",
            external=True,
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            category_id="c4ecf795-8a87-4c35-927d-368c8cc9adec",
            description="Job Description",
            number="Unique job number which is string",
            occupational_codes=[
                {
                    "country": "NOR",
                    "code": "0112117",
                }
            ],
            status="active",
            title="Job title",
        )
        assert_matches_type(JobUpdateFieldsResponse, job, path=["response"])

    @parametrize
    def test_raw_response_update_fields(self, client: SDK4human) -> None:
        response = client.personnel.jobs.with_raw_response.update_fields(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobUpdateFieldsResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_update_fields(self, client: SDK4human) -> None:
        with client.personnel.jobs.with_streaming_response.update_fields(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobUpdateFieldsResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_fields(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.personnel.jobs.with_raw_response.update_fields(
                "",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.create(
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.create(
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
            category_id="c4ecf795-8a87-4c35-927d-368c8cc9adec",
            description="Job Description",
            occupational_codes=[
                {
                    "country": "NOR",
                    "code": "0112102",
                }
            ],
            status="active",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.jobs.with_raw_response.create(
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.jobs.with_streaming_response.create(
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.retrieve(
            "string",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.retrieve(
            "string",
            external=True,
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.jobs.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.jobs.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobRetrieveResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.personnel.jobs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.update(
            "string",
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.update(
            "string",
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
            external=True,
            category_id="c4ecf795-8a87-4c35-927d-368c8cc9adec",
            description="Job Description",
            occupational_codes=[
                {
                    "country": "NOR",
                    "code": "0112102",
                }
            ],
            status="active",
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.jobs.with_raw_response.update(
            "string",
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.jobs.with_streaming_response.update(
            "string",
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            number="Unique job number which is string",
            title="Job title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobUpdateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.personnel.jobs.with_raw_response.update(
                "",
                acl=[
                    {
                        "subject_type": "org_unit",
                        "subject_id": "8",
                        "setting": "allow",
                    },
                    {
                        "subject_type": "org_unit",
                        "subject_id": "4",
                        "setting": "allow",
                    },
                ],
                number="Unique job number which is string",
                title="Job title",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.list(
            limit=0,
            page=0,
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_fields(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.update_fields(
            "string",
        )
        assert_matches_type(JobUpdateFieldsResponse, job, path=["response"])

    @parametrize
    async def test_method_update_fields_with_all_params(self, async_client: AsyncSDK4human) -> None:
        job = await async_client.personnel.jobs.update_fields(
            "string",
            external=True,
            acl=[
                {
                    "subject_type": "org_unit",
                    "subject_id": "8",
                    "setting": "allow",
                },
                {
                    "subject_type": "org_unit",
                    "subject_id": "4",
                    "setting": "allow",
                },
            ],
            category_id="c4ecf795-8a87-4c35-927d-368c8cc9adec",
            description="Job Description",
            number="Unique job number which is string",
            occupational_codes=[
                {
                    "country": "NOR",
                    "code": "0112117",
                }
            ],
            status="active",
            title="Job title",
        )
        assert_matches_type(JobUpdateFieldsResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_update_fields(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.jobs.with_raw_response.update_fields(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobUpdateFieldsResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_update_fields(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.jobs.with_streaming_response.update_fields(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobUpdateFieldsResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_fields(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.personnel.jobs.with_raw_response.update_fields(
                "",
            )
