# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AbsenceDeleteResponse", "Absences"]


class Absences(BaseModel):
    errors: Union[List[object], object, None] = None

    success: Optional[List[int]] = None


class AbsenceDeleteResponse(BaseModel):
    absences: Optional[Absences] = None

    method: Optional[Literal["DELETE"]] = None
