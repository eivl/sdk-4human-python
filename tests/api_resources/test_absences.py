# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import (
    AbsenceListResponse,
    AbsenceCreateResponse,
    AbsenceDeleteResponse,
    AbsenceUpdateResponse,
)
from sdk_minus_4human._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAbsences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        absence = client.absences.create()
        assert_matches_type(AbsenceCreateResponse, absence, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        absence = client.absences.create(
            absences=[
                {
                    "employee_id": "30",
                    "external_absence_id": "some string 7",
                    "employment_id": [0, 0, 0],
                    "company_id": None,
                    "unit_id": "66",
                    "company_employee_id": 3,
                    "absence_code_id": 19,
                    "absence_code_id_external": None,
                    "date_from": "2023-09-11T00:00:00+00:00",
                    "date_to": "2023-09-11T00:00:00+00:00",
                    "hours": 5,
                    "percentage": 0,
                    "source_system": "Legacy absence system",
                    "status": "approved",
                    "comment": "some comment",
                },
                {
                    "employee_id": "string",
                    "external_absence_id": "56",
                    "employment_id": [3],
                    "company_id": 4,
                    "unit_id": "4",
                    "company_employee_id": 3,
                    "absence_code_id": 12,
                    "absence_code_id_external": "100",
                    "date_from": "2024-03-06T00:00:00+00:00",
                    "date_to": "2024-03-06T00:00:00+00:00",
                    "hours": 0,
                    "percentage": 100,
                    "source_system": "Absenso",
                    "status": "for_approval",
                    "comment": "some comment",
                },
            ],
        )
        assert_matches_type(AbsenceCreateResponse, absence, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.absences.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        absence = response.parse()
        assert_matches_type(AbsenceCreateResponse, absence, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.absences.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            absence = response.parse()
            assert_matches_type(AbsenceCreateResponse, absence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        absence = client.absences.update()
        assert_matches_type(AbsenceUpdateResponse, absence, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        absence = client.absences.update(
            absences=[
                {
                    "id": 8180,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 5,
                    "percentage": 0,
                    "source_system": "AbsenceSystemName",
                    "comment": "string",
                },
                {
                    "id": 8181,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "104",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 3,
                    "percentage": 0,
                    "source_system": "string",
                    "comment": "string",
                },
                {
                    "id": 8182,
                    "external_absence_id": "ABC-123",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 0,
                    "percentage": 50,
                    "source_system": "string",
                    "comment": "string",
                },
                {
                    "id": 8186,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "2024-11-13T00:00:00+00:00",
                    "hours": 0,
                    "percentage": 0,
                    "source_system": "string",
                    "comment": "string",
                },
                {
                    "id": 8187,
                    "external_absence_id": "string",
                    "absence_code_id": 11,
                    "absence_code_id_external": "string",
                    "date_from": "2024-12-12T00:00:00+00:00",
                    "date_to": "string",
                    "hours": 0,
                    "percentage": 0,
                    "source_system": "string",
                    "comment": "string",
                },
                {
                    "id": 8188,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 0,
                    "percentage": 0,
                    "source_system": "string",
                    "comment": "Quick comment on this specific absence",
                },
                {
                    "id": 8189,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 0,
                    "percentage": 100,
                    "source_system": "string",
                    "comment": "string",
                },
            ],
        )
        assert_matches_type(AbsenceUpdateResponse, absence, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.absences.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        absence = response.parse()
        assert_matches_type(AbsenceUpdateResponse, absence, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.absences.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            absence = response.parse()
            assert_matches_type(AbsenceUpdateResponse, absence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        absence = client.absences.list()
        assert_matches_type(AbsenceListResponse, absence, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        absence = client.absences.list(
            absence_code_category="leave_of_absence",
            absence_code_external_id="string",
            absence_code_ids="string",
            absence_code_internal_id="string",
            absence_code_type="self_certified",
            company_employee_id="string",
            company_id=0,
            created_at_from=parse_date("2019-12-27"),
            created_at_to=parse_date("2019-12-27"),
            created_by="string",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            employee_id="string",
            external_absence_id="string",
            instance_id="string",
            limit=0,
            origin="ABSENCE_REGISTERED_BY_API",
            page=0,
            source_system="string",
            status="for_approval",
            updated_at_from=parse_date("2019-12-27"),
            updated_at_to=parse_date("2019-12-27"),
            updated_by="string",
            user_id="string",
        )
        assert_matches_type(AbsenceListResponse, absence, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.absences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        absence = response.parse()
        assert_matches_type(AbsenceListResponse, absence, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.absences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            absence = response.parse()
            assert_matches_type(AbsenceListResponse, absence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: SDK4human) -> None:
        absence = client.absences.delete()
        assert_matches_type(AbsenceDeleteResponse, absence, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: SDK4human) -> None:
        absence = client.absences.delete(
            company_employee_id=4,
            company_id=2,
            created_by="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
            date_from=parse_datetime("2023-09-11T00:00:00+00:00"),
            date_to=parse_datetime("2023-10-30T00:00:00+00:00"),
            employee_id="3",
            external_absence_code_ids=["string", "string", "string"],
            external_absence_id=[0, 0, 0],
            internal_absence_id=[0, 0, 0],
            origin="ABSENCE_REGISTERED_BY_API",
            source_system="api",
            unit_id="2",
        )
        assert_matches_type(AbsenceDeleteResponse, absence, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: SDK4human) -> None:
        response = client.absences.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        absence = response.parse()
        assert_matches_type(AbsenceDeleteResponse, absence, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: SDK4human) -> None:
        with client.absences.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            absence = response.parse()
            assert_matches_type(AbsenceDeleteResponse, absence, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAbsences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        absence = await async_client.absences.create()
        assert_matches_type(AbsenceCreateResponse, absence, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        absence = await async_client.absences.create(
            absences=[
                {
                    "employee_id": "30",
                    "external_absence_id": "some string 7",
                    "employment_id": [0, 0, 0],
                    "company_id": None,
                    "unit_id": "66",
                    "company_employee_id": 3,
                    "absence_code_id": 19,
                    "absence_code_id_external": None,
                    "date_from": "2023-09-11T00:00:00+00:00",
                    "date_to": "2023-09-11T00:00:00+00:00",
                    "hours": 5,
                    "percentage": 0,
                    "source_system": "Legacy absence system",
                    "status": "approved",
                    "comment": "some comment",
                },
                {
                    "employee_id": "string",
                    "external_absence_id": "56",
                    "employment_id": [3],
                    "company_id": 4,
                    "unit_id": "4",
                    "company_employee_id": 3,
                    "absence_code_id": 12,
                    "absence_code_id_external": "100",
                    "date_from": "2024-03-06T00:00:00+00:00",
                    "date_to": "2024-03-06T00:00:00+00:00",
                    "hours": 0,
                    "percentage": 100,
                    "source_system": "Absenso",
                    "status": "for_approval",
                    "comment": "some comment",
                },
            ],
        )
        assert_matches_type(AbsenceCreateResponse, absence, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.absences.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        absence = await response.parse()
        assert_matches_type(AbsenceCreateResponse, absence, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.absences.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            absence = await response.parse()
            assert_matches_type(AbsenceCreateResponse, absence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        absence = await async_client.absences.update()
        assert_matches_type(AbsenceUpdateResponse, absence, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        absence = await async_client.absences.update(
            absences=[
                {
                    "id": 8180,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 5,
                    "percentage": 0,
                    "source_system": "AbsenceSystemName",
                    "comment": "string",
                },
                {
                    "id": 8181,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "104",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 3,
                    "percentage": 0,
                    "source_system": "string",
                    "comment": "string",
                },
                {
                    "id": 8182,
                    "external_absence_id": "ABC-123",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 0,
                    "percentage": 50,
                    "source_system": "string",
                    "comment": "string",
                },
                {
                    "id": 8186,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "2024-11-13T00:00:00+00:00",
                    "hours": 0,
                    "percentage": 0,
                    "source_system": "string",
                    "comment": "string",
                },
                {
                    "id": 8187,
                    "external_absence_id": "string",
                    "absence_code_id": 11,
                    "absence_code_id_external": "string",
                    "date_from": "2024-12-12T00:00:00+00:00",
                    "date_to": "string",
                    "hours": 0,
                    "percentage": 0,
                    "source_system": "string",
                    "comment": "string",
                },
                {
                    "id": 8188,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 0,
                    "percentage": 0,
                    "source_system": "string",
                    "comment": "Quick comment on this specific absence",
                },
                {
                    "id": 8189,
                    "external_absence_id": "string",
                    "absence_code_id": 0,
                    "absence_code_id_external": "string",
                    "date_from": "string",
                    "date_to": "string",
                    "hours": 0,
                    "percentage": 100,
                    "source_system": "string",
                    "comment": "string",
                },
            ],
        )
        assert_matches_type(AbsenceUpdateResponse, absence, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.absences.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        absence = await response.parse()
        assert_matches_type(AbsenceUpdateResponse, absence, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.absences.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            absence = await response.parse()
            assert_matches_type(AbsenceUpdateResponse, absence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        absence = await async_client.absences.list()
        assert_matches_type(AbsenceListResponse, absence, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        absence = await async_client.absences.list(
            absence_code_category="leave_of_absence",
            absence_code_external_id="string",
            absence_code_ids="string",
            absence_code_internal_id="string",
            absence_code_type="self_certified",
            company_employee_id="string",
            company_id=0,
            created_at_from=parse_date("2019-12-27"),
            created_at_to=parse_date("2019-12-27"),
            created_by="string",
            date_from=parse_date("2019-12-27"),
            date_to=parse_date("2019-12-27"),
            employee_id="string",
            external_absence_id="string",
            instance_id="string",
            limit=0,
            origin="ABSENCE_REGISTERED_BY_API",
            page=0,
            source_system="string",
            status="for_approval",
            updated_at_from=parse_date("2019-12-27"),
            updated_at_to=parse_date("2019-12-27"),
            updated_by="string",
            user_id="string",
        )
        assert_matches_type(AbsenceListResponse, absence, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.absences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        absence = await response.parse()
        assert_matches_type(AbsenceListResponse, absence, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.absences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            absence = await response.parse()
            assert_matches_type(AbsenceListResponse, absence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSDK4human) -> None:
        absence = await async_client.absences.delete()
        assert_matches_type(AbsenceDeleteResponse, absence, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSDK4human) -> None:
        absence = await async_client.absences.delete(
            company_employee_id=4,
            company_id=2,
            created_by="f8f8bf26-4bb6-11e9-ab3d-02638e2cefcd",
            date_from=parse_datetime("2023-09-11T00:00:00+00:00"),
            date_to=parse_datetime("2023-10-30T00:00:00+00:00"),
            employee_id="3",
            external_absence_code_ids=["string", "string", "string"],
            external_absence_id=[0, 0, 0],
            internal_absence_id=[0, 0, 0],
            origin="ABSENCE_REGISTERED_BY_API",
            source_system="api",
            unit_id="2",
        )
        assert_matches_type(AbsenceDeleteResponse, absence, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.absences.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        absence = await response.parse()
        assert_matches_type(AbsenceDeleteResponse, absence, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSDK4human) -> None:
        async with async_client.absences.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            absence = await response.parse()
            assert_matches_type(AbsenceDeleteResponse, absence, path=["response"])

        assert cast(Any, response.is_closed) is True
