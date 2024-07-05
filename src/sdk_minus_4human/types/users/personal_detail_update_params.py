# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PersonalDetailUpdateParams"]


class PersonalDetailUpdateParams(TypedDict, total=False):
    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """

    alias: Optional[str]

    country_of_origin: Annotated[Optional[str], PropertyInfo(alias="countryOfOrigin")]

    date_of_birth: Annotated[Union[str, datetime, None], PropertyInfo(alias="dateOfBirth", format="iso8601")]

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    gender: Optional[Literal["-", "M", "F"]]

    initials: Optional[str]

    marital_status: Annotated[
        Optional[
            Literal[
                "unmarried",
                "married",
                "widowed",
                "divorced",
                "separated",
                "registeredPartner",
                "separatedPartner",
                "divorcedPartner",
                "survivingPartner",
                "cohabitant",
            ]
        ],
        PropertyInfo(alias="maritalStatus"),
    ]

    nationality: Optional[str]

    surname: str
