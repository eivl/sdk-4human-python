# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoginMethodUpdateResponse", "LoginMethod"]


class LoginMethod(BaseModel):
    active_directory_login: Optional[str] = FieldInfo(alias="activeDirectoryLogin", default=None)

    email: str

    login_method: Literal["NO_USER", "ACTIVE_DIRECTORY", "AUTH0"] = FieldInfo(alias="loginMethod")


class LoginMethodUpdateResponse(BaseModel):
    login_method: LoginMethod = FieldInfo(alias="loginMethod")
