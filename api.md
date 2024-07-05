# Authentications

Types:

```python
from sdk_minus_4human.types import AuthenticationCreateResponse
```

Methods:

- <code title="post /token">client.authentications.<a href="./src/sdk_minus_4human/resources/authentications.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/authentication_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/authentication_create_response.py">AuthenticationCreateResponse</a></code>

# Absences

Types:

```python
from sdk_minus_4human.types import (
    AbsenceCreateResponse,
    AbsenceUpdateResponse,
    AbsenceListResponse,
    AbsenceDeleteResponse,
)
```

Methods:

- <code title="post /absences">client.absences.<a href="./src/sdk_minus_4human/resources/absences/absences.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/absence_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/absence_create_response.py">AbsenceCreateResponse</a></code>
- <code title="patch /absences">client.absences.<a href="./src/sdk_minus_4human/resources/absences/absences.py">update</a>(\*\*<a href="src/sdk_minus_4human/types/absence_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/absence_update_response.py">AbsenceUpdateResponse</a></code>
- <code title="get /absences">client.absences.<a href="./src/sdk_minus_4human/resources/absences/absences.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/absence_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/absence_list_response.py">AbsenceListResponse</a></code>
- <code title="delete /absences">client.absences.<a href="./src/sdk_minus_4human/resources/absences/absences.py">delete</a>(\*\*<a href="src/sdk_minus_4human/types/absence_delete_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/absence_delete_response.py">AbsenceDeleteResponse</a></code>

## DeletedAbsences

Types:

```python
from sdk_minus_4human.types.absences import DeletedAbsenceListResponse
```

Methods:

- <code title="get /absences/deleted-absences">client.absences.deleted_absences.<a href="./src/sdk_minus_4human/resources/absences/deleted_absences.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/absences/deleted_absence_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/absences/deleted_absence_list_response.py">DeletedAbsenceListResponse</a></code>

## AbsenceCodes

Types:

```python
from sdk_minus_4human.types.absences import AbsenceCodeListResponse
```

Methods:

- <code title="get /absences/absence-codes">client.absences.absence_codes.<a href="./src/sdk_minus_4human/resources/absences/absence_codes.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/absences/absence_code_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/absences/absence_code_list_response.py">AbsenceCodeListResponse</a></code>

# OrgstructureUnits

Types:

```python
from sdk_minus_4human.types import (
    OrgstructureUnitCreateResponse,
    OrgstructureUnitRetrieveResponse,
    OrgstructureUnitUpdateResponse,
)
```

Methods:

- <code title="post /orgstructure/units">client.orgstructure_units.<a href="./src/sdk_minus_4human/resources/orgstructure_units.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure_unit_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure_unit_create_response.py">OrgstructureUnitCreateResponse</a></code>
- <code title="get /orgstructure/units/{organizationUnitId}">client.orgstructure_units.<a href="./src/sdk_minus_4human/resources/orgstructure_units.py">retrieve</a>(organization_unit_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure_unit_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure_unit_retrieve_response.py">OrgstructureUnitRetrieveResponse</a></code>
- <code title="put /orgstructure/units/{organizationUnitId}">client.orgstructure_units.<a href="./src/sdk_minus_4human/resources/orgstructure_units.py">update</a>(organization_unit_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure_unit_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure_unit_update_response.py">OrgstructureUnitUpdateResponse</a></code>

# Orgstructure

Types:

```python
from sdk_minus_4human.types import OrgstructureListResponse
```

Methods:

- <code title="get /orgstructure">client.orgstructure.<a href="./src/sdk_minus_4human/resources/orgstructure/orgstructure.py">list</a>() -> <a href="./src/sdk_minus_4human/types/orgstructure_list_response.py">OrgstructureListResponse</a></code>

## Units

Types:

```python
from sdk_minus_4human.types.orgstructure import UnitUpdateResponse
```

Methods:

- <code title="patch /orgstructure/units/{organizationUnitId}">client.orgstructure.units.<a href="./src/sdk_minus_4human/resources/orgstructure/units/units.py">update</a>(organization_unit_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure/unit_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/unit_update_response.py">UnitUpdateResponse</a></code>

### Changes

Types:

```python
from sdk_minus_4human.types.orgstructure.units import ChangeListResponse
```

Methods:

- <code title="get /orgstructure/units/changes">client.orgstructure.units.changes.<a href="./src/sdk_minus_4human/resources/orgstructure/units/changes.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure/units/change_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/units/change_list_response.py">ChangeListResponse</a></code>

## Companies

Types:

```python
from sdk_minus_4human.types.orgstructure import (
    CompanyCreateResponse,
    CompanyRetrieveResponse,
    CompanyUpdateResponse,
    CompanyUpdateFieldResponse,
    CompanyUpdateLocationsResponse,
)
```

Methods:

- <code title="post /orgstructure/companies">client.orgstructure.companies.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/companies.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure/company_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/company_create_response.py">CompanyCreateResponse</a></code>
- <code title="get /orgstructure/companies/{companyId}">client.orgstructure.companies.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/companies.py">retrieve</a>(company_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure/company_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/company_retrieve_response.py">CompanyRetrieveResponse</a></code>
- <code title="put /orgstructure/companies/{companyId}">client.orgstructure.companies.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/companies.py">update</a>(company_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure/company_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/company_update_response.py">CompanyUpdateResponse</a></code>
- <code title="patch /orgstructure/companies/{companyId}">client.orgstructure.companies.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/companies.py">update_field</a>(company_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure/company_update_field_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/company_update_field_response.py">CompanyUpdateFieldResponse</a></code>
- <code title="patch /orgstructure/companies/{companyId}/update-locations">client.orgstructure.companies.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/companies.py">update_locations</a>(company_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure/company_update_locations_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/company_update_locations_response.py">CompanyUpdateLocationsResponse</a></code>

### CustomFields

#### Templates

Types:

```python
from sdk_minus_4human.types.orgstructure.companies.custom_fields import (
    TemplateCreateResponse,
    TemplateListResponse,
)
```

Methods:

- <code title="post /orgstructure/companies/custom-fields/templates">client.orgstructure.companies.custom_fields.templates.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/custom_fields/templates.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure/companies/custom_fields/template_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/companies/custom_fields/template_create_response.py">TemplateCreateResponse</a></code>
- <code title="get /orgstructure/companies/custom-fields/templates">client.orgstructure.companies.custom_fields.templates.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/custom_fields/templates.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure/companies/custom_fields/template_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/companies/custom_fields/template_list_response.py">TemplateListResponse</a></code>

### Locations

Types:

```python
from sdk_minus_4human.types.orgstructure.companies import LocationListResponse
```

Methods:

- <code title="get /orgstructure/companies/{companyId}/locations">client.orgstructure.companies.locations.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/locations.py">list</a>(company_id) -> <a href="./src/sdk_minus_4human/types/orgstructure/companies/location_list_response.py">LocationListResponse</a></code>

### Changes

Types:

```python
from sdk_minus_4human.types.orgstructure.companies import ChangeListResponse
```

Methods:

- <code title="get /orgstructure/companies/changes">client.orgstructure.companies.changes.<a href="./src/sdk_minus_4human/resources/orgstructure/companies/changes.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure/companies/change_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/companies/change_list_response.py">ChangeListResponse</a></code>

## Locations

Types:

```python
from sdk_minus_4human.types.orgstructure import LocationListResponse
```

Methods:

- <code title="get /orgstructure/locations">client.orgstructure.locations.<a href="./src/sdk_minus_4human/resources/orgstructure/locations.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure/location_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/location_list_response.py">LocationListResponse</a></code>

## UnitTypes

Types:

```python
from sdk_minus_4human.types.orgstructure import (
    UnitTypeCreateResponse,
    UnitTypeRetrieveResponse,
    UnitTypeUpdateResponse,
    UnitTypeListResponse,
    UnitTypeUpdateFieldResponse,
)
```

Methods:

- <code title="post /orgstructure/unit-types">client.orgstructure.unit_types.<a href="./src/sdk_minus_4human/resources/orgstructure/unit_types.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure/unit_type_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/unit_type_create_response.py">UnitTypeCreateResponse</a></code>
- <code title="get /orgstructure/unit-types/{unitTypeId}">client.orgstructure.unit_types.<a href="./src/sdk_minus_4human/resources/orgstructure/unit_types.py">retrieve</a>(unit_type_id) -> <a href="./src/sdk_minus_4human/types/orgstructure/unit_type_retrieve_response.py">UnitTypeRetrieveResponse</a></code>
- <code title="put /orgstructure/unit-types/{unitTypeId}">client.orgstructure.unit_types.<a href="./src/sdk_minus_4human/resources/orgstructure/unit_types.py">update</a>(unit_type_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure/unit_type_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/unit_type_update_response.py">UnitTypeUpdateResponse</a></code>
- <code title="get /orgstructure/unit-types">client.orgstructure.unit_types.<a href="./src/sdk_minus_4human/resources/orgstructure/unit_types.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/orgstructure/unit_type_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/unit_type_list_response.py">UnitTypeListResponse</a></code>
- <code title="patch /orgstructure/unit-types/{unitTypeId}">client.orgstructure.unit_types.<a href="./src/sdk_minus_4human/resources/orgstructure/unit_types.py">update_field</a>(unit_type_id, \*\*<a href="src/sdk_minus_4human/types/orgstructure/unit_type_update_field_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/orgstructure/unit_type_update_field_response.py">UnitTypeUpdateFieldResponse</a></code>

# Personnel

## ExportedFiles

Types:

```python
from sdk_minus_4human.types.personnel import ExportedFileRetrieveResponse
```

Methods:

- <code title="get /personnel/exported-files/{fileName}/{date}">client.personnel.exported_files.<a href="./src/sdk_minus_4human/resources/personnel/exported_files.py">retrieve</a>(date, \*, file_name) -> str</code>

## HrRoles

Types:

```python
from sdk_minus_4human.types.personnel import HrRoleListResponse
```

Methods:

- <code title="get /personnel/hr-roles">client.personnel.hr_roles.<a href="./src/sdk_minus_4human/resources/personnel/hr_roles.py">list</a>() -> <a href="./src/sdk_minus_4human/types/personnel/hr_role_list_response.py">HrRoleListResponse</a></code>

## Dictionary

Types:

```python
from sdk_minus_4human.types.personnel import DictionaryListResponse
```

Methods:

- <code title="get /personnel/dictionary">client.personnel.dictionary.<a href="./src/sdk_minus_4human/resources/personnel/dictionary/dictionary.py">list</a>() -> <a href="./src/sdk_minus_4human/types/personnel/dictionary_list_response.py">DictionaryListResponse</a></code>

### OccupationalCodes

Types:

```python
from sdk_minus_4human.types.personnel.dictionary import OccupationalCodeListResponse
```

Methods:

- <code title="get /personnel/dictionary/occupational-codes">client.personnel.dictionary.occupational_codes.<a href="./src/sdk_minus_4human/resources/personnel/dictionary/occupational_codes.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/dictionary/occupational_code_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/dictionary/occupational_code_list_response.py">OccupationalCodeListResponse</a></code>

## EmploymentTypes

Types:

```python
from sdk_minus_4human.types.personnel import EmploymentTypeListResponse
```

Methods:

- <code title="get /personnel/employment-types">client.personnel.employment_types.<a href="./src/sdk_minus_4human/resources/personnel/employment_types.py">list</a>() -> <a href="./src/sdk_minus_4human/types/personnel/employment_type_list_response.py">EmploymentTypeListResponse</a></code>

## Jobs

Types:

```python
from sdk_minus_4human.types.personnel import (
    JobCreateResponse,
    JobRetrieveResponse,
    JobUpdateResponse,
    JobListResponse,
    JobUpdateFieldsResponse,
)
```

Methods:

- <code title="post /personnel/jobs">client.personnel.jobs.<a href="./src/sdk_minus_4human/resources/personnel/jobs.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/job_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/job_create_response.py">JobCreateResponse</a></code>
- <code title="get /personnel/jobs/{jobId}">client.personnel.jobs.<a href="./src/sdk_minus_4human/resources/personnel/jobs.py">retrieve</a>(job_id, \*\*<a href="src/sdk_minus_4human/types/personnel/job_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/job_retrieve_response.py">JobRetrieveResponse</a></code>
- <code title="put /personnel/jobs/{jobId}">client.personnel.jobs.<a href="./src/sdk_minus_4human/resources/personnel/jobs.py">update</a>(job_id, \*\*<a href="src/sdk_minus_4human/types/personnel/job_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/job_update_response.py">JobUpdateResponse</a></code>
- <code title="get /personnel/jobs">client.personnel.jobs.<a href="./src/sdk_minus_4human/resources/personnel/jobs.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/job_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/job_list_response.py">JobListResponse</a></code>
- <code title="patch /personnel/jobs/{jobId}">client.personnel.jobs.<a href="./src/sdk_minus_4human/resources/personnel/jobs.py">update_fields</a>(job_id, \*\*<a href="src/sdk_minus_4human/types/personnel/job_update_fields_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/job_update_fields_response.py">JobUpdateFieldsResponse</a></code>

## JobCategories

Types:

```python
from sdk_minus_4human.types.personnel import JobCategoryCreateResponse, JobCategoryListResponse
```

Methods:

- <code title="post /personnel/job-categories">client.personnel.job_categories.<a href="./src/sdk_minus_4human/resources/personnel/job_categories.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/job_category_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/job_category_create_response.py">JobCategoryCreateResponse</a></code>
- <code title="get /personnel/job-categories">client.personnel.job_categories.<a href="./src/sdk_minus_4human/resources/personnel/job_categories.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/job_category_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/job_category_list_response.py">JobCategoryListResponse</a></code>

## ResourceTypes

Types:

```python
from sdk_minus_4human.types.personnel import (
    ResourceTypeCreateResponse,
    ResourceTypeRetrieveResponse,
    ResourceTypeUpdateResponse,
)
```

Methods:

- <code title="post /personnel/resource-types">client.personnel.resource_types.<a href="./src/sdk_minus_4human/resources/personnel/resource_types.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/resource_type_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/resource_type_create_response.py">ResourceTypeCreateResponse</a></code>
- <code title="get /personnel/resource-types/{resourceTypeId}">client.personnel.resource_types.<a href="./src/sdk_minus_4human/resources/personnel/resource_types.py">retrieve</a>(resource_type_id) -> <a href="./src/sdk_minus_4human/types/personnel/resource_type_retrieve_response.py">ResourceTypeRetrieveResponse</a></code>
- <code title="patch /personnel/resource-types/{resourceTypeId}">client.personnel.resource_types.<a href="./src/sdk_minus_4human/resources/personnel/resource_types.py">update</a>(resource_type_id, \*\*<a href="src/sdk_minus_4human/types/personnel/resource_type_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/resource_type_update_response.py">ResourceTypeUpdateResponse</a></code>

## Employments

Types:

```python
from sdk_minus_4human.types.personnel import (
    EmploymentCreateResponse,
    EmploymentRetrieveResponse,
    EmploymentUpdateResponse,
    EmploymentListResponse,
)
```

Methods:

- <code title="post /personnel/employments">client.personnel.employments.<a href="./src/sdk_minus_4human/resources/personnel/employments/employments.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/employment_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/employment_create_response.py">EmploymentCreateResponse</a></code>
- <code title="get /personnel/employments/{employmentId}">client.personnel.employments.<a href="./src/sdk_minus_4human/resources/personnel/employments/employments.py">retrieve</a>(employment_id, \*\*<a href="src/sdk_minus_4human/types/personnel/employment_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/employment_retrieve_response.py">EmploymentRetrieveResponse</a></code>
- <code title="put /personnel/employments/{employmentId}">client.personnel.employments.<a href="./src/sdk_minus_4human/resources/personnel/employments/employments.py">update</a>(employment_id, \*\*<a href="src/sdk_minus_4human/types/personnel/employment_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/employment_update_response.py">EmploymentUpdateResponse</a></code>
- <code title="get /personnel/employments">client.personnel.employments.<a href="./src/sdk_minus_4human/resources/personnel/employments/employments.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/employment_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/employment_list_response.py">EmploymentListResponse</a></code>

### Formers

Types:

```python
from sdk_minus_4human.types.personnel.employments import FormerCreateResponse
```

Methods:

- <code title="post /personnel/employments/formers">client.personnel.employments.formers.<a href="./src/sdk_minus_4human/resources/personnel/employments/formers.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/employments/former_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/employments/former_create_response.py">FormerCreateResponse</a></code>

### Configuration

Types:

```python
from sdk_minus_4human.types.personnel.employments import ConfigurationListResponse
```

Methods:

- <code title="get /personnel/employments/configuration">client.personnel.employments.configuration.<a href="./src/sdk_minus_4human/resources/personnel/employments/configuration.py">list</a>() -> <a href="./src/sdk_minus_4human/types/personnel/employments/configuration_list_response.py">ConfigurationListResponse</a></code>

## CustomFields

Types:

```python
from sdk_minus_4human.types.personnel import CustomFieldChangeStatusResponse
```

Methods:

- <code title="patch /personnel/custom-fields/change-status/{id}">client.personnel.custom_fields.<a href="./src/sdk_minus_4human/resources/personnel/custom_fields/custom_fields.py">change_status</a>(\*, path_id, \*\*<a href="src/sdk_minus_4human/types/personnel/custom_field_change_status_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/custom_field_change_status_response.py">CustomFieldChangeStatusResponse</a></code>

### Templates

Types:

```python
from sdk_minus_4human.types.personnel.custom_fields import TemplateUpdateResponse
```

Methods:

- <code title="patch /personnel/custom-fields/templates/{templateId}">client.personnel.custom_fields.templates.<a href="./src/sdk_minus_4human/resources/personnel/custom_fields/templates/templates.py">update</a>(template_id, \*\*<a href="src/sdk_minus_4human/types/personnel/custom_fields/template_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/custom_fields/template_update_response.py">TemplateUpdateResponse</a></code>

#### Fields

Types:

```python
from sdk_minus_4human.types.personnel.custom_fields.templates import (
    FieldCreateResponse,
    FieldUpdateResponse,
)
```

Methods:

- <code title="post /personnel/custom-fields/templates/{templateId}/fields">client.personnel.custom_fields.templates.fields.<a href="./src/sdk_minus_4human/resources/personnel/custom_fields/templates/fields/fields.py">create</a>(template_id, \*\*<a href="src/sdk_minus_4human/types/personnel/custom_fields/templates/field_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/custom_fields/templates/field_create_response.py">FieldCreateResponse</a></code>
- <code title="patch /personnel/custom-fields/templates/{templateId}/fields/{fieldId}">client.personnel.custom_fields.templates.fields.<a href="./src/sdk_minus_4human/resources/personnel/custom_fields/templates/fields/fields.py">update</a>(field_id, \*, template_id, \*\*<a href="src/sdk_minus_4human/types/personnel/custom_fields/templates/field_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/custom_fields/templates/field_update_response.py">FieldUpdateResponse</a></code>

### Fields

#### Dimensions

Types:

```python
from sdk_minus_4human.types.personnel.custom_fields.fields import (
    DimensionCreateResponse,
    DimensionUpdateResponse,
)
```

Methods:

- <code title="post /personnel/custom-fields/fields/{fieldId}/dimensions">client.personnel.custom_fields.fields.dimensions.<a href="./src/sdk_minus_4human/resources/personnel/custom_fields/fields/dimensions.py">create</a>(field_id, \*\*<a href="src/sdk_minus_4human/types/personnel/custom_fields/fields/dimension_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/custom_fields/fields/dimension_create_response.py">DimensionCreateResponse</a></code>
- <code title="patch /personnel/custom-fields/fields/dimensions/{dimensionId}">client.personnel.custom_fields.fields.dimensions.<a href="./src/sdk_minus_4human/resources/personnel/custom_fields/fields/dimensions.py">update</a>(dimension_id, \*\*<a href="src/sdk_minus_4human/types/personnel/custom_fields/fields/dimension_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/custom_fields/fields/dimension_update_response.py">DimensionUpdateResponse</a></code>

### Values

#### Global

Types:

```python
from sdk_minus_4human.types.personnel.custom_fields.values import GlobalListResponse
```

Methods:

- <code title="get /personnel/custom-fields/values/global/tree">client.personnel.custom*fields.values.global*.<a href="./src/sdk_minus_4human/resources/personnel/custom_fields/values/global_.py">list</a>() -> <a href="./src/sdk_minus_4human/types/personnel/custom_fields/values/global_list_response.py">GlobalListResponse</a></code>

#### Company

Types:

```python
from sdk_minus_4human.types.personnel.custom_fields.values import CompanyListResponse
```

Methods:

- <code title="get /personnel/custom-fields/values/company/{companyId}/tree">client.personnel.custom_fields.values.company.<a href="./src/sdk_minus_4human/resources/personnel/custom_fields/values/company.py">list</a>(company_id) -> <a href="./src/sdk_minus_4human/types/personnel/custom_fields/values/company_list_response.py">CompanyListResponse</a></code>

## CompanyEmployees

### CustomFieldsByName

Types:

```python
from sdk_minus_4human.types.personnel.company_employees import CustomFieldsByNameUpdateResponse
```

Methods:

- <code title="put /personnel/company-employees/{companyEmployeeId}/custom-fields-by-name">client.personnel.company_employees.custom_fields_by_name.<a href="./src/sdk_minus_4human/resources/personnel/company_employees/custom_fields_by_name.py">update</a>(company_employee_id, \*\*<a href="src/sdk_minus_4human/types/personnel/company_employees/custom_fields_by_name_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/company_employees/custom_fields_by_name_update_response.py">CustomFieldsByNameUpdateResponse</a></code>

### History

Types:

```python
from sdk_minus_4human.types.personnel.company_employees import HistoryRetrieveResponse
```

Methods:

- <code title="get /personnel/company-employees/{companyEmployeeId}/history">client.personnel.company_employees.history.<a href="./src/sdk_minus_4human/resources/personnel/company_employees/history.py">retrieve</a>(company_employee_id, \*\*<a href="src/sdk_minus_4human/types/personnel/company_employees/history_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/company_employees/history_retrieve_response.py">HistoryRetrieveResponse</a></code>

## IndividualMainSalaries

Types:

```python
from sdk_minus_4human.types.personnel import (
    IndividualMainSalaryCreateResponse,
    IndividualMainSalaryRetrieveResponse,
    IndividualMainSalaryUpdateResponse,
    IndividualMainSalaryListResponse,
)
```

Methods:

- <code title="post /personnel/individual-main-salary">client.personnel.individual_main_salaries.<a href="./src/sdk_minus_4human/resources/personnel/individual_main_salaries.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/individual_main_salary_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/individual_main_salary_create_response.py">IndividualMainSalaryCreateResponse</a></code>
- <code title="get /personnel/individual-main-salary/{id}">client.personnel.individual_main_salaries.<a href="./src/sdk_minus_4human/resources/personnel/individual_main_salaries.py">retrieve</a>(id) -> <a href="./src/sdk_minus_4human/types/personnel/individual_main_salary_retrieve_response.py">IndividualMainSalaryRetrieveResponse</a></code>
- <code title="patch /personnel/individual-main-salary/{id}">client.personnel.individual_main_salaries.<a href="./src/sdk_minus_4human/resources/personnel/individual_main_salaries.py">update</a>(id, \*\*<a href="src/sdk_minus_4human/types/personnel/individual_main_salary_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/individual_main_salary_update_response.py">IndividualMainSalaryUpdateResponse</a></code>
- <code title="get /personnel/individual-main-salary">client.personnel.individual_main_salaries.<a href="./src/sdk_minus_4human/resources/personnel/individual_main_salaries.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/individual_main_salary_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/individual_main_salary_list_response.py">IndividualMainSalaryListResponse</a></code>

## Salary

### Elements

#### AdditionalSalaries

Types:

```python
from sdk_minus_4human.types.personnel.salary.elements import (
    AdditionalSalaryCreateResponse,
    AdditionalSalaryRetrieveResponse,
    AdditionalSalaryUpdateResponse,
    AdditionalSalaryListResponse,
)
```

Methods:

- <code title="post /personnel/salary/elements/additional-salaries">client.personnel.salary.elements.additional_salaries.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/additional_salaries.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/additional_salary_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/additional_salary_create_response.py">AdditionalSalaryCreateResponse</a></code>
- <code title="get /personnel/salary/elements/additional-salaries/{additionalSalaryId}">client.personnel.salary.elements.additional_salaries.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/additional_salaries.py">retrieve</a>(additional_salary_id) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/additional_salary_retrieve_response.py">AdditionalSalaryRetrieveResponse</a></code>
- <code title="patch /personnel/salary/elements/additional-salaries/{additionalSalaryId}">client.personnel.salary.elements.additional_salaries.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/additional_salaries.py">update</a>(additional_salary_id, \*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/additional_salary_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/additional_salary_update_response.py">AdditionalSalaryUpdateResponse</a></code>
- <code title="get /personnel/salary/elements/additional-salaries">client.personnel.salary.elements.additional_salaries.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/additional_salaries.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/additional_salary_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/additional_salary_list_response.py">AdditionalSalaryListResponse</a></code>

#### Benefits

Types:

```python
from sdk_minus_4human.types.personnel.salary.elements import (
    BenefitCreateResponse,
    BenefitRetrieveResponse,
    BenefitUpdateResponse,
    BenefitListResponse,
)
```

Methods:

- <code title="post /personnel/salary/elements/benefits">client.personnel.salary.elements.benefits.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/benefits.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/benefit_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/benefit_create_response.py">BenefitCreateResponse</a></code>
- <code title="get /personnel/salary/elements/benefits/{benefitId}">client.personnel.salary.elements.benefits.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/benefits.py">retrieve</a>(benefit_id) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/benefit_retrieve_response.py">BenefitRetrieveResponse</a></code>
- <code title="patch /personnel/salary/elements/benefits/{benefitId}">client.personnel.salary.elements.benefits.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/benefits.py">update</a>(benefit_id, \*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/benefit_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/benefit_update_response.py">BenefitUpdateResponse</a></code>
- <code title="get /personnel/salary/elements/benefits">client.personnel.salary.elements.benefits.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/benefits.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/benefit_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/benefit_list_response.py">BenefitListResponse</a></code>

#### Deductions

Types:

```python
from sdk_minus_4human.types.personnel.salary.elements import (
    DeductionCreateResponse,
    DeductionRetrieveResponse,
    DeductionUpdateResponse,
    DeductionListResponse,
)
```

Methods:

- <code title="post /personnel/salary/elements/deductions">client.personnel.salary.elements.deductions.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/deductions.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/deduction_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/deduction_create_response.py">DeductionCreateResponse</a></code>
- <code title="get /personnel/salary/elements/deductions/{deductionId}">client.personnel.salary.elements.deductions.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/deductions.py">retrieve</a>(deduction_id) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/deduction_retrieve_response.py">DeductionRetrieveResponse</a></code>
- <code title="patch /personnel/salary/elements/deductions/{deductionId}">client.personnel.salary.elements.deductions.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/deductions.py">update</a>(deduction_id, \*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/deduction_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/deduction_update_response.py">DeductionUpdateResponse</a></code>
- <code title="get /personnel/salary/elements/deductions">client.personnel.salary.elements.deductions.<a href="./src/sdk_minus_4human/resources/personnel/salary/elements/deductions.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/salary/elements/deduction_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary/elements/deduction_list_response.py">DeductionListResponse</a></code>

## SalaryRegulations

Types:

```python
from sdk_minus_4human.types.personnel import SalaryRegulationListResponse
```

Methods:

- <code title="get /personnel/salary-regulations">client.personnel.salary_regulations.<a href="./src/sdk_minus_4human/resources/personnel/salary_regulations.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/salary_regulation_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/salary_regulation_list_response.py">SalaryRegulationListResponse</a></code>

## Profiles

Types:

```python
from sdk_minus_4human.types.personnel import ProfileRetrieveResponse
```

Methods:

- <code title="get /personnel/profiles/{userId}">client.personnel.profiles.<a href="./src/sdk_minus_4human/resources/personnel/profiles/profiles.py">retrieve</a>(user_id) -> <a href="./src/sdk_minus_4human/types/personnel/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>

### History

Types:

```python
from sdk_minus_4human.types.personnel.profiles import HistoryListResponse
```

Methods:

- <code title="get /personnel/profiles/{userId}/history">client.personnel.profiles.history.<a href="./src/sdk_minus_4human/resources/personnel/profiles/history.py">list</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/personnel/profiles/history_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/profiles/history_list_response.py">HistoryListResponse</a></code>

## NextOfKin

Types:

```python
from sdk_minus_4human.types.personnel import NextOfKinUpdateResponse
```

Methods:

- <code title="patch /personnel/next-of-kin/{nextOfKinId}">client.personnel.next_of_kin.<a href="./src/sdk_minus_4human/resources/personnel/next_of_kin/next_of_kin.py">update</a>(next_of_kin_id, \*\*<a href="src/sdk_minus_4human/types/personnel/next_of_kin_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/next_of_kin_update_response.py">NextOfKinUpdateResponse</a></code>

### User

Types:

```python
from sdk_minus_4human.types.personnel.next_of_kin import UserCreateResponse, UserListResponse
```

Methods:

- <code title="post /personnel/next-of-kin/user/{userId}">client.personnel.next_of_kin.user.<a href="./src/sdk_minus_4human/resources/personnel/next_of_kin/user.py">create</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/personnel/next_of_kin/user_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/next_of_kin/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /personnel/next-of-kin/user/{userId}">client.personnel.next_of_kin.user.<a href="./src/sdk_minus_4human/resources/personnel/next_of_kin/user.py">list</a>(user_id) -> <a href="./src/sdk_minus_4human/types/personnel/next_of_kin/user_list_response.py">UserListResponse</a></code>

## Children

Types:

```python
from sdk_minus_4human.types.personnel import ChildUpdateResponse
```

Methods:

- <code title="patch /personnel/children/{childId}">client.personnel.children.<a href="./src/sdk_minus_4human/resources/personnel/children/children.py">update</a>(child_id, \*\*<a href="src/sdk_minus_4human/types/personnel/child_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/child_update_response.py">ChildUpdateResponse</a></code>

### User

Types:

```python
from sdk_minus_4human.types.personnel.children import UserCreateResponse, UserRetrieveResponse
```

Methods:

- <code title="post /personnel/children/user/{userId}">client.personnel.children.user.<a href="./src/sdk_minus_4human/resources/personnel/children/user.py">create</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/personnel/children/user_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/children/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /personnel/children/user/{userId}">client.personnel.children.user.<a href="./src/sdk_minus_4human/resources/personnel/children/user.py">retrieve</a>(user_id) -> <a href="./src/sdk_minus_4human/types/personnel/children/user_retrieve_response.py">UserRetrieveResponse</a></code>

## WorkingHoursArrangements

Types:

```python
from sdk_minus_4human.types.personnel import (
    WorkingHoursArrangementCreateResponse,
    WorkingHoursArrangementRetrieveResponse,
    WorkingHoursArrangementUpdateResponse,
    WorkingHoursArrangementListResponse,
)
```

Methods:

- <code title="post /personnel/working-hours-arrangements">client.personnel.working_hours_arrangements.<a href="./src/sdk_minus_4human/resources/personnel/working_hours_arrangements.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/working_hours_arrangement_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/working_hours_arrangement_create_response.py">WorkingHoursArrangementCreateResponse</a></code>
- <code title="get /personnel/working-hours-arrangements/{id}">client.personnel.working_hours_arrangements.<a href="./src/sdk_minus_4human/resources/personnel/working_hours_arrangements.py">retrieve</a>(id, \*\*<a href="src/sdk_minus_4human/types/personnel/working_hours_arrangement_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/working_hours_arrangement_retrieve_response.py">WorkingHoursArrangementRetrieveResponse</a></code>
- <code title="patch /personnel/working-hours-arrangements/{id}">client.personnel.working_hours_arrangements.<a href="./src/sdk_minus_4human/resources/personnel/working_hours_arrangements.py">update</a>(id, \*\*<a href="src/sdk_minus_4human/types/personnel/working_hours_arrangement_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/working_hours_arrangement_update_response.py">WorkingHoursArrangementUpdateResponse</a></code>
- <code title="get /personnel/working-hours-arrangements">client.personnel.working_hours_arrangements.<a href="./src/sdk_minus_4human/resources/personnel/working_hours_arrangements.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/working_hours_arrangement_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/working_hours_arrangement_list_response.py">WorkingHoursArrangementListResponse</a></code>

## WorkContactDetails

Types:

```python
from sdk_minus_4human.types.personnel import WorkContactDetailUpdateResponse
```

Methods:

- <code title="put /personnel/work-contact-details/{userId}">client.personnel.work_contact_details.<a href="./src/sdk_minus_4human/resources/personnel/work_contact_details.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/personnel/work_contact_detail_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/work_contact_detail_update_response.py">WorkContactDetailUpdateResponse</a></code>

## PrivateContactDetails

Types:

```python
from sdk_minus_4human.types.personnel import PrivateContactDetailUpdateResponse
```

Methods:

- <code title="put /personnel/private-contact-details/{userId}">client.personnel.private_contact_details.<a href="./src/sdk_minus_4human/resources/personnel/private_contact_details.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/personnel/private_contact_detail_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/private_contact_detail_update_response.py">PrivateContactDetailUpdateResponse</a></code>

## ContactDetails

Types:

```python
from sdk_minus_4human.types.personnel import ContactDetailUpdateResponse
```

Methods:

- <code title="patch /personnel/contact-details/{userId}">client.personnel.contact_details.<a href="./src/sdk_minus_4human/resources/personnel/contact_details.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/personnel/contact_detail_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/contact_detail_update_response.py">ContactDetailUpdateResponse</a></code>

## Changes

Types:

```python
from sdk_minus_4human.types.personnel import ChangeListResponse
```

Methods:

- <code title="get /personnel/changes">client.personnel.changes.<a href="./src/sdk_minus_4human/resources/personnel/changes/changes.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/change_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/change_list_response.py">ChangeListResponse</a></code>

### Details

Types:

```python
from sdk_minus_4human.types.personnel.changes import (
    DetailListCompanyEmployeeChangesResponse,
    DetailRetrieveEmploymentChangesResponse,
    DetailRetrieveUserChangesResponse,
)
```

Methods:

- <code title="get /personnel/changes/details/companyEmployee">client.personnel.changes.details.<a href="./src/sdk_minus_4human/resources/personnel/changes/details.py">list_company_employee_changes</a>(\*\*<a href="src/sdk_minus_4human/types/personnel/changes/detail_list_company_employee_changes_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/changes/detail_list_company_employee_changes_response.py">DetailListCompanyEmployeeChangesResponse</a></code>
- <code title="get /personnel/changes/details/employment/{employmentId}">client.personnel.changes.details.<a href="./src/sdk_minus_4human/resources/personnel/changes/details.py">retrieve_employment_changes</a>(employment_id, \*\*<a href="src/sdk_minus_4human/types/personnel/changes/detail_retrieve_employment_changes_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/changes/detail_retrieve_employment_changes_response.py">DetailRetrieveEmploymentChangesResponse</a></code>
- <code title="get /personnel/changes/details/user/{userId}">client.personnel.changes.details.<a href="./src/sdk_minus_4human/resources/personnel/changes/details.py">retrieve_user_changes</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/personnel/changes/detail_retrieve_user_changes_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/personnel/changes/detail_retrieve_user_changes_response.py">DetailRetrieveUserChangesResponse</a></code>

# JobCategories

Types:

```python
from sdk_minus_4human.types import (
    JobCategoryRetrieveResponse,
    JobCategoryUpdateResponse,
    JobCategoryStatusResponse,
)
```

Methods:

- <code title="get /personnel/job-categories/{jobCategoryId}">client.job_categories.<a href="./src/sdk_minus_4human/resources/job_categories.py">retrieve</a>(job_category_id) -> <a href="./src/sdk_minus_4human/types/job_category_retrieve_response.py">JobCategoryRetrieveResponse</a></code>
- <code title="patch /personnel/job-categories/{jobCategoryId}">client.job_categories.<a href="./src/sdk_minus_4human/resources/job_categories.py">update</a>(job_category_id, \*\*<a href="src/sdk_minus_4human/types/job_category_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/job_category_update_response.py">JobCategoryUpdateResponse</a></code>
- <code title="patch /personnel/job-categories/{jobCategoryId}/status">client.job_categories.<a href="./src/sdk_minus_4human/resources/job_categories.py">status</a>(job_category_id, \*\*<a href="src/sdk_minus_4human/types/job_category_status_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/job_category_status_response.py">JobCategoryStatusResponse</a></code>

# EmployeeTypes

Types:

```python
from sdk_minus_4human.types import (
    EmployeeTypeCreateResponse,
    EmployeeTypeRetrieveResponse,
    EmployeeTypeUpdateResponse,
    EmployeeTypeListResponse,
)
```

Methods:

- <code title="post /personnel/employee-types">client.employee_types.<a href="./src/sdk_minus_4human/resources/employee_types.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/employee_type_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/employee_type_create_response.py">EmployeeTypeCreateResponse</a></code>
- <code title="get /personnel/employee-types/{employeeTypeId}">client.employee_types.<a href="./src/sdk_minus_4human/resources/employee_types.py">retrieve</a>(employee_type_id) -> <a href="./src/sdk_minus_4human/types/employee_type_retrieve_response.py">EmployeeTypeRetrieveResponse</a></code>
- <code title="patch /personnel/employee-types/{employeeTypeId}">client.employee_types.<a href="./src/sdk_minus_4human/resources/employee_types.py">update</a>(employee_type_id, \*\*<a href="src/sdk_minus_4human/types/employee_type_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/employee_type_update_response.py">EmployeeTypeUpdateResponse</a></code>
- <code title="get /personnel/employee-types">client.employee_types.<a href="./src/sdk_minus_4human/resources/employee_types.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/employee_type_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/employee_type_list_response.py">EmployeeTypeListResponse</a></code>

# ResourceTypes

Types:

```python
from sdk_minus_4human.types import ResourceTypeListResponse
```

Methods:

- <code title="get /personnel/resource-types">client.resource_types.<a href="./src/sdk_minus_4human/resources/resource_types.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/resource_type_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/resource_type_list_response.py">ResourceTypeListResponse</a></code>

# Employments

Types:

```python
from sdk_minus_4human.types import EmploymentUpdateResponse
```

Methods:

- <code title="patch /personnel/employments/{employmentId}">client.employments.<a href="./src/sdk_minus_4human/resources/employments/employments.py">update</a>(employment_id, \*\*<a href="src/sdk_minus_4human/types/employment_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/employment_update_response.py">EmploymentUpdateResponse</a></code>

## CustomFieldsByName

Types:

```python
from sdk_minus_4human.types.employments import CustomFieldsByNameUpdateResponse
```

Methods:

- <code title="put /personnel/employments/{employmentId}/custom-fields-by-name">client.employments.custom_fields_by_name.<a href="./src/sdk_minus_4human/resources/employments/custom_fields_by_name.py">update</a>(employment_id, \*\*<a href="src/sdk_minus_4human/types/employments/custom_fields_by_name_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/employments/custom_fields_by_name_update_response.py">CustomFieldsByNameUpdateResponse</a></code>

## History

Types:

```python
from sdk_minus_4human.types.employments import HistoryRetrieveResponse
```

Methods:

- <code title="get /personnel/employments/{employmentId}/history">client.employments.history.<a href="./src/sdk_minus_4human/resources/employments/history.py">retrieve</a>(employment_id, \*\*<a href="src/sdk_minus_4human/types/employments/history_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/employments/history_retrieve_response.py">HistoryRetrieveResponse</a></code>

## Elements

Types:

```python
from sdk_minus_4human.types.employments import ElementRetrieveResponse
```

Methods:

- <code title="get /personnel/employments/{employmentId}/elements">client.employments.elements.<a href="./src/sdk_minus_4human/resources/employments/elements.py">retrieve</a>(employment_id, \*\*<a href="src/sdk_minus_4human/types/employments/element_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/employments/element_retrieve_response.py">ElementRetrieveResponse</a></code>

## SalaryElements

### History

Types:

```python
from sdk_minus_4human.types.employments.salary_elements import HistoryListResponse
```

Methods:

- <code title="get /personnel/employments/{employmentId}/salary-elements/history">client.employments.salary_elements.history.<a href="./src/sdk_minus_4human/resources/employments/salary_elements/history.py">list</a>(employment_id, \*\*<a href="src/sdk_minus_4human/types/employments/salary_elements/history_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/employments/salary_elements/history_list_response.py">HistoryListResponse</a></code>

# CustomFields

## Templates

Types:

```python
from sdk_minus_4human.types.custom_fields import (
    TemplateCreateResponse,
    TemplateRetrieveResponse,
    TemplateUpdateResponse,
    TemplateListResponse,
)
```

Methods:

- <code title="post /personnel/custom-fields/templates">client.custom_fields.templates.<a href="./src/sdk_minus_4human/resources/custom_fields/templates/templates.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/custom_fields/template_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/custom_fields/template_create_response.py">TemplateCreateResponse</a></code>
- <code title="get /personnel/custom-fields/templates/{companyId}">client.custom_fields.templates.<a href="./src/sdk_minus_4human/resources/custom_fields/templates/templates.py">retrieve</a>(company_id) -> <a href="./src/sdk_minus_4human/types/custom_fields/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="put /personnel/custom-fields/templates/{templateId}">client.custom_fields.templates.<a href="./src/sdk_minus_4human/resources/custom_fields/templates/templates.py">update</a>(template_id, \*\*<a href="src/sdk_minus_4human/types/custom_fields/template_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/custom_fields/template_update_response.py">TemplateUpdateResponse</a></code>
- <code title="get /personnel/custom-fields/templates">client.custom_fields.templates.<a href="./src/sdk_minus_4human/resources/custom_fields/templates/templates.py">list</a>() -> <a href="./src/sdk_minus_4human/types/custom_fields/template_list_response.py">TemplateListResponse</a></code>

### Global

Types:

```python
from sdk_minus_4human.types.custom_fields.templates import GlobalRetrieveResponse
```

Methods:

- <code title="get /personnel/custom-fields/templates/global">client.custom*fields.templates.global*.<a href="./src/sdk_minus_4human/resources/custom_fields/templates/global_.py">retrieve</a>() -> <a href="./src/sdk_minus_4human/types/custom_fields/templates/global_retrieve_response.py">GlobalRetrieveResponse</a></code>

## Values

Types:

```python
from sdk_minus_4human.types.custom_fields import (
    ValueCreateResponse,
    ValueUpdateResponse,
    ValueChangeStatusResponse,
    ValueUpdatePartialResponse,
)
```

Methods:

- <code title="post /personnel/custom-fields/values/{valueId}">client.custom_fields.values.<a href="./src/sdk_minus_4human/resources/custom_fields/values.py">create</a>(value_id, \*\*<a href="src/sdk_minus_4human/types/custom_fields/value_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/custom_fields/value_create_response.py">ValueCreateResponse</a></code>
- <code title="put /personnel/custom-fields/values/{valueId}">client.custom_fields.values.<a href="./src/sdk_minus_4human/resources/custom_fields/values.py">update</a>(value_id, \*\*<a href="src/sdk_minus_4human/types/custom_fields/value_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/custom_fields/value_update_response.py">ValueUpdateResponse</a></code>
- <code title="patch /personnel/custom-fields/values/change-status/{valueId}">client.custom_fields.values.<a href="./src/sdk_minus_4human/resources/custom_fields/values.py">change_status</a>(value_id, \*\*<a href="src/sdk_minus_4human/types/custom_fields/value_change_status_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/custom_fields/value_change_status_response.py">ValueChangeStatusResponse</a></code>
- <code title="patch /personnel/custom-fields/values/{valueId}">client.custom_fields.values.<a href="./src/sdk_minus_4human/resources/custom_fields/values.py">update_partial</a>(value_id, \*\*<a href="src/sdk_minus_4human/types/custom_fields/value_update_partial_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/custom_fields/value_update_partial_response.py">ValueUpdatePartialResponse</a></code>

## Personnel

Types:

```python
from sdk_minus_4human.types.custom_fields import (
    PersonnelUpdateResponse,
    PersonnelUpdateByNameResponse,
)
```

Methods:

- <code title="put /personnel/custom-fields/{userId}">client.custom_fields.personnel.<a href="./src/sdk_minus_4human/resources/custom_fields/personnel.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/custom_fields/personnel_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/custom_fields/personnel_update_response.py">PersonnelUpdateResponse</a></code>
- <code title="put /personnel/custom-fields-by-name/{userId}">client.custom_fields.personnel.<a href="./src/sdk_minus_4human/resources/custom_fields/personnel.py">update_by_name</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/custom_fields/personnel_update_by_name_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/custom_fields/personnel_update_by_name_response.py">PersonnelUpdateByNameResponse</a></code>

# CompanyEmployees

Types:

```python
from sdk_minus_4human.types import (
    CompanyEmployeeRetrieveResponse,
    CompanyEmployeeUpdateResponse,
    CompanyEmployeeListResponse,
    CompanyEmployeeUpdatePartialResponse,
)
```

Methods:

- <code title="get /personnel/company-employees/{companyEmployeeId}">client.company_employees.<a href="./src/sdk_minus_4human/resources/company_employees.py">retrieve</a>(company_employee_id, \*\*<a href="src/sdk_minus_4human/types/company_employee_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/company_employee_retrieve_response.py">CompanyEmployeeRetrieveResponse</a></code>
- <code title="put /personnel/company-employees/{companyEmployeeId}">client.company_employees.<a href="./src/sdk_minus_4human/resources/company_employees.py">update</a>(company_employee_id, \*\*<a href="src/sdk_minus_4human/types/company_employee_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/company_employee_update_response.py">CompanyEmployeeUpdateResponse</a></code>
- <code title="get /personnel/company-employees">client.company_employees.<a href="./src/sdk_minus_4human/resources/company_employees.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/company_employee_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/company_employee_list_response.py">CompanyEmployeeListResponse</a></code>
- <code title="patch /personnel/company-employees/{companyEmployeeId}">client.company_employees.<a href="./src/sdk_minus_4human/resources/company_employees.py">update_partial</a>(company_employee_id, \*\*<a href="src/sdk_minus_4human/types/company_employee_update_partial_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/company_employee_update_partial_response.py">CompanyEmployeeUpdatePartialResponse</a></code>

# Competence

## SkillTypeCategories

Types:

```python
from sdk_minus_4human.types.competence import (
    SkillTypeCategoryCreateResponse,
    SkillTypeCategoryRetrieveResponse,
    SkillTypeCategoryUpdateResponse,
    SkillTypeCategoryListResponse,
)
```

Methods:

- <code title="post /competence/skill-type-categories">client.competence.skill_type_categories.<a href="./src/sdk_minus_4human/resources/competence/skill_type_categories.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/competence/skill_type_category_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/competence/skill_type_category_create_response.py">SkillTypeCategoryCreateResponse</a></code>
- <code title="get /competence/skill-type-categories/{id}">client.competence.skill_type_categories.<a href="./src/sdk_minus_4human/resources/competence/skill_type_categories.py">retrieve</a>(id, \*\*<a href="src/sdk_minus_4human/types/competence/skill_type_category_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/competence/skill_type_category_retrieve_response.py">SkillTypeCategoryRetrieveResponse</a></code>
- <code title="patch /competence/skill-type-categories/{id}">client.competence.skill_type_categories.<a href="./src/sdk_minus_4human/resources/competence/skill_type_categories.py">update</a>(id, \*\*<a href="src/sdk_minus_4human/types/competence/skill_type_category_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/competence/skill_type_category_update_response.py">SkillTypeCategoryUpdateResponse</a></code>
- <code title="get /competence/skill-type-categories">client.competence.skill_type_categories.<a href="./src/sdk_minus_4human/resources/competence/skill_type_categories.py">list</a>() -> <a href="./src/sdk_minus_4human/types/competence/skill_type_category_list_response.py">SkillTypeCategoryListResponse</a></code>

## SkillTypes

Types:

```python
from sdk_minus_4human.types.competence import SkillTypeListResponse
```

Methods:

- <code title="get /competence/skill-types">client.competence.skill_types.<a href="./src/sdk_minus_4human/resources/competence/skill_types/skill_types.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/competence/skill_type_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/competence/skill_type_list_response.py">SkillTypeListResponse</a></code>

### Configuration

Types:

```python
from sdk_minus_4human.types.competence.skill_types import ConfigurationListResponse
```

Methods:

- <code title="get /competence/skill-types/configuration">client.competence.skill_types.configuration.<a href="./src/sdk_minus_4human/resources/competence/skill_types/configuration.py">list</a>() -> <a href="./src/sdk_minus_4human/types/competence/skill_types/configuration_list_response.py">ConfigurationListResponse</a></code>

# SkillTypes

Types:

```python
from sdk_minus_4human.types import (
    SkillTypeCreateResponse,
    SkillTypeRetrieveResponse,
    SkillTypeUpdateResponse,
    SkillTypeStatusResponse,
)
```

Methods:

- <code title="post /competence/skill-types">client.skill_types.<a href="./src/sdk_minus_4human/resources/skill_types.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/skill_type_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/skill_type_create_response.py">SkillTypeCreateResponse</a></code>
- <code title="get /competence/skill-types/{id}">client.skill_types.<a href="./src/sdk_minus_4human/resources/skill_types.py">retrieve</a>(id, \*\*<a href="src/sdk_minus_4human/types/skill_type_retrieve_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/skill_type_retrieve_response.py">SkillTypeRetrieveResponse</a></code>
- <code title="patch /competence/skill-types/{id}">client.skill_types.<a href="./src/sdk_minus_4human/resources/skill_types.py">update</a>(id, \*\*<a href="src/sdk_minus_4human/types/skill_type_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/skill_type_update_response.py">SkillTypeUpdateResponse</a></code>
- <code title="patch /competence/skill-types/{id}/status">client.skill_types.<a href="./src/sdk_minus_4human/resources/skill_types.py">status</a>(id, \*\*<a href="src/sdk_minus_4human/types/skill_type_status_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/skill_type_status_response.py">SkillTypeStatusResponse</a></code>

# Skills

Types:

```python
from sdk_minus_4human.types import (
    SkillCreateResponse,
    SkillRetrieveResponse,
    SkillUpdateResponse,
    SkillListResponse,
)
```

Methods:

- <code title="post /competence/skills">client.skills.<a href="./src/sdk_minus_4human/resources/skills/skills.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/skill_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/skill_create_response.py">SkillCreateResponse</a></code>
- <code title="get /competence/skills/{skillId}">client.skills.<a href="./src/sdk_minus_4human/resources/skills/skills.py">retrieve</a>(skill_id) -> <a href="./src/sdk_minus_4human/types/skill_retrieve_response.py">SkillRetrieveResponse</a></code>
- <code title="patch /competence/skills/{skillId}">client.skills.<a href="./src/sdk_minus_4human/resources/skills/skills.py">update</a>(skill_id, \*\*<a href="src/sdk_minus_4human/types/skill_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/skill_update_response.py">SkillUpdateResponse</a></code>
- <code title="get /competence/skills">client.skills.<a href="./src/sdk_minus_4human/resources/skills/skills.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/skill_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/skill_list_response.py">SkillListResponse</a></code>

## UserSkill

Types:

```python
from sdk_minus_4human.types.skills import UserSkillUpdateResponse
```

Methods:

- <code title="put /competence/import/user-skill">client.skills.user_skill.<a href="./src/sdk_minus_4human/resources/skills/user_skill.py">update</a>(\*\*<a href="src/sdk_minus_4human/types/skills/user_skill_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/skills/user_skill_update_response.py">UserSkillUpdateResponse</a></code>

# ExternalIntegrations

Types:

```python
from sdk_minus_4human.types import ExternalIntegrationRunResponse
```

Methods:

- <code title="post /external-integrations/run">client.external_integrations.<a href="./src/sdk_minus_4human/resources/external_integrations/external_integrations.py">run</a>(\*\*<a href="src/sdk_minus_4human/types/external_integration_run_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/external_integration_run_response.py">ExternalIntegrationRunResponse</a></code>

## FeatureStatus

Types:

```python
from sdk_minus_4human.types.external_integrations import FeatureStatusRetrieveResponse
```

Methods:

- <code title="get /external-integrations/status/{featureName}">client.external_integrations.feature_status.<a href="./src/sdk_minus_4human/resources/external_integrations/feature_status.py">retrieve</a>(feature_name) -> <a href="./src/sdk_minus_4human/types/external_integrations/feature_status_retrieve_response.py">FeatureStatusRetrieveResponse</a></code>

# Users

Types:

```python
from sdk_minus_4human.types import UserCreateResponse, UserListResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/sdk_minus_4human/resources/users/users.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/user_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /users">client.users.<a href="./src/sdk_minus_4human/resources/users/users.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/user_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/user_list_response.py">UserListResponse</a></code>
- <code title="delete /users/{userId}">client.users.<a href="./src/sdk_minus_4human/resources/users/users.py">delete</a>(user_id) -> None</code>

## LoggedUser

### Details

Types:

```python
from sdk_minus_4human.types.users.logged_user import DetailRetrieveResponse
```

Methods:

- <code title="get /users/logged-user/details">client.users.logged_user.details.<a href="./src/sdk_minus_4human/resources/users/logged_user/details.py">retrieve</a>() -> <a href="./src/sdk_minus_4human/types/users/logged_user/detail_retrieve_response.py">DetailRetrieveResponse</a></code>

## ByLogin

Types:

```python
from sdk_minus_4human.types.users import ByLoginCreateResponse
```

Methods:

- <code title="post /users/by-login">client.users.by_login.<a href="./src/sdk_minus_4human/resources/users/by_login.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/users/by_login_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/by_login_create_response.py">ByLoginCreateResponse</a></code>

## ActiveDirectoryData

Types:

```python
from sdk_minus_4human.types.users import ActiveDirectoryDataUpdateResponse
```

Methods:

- <code title="patch /users/active-directory-data/{userId}">client.users.active_directory_data.<a href="./src/sdk_minus_4human/resources/users/active_directory_data.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/users/active_directory_data_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/active_directory_data_update_response.py">ActiveDirectoryDataUpdateResponse</a></code>

## LoginMethod

Types:

```python
from sdk_minus_4human.types.users import LoginMethodUpdateResponse
```

Methods:

- <code title="patch /users/login-method/{userId}">client.users.login_method.<a href="./src/sdk_minus_4human/resources/users/login_method.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/users/login_method_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/login_method_update_response.py">LoginMethodUpdateResponse</a></code>

## PersonalDetails

Types:

```python
from sdk_minus_4human.types.users import PersonalDetailUpdateResponse
```

Methods:

- <code title="patch /users/personal-details/{userId}">client.users.personal_details.<a href="./src/sdk_minus_4human/resources/users/personal_details.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/users/personal_detail_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/personal_detail_update_response.py">PersonalDetailUpdateResponse</a></code>

## PersonalID

Types:

```python
from sdk_minus_4human.types.users import (
    PersonalIDCreateResponse,
    PersonalIDUpdateResponse,
    PersonalIDDeleteResponse,
    PersonalIDImportResponse,
)
```

Methods:

- <code title="post /users/personal-id/{userId}">client.users.personal_id.<a href="./src/sdk_minus_4human/resources/users/personal_id.py">create</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/users/personal_id_create_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/personal_id_create_response.py">PersonalIDCreateResponse</a></code>
- <code title="patch /users/personal-id/{userId}/{id}">client.users.personal_id.<a href="./src/sdk_minus_4human/resources/users/personal_id.py">update</a>(id, \*, user_id, \*\*<a href="src/sdk_minus_4human/types/users/personal_id_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/personal_id_update_response.py">PersonalIDUpdateResponse</a></code>
- <code title="delete /users/personal-id/{userId}/{id}">client.users.personal_id.<a href="./src/sdk_minus_4human/resources/users/personal_id.py">delete</a>(id, \*, user_id, \*\*<a href="src/sdk_minus_4human/types/users/personal_id_delete_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/personal_id_delete_response.py">PersonalIDDeleteResponse</a></code>
- <code title="put /users/personal-id/{userId}/import">client.users.personal*id.<a href="./src/sdk_minus_4human/resources/users/personal_id.py">import*</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/users/personal_id_import_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/personal_id_import_response.py">PersonalIDImportResponse</a></code>

## PaymentDetailsData

Types:

```python
from sdk_minus_4human.types.users import PaymentDetailsDataUpdateResponse
```

Methods:

- <code title="patch /users/payment-details-data/{userId}">client.users.payment_details_data.<a href="./src/sdk_minus_4human/resources/users/payment_details_data.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/users/payment_details_data_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/payment_details_data_update_response.py">PaymentDetailsDataUpdateResponse</a></code>

## SendInvitation

Types:

```python
from sdk_minus_4human.types.users import SendInvitationUpdateResponse
```

Methods:

- <code title="patch /users/send-invitation/{userId}">client.users.send_invitation.<a href="./src/sdk_minus_4human/resources/users/send_invitation.py">update</a>(user_id, \*\*<a href="src/sdk_minus_4human/types/users/send_invitation_update_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/send_invitation_update_response.py">SendInvitationUpdateResponse</a></code>

## AccessGroups

Types:

```python
from sdk_minus_4human.types.users import AccessGroupListResponse, AccessGroupAssignResponse
```

Methods:

- <code title="get /users/access-groups">client.users.access_groups.<a href="./src/sdk_minus_4human/resources/users/access_groups/access_groups.py">list</a>() -> <a href="./src/sdk_minus_4human/types/users/access_group_list_response.py">AccessGroupListResponse</a></code>
- <code title="put /users/access-groups/assign">client.users.access_groups.<a href="./src/sdk_minus_4human/resources/users/access_groups/access_groups.py">assign</a>(\*\*<a href="src/sdk_minus_4human/types/users/access_group_assign_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/users/access_group_assign_response.py">AccessGroupAssignResponse</a></code>

### User

Types:

```python
from sdk_minus_4human.types.users.access_groups import UserRetrieveResponse
```

Methods:

- <code title="get /users/access-groups/user/{userId}">client.users.access_groups.user.<a href="./src/sdk_minus_4human/resources/users/access_groups/user.py">retrieve</a>(user_id) -> <a href="./src/sdk_minus_4human/types/users/access_groups/user_retrieve_response.py">UserRetrieveResponse</a></code>

# Workplans

Types:

```python
from sdk_minus_4human.types import WorkplanListResponse, WorkplanDeleteResponse
```

Methods:

- <code title="post /workplans">client.workplans.<a href="./src/sdk_minus_4human/resources/workplans.py">create</a>(\*\*<a href="src/sdk_minus_4human/types/workplan_create_params.py">params</a>) -> None</code>
- <code title="get /workplans">client.workplans.<a href="./src/sdk_minus_4human/resources/workplans.py">list</a>(\*\*<a href="src/sdk_minus_4human/types/workplan_list_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/workplan_list_response.py">WorkplanListResponse</a></code>
- <code title="delete /workplans">client.workplans.<a href="./src/sdk_minus_4human/resources/workplans.py">delete</a>(\*\*<a href="src/sdk_minus_4human/types/workplan_delete_params.py">params</a>) -> <a href="./src/sdk_minus_4human/types/workplan_delete_response.py">WorkplanDeleteResponse</a></code>
