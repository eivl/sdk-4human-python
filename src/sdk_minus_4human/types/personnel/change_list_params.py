# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ChangeListParams"]


class ChangeListParams(TypedDict, total=False):
    from_: Required[Annotated[Union[int, str], PropertyInfo(alias="from")]]
    """
    Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
    ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`
    """

    to: Required[Union[int, str]]
    """
    Maximum date of changes, could be timestamp or date (YYYY-MM-DD) depending on
    selected `format`
    """

    company_id: Annotated[int, PropertyInfo(alias="companyId")]
    """database id of company"""

    external: bool
    """
    Param determines if returned ID is external or internal: Fields used as external
    ID:

    - `number` field in employment object
    - `employeeId` field in company-employee object
    - there is no external ID for user object, so always internal ID is returned
    """

    format: Literal["timestamp", "date", "dateTime"]
    """
    Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
    8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters
    """

    organisation_number: Annotated[str, PropertyInfo(alias="organisationNumber")]
    """
    ID of the company fetched from [brreg.no](https://www.brreg.no) for norway or
    custom one for other countries.
    """
