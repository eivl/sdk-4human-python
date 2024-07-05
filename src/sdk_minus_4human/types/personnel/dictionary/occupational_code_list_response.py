# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["OccupationalCodeListResponse", "OccupationalCodeListResponseItem"]


class OccupationalCodeListResponseItem(BaseModel):
    code: str

    name: str


OccupationalCodeListResponse = List[OccupationalCodeListResponseItem]
