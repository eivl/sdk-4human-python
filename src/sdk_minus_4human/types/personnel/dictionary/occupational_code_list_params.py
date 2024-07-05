# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OccupationalCodeListParams"]


class OccupationalCodeListParams(TypedDict, total=False):
    country: Required[str]
    """country - code of the country with occupational code, e.g. 'NOR'"""

    query: Required[str]
    """query - phrase to search occupational code by the title, e.g. 'KORIN'"""
