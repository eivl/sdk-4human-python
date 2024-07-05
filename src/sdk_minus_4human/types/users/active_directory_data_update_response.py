# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActiveDirectoryDataUpdateResponse"]


class ActiveDirectoryDataUpdateResponse(BaseModel):
    active_directory_username: Optional[str] = FieldInfo(alias="activeDirectoryUsername", default=None)

    email: Optional[str] = None

    user_id: str = FieldInfo(alias="userId")
