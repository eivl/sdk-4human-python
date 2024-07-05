# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human._utils import parse_date
from sdk_minus_4human.types.absences import DeletedAbsenceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeletedAbsences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        deleted_absence = client.absences.deleted_absences.list()
        assert_matches_type(DeletedAbsenceListResponse, deleted_absence, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        deleted_absence = client.absences.deleted_absences.list(
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
            status="for_approval",
            updated_at_from=parse_date("2019-12-27"),
            updated_at_to=parse_date("2019-12-27"),
            updated_by="string",
            user_id="string",
        )
        assert_matches_type(DeletedAbsenceListResponse, deleted_absence, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.absences.deleted_absences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted_absence = response.parse()
        assert_matches_type(DeletedAbsenceListResponse, deleted_absence, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.absences.deleted_absences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted_absence = response.parse()
            assert_matches_type(DeletedAbsenceListResponse, deleted_absence, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeletedAbsences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        deleted_absence = await async_client.absences.deleted_absences.list()
        assert_matches_type(DeletedAbsenceListResponse, deleted_absence, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        deleted_absence = await async_client.absences.deleted_absences.list(
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
            status="for_approval",
            updated_at_from=parse_date("2019-12-27"),
            updated_at_to=parse_date("2019-12-27"),
            updated_by="string",
            user_id="string",
        )
        assert_matches_type(DeletedAbsenceListResponse, deleted_absence, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.absences.deleted_absences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted_absence = await response.parse()
        assert_matches_type(DeletedAbsenceListResponse, deleted_absence, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.absences.deleted_absences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted_absence = await response.parse()
            assert_matches_type(DeletedAbsenceListResponse, deleted_absence, path=["response"])

        assert cast(Any, response.is_closed) is True
