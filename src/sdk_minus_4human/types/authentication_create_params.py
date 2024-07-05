# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuthenticationCreateParams"]


class AuthenticationCreateParams(TypedDict, total=False):
    client_id: Required[str]
    """Value is unique for each api user in instance.

    Must be generated for each instance user individually.
    """

    client_secret: Required[str]
    """Value is unique for each api user in instance.

    Must be generated for each instance user individually.
    """

    grant_type: Required[Literal["client_credentials"]]
