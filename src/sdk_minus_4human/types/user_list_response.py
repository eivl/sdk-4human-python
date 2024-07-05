# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserListResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    company_id: Optional[int] = FieldInfo(alias="companyId", default=None)

    employed: Optional[bool] = None

    employment_calculated_status: Optional[
        Literal["vacant", "active", "terminating", "former", "dueForTermination", "pastDueTermination", "pending"]
    ] = FieldInfo(alias="employmentCalculatedStatus", default=None)

    employment_count: Optional[int] = FieldInfo(alias="employmentCount", default=None)

    employment_status: Optional[
        Literal[
            "offboarding",
            "vacant",
            "active",
            "terminating",
            "former",
            "dueForTermination",
            "pastDueTermination",
            "pending",
        ]
    ] = FieldInfo(alias="employmentStatus", default=None)

    has_active_directory_login: Optional[bool] = FieldInfo(alias="hasActiveDirectoryLogin", default=None)

    has_user_email: Optional[bool] = FieldInfo(alias="hasUserEmail", default=None)

    identity_provider: Optional[str] = FieldInfo(alias="identityProvider", default=None)

    instance_user_id: Optional[int] = FieldInfo(alias="instanceUserId", default=None)

    invitation_date_timestamp: Optional[int] = FieldInfo(alias="invitationDateTimestamp", default=None)

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)

    login_method: Optional[Literal["AUTH0", "NO_USER", "ACTIVE_DIRECTORY"]] = FieldInfo(
        alias="loginMethod", default=None
    )

    multiple_company_employments: Optional[bool] = FieldInfo(alias="multipleCompanyEmployments", default=None)

    primary_employment_id: Optional[int] = FieldInfo(alias="primaryEmploymentId", default=None)

    redirect_employment_id: Optional[int] = FieldInfo(alias="redirectEmploymentId", default=None)

    remaining_days: Optional[int] = FieldInfo(alias="remainingDays", default=None)

    user_calculated_status: Optional[
        Literal["active", "invited", "invitedOffboarding", "offboarding", "offboardingSoon", "expired"]
    ] = FieldInfo(alias="userCalculatedStatus", default=None)

    user_name: Optional[str] = FieldInfo(alias="userName", default=None)

    user_photo: Optional[str] = FieldInfo(alias="userPhoto", default=None)

    user_status: Optional[Literal["active", "invited"]] = FieldInfo(alias="userStatus", default=None)


class UserListResponse(BaseModel):
    items: List[Item]

    limit: Optional[int] = None

    page: Optional[int] = None

    pages: Optional[int] = None

    total: Optional[int] = None
