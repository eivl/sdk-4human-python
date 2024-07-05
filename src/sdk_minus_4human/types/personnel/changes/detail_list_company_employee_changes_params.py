# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DetailListCompanyEmployeeChangesParams"]


class DetailListCompanyEmployeeChangesParams(TypedDict, total=False):
    from_: Required[Annotated[Union[int, str], PropertyInfo(alias="from")]]
    """
    Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
    ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`. Filter `from` and `to`
    searches data (in the selected period) using updated/created dates of snapshots.
    """

    to: Required[Union[int, str]]
    """
    Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
    selected `format`
    """

    company_id: Annotated[str, PropertyInfo(alias="companyId")]
    """Company ID parameter"""

    database_id: Annotated[str, PropertyInfo(alias="databaseId")]
    """Employee ID parameter"""

    employee_id: Annotated[str, PropertyInfo(alias="employeeId")]
    """Employee ID parameter"""

    employment_id: Annotated[str, PropertyInfo(alias="employmentId")]
    """External Employment ID"""

    format: Literal["timestamp", "date", "dateTime"]
    """
    Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
    8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters
    """

    limit: int

    organization_number: Annotated[str, PropertyInfo(alias="organizationNumber")]
    """Organization Number parameter"""

    page: int

    response_as_objects: Annotated[bool, PropertyInfo(alias="responseAsObjects")]
    """Determine the format of the response for relatedChanges key."""

    salary_system_company_id: Annotated[str, PropertyInfo(alias="salarySystemCompanyId")]
    """Salary System Company ID parameter"""

    sort_by: Annotated[Literal["createdAt", "-createdAt", "validFrom", "-validFrom"], PropertyInfo(alias="sortBy")]
    """Direction of sort"""

    unit_id: Annotated[str, PropertyInfo(alias="unitId")]
    """Unit ID parameter"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """User ID parameter"""

    with_custom_fields_tree: Annotated[bool, PropertyInfo(alias="withCustomFieldsTree")]
    """
    Determine if structure of custom fields should be returned (resource demanding
    operation).
    """
