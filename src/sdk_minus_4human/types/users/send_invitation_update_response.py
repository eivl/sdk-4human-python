# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SendInvitationUpdateResponse"]


class SendInvitationUpdateResponse(BaseModel):
    invitation_link: Optional[str] = FieldInfo(alias="invitationLink", default=None)
