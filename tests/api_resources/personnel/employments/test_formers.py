# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human._utils import parse_datetime
from sdk_minus_4human.types.personnel.employments import FormerCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFormers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        former = client.personnel.employments.formers.create(
            company_employee={},
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            internal_termination_reason_id="47ea068b-a752-11eb-b815-0242ac120006",
            personal_identification={},
            termination_reason_id="23420948",
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        )
        assert_matches_type(FormerCreateResponse, former, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        former = client.personnel.employments.formers.create(
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
                        "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
                "resource_type": 1,
            },
            employment={
                "number": "123EF",
                "phone_number_work": "1234567789",
                "email_work": "jdoe@pgs-soft.com",
                "start_date": "2018-05-17T08:08:56Z",
                "end_date": "2018-05-17T08:08:56Z",
                "first_working_day": "2018-05-17T08:08:56Z",
                "last_working_day": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "seniority_date": "2018-05-17T08:08:56Z",
                "fte_factor": 1,
                "present_fte_factor": 1,
                "salary_seniority_date": "2018-05-17T08:08:56Z",
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
            internal_termination_reason_id="47ea068b-a752-11eb-b815-0242ac120006",
            personal_identification={
                "id_type": "none",
                "id_country": None,
                "id_number": None,
                "passport_country": "NOR",
                "passport_number": "987654321",
            },
            termination_reason_id="23420948",
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
        )
        assert_matches_type(FormerCreateResponse, former, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.personnel.employments.formers.with_raw_response.create(
            company_employee={},
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            internal_termination_reason_id="47ea068b-a752-11eb-b815-0242ac120006",
            personal_identification={},
            termination_reason_id="23420948",
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        former = response.parse()
        assert_matches_type(FormerCreateResponse, former, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.personnel.employments.formers.with_streaming_response.create(
            company_employee={},
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            internal_termination_reason_id="47ea068b-a752-11eb-b815-0242ac120006",
            personal_identification={},
            termination_reason_id="23420948",
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            former = response.parse()
            assert_matches_type(FormerCreateResponse, former, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFormers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        former = await async_client.personnel.employments.formers.create(
            company_employee={},
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            internal_termination_reason_id="47ea068b-a752-11eb-b815-0242ac120006",
            personal_identification={},
            termination_reason_id="23420948",
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        )
        assert_matches_type(FormerCreateResponse, former, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        former = await async_client.personnel.employments.formers.create(
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
                        "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
                "resource_type": 1,
            },
            employment={
                "number": "123EF",
                "phone_number_work": "1234567789",
                "email_work": "jdoe@pgs-soft.com",
                "start_date": "2018-05-17T08:08:56Z",
                "end_date": "2018-05-17T08:08:56Z",
                "first_working_day": "2018-05-17T08:08:56Z",
                "last_working_day": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "seniority_date": "2018-05-17T08:08:56Z",
                "fte_factor": 1,
                "present_fte_factor": 1,
                "salary_seniority_date": "2018-05-17T08:08:56Z",
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
            internal_termination_reason_id="47ea068b-a752-11eb-b815-0242ac120006",
            personal_identification={
                "id_type": "none",
                "id_country": None,
                "id_number": None,
                "passport_country": "NOR",
                "passport_number": "987654321",
            },
            termination_reason_id="23420948",
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
        )
        assert_matches_type(FormerCreateResponse, former, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.employments.formers.with_raw_response.create(
            company_employee={},
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            internal_termination_reason_id="47ea068b-a752-11eb-b815-0242ac120006",
            personal_identification={},
            termination_reason_id="23420948",
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        former = await response.parse()
        assert_matches_type(FormerCreateResponse, former, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.employments.formers.with_streaming_response.create(
            company_employee={},
            employment={
                "start_date": "2018-05-17T08:08:56Z",
                "hr_role_id": "2c623c34-1a36-11e9-a48f-080027122a07",
                "job_id": 666,
                "org_units_with_advanced_access": [17],
            },
            internal_termination_reason_id="47ea068b-a752-11eb-b815-0242ac120006",
            personal_identification={},
            termination_reason_id="23420948",
            user={
                "first_name": "John",
                "last_name": "Doe",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            former = await response.parse()
            assert_matches_type(FormerCreateResponse, former, path=["response"])

        assert cast(Any, response.is_closed) is True
