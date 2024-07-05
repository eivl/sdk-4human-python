# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ByLoginCreateResponse", "ByLoginCreateResponseItem"]


class ByLoginCreateResponseItem(BaseModel):
    active_directory_username: Optional[str] = FieldInfo(alias="activeDirectoryUsername", default=None)

    email: str

    login_method: Literal["AUTH0", "ACTIVE_DIRECTORY", "NO_USER"] = FieldInfo(alias="loginMethod")

    user_calculated_status: Literal["invited", "active", "offboarding", "inactive", "expired", "uninvited"] = FieldInfo(
        alias="userCalculatedStatus"
    )

    user_id: str = FieldInfo(alias="userId")

    user_name: str = FieldInfo(alias="userName")


ByLoginCreateResponse = List[ByLoginCreateResponseItem]
