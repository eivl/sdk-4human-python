# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["AuthenticationCreateResponse"]


class AuthenticationCreateResponse(BaseModel):
    access_token: str

    expires_in: int

    token_type: str
