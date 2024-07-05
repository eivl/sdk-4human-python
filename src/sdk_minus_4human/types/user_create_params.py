# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    email: Required[str]

    first_name: Required[Annotated[Optional[str], PropertyInfo(alias="firstName")]]

    language: Required[Literal["en", "no"]]

    last_name: Required[Annotated[Optional[str], PropertyInfo(alias="lastName")]]

    send_invitation: Annotated[bool, PropertyInfo(alias="sendInvitation")]
    """Param determines if the email notification should be sent for created user."""

    access_groups: Annotated[List[str], PropertyInfo(alias="accessGroups")]

    active_directory_user_name: Annotated[Optional[str], PropertyInfo(alias="activeDirectoryUserName")]

    login_method: Annotated[Literal["ACTIVE_DIRECTORY", "AUTH0"], PropertyInfo(alias="loginMethod")]
