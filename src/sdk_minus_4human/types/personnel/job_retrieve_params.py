# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["JobRetrieveParams"]


class JobRetrieveParams(TypedDict, total=False):
    external: bool
    """
    Param determines if `jobId` parameter is provided as external ID (field called
    `number`) or internal 4human's ID (field called `id`)
    """
