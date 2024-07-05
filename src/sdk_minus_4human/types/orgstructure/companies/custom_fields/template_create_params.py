# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    company_id: Required[Annotated[int, PropertyInfo(alias="companyId")]]
    """Internal company ID"""

    template_id: Required[Annotated[str, PropertyInfo(alias="templateId")]]
    """Id of custom field template"""
