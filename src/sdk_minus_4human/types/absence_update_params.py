# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AbsenceUpdateParams", "Absence"]


class AbsenceUpdateParams(TypedDict, total=False):
    absences: Iterable[Absence]


class Absence(TypedDict, total=False):
    id: Union[str, int]
    """
    Internal id used to identify absence, when in `external` mode You should use
    `externalAbsenceId` values with it.
    """

    absence_code_id: Annotated[int, PropertyInfo(alias="absenceCodeId")]
    """Absence code internal identifier (id field)"""

    absence_code_id_external: Annotated[str, PropertyInfo(alias="absenceCodeIdExternal")]
    """
    External absence code id, the id that comes from other system that utilizes
    absence codes
    """

    comment: str
    """Comment that will be added to the absence"""

    date_from: Annotated[str, PropertyInfo(alias="dateFrom")]
    """
    The start date of the absence, use format `Y-m-d\\TTH:i:sP` for example
    `2024-01-05T00:00:00+00:00`
    """

    date_to: Annotated[str, PropertyInfo(alias="dateTo")]
    """
    The end date of the absence, use format `Y-m-d\\TTH:i:sP` for example
    `2024-01-05T00:00:00+00:00`
    """

    external_absence_id: Annotated[Union[str, int, None], PropertyInfo(alias="externalAbsenceId")]
    """Endpoint accepts both string and int.

    But the value is saved as a string. So if 1 provided it will be saved as '1'
    """

    hours: float
    """Number value for part time absence measured in hours"""

    percentage: float
    """
    Number value for part time absence measured in %, 100 value accepted as well, if
    absence code allows it is transformed into full time absence
    """

    source_system: Annotated[Optional[str], PropertyInfo(alias="sourceSystem")]
    """Name of the system that is responsible for the absence creation"""
