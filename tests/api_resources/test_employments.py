# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types import EmploymentUpdateResponse
from sdk_minus_4human._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        employment = client.employments.update(
            "string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        employment = client.employments.update(
            "string",
            external=True,
            force_no_approval_policy=True,
            additional_salaries=[
                {
                    "id": 1,
                    "amount": "1000",
                    "currency": "NOK",
                    "details": "Quarterly Bonus",
                }
            ],
            benefits=[
                {
                    "id": 1,
                    "amount": "500",
                    "currency": "NOK",
                    "details": None,
                }
            ],
            comment="OM NOM NOM",
            cost_place="costPlace",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": "string",
                },
                {
                    "field_id": "8ff718f0-a391-11ec-b67d-02012b4602c5",
                    "value_id": None,
                    "value": "string",
                },
            ],
            deductions=[
                {
                    "id": 1,
                    "amount": "200.00",
                    "currency": "NOK",
                    "details": "Estimated taxes for this year",
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            end_date="1990-01-01T00:00:00+0100",
            external_id=None,
            first_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            fte_factor=0.3,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            location="333-333-333",
            main_salary={
                "id": 2,
                "type": "MAIN_SALARY_TYPE_INDIVIDUAL",
                "currency": "NOK",
                "amount": "77676.00",
                "regulation_id": None,
                "step_id": None,
            },
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            org_units_with_advanced_access=[17],
            overtime_allowance="FIELD_OVERTIME_ALLOWANCE_YES",
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.1,
            probation_period="2m",
            reason_for_employment="reason",
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            substitute_for_employment=[
                {
                    "id": 1,
                    "value": "John Doe,007 (Investigator)",
                }
            ],
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.employments.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.employments.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = response.parse()
            assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            client.employments.with_raw_response.update(
                "",
            )


class TestAsyncEmployments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.employments.update(
            "string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.employments.update(
            "string",
            external=True,
            force_no_approval_policy=True,
            additional_salaries=[
                {
                    "id": 1,
                    "amount": "1000",
                    "currency": "NOK",
                    "details": "Quarterly Bonus",
                }
            ],
            benefits=[
                {
                    "id": 1,
                    "amount": "500",
                    "currency": "NOK",
                    "details": None,
                }
            ],
            comment="OM NOM NOM",
            cost_place="costPlace",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": "string",
                },
                {
                    "field_id": "8ff718f0-a391-11ec-b67d-02012b4602c5",
                    "value_id": None,
                    "value": "string",
                },
            ],
            deductions=[
                {
                    "id": 1,
                    "amount": "200.00",
                    "currency": "NOK",
                    "details": "Estimated taxes for this year",
                }
            ],
            effective_dates={
                "comment": None,
                "start_validity_date": None,
                "end_validity_date": None,
                "immediate": True,
            },
            employee_type_id="8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
            end_date="1990-01-01T00:00:00+0100",
            external_id=None,
            first_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            fte_factor=0.3,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            location="333-333-333",
            main_salary={
                "id": 2,
                "type": "MAIN_SALARY_TYPE_INDIVIDUAL",
                "currency": "NOK",
                "amount": "77676.00",
                "regulation_id": None,
                "step_id": None,
            },
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            org_units_with_advanced_access=[17],
            overtime_allowance="FIELD_OVERTIME_ALLOWANCE_YES",
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.1,
            probation_period="2m",
            reason_for_employment="reason",
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            substitute_for_employment=[
                {
                    "id": 1,
                    "value": "John Doe,007 (Investigator)",
                }
            ],
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.employments.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = await response.parse()
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.employments.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = await response.parse()
            assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            await async_client.employments.with_raw_response.update(
                "",
            )
