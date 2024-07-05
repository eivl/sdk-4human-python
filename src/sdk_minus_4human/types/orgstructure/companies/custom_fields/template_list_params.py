# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    sort_by: Annotated[
        Literal[
            "companyId", "organizationNumber", "companyName", "salarySystemCompanyId", "templateId", "templateName"
        ],
        PropertyInfo(alias="sortBy"),
    ]
