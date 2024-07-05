# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TemplateCreateResponse", "Item"]


class Item(BaseModel):
    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)
    """Internal company ID"""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """Name of the company"""

    organization_number: Optional[str] = FieldInfo(alias="organizationNumber", default=None)
    """Internal company number"""

    salary_system_company_id: Optional[str] = FieldInfo(alias="salarySystemCompanyId", default=None)
    """External salary system ID"""

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)
    """Id of custom field template"""

    template_name: Optional[str] = FieldInfo(alias="templateName", default=None)
    """Name of custom field template"""


class TemplateCreateResponse(BaseModel):
    items: Optional[List[Item]] = None
