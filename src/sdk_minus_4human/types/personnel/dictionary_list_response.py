# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DictionaryListResponse", "WorkRelationType"]


class WorkRelationType(BaseModel):
    object: Optional[List[str]] = None


class DictionaryListResponse(BaseModel):
    salary_type: Optional[List[str]] = FieldInfo(alias="salaryType", default=None)

    work_relation_type: Optional[WorkRelationType] = FieldInfo(alias="workRelationType", default=None)

    work_status: Optional[List[str]] = FieldInfo(alias="workStatus", default=None)
