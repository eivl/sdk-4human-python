# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, SDK4humanError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "SDK4human",
    "AsyncSDK4human",
    "Client",
    "AsyncClient",
]


class SDK4human(SyncAPIClient):
    authentications: resources.AuthenticationsResource
    absences: resources.AbsencesResource
    orgstructure_units: resources.OrgstructureUnitsResource
    orgstructure: resources.OrgstructureResource
    personnel: resources.PersonnelResource
    job_categories: resources.JobCategoriesResource
    employee_types: resources.EmployeeTypesResource
    resource_types: resources.ResourceTypesResource
    employments: resources.EmploymentsResource
    custom_fields: resources.CustomFieldsResource
    company_employees: resources.CompanyEmployeesResource
    competence: resources.CompetenceResource
    skill_types: resources.SkillTypesResource
    skills: resources.SkillsResource
    external_integrations: resources.ExternalIntegrationsResource
    users: resources.UsersResource
    workplans: resources.WorkplansResource
    with_raw_response: SDK4humanWithRawResponse
    with_streaming_response: SDK4humanWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous sdk-4human client instance.

        This automatically infers the `bearer_token` argument from the `SDK_4HUMAN_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("SDK_4HUMAN_BEARER_TOKEN")
        if bearer_token is None:
            raise SDK4humanError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the SDK_4HUMAN_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("SDK_4HUMAN_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hrm-4human.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.authentications = resources.AuthenticationsResource(self)
        self.absences = resources.AbsencesResource(self)
        self.orgstructure_units = resources.OrgstructureUnitsResource(self)
        self.orgstructure = resources.OrgstructureResource(self)
        self.personnel = resources.PersonnelResource(self)
        self.job_categories = resources.JobCategoriesResource(self)
        self.employee_types = resources.EmployeeTypesResource(self)
        self.resource_types = resources.ResourceTypesResource(self)
        self.employments = resources.EmploymentsResource(self)
        self.custom_fields = resources.CustomFieldsResource(self)
        self.company_employees = resources.CompanyEmployeesResource(self)
        self.competence = resources.CompetenceResource(self)
        self.skill_types = resources.SkillTypesResource(self)
        self.skills = resources.SkillsResource(self)
        self.external_integrations = resources.ExternalIntegrationsResource(self)
        self.users = resources.UsersResource(self)
        self.workplans = resources.WorkplansResource(self)
        self.with_raw_response = SDK4humanWithRawResponse(self)
        self.with_streaming_response = SDK4humanWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSDK4human(AsyncAPIClient):
    authentications: resources.AsyncAuthenticationsResource
    absences: resources.AsyncAbsencesResource
    orgstructure_units: resources.AsyncOrgstructureUnitsResource
    orgstructure: resources.AsyncOrgstructureResource
    personnel: resources.AsyncPersonnelResource
    job_categories: resources.AsyncJobCategoriesResource
    employee_types: resources.AsyncEmployeeTypesResource
    resource_types: resources.AsyncResourceTypesResource
    employments: resources.AsyncEmploymentsResource
    custom_fields: resources.AsyncCustomFieldsResource
    company_employees: resources.AsyncCompanyEmployeesResource
    competence: resources.AsyncCompetenceResource
    skill_types: resources.AsyncSkillTypesResource
    skills: resources.AsyncSkillsResource
    external_integrations: resources.AsyncExternalIntegrationsResource
    users: resources.AsyncUsersResource
    workplans: resources.AsyncWorkplansResource
    with_raw_response: AsyncSDK4humanWithRawResponse
    with_streaming_response: AsyncSDK4humanWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async sdk-4human client instance.

        This automatically infers the `bearer_token` argument from the `SDK_4HUMAN_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("SDK_4HUMAN_BEARER_TOKEN")
        if bearer_token is None:
            raise SDK4humanError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the SDK_4HUMAN_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("SDK_4HUMAN_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hrm-4human.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.authentications = resources.AsyncAuthenticationsResource(self)
        self.absences = resources.AsyncAbsencesResource(self)
        self.orgstructure_units = resources.AsyncOrgstructureUnitsResource(self)
        self.orgstructure = resources.AsyncOrgstructureResource(self)
        self.personnel = resources.AsyncPersonnelResource(self)
        self.job_categories = resources.AsyncJobCategoriesResource(self)
        self.employee_types = resources.AsyncEmployeeTypesResource(self)
        self.resource_types = resources.AsyncResourceTypesResource(self)
        self.employments = resources.AsyncEmploymentsResource(self)
        self.custom_fields = resources.AsyncCustomFieldsResource(self)
        self.company_employees = resources.AsyncCompanyEmployeesResource(self)
        self.competence = resources.AsyncCompetenceResource(self)
        self.skill_types = resources.AsyncSkillTypesResource(self)
        self.skills = resources.AsyncSkillsResource(self)
        self.external_integrations = resources.AsyncExternalIntegrationsResource(self)
        self.users = resources.AsyncUsersResource(self)
        self.workplans = resources.AsyncWorkplansResource(self)
        self.with_raw_response = AsyncSDK4humanWithRawResponse(self)
        self.with_streaming_response = AsyncSDK4humanWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SDK4humanWithRawResponse:
    def __init__(self, client: SDK4human) -> None:
        self.authentications = resources.AuthenticationsResourceWithRawResponse(client.authentications)
        self.absences = resources.AbsencesResourceWithRawResponse(client.absences)
        self.orgstructure_units = resources.OrgstructureUnitsResourceWithRawResponse(client.orgstructure_units)
        self.orgstructure = resources.OrgstructureResourceWithRawResponse(client.orgstructure)
        self.personnel = resources.PersonnelResourceWithRawResponse(client.personnel)
        self.job_categories = resources.JobCategoriesResourceWithRawResponse(client.job_categories)
        self.employee_types = resources.EmployeeTypesResourceWithRawResponse(client.employee_types)
        self.resource_types = resources.ResourceTypesResourceWithRawResponse(client.resource_types)
        self.employments = resources.EmploymentsResourceWithRawResponse(client.employments)
        self.custom_fields = resources.CustomFieldsResourceWithRawResponse(client.custom_fields)
        self.company_employees = resources.CompanyEmployeesResourceWithRawResponse(client.company_employees)
        self.competence = resources.CompetenceResourceWithRawResponse(client.competence)
        self.skill_types = resources.SkillTypesResourceWithRawResponse(client.skill_types)
        self.skills = resources.SkillsResourceWithRawResponse(client.skills)
        self.external_integrations = resources.ExternalIntegrationsResourceWithRawResponse(client.external_integrations)
        self.users = resources.UsersResourceWithRawResponse(client.users)
        self.workplans = resources.WorkplansResourceWithRawResponse(client.workplans)


class AsyncSDK4humanWithRawResponse:
    def __init__(self, client: AsyncSDK4human) -> None:
        self.authentications = resources.AsyncAuthenticationsResourceWithRawResponse(client.authentications)
        self.absences = resources.AsyncAbsencesResourceWithRawResponse(client.absences)
        self.orgstructure_units = resources.AsyncOrgstructureUnitsResourceWithRawResponse(client.orgstructure_units)
        self.orgstructure = resources.AsyncOrgstructureResourceWithRawResponse(client.orgstructure)
        self.personnel = resources.AsyncPersonnelResourceWithRawResponse(client.personnel)
        self.job_categories = resources.AsyncJobCategoriesResourceWithRawResponse(client.job_categories)
        self.employee_types = resources.AsyncEmployeeTypesResourceWithRawResponse(client.employee_types)
        self.resource_types = resources.AsyncResourceTypesResourceWithRawResponse(client.resource_types)
        self.employments = resources.AsyncEmploymentsResourceWithRawResponse(client.employments)
        self.custom_fields = resources.AsyncCustomFieldsResourceWithRawResponse(client.custom_fields)
        self.company_employees = resources.AsyncCompanyEmployeesResourceWithRawResponse(client.company_employees)
        self.competence = resources.AsyncCompetenceResourceWithRawResponse(client.competence)
        self.skill_types = resources.AsyncSkillTypesResourceWithRawResponse(client.skill_types)
        self.skills = resources.AsyncSkillsResourceWithRawResponse(client.skills)
        self.external_integrations = resources.AsyncExternalIntegrationsResourceWithRawResponse(
            client.external_integrations
        )
        self.users = resources.AsyncUsersResourceWithRawResponse(client.users)
        self.workplans = resources.AsyncWorkplansResourceWithRawResponse(client.workplans)


class SDK4humanWithStreamedResponse:
    def __init__(self, client: SDK4human) -> None:
        self.authentications = resources.AuthenticationsResourceWithStreamingResponse(client.authentications)
        self.absences = resources.AbsencesResourceWithStreamingResponse(client.absences)
        self.orgstructure_units = resources.OrgstructureUnitsResourceWithStreamingResponse(client.orgstructure_units)
        self.orgstructure = resources.OrgstructureResourceWithStreamingResponse(client.orgstructure)
        self.personnel = resources.PersonnelResourceWithStreamingResponse(client.personnel)
        self.job_categories = resources.JobCategoriesResourceWithStreamingResponse(client.job_categories)
        self.employee_types = resources.EmployeeTypesResourceWithStreamingResponse(client.employee_types)
        self.resource_types = resources.ResourceTypesResourceWithStreamingResponse(client.resource_types)
        self.employments = resources.EmploymentsResourceWithStreamingResponse(client.employments)
        self.custom_fields = resources.CustomFieldsResourceWithStreamingResponse(client.custom_fields)
        self.company_employees = resources.CompanyEmployeesResourceWithStreamingResponse(client.company_employees)
        self.competence = resources.CompetenceResourceWithStreamingResponse(client.competence)
        self.skill_types = resources.SkillTypesResourceWithStreamingResponse(client.skill_types)
        self.skills = resources.SkillsResourceWithStreamingResponse(client.skills)
        self.external_integrations = resources.ExternalIntegrationsResourceWithStreamingResponse(
            client.external_integrations
        )
        self.users = resources.UsersResourceWithStreamingResponse(client.users)
        self.workplans = resources.WorkplansResourceWithStreamingResponse(client.workplans)


class AsyncSDK4humanWithStreamedResponse:
    def __init__(self, client: AsyncSDK4human) -> None:
        self.authentications = resources.AsyncAuthenticationsResourceWithStreamingResponse(client.authentications)
        self.absences = resources.AsyncAbsencesResourceWithStreamingResponse(client.absences)
        self.orgstructure_units = resources.AsyncOrgstructureUnitsResourceWithStreamingResponse(
            client.orgstructure_units
        )
        self.orgstructure = resources.AsyncOrgstructureResourceWithStreamingResponse(client.orgstructure)
        self.personnel = resources.AsyncPersonnelResourceWithStreamingResponse(client.personnel)
        self.job_categories = resources.AsyncJobCategoriesResourceWithStreamingResponse(client.job_categories)
        self.employee_types = resources.AsyncEmployeeTypesResourceWithStreamingResponse(client.employee_types)
        self.resource_types = resources.AsyncResourceTypesResourceWithStreamingResponse(client.resource_types)
        self.employments = resources.AsyncEmploymentsResourceWithStreamingResponse(client.employments)
        self.custom_fields = resources.AsyncCustomFieldsResourceWithStreamingResponse(client.custom_fields)
        self.company_employees = resources.AsyncCompanyEmployeesResourceWithStreamingResponse(client.company_employees)
        self.competence = resources.AsyncCompetenceResourceWithStreamingResponse(client.competence)
        self.skill_types = resources.AsyncSkillTypesResourceWithStreamingResponse(client.skill_types)
        self.skills = resources.AsyncSkillsResourceWithStreamingResponse(client.skills)
        self.external_integrations = resources.AsyncExternalIntegrationsResourceWithStreamingResponse(
            client.external_integrations
        )
        self.users = resources.AsyncUsersResourceWithStreamingResponse(client.users)
        self.workplans = resources.AsyncWorkplansResourceWithStreamingResponse(client.workplans)


Client = SDK4human

AsyncClient = AsyncSDK4human
