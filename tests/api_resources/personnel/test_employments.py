# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human._utils import parse_datetime
from sdk_minus_4human.types.personnel import (
    EmploymentListResponse,
    EmploymentCreateResponse,
    EmploymentUpdateResponse,
    EmploymentRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        employment = client.personnel.employments.create(
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            personal_identification={},
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        )
        assert_matches_type(EmploymentCreateResponse, employment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        employment = client.personnel.employments.create(
            employment={
                "id": 1,
                "number": "123EF",
                "phone_number_work": "1234567789",
                "email_work": "jdoe@pgs-soft.com",
                "start_date": "2018-05-17T08:08:56Z",
                "end_date": "2018-05-17T08:08:56Z",
                "first_working_day": "2018-05-17T08:08:56Z",
                "last_working_day": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "seniority_date": "2018-05-17T08:08:56Z",
                "main_salary": {
                    "id": 1,
                    "type": "MAIN_SALARY_TYPE_INDIVIDUAL",
                    "currency": "PLN",
                    "amount": "10",
                    "regulation_id": None,
                    "step_id": None,
                },
                "deductions": [
                    {
                        "id": 3,
                        "currency": "xxx",
                        "amount": "string",
                        "details": "string",
                    }
                ],
                "additional_salaries": [
                    {
                        "id": 1,
                        "currency": "xxx",
                        "amount": "string",
                        "details": "string",
                    }
                ],
                "benefits": [
                    {
                        "id": 2,
                        "currency": "MYR",
                        "amount": "1231",
                        "details": "string",
                    }
                ],
                "fte_factor": 1,
                "present_fte_factor": 1,
                "salary_seniority_date": "2018-05-17T08:08:56Z",
                "salary_type": "fixed_salary",
                "notice_period": "2m",
                "probation_period": "2m",
                "employee_type": "8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
                "comment": "OM NOM NOM",
                "main_workplace": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                "manager_id": 12345,
                "org_unit_id": 1,
                "job_id": 666,
                "position_title": "Sandwich artist",
                "personal_job_description": "I make the edible artistry happen.",
                "cost_place": "string",
                "location": "13131332",
                "work_relation_type": "WORK_RELATION_NOR_CONTRACTOR",
                "working_hours_arrangement": "480edc96-89de-4682-8c41-beeeb392a604",
                "working_hours_per_week": 37.5,
                "occupational_code": "1236101",
                "external_id": "externalId",
                "custom_fields": [
                    {
                        "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                        "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    }
                ],
                "org_units_with_advanced_access": [17],
                "reason_for_employment": "reason",
                "substitute_for_employment": [1, 2, 3],
                "overtime_allowance": "FIELD_OVERTIME_ALLOWANCE_YES",
            },
            personal_identification={
                "id_type": "none",
                "id_country": None,
                "id_number": None,
                "passport_country": "NOR",
                "passport_number": "987654321",
            },
            user={
                "id": "12345",
                "first_name": "John",
                "last_name": "Doe",
                "email": "jdoe@gmail.com",
                "language": "en",
                "date_of_birth": parse_datetime("1970-01-01T00:00:00Z"),
                "gender": "M",
                "active_directory_login": "jdoe@4human.no",
                "login_method": "ACTIVE_DIRECTORY",
                "phone_number_work": "111-111-111",
                "office_phone": "222-222-222",
                "email_work": "jdoe.work@gmail.com",
                "phone_number_private": "333-333-333",
                "home_phone": "444-444-444",
                "email_private": "jdoe.home@gmail.com",
                "address_info": [
                    {
                        "id": None,
                        "type": "primary",
                        "name": "Great Company HRM AS",
                        "post_address": {
                            "address": "Street 123",
                            "zip_code": "7068",
                            "city": "TRONDHEIM",
                            "municipality": "TRONDHEIM",
                            "building_entrance": None,
                            "country": "NOR",
                        },
                        "visit_address": {
                            "address": "Other Street 123",
                            "zip_code": "7069",
                            "city": "TRONDHEIM",
                            "municipality": "TRONDHEIM",
                            "building_entrance": None,
                            "country": "NOR",
                        },
                    },
                    {
                        "id": None,
                        "type": "additional",
                        "name": None,
                        "post_address": {
                            "address": "Street 123",
                            "zip_code": None,
                            "city": "TRONDHEIM",
                            "municipality": None,
                            "building_entrance": None,
                            "country": "NOR",
                        },
                        "visit_address": {
                            "address": "Other Street 123",
                            "zip_code": None,
                            "city": "TRONDHEIM",
                            "municipality": None,
                            "building_entrance": None,
                            "country": "NOR",
                        },
                    },
                ],
                "account_number": "8601.11.17947",
                "country_of_bank": "NOR",
                "iban": "NO9386011117947",
                "country_of_origin": "NOR",
                "initials": "JD",
            },
            force_no_approval_policy=True,
            send_invitation=True,
            company_employee={
                "seniority_date": "2019-08-29T00:00:00+02:00",
                "employee_id": "66",
                "main_employer": False,
                "salary_number": "1",
                "self_sickness": "2019-07-30T00:00:00+02:00",
                "free_employer": {
                    "from": "2019-07-30T00:00:00+02:00",
                    "to": "2019-07-30T00:00:00+02:00",
                },
                "work_permit": {
                    "from": "2019-07-30T00:00:00+02:00",
                    "to": "2019-07-30T00:00:00+02:00",
                },
                "termination_seniority_date": "2019-08-29T00:00:00+02:00",
                "residence_permit": {
                    "from": "2019-07-30T00:00:00+02:00",
                    "to": "2019-07-30T00:00:00+02:00",
                },
                "ready_for_payment": True,
                "custom_fields": [
                    {
                        "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                        "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    }
                ],
                "resource_type": 1,
            },
            personal_greetings="Hello",
            program_template_id=13,
            reference_date="2019-12-25T00:00:00+0000",
            task_template_changes=[
                {
                    "task_template_id": 10,
                    "actor_employment_id": 70,
                }
            ],
        )
        assert_matches_type(EmploymentCreateResponse, employment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.employments.with_raw_response.create(
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            personal_identification={},
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentCreateResponse, employment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.employments.with_streaming_response.create(
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            personal_identification={},
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = response.parse()
            assert_matches_type(EmploymentCreateResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        employment = client.personnel.employments.retrieve(
            "string",
        )
        assert_matches_type(EmploymentRetrieveResponse, employment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        employment = client.personnel.employments.retrieve(
            "string",
            external=True,
            on_given_date="string",
        )
        assert_matches_type(EmploymentRetrieveResponse, employment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.personnel.employments.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentRetrieveResponse, employment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.personnel.employments.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = response.parse()
            assert_matches_type(EmploymentRetrieveResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            client.personnel.employments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        employment = client.personnel.employments.update(
            "string",
            comment="OM NOM NOM",
            cost_place="string",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
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
            fte_factor=1,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.3,
            probation_period="2m",
            salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        employment = client.personnel.employments.update(
            "string",
            comment="OM NOM NOM",
            cost_place="string",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": "string",
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
            fte_factor=1,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.3,
            probation_period="2m",
            salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
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
            deductions=[
                {
                    "id": 1,
                    "amount": "200.00",
                    "currency": "NOK",
                    "details": "Estimated taxes for this year",
                }
            ],
            main_salary={
                "id": 1,
                "type": "MAIN_SALARY_TYPE_INDIVIDUAL",
                "currency": "NOK",
                "amount": "39888.50",
                "regulation_id": None,
                "step_id": None,
            },
            overtime_allowance="FIELD_OVERTIME_ALLOWANCE_YES",
            reason_for_employment="reason",
            substitute_for_employment=[
                {
                    "id": 1,
                    "value": "John Doe,007 (Investigator)",
                }
            ],
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.personnel.employments.with_raw_response.update(
            "string",
            comment="OM NOM NOM",
            cost_place="string",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
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
            fte_factor=1,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.3,
            probation_period="2m",
            salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.personnel.employments.with_streaming_response.update(
            "string",
            comment="OM NOM NOM",
            cost_place="string",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
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
            fte_factor=1,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.3,
            probation_period="2m",
            salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = response.parse()
            assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            client.personnel.employments.with_raw_response.update(
                "",
                comment="OM NOM NOM",
                cost_place="string",
                custom_fields=[
                    {
                        "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                        "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
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
                fte_factor=1,
                hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
                job_id=13,
                last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
                main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
                manager_id=123192837,
                notice_period="2m",
                number="Unique employment number which is string",
                occupational_code="1236101",
                org_unit_id=34,
                personal_job_description="I make the sandwich artistry happen",
                position_title="Sandwich artist",
                present_fte_factor=0.3,
                probation_period="2m",
                salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
                salary_type="fixed_salary",
                start_date="1990-01-01T00:00:00+0100",
                working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
                working_hours_per_week=37.5,
                work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
            )

    @parametrize
    def test_method_list(self, client: SDK4human) -> None:
        employment = client.personnel.employments.list()
        assert_matches_type(EmploymentListResponse, employment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SDK4human) -> None:
        employment = client.personnel.employments.list(
            employee_id="string",
            employment_id="string",
            external=True,
            limit=0,
            organisation_number="string",
            page=0,
        )
        assert_matches_type(EmploymentListResponse, employment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SDK4human) -> None:
        response = client.personnel.employments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentListResponse, employment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SDK4human) -> None:
        with client.personnel.employments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = response.parse()
            assert_matches_type(EmploymentListResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmployments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.personnel.employments.create(
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            personal_identification={},
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        )
        assert_matches_type(EmploymentCreateResponse, employment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.personnel.employments.create(
            employment={
                "id": 1,
                "number": "123EF",
                "phone_number_work": "1234567789",
                "email_work": "jdoe@pgs-soft.com",
                "start_date": "2018-05-17T08:08:56Z",
                "end_date": "2018-05-17T08:08:56Z",
                "first_working_day": "2018-05-17T08:08:56Z",
                "last_working_day": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "seniority_date": "2018-05-17T08:08:56Z",
                "main_salary": {
                    "id": 1,
                    "type": "MAIN_SALARY_TYPE_INDIVIDUAL",
                    "currency": "PLN",
                    "amount": "10",
                    "regulation_id": None,
                    "step_id": None,
                },
                "deductions": [
                    {
                        "id": 3,
                        "currency": "xxx",
                        "amount": "string",
                        "details": "string",
                    }
                ],
                "additional_salaries": [
                    {
                        "id": 1,
                        "currency": "xxx",
                        "amount": "string",
                        "details": "string",
                    }
                ],
                "benefits": [
                    {
                        "id": 2,
                        "currency": "MYR",
                        "amount": "1231",
                        "details": "string",
                    }
                ],
                "fte_factor": 1,
                "present_fte_factor": 1,
                "salary_seniority_date": "2018-05-17T08:08:56Z",
                "salary_type": "fixed_salary",
                "notice_period": "2m",
                "probation_period": "2m",
                "employee_type": "8e749ffa-bd74-4ff5-8365-96c673f1bb8e",
                "comment": "OM NOM NOM",
                "main_workplace": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                "manager_id": 12345,
                "org_unit_id": 1,
                "job_id": 666,
                "position_title": "Sandwich artist",
                "personal_job_description": "I make the edible artistry happen.",
                "cost_place": "string",
                "location": "13131332",
                "work_relation_type": "WORK_RELATION_NOR_CONTRACTOR",
                "working_hours_arrangement": "480edc96-89de-4682-8c41-beeeb392a604",
                "working_hours_per_week": 37.5,
                "occupational_code": "1236101",
                "external_id": "externalId",
                "custom_fields": [
                    {
                        "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                        "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    }
                ],
                "org_units_with_advanced_access": [17],
                "reason_for_employment": "reason",
                "substitute_for_employment": [1, 2, 3],
                "overtime_allowance": "FIELD_OVERTIME_ALLOWANCE_YES",
            },
            personal_identification={
                "id_type": "none",
                "id_country": None,
                "id_number": None,
                "passport_country": "NOR",
                "passport_number": "987654321",
            },
            user={
                "id": "12345",
                "first_name": "John",
                "last_name": "Doe",
                "email": "jdoe@gmail.com",
                "language": "en",
                "date_of_birth": parse_datetime("1970-01-01T00:00:00Z"),
                "gender": "M",
                "active_directory_login": "jdoe@4human.no",
                "login_method": "ACTIVE_DIRECTORY",
                "phone_number_work": "111-111-111",
                "office_phone": "222-222-222",
                "email_work": "jdoe.work@gmail.com",
                "phone_number_private": "333-333-333",
                "home_phone": "444-444-444",
                "email_private": "jdoe.home@gmail.com",
                "address_info": [
                    {
                        "id": None,
                        "type": "primary",
                        "name": "Great Company HRM AS",
                        "post_address": {
                            "address": "Street 123",
                            "zip_code": "7068",
                            "city": "TRONDHEIM",
                            "municipality": "TRONDHEIM",
                            "building_entrance": None,
                            "country": "NOR",
                        },
                        "visit_address": {
                            "address": "Other Street 123",
                            "zip_code": "7069",
                            "city": "TRONDHEIM",
                            "municipality": "TRONDHEIM",
                            "building_entrance": None,
                            "country": "NOR",
                        },
                    },
                    {
                        "id": None,
                        "type": "additional",
                        "name": None,
                        "post_address": {
                            "address": "Street 123",
                            "zip_code": None,
                            "city": "TRONDHEIM",
                            "municipality": None,
                            "building_entrance": None,
                            "country": "NOR",
                        },
                        "visit_address": {
                            "address": "Other Street 123",
                            "zip_code": None,
                            "city": "TRONDHEIM",
                            "municipality": None,
                            "building_entrance": None,
                            "country": "NOR",
                        },
                    },
                ],
                "account_number": "8601.11.17947",
                "country_of_bank": "NOR",
                "iban": "NO9386011117947",
                "country_of_origin": "NOR",
                "initials": "JD",
            },
            force_no_approval_policy=True,
            send_invitation=True,
            company_employee={
                "seniority_date": "2019-08-29T00:00:00+02:00",
                "employee_id": "66",
                "main_employer": False,
                "salary_number": "1",
                "self_sickness": "2019-07-30T00:00:00+02:00",
                "free_employer": {
                    "from": "2019-07-30T00:00:00+02:00",
                    "to": "2019-07-30T00:00:00+02:00",
                },
                "work_permit": {
                    "from": "2019-07-30T00:00:00+02:00",
                    "to": "2019-07-30T00:00:00+02:00",
                },
                "termination_seniority_date": "2019-08-29T00:00:00+02:00",
                "residence_permit": {
                    "from": "2019-07-30T00:00:00+02:00",
                    "to": "2019-07-30T00:00:00+02:00",
                },
                "ready_for_payment": True,
                "custom_fields": [
                    {
                        "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                        "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    }
                ],
                "resource_type": 1,
            },
            personal_greetings="Hello",
            program_template_id=13,
            reference_date="2019-12-25T00:00:00+0000",
            task_template_changes=[
                {
                    "task_template_id": 10,
                    "actor_employment_id": 70,
                }
            ],
        )
        assert_matches_type(EmploymentCreateResponse, employment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.employments.with_raw_response.create(
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            personal_identification={},
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = await response.parse()
        assert_matches_type(EmploymentCreateResponse, employment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.employments.with_streaming_response.create(
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            personal_identification={},
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = await response.parse()
            assert_matches_type(EmploymentCreateResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.personnel.employments.retrieve(
            "string",
        )
        assert_matches_type(EmploymentRetrieveResponse, employment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.personnel.employments.retrieve(
            "string",
            external=True,
            on_given_date="string",
        )
        assert_matches_type(EmploymentRetrieveResponse, employment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.employments.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = await response.parse()
        assert_matches_type(EmploymentRetrieveResponse, employment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.employments.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = await response.parse()
            assert_matches_type(EmploymentRetrieveResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            await async_client.personnel.employments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.personnel.employments.update(
            "string",
            comment="OM NOM NOM",
            cost_place="string",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
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
            fte_factor=1,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.3,
            probation_period="2m",
            salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.personnel.employments.update(
            "string",
            comment="OM NOM NOM",
            cost_place="string",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                    "value": "string",
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
            fte_factor=1,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.3,
            probation_period="2m",
            salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
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
            deductions=[
                {
                    "id": 1,
                    "amount": "200.00",
                    "currency": "NOK",
                    "details": "Estimated taxes for this year",
                }
            ],
            main_salary={
                "id": 1,
                "type": "MAIN_SALARY_TYPE_INDIVIDUAL",
                "currency": "NOK",
                "amount": "39888.50",
                "regulation_id": None,
                "step_id": None,
            },
            overtime_allowance="FIELD_OVERTIME_ALLOWANCE_YES",
            reason_for_employment="reason",
            substitute_for_employment=[
                {
                    "id": 1,
                    "value": "John Doe,007 (Investigator)",
                }
            ],
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.employments.with_raw_response.update(
            "string",
            comment="OM NOM NOM",
            cost_place="string",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
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
            fte_factor=1,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.3,
            probation_period="2m",
            salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = await response.parse()
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.employments.with_streaming_response.update(
            "string",
            comment="OM NOM NOM",
            cost_place="string",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
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
            fte_factor=1,
            hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
            job_id=13,
            last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
            main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
            manager_id=123192837,
            notice_period="2m",
            number="Unique employment number which is string",
            occupational_code="1236101",
            org_unit_id=34,
            personal_job_description="I make the sandwich artistry happen",
            position_title="Sandwich artist",
            present_fte_factor=0.3,
            probation_period="2m",
            salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
            salary_type="fixed_salary",
            start_date="1990-01-01T00:00:00+0100",
            working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
            working_hours_per_week=37.5,
            work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = await response.parse()
            assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            await async_client.personnel.employments.with_raw_response.update(
                "",
                comment="OM NOM NOM",
                cost_place="string",
                custom_fields=[
                    {
                        "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                        "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
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
                fte_factor=1,
                hr_role_id="2c623c34-1a36-11e9-a48f-080027122a07",
                job_id=13,
                last_working_day=parse_datetime("1990-01-01T12:00:00Z"),
                main_workplace_id="b9ee8cbc-cda5-11e9-8233-080027122a07",
                manager_id=123192837,
                notice_period="2m",
                number="Unique employment number which is string",
                occupational_code="1236101",
                org_unit_id=34,
                personal_job_description="I make the sandwich artistry happen",
                position_title="Sandwich artist",
                present_fte_factor=0.3,
                probation_period="2m",
                salary_seniority_date=parse_datetime("1990-01-01T12:00:00Z"),
                salary_type="fixed_salary",
                start_date="1990-01-01T00:00:00+0100",
                working_hours_arrangement="480edc96-89de-4682-8c41-beeeb392a604",
                working_hours_per_week=37.5,
                work_relation_type="WORK_RELATION_NOR_CONTRACTOR",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.personnel.employments.list()
        assert_matches_type(EmploymentListResponse, employment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSDK4human) -> None:
        employment = await async_client.personnel.employments.list(
            employee_id="string",
            employment_id="string",
            external=True,
            limit=0,
            organisation_number="string",
            page=0,
        )
        assert_matches_type(EmploymentListResponse, employment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.employments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = await response.parse()
        assert_matches_type(EmploymentListResponse, employment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.employments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = await response.parse()
            assert_matches_type(EmploymentListResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True
