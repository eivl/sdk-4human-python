# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    limit: int
    """Number of records returned in one request"""

    page: int
    """Number of returned page"""
