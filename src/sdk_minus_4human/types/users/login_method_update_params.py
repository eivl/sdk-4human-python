# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LoginMethodUpdateParams"]


class LoginMethodUpdateParams(TypedDict, total=False):
    active_directory_login: Required[Annotated[Optional[str], PropertyInfo(alias="activeDirectoryLogin")]]

    email: Required[Optional[str]]

    login_method: Required[
        Annotated[Literal["NO_USER", "ACTIVE_DIRECTORY", "AUTH0"], PropertyInfo(alias="loginMethod")]
    ]

    should_send_email: Annotated[bool, PropertyInfo(alias="shouldSendEmail")]
    """Param determines if email with details of login method should be sent."""
