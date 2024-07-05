# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .salary import (
    SalaryResource,
    AsyncSalaryResource,
    SalaryResourceWithRawResponse,
    AsyncSalaryResourceWithRawResponse,
    SalaryResourceWithStreamingResponse,
    AsyncSalaryResourceWithStreamingResponse,
)
from .changes import (
    ChangesResource,
    AsyncChangesResource,
    ChangesResourceWithRawResponse,
    AsyncChangesResourceWithRawResponse,
    ChangesResourceWithStreamingResponse,
    AsyncChangesResourceWithStreamingResponse,
)
from .children import (
    ChildrenResource,
    AsyncChildrenResource,
    ChildrenResourceWithRawResponse,
    AsyncChildrenResourceWithRawResponse,
    ChildrenResourceWithStreamingResponse,
    AsyncChildrenResourceWithStreamingResponse,
)
from .hr_roles import (
    HrRolesResource,
    AsyncHrRolesResource,
    HrRolesResourceWithRawResponse,
    AsyncHrRolesResourceWithRawResponse,
    HrRolesResourceWithStreamingResponse,
    AsyncHrRolesResourceWithStreamingResponse,
)
from .profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .dictionary import (
    DictionaryResource,
    AsyncDictionaryResource,
    DictionaryResourceWithRawResponse,
    AsyncDictionaryResourceWithRawResponse,
    DictionaryResourceWithStreamingResponse,
    AsyncDictionaryResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .employments import (
    EmploymentsResource,
    AsyncEmploymentsResource,
    EmploymentsResourceWithRawResponse,
    AsyncEmploymentsResourceWithRawResponse,
    EmploymentsResourceWithStreamingResponse,
    AsyncEmploymentsResourceWithStreamingResponse,
)
from .next_of_kin import (
    NextOfKinResource,
    AsyncNextOfKinResource,
    NextOfKinResourceWithRawResponse,
    AsyncNextOfKinResourceWithRawResponse,
    NextOfKinResourceWithStreamingResponse,
    AsyncNextOfKinResourceWithStreamingResponse,
)
from .custom_fields import (
    CustomFieldsResource,
    AsyncCustomFieldsResource,
    CustomFieldsResourceWithRawResponse,
    AsyncCustomFieldsResourceWithRawResponse,
    CustomFieldsResourceWithStreamingResponse,
    AsyncCustomFieldsResourceWithStreamingResponse,
)
from .salary.salary import SalaryResource, AsyncSalaryResource
from .exported_files import (
    ExportedFilesResource,
    AsyncExportedFilesResource,
    ExportedFilesResourceWithRawResponse,
    AsyncExportedFilesResourceWithRawResponse,
    ExportedFilesResourceWithStreamingResponse,
    AsyncExportedFilesResourceWithStreamingResponse,
)
from .job_categories import (
    JobCategoriesResource,
    AsyncJobCategoriesResource,
    JobCategoriesResourceWithRawResponse,
    AsyncJobCategoriesResourceWithRawResponse,
    JobCategoriesResourceWithStreamingResponse,
    AsyncJobCategoriesResourceWithStreamingResponse,
)
from .resource_types import (
    ResourceTypesResource,
    AsyncResourceTypesResource,
    ResourceTypesResourceWithRawResponse,
    AsyncResourceTypesResourceWithRawResponse,
    ResourceTypesResourceWithStreamingResponse,
    AsyncResourceTypesResourceWithStreamingResponse,
)
from .changes.changes import ChangesResource, AsyncChangesResource
from .contact_details import (
    ContactDetailsResource,
    AsyncContactDetailsResource,
    ContactDetailsResourceWithRawResponse,
    AsyncContactDetailsResourceWithRawResponse,
    ContactDetailsResourceWithStreamingResponse,
    AsyncContactDetailsResourceWithStreamingResponse,
)
from .employment_types import (
    EmploymentTypesResource,
    AsyncEmploymentTypesResource,
    EmploymentTypesResourceWithRawResponse,
    AsyncEmploymentTypesResourceWithRawResponse,
    EmploymentTypesResourceWithStreamingResponse,
    AsyncEmploymentTypesResourceWithStreamingResponse,
)
from .children.children import ChildrenResource, AsyncChildrenResource
from .company_employees import (
    CompanyEmployeesResource,
    AsyncCompanyEmployeesResource,
    CompanyEmployeesResourceWithRawResponse,
    AsyncCompanyEmployeesResourceWithRawResponse,
    CompanyEmployeesResourceWithStreamingResponse,
    AsyncCompanyEmployeesResourceWithStreamingResponse,
)
from .profiles.profiles import ProfilesResource, AsyncProfilesResource
from .salary_regulations import (
    SalaryRegulationsResource,
    AsyncSalaryRegulationsResource,
    SalaryRegulationsResourceWithRawResponse,
    AsyncSalaryRegulationsResourceWithRawResponse,
    SalaryRegulationsResourceWithStreamingResponse,
    AsyncSalaryRegulationsResourceWithStreamingResponse,
)
from .work_contact_details import (
    WorkContactDetailsResource,
    AsyncWorkContactDetailsResource,
    WorkContactDetailsResourceWithRawResponse,
    AsyncWorkContactDetailsResourceWithRawResponse,
    WorkContactDetailsResourceWithStreamingResponse,
    AsyncWorkContactDetailsResourceWithStreamingResponse,
)
from .dictionary.dictionary import DictionaryResource, AsyncDictionaryResource
from .employments.employments import EmploymentsResource, AsyncEmploymentsResource
from .next_of_kin.next_of_kin import NextOfKinResource, AsyncNextOfKinResource
from .private_contact_details import (
    PrivateContactDetailsResource,
    AsyncPrivateContactDetailsResource,
    PrivateContactDetailsResourceWithRawResponse,
    AsyncPrivateContactDetailsResourceWithRawResponse,
    PrivateContactDetailsResourceWithStreamingResponse,
    AsyncPrivateContactDetailsResourceWithStreamingResponse,
)
from .individual_main_salaries import (
    IndividualMainSalariesResource,
    AsyncIndividualMainSalariesResource,
    IndividualMainSalariesResourceWithRawResponse,
    AsyncIndividualMainSalariesResourceWithRawResponse,
    IndividualMainSalariesResourceWithStreamingResponse,
    AsyncIndividualMainSalariesResourceWithStreamingResponse,
)
from .working_hours_arrangements import (
    WorkingHoursArrangementsResource,
    AsyncWorkingHoursArrangementsResource,
    WorkingHoursArrangementsResourceWithRawResponse,
    AsyncWorkingHoursArrangementsResourceWithRawResponse,
    WorkingHoursArrangementsResourceWithStreamingResponse,
    AsyncWorkingHoursArrangementsResourceWithStreamingResponse,
)
from .custom_fields.custom_fields import CustomFieldsResource, AsyncCustomFieldsResource
from .company_employees.company_employees import CompanyEmployeesResource, AsyncCompanyEmployeesResource

__all__ = ["PersonnelResource", "AsyncPersonnelResource"]


class PersonnelResource(SyncAPIResource):
    @cached_property
    def exported_files(self) -> ExportedFilesResource:
        return ExportedFilesResource(self._client)

    @cached_property
    def hr_roles(self) -> HrRolesResource:
        return HrRolesResource(self._client)

    @cached_property
    def dictionary(self) -> DictionaryResource:
        return DictionaryResource(self._client)

    @cached_property
    def employment_types(self) -> EmploymentTypesResource:
        return EmploymentTypesResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def job_categories(self) -> JobCategoriesResource:
        return JobCategoriesResource(self._client)

    @cached_property
    def resource_types(self) -> ResourceTypesResource:
        return ResourceTypesResource(self._client)

    @cached_property
    def employments(self) -> EmploymentsResource:
        return EmploymentsResource(self._client)

    @cached_property
    def custom_fields(self) -> CustomFieldsResource:
        return CustomFieldsResource(self._client)

    @cached_property
    def company_employees(self) -> CompanyEmployeesResource:
        return CompanyEmployeesResource(self._client)

    @cached_property
    def individual_main_salaries(self) -> IndividualMainSalariesResource:
        return IndividualMainSalariesResource(self._client)

    @cached_property
    def salary(self) -> SalaryResource:
        return SalaryResource(self._client)

    @cached_property
    def salary_regulations(self) -> SalaryRegulationsResource:
        return SalaryRegulationsResource(self._client)

    @cached_property
    def profiles(self) -> ProfilesResource:
        return ProfilesResource(self._client)

    @cached_property
    def next_of_kin(self) -> NextOfKinResource:
        return NextOfKinResource(self._client)

    @cached_property
    def children(self) -> ChildrenResource:
        return ChildrenResource(self._client)

    @cached_property
    def working_hours_arrangements(self) -> WorkingHoursArrangementsResource:
        return WorkingHoursArrangementsResource(self._client)

    @cached_property
    def work_contact_details(self) -> WorkContactDetailsResource:
        return WorkContactDetailsResource(self._client)

    @cached_property
    def private_contact_details(self) -> PrivateContactDetailsResource:
        return PrivateContactDetailsResource(self._client)

    @cached_property
    def contact_details(self) -> ContactDetailsResource:
        return ContactDetailsResource(self._client)

    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PersonnelResourceWithRawResponse:
        return PersonnelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonnelResourceWithStreamingResponse:
        return PersonnelResourceWithStreamingResponse(self)


class AsyncPersonnelResource(AsyncAPIResource):
    @cached_property
    def exported_files(self) -> AsyncExportedFilesResource:
        return AsyncExportedFilesResource(self._client)

    @cached_property
    def hr_roles(self) -> AsyncHrRolesResource:
        return AsyncHrRolesResource(self._client)

    @cached_property
    def dictionary(self) -> AsyncDictionaryResource:
        return AsyncDictionaryResource(self._client)

    @cached_property
    def employment_types(self) -> AsyncEmploymentTypesResource:
        return AsyncEmploymentTypesResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def job_categories(self) -> AsyncJobCategoriesResource:
        return AsyncJobCategoriesResource(self._client)

    @cached_property
    def resource_types(self) -> AsyncResourceTypesResource:
        return AsyncResourceTypesResource(self._client)

    @cached_property
    def employments(self) -> AsyncEmploymentsResource:
        return AsyncEmploymentsResource(self._client)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResource:
        return AsyncCustomFieldsResource(self._client)

    @cached_property
    def company_employees(self) -> AsyncCompanyEmployeesResource:
        return AsyncCompanyEmployeesResource(self._client)

    @cached_property
    def individual_main_salaries(self) -> AsyncIndividualMainSalariesResource:
        return AsyncIndividualMainSalariesResource(self._client)

    @cached_property
    def salary(self) -> AsyncSalaryResource:
        return AsyncSalaryResource(self._client)

    @cached_property
    def salary_regulations(self) -> AsyncSalaryRegulationsResource:
        return AsyncSalaryRegulationsResource(self._client)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        return AsyncProfilesResource(self._client)

    @cached_property
    def next_of_kin(self) -> AsyncNextOfKinResource:
        return AsyncNextOfKinResource(self._client)

    @cached_property
    def children(self) -> AsyncChildrenResource:
        return AsyncChildrenResource(self._client)

    @cached_property
    def working_hours_arrangements(self) -> AsyncWorkingHoursArrangementsResource:
        return AsyncWorkingHoursArrangementsResource(self._client)

    @cached_property
    def work_contact_details(self) -> AsyncWorkContactDetailsResource:
        return AsyncWorkContactDetailsResource(self._client)

    @cached_property
    def private_contact_details(self) -> AsyncPrivateContactDetailsResource:
        return AsyncPrivateContactDetailsResource(self._client)

    @cached_property
    def contact_details(self) -> AsyncContactDetailsResource:
        return AsyncContactDetailsResource(self._client)

    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPersonnelResourceWithRawResponse:
        return AsyncPersonnelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonnelResourceWithStreamingResponse:
        return AsyncPersonnelResourceWithStreamingResponse(self)


class PersonnelResourceWithRawResponse:
    def __init__(self, personnel: PersonnelResource) -> None:
        self._personnel = personnel

    @cached_property
    def exported_files(self) -> ExportedFilesResourceWithRawResponse:
        return ExportedFilesResourceWithRawResponse(self._personnel.exported_files)

    @cached_property
    def hr_roles(self) -> HrRolesResourceWithRawResponse:
        return HrRolesResourceWithRawResponse(self._personnel.hr_roles)

    @cached_property
    def dictionary(self) -> DictionaryResourceWithRawResponse:
        return DictionaryResourceWithRawResponse(self._personnel.dictionary)

    @cached_property
    def employment_types(self) -> EmploymentTypesResourceWithRawResponse:
        return EmploymentTypesResourceWithRawResponse(self._personnel.employment_types)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._personnel.jobs)

    @cached_property
    def job_categories(self) -> JobCategoriesResourceWithRawResponse:
        return JobCategoriesResourceWithRawResponse(self._personnel.job_categories)

    @cached_property
    def resource_types(self) -> ResourceTypesResourceWithRawResponse:
        return ResourceTypesResourceWithRawResponse(self._personnel.resource_types)

    @cached_property
    def employments(self) -> EmploymentsResourceWithRawResponse:
        return EmploymentsResourceWithRawResponse(self._personnel.employments)

    @cached_property
    def custom_fields(self) -> CustomFieldsResourceWithRawResponse:
        return CustomFieldsResourceWithRawResponse(self._personnel.custom_fields)

    @cached_property
    def company_employees(self) -> CompanyEmployeesResourceWithRawResponse:
        return CompanyEmployeesResourceWithRawResponse(self._personnel.company_employees)

    @cached_property
    def individual_main_salaries(self) -> IndividualMainSalariesResourceWithRawResponse:
        return IndividualMainSalariesResourceWithRawResponse(self._personnel.individual_main_salaries)

    @cached_property
    def salary(self) -> SalaryResourceWithRawResponse:
        return SalaryResourceWithRawResponse(self._personnel.salary)

    @cached_property
    def salary_regulations(self) -> SalaryRegulationsResourceWithRawResponse:
        return SalaryRegulationsResourceWithRawResponse(self._personnel.salary_regulations)

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self._personnel.profiles)

    @cached_property
    def next_of_kin(self) -> NextOfKinResourceWithRawResponse:
        return NextOfKinResourceWithRawResponse(self._personnel.next_of_kin)

    @cached_property
    def children(self) -> ChildrenResourceWithRawResponse:
        return ChildrenResourceWithRawResponse(self._personnel.children)

    @cached_property
    def working_hours_arrangements(self) -> WorkingHoursArrangementsResourceWithRawResponse:
        return WorkingHoursArrangementsResourceWithRawResponse(self._personnel.working_hours_arrangements)

    @cached_property
    def work_contact_details(self) -> WorkContactDetailsResourceWithRawResponse:
        return WorkContactDetailsResourceWithRawResponse(self._personnel.work_contact_details)

    @cached_property
    def private_contact_details(self) -> PrivateContactDetailsResourceWithRawResponse:
        return PrivateContactDetailsResourceWithRawResponse(self._personnel.private_contact_details)

    @cached_property
    def contact_details(self) -> ContactDetailsResourceWithRawResponse:
        return ContactDetailsResourceWithRawResponse(self._personnel.contact_details)

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._personnel.changes)


class AsyncPersonnelResourceWithRawResponse:
    def __init__(self, personnel: AsyncPersonnelResource) -> None:
        self._personnel = personnel

    @cached_property
    def exported_files(self) -> AsyncExportedFilesResourceWithRawResponse:
        return AsyncExportedFilesResourceWithRawResponse(self._personnel.exported_files)

    @cached_property
    def hr_roles(self) -> AsyncHrRolesResourceWithRawResponse:
        return AsyncHrRolesResourceWithRawResponse(self._personnel.hr_roles)

    @cached_property
    def dictionary(self) -> AsyncDictionaryResourceWithRawResponse:
        return AsyncDictionaryResourceWithRawResponse(self._personnel.dictionary)

    @cached_property
    def employment_types(self) -> AsyncEmploymentTypesResourceWithRawResponse:
        return AsyncEmploymentTypesResourceWithRawResponse(self._personnel.employment_types)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._personnel.jobs)

    @cached_property
    def job_categories(self) -> AsyncJobCategoriesResourceWithRawResponse:
        return AsyncJobCategoriesResourceWithRawResponse(self._personnel.job_categories)

    @cached_property
    def resource_types(self) -> AsyncResourceTypesResourceWithRawResponse:
        return AsyncResourceTypesResourceWithRawResponse(self._personnel.resource_types)

    @cached_property
    def employments(self) -> AsyncEmploymentsResourceWithRawResponse:
        return AsyncEmploymentsResourceWithRawResponse(self._personnel.employments)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResourceWithRawResponse:
        return AsyncCustomFieldsResourceWithRawResponse(self._personnel.custom_fields)

    @cached_property
    def company_employees(self) -> AsyncCompanyEmployeesResourceWithRawResponse:
        return AsyncCompanyEmployeesResourceWithRawResponse(self._personnel.company_employees)

    @cached_property
    def individual_main_salaries(self) -> AsyncIndividualMainSalariesResourceWithRawResponse:
        return AsyncIndividualMainSalariesResourceWithRawResponse(self._personnel.individual_main_salaries)

    @cached_property
    def salary(self) -> AsyncSalaryResourceWithRawResponse:
        return AsyncSalaryResourceWithRawResponse(self._personnel.salary)

    @cached_property
    def salary_regulations(self) -> AsyncSalaryRegulationsResourceWithRawResponse:
        return AsyncSalaryRegulationsResourceWithRawResponse(self._personnel.salary_regulations)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self._personnel.profiles)

    @cached_property
    def next_of_kin(self) -> AsyncNextOfKinResourceWithRawResponse:
        return AsyncNextOfKinResourceWithRawResponse(self._personnel.next_of_kin)

    @cached_property
    def children(self) -> AsyncChildrenResourceWithRawResponse:
        return AsyncChildrenResourceWithRawResponse(self._personnel.children)

    @cached_property
    def working_hours_arrangements(self) -> AsyncWorkingHoursArrangementsResourceWithRawResponse:
        return AsyncWorkingHoursArrangementsResourceWithRawResponse(self._personnel.working_hours_arrangements)

    @cached_property
    def work_contact_details(self) -> AsyncWorkContactDetailsResourceWithRawResponse:
        return AsyncWorkContactDetailsResourceWithRawResponse(self._personnel.work_contact_details)

    @cached_property
    def private_contact_details(self) -> AsyncPrivateContactDetailsResourceWithRawResponse:
        return AsyncPrivateContactDetailsResourceWithRawResponse(self._personnel.private_contact_details)

    @cached_property
    def contact_details(self) -> AsyncContactDetailsResourceWithRawResponse:
        return AsyncContactDetailsResourceWithRawResponse(self._personnel.contact_details)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._personnel.changes)


class PersonnelResourceWithStreamingResponse:
    def __init__(self, personnel: PersonnelResource) -> None:
        self._personnel = personnel

    @cached_property
    def exported_files(self) -> ExportedFilesResourceWithStreamingResponse:
        return ExportedFilesResourceWithStreamingResponse(self._personnel.exported_files)

    @cached_property
    def hr_roles(self) -> HrRolesResourceWithStreamingResponse:
        return HrRolesResourceWithStreamingResponse(self._personnel.hr_roles)

    @cached_property
    def dictionary(self) -> DictionaryResourceWithStreamingResponse:
        return DictionaryResourceWithStreamingResponse(self._personnel.dictionary)

    @cached_property
    def employment_types(self) -> EmploymentTypesResourceWithStreamingResponse:
        return EmploymentTypesResourceWithStreamingResponse(self._personnel.employment_types)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._personnel.jobs)

    @cached_property
    def job_categories(self) -> JobCategoriesResourceWithStreamingResponse:
        return JobCategoriesResourceWithStreamingResponse(self._personnel.job_categories)

    @cached_property
    def resource_types(self) -> ResourceTypesResourceWithStreamingResponse:
        return ResourceTypesResourceWithStreamingResponse(self._personnel.resource_types)

    @cached_property
    def employments(self) -> EmploymentsResourceWithStreamingResponse:
        return EmploymentsResourceWithStreamingResponse(self._personnel.employments)

    @cached_property
    def custom_fields(self) -> CustomFieldsResourceWithStreamingResponse:
        return CustomFieldsResourceWithStreamingResponse(self._personnel.custom_fields)

    @cached_property
    def company_employees(self) -> CompanyEmployeesResourceWithStreamingResponse:
        return CompanyEmployeesResourceWithStreamingResponse(self._personnel.company_employees)

    @cached_property
    def individual_main_salaries(self) -> IndividualMainSalariesResourceWithStreamingResponse:
        return IndividualMainSalariesResourceWithStreamingResponse(self._personnel.individual_main_salaries)

    @cached_property
    def salary(self) -> SalaryResourceWithStreamingResponse:
        return SalaryResourceWithStreamingResponse(self._personnel.salary)

    @cached_property
    def salary_regulations(self) -> SalaryRegulationsResourceWithStreamingResponse:
        return SalaryRegulationsResourceWithStreamingResponse(self._personnel.salary_regulations)

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self._personnel.profiles)

    @cached_property
    def next_of_kin(self) -> NextOfKinResourceWithStreamingResponse:
        return NextOfKinResourceWithStreamingResponse(self._personnel.next_of_kin)

    @cached_property
    def children(self) -> ChildrenResourceWithStreamingResponse:
        return ChildrenResourceWithStreamingResponse(self._personnel.children)

    @cached_property
    def working_hours_arrangements(self) -> WorkingHoursArrangementsResourceWithStreamingResponse:
        return WorkingHoursArrangementsResourceWithStreamingResponse(self._personnel.working_hours_arrangements)

    @cached_property
    def work_contact_details(self) -> WorkContactDetailsResourceWithStreamingResponse:
        return WorkContactDetailsResourceWithStreamingResponse(self._personnel.work_contact_details)

    @cached_property
    def private_contact_details(self) -> PrivateContactDetailsResourceWithStreamingResponse:
        return PrivateContactDetailsResourceWithStreamingResponse(self._personnel.private_contact_details)

    @cached_property
    def contact_details(self) -> ContactDetailsResourceWithStreamingResponse:
        return ContactDetailsResourceWithStreamingResponse(self._personnel.contact_details)

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._personnel.changes)


class AsyncPersonnelResourceWithStreamingResponse:
    def __init__(self, personnel: AsyncPersonnelResource) -> None:
        self._personnel = personnel

    @cached_property
    def exported_files(self) -> AsyncExportedFilesResourceWithStreamingResponse:
        return AsyncExportedFilesResourceWithStreamingResponse(self._personnel.exported_files)

    @cached_property
    def hr_roles(self) -> AsyncHrRolesResourceWithStreamingResponse:
        return AsyncHrRolesResourceWithStreamingResponse(self._personnel.hr_roles)

    @cached_property
    def dictionary(self) -> AsyncDictionaryResourceWithStreamingResponse:
        return AsyncDictionaryResourceWithStreamingResponse(self._personnel.dictionary)

    @cached_property
    def employment_types(self) -> AsyncEmploymentTypesResourceWithStreamingResponse:
        return AsyncEmploymentTypesResourceWithStreamingResponse(self._personnel.employment_types)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._personnel.jobs)

    @cached_property
    def job_categories(self) -> AsyncJobCategoriesResourceWithStreamingResponse:
        return AsyncJobCategoriesResourceWithStreamingResponse(self._personnel.job_categories)

    @cached_property
    def resource_types(self) -> AsyncResourceTypesResourceWithStreamingResponse:
        return AsyncResourceTypesResourceWithStreamingResponse(self._personnel.resource_types)

    @cached_property
    def employments(self) -> AsyncEmploymentsResourceWithStreamingResponse:
        return AsyncEmploymentsResourceWithStreamingResponse(self._personnel.employments)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResourceWithStreamingResponse:
        return AsyncCustomFieldsResourceWithStreamingResponse(self._personnel.custom_fields)

    @cached_property
    def company_employees(self) -> AsyncCompanyEmployeesResourceWithStreamingResponse:
        return AsyncCompanyEmployeesResourceWithStreamingResponse(self._personnel.company_employees)

    @cached_property
    def individual_main_salaries(self) -> AsyncIndividualMainSalariesResourceWithStreamingResponse:
        return AsyncIndividualMainSalariesResourceWithStreamingResponse(self._personnel.individual_main_salaries)

    @cached_property
    def salary(self) -> AsyncSalaryResourceWithStreamingResponse:
        return AsyncSalaryResourceWithStreamingResponse(self._personnel.salary)

    @cached_property
    def salary_regulations(self) -> AsyncSalaryRegulationsResourceWithStreamingResponse:
        return AsyncSalaryRegulationsResourceWithStreamingResponse(self._personnel.salary_regulations)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self._personnel.profiles)

    @cached_property
    def next_of_kin(self) -> AsyncNextOfKinResourceWithStreamingResponse:
        return AsyncNextOfKinResourceWithStreamingResponse(self._personnel.next_of_kin)

    @cached_property
    def children(self) -> AsyncChildrenResourceWithStreamingResponse:
        return AsyncChildrenResourceWithStreamingResponse(self._personnel.children)

    @cached_property
    def working_hours_arrangements(self) -> AsyncWorkingHoursArrangementsResourceWithStreamingResponse:
        return AsyncWorkingHoursArrangementsResourceWithStreamingResponse(self._personnel.working_hours_arrangements)

    @cached_property
    def work_contact_details(self) -> AsyncWorkContactDetailsResourceWithStreamingResponse:
        return AsyncWorkContactDetailsResourceWithStreamingResponse(self._personnel.work_contact_details)

    @cached_property
    def private_contact_details(self) -> AsyncPrivateContactDetailsResourceWithStreamingResponse:
        return AsyncPrivateContactDetailsResourceWithStreamingResponse(self._personnel.private_contact_details)

    @cached_property
    def contact_details(self) -> AsyncContactDetailsResourceWithStreamingResponse:
        return AsyncContactDetailsResourceWithStreamingResponse(self._personnel.contact_details)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._personnel.changes)
