# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sdk_minus_4human import SDK4human, AsyncSDK4human
from sdk_minus_4human.types.personnel.changes import (
    DetailRetrieveUserChangesResponse,
    DetailRetrieveEmploymentChangesResponse,
    DetailListCompanyEmployeeChangesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_company_employee_changes(self, client: SDK4human) -> None:
        detail = client.personnel.changes.details.list_company_employee_changes(
            from_=0,
            to=0,
        )
        assert_matches_type(DetailListCompanyEmployeeChangesResponse, detail, path=["response"])

    @parametrize
    def test_method_list_company_employee_changes_with_all_params(self, client: SDK4human) -> None:
        detail = client.personnel.changes.details.list_company_employee_changes(
            from_=0,
            to=0,
            company_id="string",
            database_id="string",
            employee_id="string",
            employment_id="string",
            format="timestamp",
            limit=0,
            organization_number="string",
            page=0,
            response_as_objects=True,
            salary_system_company_id="string",
            sort_by="createdAt",
            unit_id="string",
            user_id="string",
            with_custom_fields_tree=True,
        )
        assert_matches_type(DetailListCompanyEmployeeChangesResponse, detail, path=["response"])

    @parametrize
    def test_raw_response_list_company_employee_changes(self, client: SDK4human) -> None:
        response = client.personnel.changes.details.with_raw_response.list_company_employee_changes(
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailListCompanyEmployeeChangesResponse, detail, path=["response"])

    @parametrize
    def test_streaming_response_list_company_employee_changes(self, client: SDK4human) -> None:
        with client.personnel.changes.details.with_streaming_response.list_company_employee_changes(
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailListCompanyEmployeeChangesResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_employment_changes(self, client: SDK4human) -> None:
        detail = client.personnel.changes.details.retrieve_employment_changes(
            "string",
            from_=0,
            to=0,
        )
        assert_matches_type(DetailRetrieveEmploymentChangesResponse, detail, path=["response"])

    @parametrize
    def test_method_retrieve_employment_changes_with_all_params(self, client: SDK4human) -> None:
        detail = client.personnel.changes.details.retrieve_employment_changes(
            "string",
            from_=0,
            to=0,
            format="timestamp",
            limit=0,
            page=0,
            response_as_objects=True,
            sort_by="createdAt",
            with_custom_fields_tree=True,
        )
        assert_matches_type(DetailRetrieveEmploymentChangesResponse, detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve_employment_changes(self, client: SDK4human) -> None:
        response = client.personnel.changes.details.with_raw_response.retrieve_employment_changes(
            "string",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailRetrieveEmploymentChangesResponse, detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_employment_changes(self, client: SDK4human) -> None:
        with client.personnel.changes.details.with_streaming_response.retrieve_employment_changes(
            "string",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailRetrieveEmploymentChangesResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_employment_changes(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            client.personnel.changes.details.with_raw_response.retrieve_employment_changes(
                "",
                from_=0,
                to=0,
            )

    @parametrize
    def test_method_retrieve_user_changes(self, client: SDK4human) -> None:
        detail = client.personnel.changes.details.retrieve_user_changes(
            "string",
            from_=0,
            to=0,
        )
        assert_matches_type(DetailRetrieveUserChangesResponse, detail, path=["response"])

    @parametrize
    def test_method_retrieve_user_changes_with_all_params(self, client: SDK4human) -> None:
        detail = client.personnel.changes.details.retrieve_user_changes(
            "string",
            from_=0,
            to=0,
            format="timestamp",
            limit=0,
            page=0,
            response_as_objects=True,
            sort_by="createdAt",
            with_custom_fields_tree=True,
        )
        assert_matches_type(DetailRetrieveUserChangesResponse, detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve_user_changes(self, client: SDK4human) -> None:
        response = client.personnel.changes.details.with_raw_response.retrieve_user_changes(
            "string",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailRetrieveUserChangesResponse, detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_user_changes(self, client: SDK4human) -> None:
        with client.personnel.changes.details.with_streaming_response.retrieve_user_changes(
            "string",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailRetrieveUserChangesResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_user_changes(self, client: SDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.personnel.changes.details.with_raw_response.retrieve_user_changes(
                "",
                from_=0,
                to=0,
            )


class TestAsyncDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_company_employee_changes(self, async_client: AsyncSDK4human) -> None:
        detail = await async_client.personnel.changes.details.list_company_employee_changes(
            from_=0,
            to=0,
        )
        assert_matches_type(DetailListCompanyEmployeeChangesResponse, detail, path=["response"])

    @parametrize
    async def test_method_list_company_employee_changes_with_all_params(self, async_client: AsyncSDK4human) -> None:
        detail = await async_client.personnel.changes.details.list_company_employee_changes(
            from_=0,
            to=0,
            company_id="string",
            database_id="string",
            employee_id="string",
            employment_id="string",
            format="timestamp",
            limit=0,
            organization_number="string",
            page=0,
            response_as_objects=True,
            salary_system_company_id="string",
            sort_by="createdAt",
            unit_id="string",
            user_id="string",
            with_custom_fields_tree=True,
        )
        assert_matches_type(DetailListCompanyEmployeeChangesResponse, detail, path=["response"])

    @parametrize
    async def test_raw_response_list_company_employee_changes(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.changes.details.with_raw_response.list_company_employee_changes(
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailListCompanyEmployeeChangesResponse, detail, path=["response"])

    @parametrize
    async def test_streaming_response_list_company_employee_changes(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.changes.details.with_streaming_response.list_company_employee_changes(
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailListCompanyEmployeeChangesResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_employment_changes(self, async_client: AsyncSDK4human) -> None:
        detail = await async_client.personnel.changes.details.retrieve_employment_changes(
            "string",
            from_=0,
            to=0,
        )
        assert_matches_type(DetailRetrieveEmploymentChangesResponse, detail, path=["response"])

    @parametrize
    async def test_method_retrieve_employment_changes_with_all_params(self, async_client: AsyncSDK4human) -> None:
        detail = await async_client.personnel.changes.details.retrieve_employment_changes(
            "string",
            from_=0,
            to=0,
            format="timestamp",
            limit=0,
            page=0,
            response_as_objects=True,
            sort_by="createdAt",
            with_custom_fields_tree=True,
        )
        assert_matches_type(DetailRetrieveEmploymentChangesResponse, detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_employment_changes(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.changes.details.with_raw_response.retrieve_employment_changes(
            "string",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailRetrieveEmploymentChangesResponse, detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_employment_changes(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.changes.details.with_streaming_response.retrieve_employment_changes(
            "string",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailRetrieveEmploymentChangesResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_employment_changes(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employment_id` but received ''"):
            await async_client.personnel.changes.details.with_raw_response.retrieve_employment_changes(
                "",
                from_=0,
                to=0,
            )

    @parametrize
    async def test_method_retrieve_user_changes(self, async_client: AsyncSDK4human) -> None:
        detail = await async_client.personnel.changes.details.retrieve_user_changes(
            "string",
            from_=0,
            to=0,
        )
        assert_matches_type(DetailRetrieveUserChangesResponse, detail, path=["response"])

    @parametrize
    async def test_method_retrieve_user_changes_with_all_params(self, async_client: AsyncSDK4human) -> None:
        detail = await async_client.personnel.changes.details.retrieve_user_changes(
            "string",
            from_=0,
            to=0,
            format="timestamp",
            limit=0,
            page=0,
            response_as_objects=True,
            sort_by="createdAt",
            with_custom_fields_tree=True,
        )
        assert_matches_type(DetailRetrieveUserChangesResponse, detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_user_changes(self, async_client: AsyncSDK4human) -> None:
        response = await async_client.personnel.changes.details.with_raw_response.retrieve_user_changes(
            "string",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailRetrieveUserChangesResponse, detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_user_changes(self, async_client: AsyncSDK4human) -> None:
        async with async_client.personnel.changes.details.with_streaming_response.retrieve_user_changes(
            "string",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailRetrieveUserChangesResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_user_changes(self, async_client: AsyncSDK4human) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.personnel.changes.details.with_raw_response.retrieve_user_changes(
                "",
                from_=0,
                to=0,
            )
