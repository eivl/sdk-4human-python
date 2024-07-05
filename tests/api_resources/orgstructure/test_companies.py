# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.orgstructure import (
    CompanyCreateResponse,
    CompanyUpdateResponse,
    CompanyRetrieveResponse,
    CompanyUpdateFieldResponse,
    CompanyUpdateLocationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.create(
            company_country="POL",
            manager_id=2,
            organization_number="Org1",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(CompanyCreateResponse, company, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.create(
            company_country="POL",
            manager_id=2,
            organization_number="Org1",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            approval_policy="noPolicy",
            candidate_approval_policy="none",
            company_logo_url="string",
            locations=[
                {
                    "id": 1,
                    "company_number": "007",
                    "name": "Big company",
                    "visit_address": {
                        "address": "Street",
                        "zip_code": "1221",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                    "post_address": {
                        "address": "Street",
                        "zip_code": "1221",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                }
            ],
            name="New company X",
            parent_id=1,
            post_address={
                "address": "Street",
                "zip_code": "1221",
                "city": "Rzeszow",
                "municipality": "Rzeszow",
            },
            salary_system_company_id="X-1337",
            selected_company_number="Org1",
            status="ACTIVE",
            unit_id="3498392489",
            visit_address={
                "address": "Street",
                "zip_code": "35-021",
                "city": "Rzeszow",
                "municipality": "Rzeszow",
            },
        )
        assert_matches_type(CompanyCreateResponse, company, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SDK4human) -> None:
        response = client.orgstructure.companies.with_raw_response.create(
            company_country="POL",
            manager_id=2,
            organization_number="Org1",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyCreateResponse, company, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SDK4human) -> None:
        with client.orgstructure.companies.with_streaming_response.create(
            company_country="POL",
            manager_id=2,
            organization_number="Org1",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyCreateResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.retrieve(
            "string",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.retrieve(
            "string",
            external=True,
            on_given_date="string",
            with_soft_deleted=True,
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SDK4human) -> None:
        response = client.orgstructure.companies.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SDK4human) -> None:
        with client.orgstructure.companies.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.orgstructure.companies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.update(
            "string",
            manager_id=1,
            organization_number="982247500",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.update(
            "string",
            manager_id=1,
            organization_number="982247500",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            external=True,
            approval_policy="noPolicy",
            candidate_approval_policy="none",
            company_logo_url="https://www.avatar.com/pic.png",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            locations=[
                {
                    "id": None,
                    "company_number": "007",
                    "name": "Big company",
                    "visit_address": {
                        "address": "Street",
                        "zip_code": "35-021",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                    "post_address": {
                        "address": "Street",
                        "zip_code": "1221",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                }
            ],
            name="Main Unit",
            parent_id=1,
            post_address={
                "address": "x",
                "zip_code": "x",
                "city": "x",
                "municipality": "x",
            },
            ready_for_payment_message="Message",
            salary_system_company_id="ABC123-X",
            selected_company_number="x",
            status="ACTIVE",
            visit_address={
                "address": "x",
                "zip_code": "x",
                "city": "x",
                "municipality": "x",
            },
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SDK4human) -> None:
        response = client.orgstructure.companies.with_raw_response.update(
            "string",
            manager_id=1,
            organization_number="982247500",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SDK4human) -> None:
        with client.orgstructure.companies.with_streaming_response.update(
            "string",
            manager_id=1,
            organization_number="982247500",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyUpdateResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.orgstructure.companies.with_raw_response.update(
                "",
                manager_id=1,
                organization_number="982247500",
                unit_id="unit001",
                unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            )

    @parametrize
    def test_method_update_field(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.update_field(
            "string",
        )
        assert_matches_type(CompanyUpdateFieldResponse, company, path=["response"])

    @parametrize
    def test_method_update_field_with_all_params(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.update_field(
            "string",
            external=True,
            company_logo_url="https://www.avatar.com/pic.png",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                },
                {
                    "field_id": "ae94511b-a391-11ec-b67d-02012b4602c5",
                    "value_id": None,
                },
            ],
            locations=[
                {
                    "id": None,
                    "company_number": "007",
                    "name": "Big company",
                    "visit_address": {
                        "address": "Street",
                        "zip_code": "35-322",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                    "post_address": {
                        "address": "Street",
                        "zip_code": "1221",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                }
            ],
            manager_id=1,
            name="Main Unit",
            organization_number="982247500",
            parent_id=1,
            post_address={
                "address": "x",
                "zip_code": "x",
                "city": "x",
                "municipality": "x",
            },
            ready_for_payment_message="Message",
            salary_system_company_id="ABC123-X",
            selected_company_number="x",
            status="ACTIVE",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            visit_address={
                "address": "x",
                "zip_code": "x",
                "city": "x",
                "municipality": "x",
            },
        )
        assert_matches_type(CompanyUpdateFieldResponse, company, path=["response"])

    @parametrize
    def test_raw_response_update_field(self, client: SDK4human) -> None:
        response = client.orgstructure.companies.with_raw_response.update_field(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyUpdateFieldResponse, company, path=["response"])

    @parametrize
    def test_streaming_response_update_field(self, client: SDK4human) -> None:
        with client.orgstructure.companies.with_streaming_response.update_field(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyUpdateFieldResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_field(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.orgstructure.companies.with_raw_response.update_field(
                "",
            )

    @parametrize
    def test_method_update_locations(self, client: SDK4human) -> None:
        company = client.orgstructure.companies.update_locations(
            "string",
            body={},
        )
        assert_matches_type(CompanyUpdateLocationsResponse, company, path=["response"])

    @parametrize
    def test_raw_response_update_locations(self, client: SDK4human) -> None:
        response = client.orgstructure.companies.with_raw_response.update_locations(
            "string",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyUpdateLocationsResponse, company, path=["response"])

    @parametrize
    def test_streaming_response_update_locations(self, client: SDK4human) -> None:
        with client.orgstructure.companies.with_streaming_response.update_locations(
            "string",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyUpdateLocationsResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_locations(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.orgstructure.companies.with_raw_response.update_locations(
                "",
                body={},
            )


class TestAsyncCompanies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.create(
            company_country="POL",
            manager_id=2,
            organization_number="Org1",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(CompanyCreateResponse, company, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.create(
            company_country="POL",
            manager_id=2,
            organization_number="Org1",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            approval_policy="noPolicy",
            candidate_approval_policy="none",
            company_logo_url="string",
            locations=[
                {
                    "id": 1,
                    "company_number": "007",
                    "name": "Big company",
                    "visit_address": {
                        "address": "Street",
                        "zip_code": "1221",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                    "post_address": {
                        "address": "Street",
                        "zip_code": "1221",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                }
            ],
            name="New company X",
            parent_id=1,
            post_address={
                "address": "Street",
                "zip_code": "1221",
                "city": "Rzeszow",
                "municipality": "Rzeszow",
            },
            salary_system_company_id="X-1337",
            selected_company_number="Org1",
            status="ACTIVE",
            unit_id="3498392489",
            visit_address={
                "address": "Street",
                "zip_code": "35-021",
                "city": "Rzeszow",
                "municipality": "Rzeszow",
            },
        )
        assert_matches_type(CompanyCreateResponse, company, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.companies.with_raw_response.create(
            company_country="POL",
            manager_id=2,
            organization_number="Org1",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyCreateResponse, company, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.companies.with_streaming_response.create(
            company_country="POL",
            manager_id=2,
            organization_number="Org1",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyCreateResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.retrieve(
            "string",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.retrieve(
            "string",
            external=True,
            on_given_date="string",
            with_soft_deleted=True,
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.companies.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.companies.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.orgstructure.companies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.update(
            "string",
            manager_id=1,
            organization_number="982247500",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.update(
            "string",
            manager_id=1,
            organization_number="982247500",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            external=True,
            approval_policy="noPolicy",
            candidate_approval_policy="none",
            company_logo_url="https://www.avatar.com/pic.png",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                }
            ],
            locations=[
                {
                    "id": None,
                    "company_number": "007",
                    "name": "Big company",
                    "visit_address": {
                        "address": "Street",
                        "zip_code": "35-021",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                    "post_address": {
                        "address": "Street",
                        "zip_code": "1221",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                }
            ],
            name="Main Unit",
            parent_id=1,
            post_address={
                "address": "x",
                "zip_code": "x",
                "city": "x",
                "municipality": "x",
            },
            ready_for_payment_message="Message",
            salary_system_company_id="ABC123-X",
            selected_company_number="x",
            status="ACTIVE",
            visit_address={
                "address": "x",
                "zip_code": "x",
                "city": "x",
                "municipality": "x",
            },
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.companies.with_raw_response.update(
            "string",
            manager_id=1,
            organization_number="982247500",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.companies.with_streaming_response.update(
            "string",
            manager_id=1,
            organization_number="982247500",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyUpdateResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.orgstructure.companies.with_raw_response.update(
                "",
                manager_id=1,
                organization_number="982247500",
                unit_id="unit001",
                unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            )

    @parametrize
    async def test_method_update_field(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.update_field(
            "string",
        )
        assert_matches_type(CompanyUpdateFieldResponse, company, path=["response"])

    @parametrize
    async def test_method_update_field_with_all_params(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.update_field(
            "string",
            external=True,
            company_logo_url="https://www.avatar.com/pic.png",
            custom_fields=[
                {
                    "field_id": "b9ee8cbc-cda5-11e9-8233-080027122a07",
                    "value_id": "1e8c0383-bd78-11eb-b065-0242ac150002",
                },
                {
                    "field_id": "ae94511b-a391-11ec-b67d-02012b4602c5",
                    "value_id": None,
                },
            ],
            locations=[
                {
                    "id": None,
                    "company_number": "007",
                    "name": "Big company",
                    "visit_address": {
                        "address": "Street",
                        "zip_code": "35-322",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                    "post_address": {
                        "address": "Street",
                        "zip_code": "1221",
                        "city": "Rzeszow",
                        "municipality": "Rzeszow",
                    },
                }
            ],
            manager_id=1,
            name="Main Unit",
            organization_number="982247500",
            parent_id=1,
            post_address={
                "address": "x",
                "zip_code": "x",
                "city": "x",
                "municipality": "x",
            },
            ready_for_payment_message="Message",
            salary_system_company_id="ABC123-X",
            selected_company_number="x",
            status="ACTIVE",
            unit_id="unit001",
            unit_type_id="682dda63-9113-4198-9e5b-fcf22e5c6812",
            visit_address={
                "address": "x",
                "zip_code": "x",
                "city": "x",
                "municipality": "x",
            },
        )
        assert_matches_type(CompanyUpdateFieldResponse, company, path=["response"])

    @parametrize
    async def test_raw_response_update_field(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.companies.with_raw_response.update_field(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyUpdateFieldResponse, company, path=["response"])

    @parametrize
    async def test_streaming_response_update_field(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.companies.with_streaming_response.update_field(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyUpdateFieldResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_field(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.orgstructure.companies.with_raw_response.update_field(
                "",
            )

    @parametrize
    async def test_method_update_locations(self, async_client: AsyncSDK4human) -> None:
        company = await async_client.orgstructure.companies.update_locations(
            "string",
            body={},
        )
        assert_matches_type(CompanyUpdateLocationsResponse, company, path=["response"])

    @parametrize
    async def test_raw_response_update_locations(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.orgstructure.companies.with_raw_response.update_locations(
            "string",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyUpdateLocationsResponse, company, path=["response"])

    @parametrize
    async def test_streaming_response_update_locations(self, async_client: AsyncSDK4human) -> None:
        async with async_client.orgstructure.companies.with_streaming_response.update_locations(
            "string",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyUpdateLocationsResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_locations(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.orgstructure.companies.with_raw_response.update_locations(
                "",
                body={},
            )
