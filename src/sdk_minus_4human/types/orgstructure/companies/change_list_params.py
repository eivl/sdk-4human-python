# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChangeListParams"]


class ChangeListParams(TypedDict, total=False):
    from_: Required[Annotated[Union[int, str], PropertyInfo(alias="from")]]
    """
    Minimum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
    ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`
    """

    to: Required[Union[int, str]]
    """
    Maximum date of changes, could be timestamp or date (YYYY-MM-DD) or dateTime in
    ISO 8601 (Y-m-d\\TTH:i:sP) depending on selected `format`
    """

    external: bool
    """Param determines if returned id of unit is external (unitId) or internal (id)"""

    format: Literal["timestamp", "date", "dateTime"]
    """
    Param determines whether a timestamp or date (YYYY-MM-DD) or dateTime in ISO
    8601 (Y-m-d\\TTH:i:sP) will be used for `from` and `to` parameters
    """
