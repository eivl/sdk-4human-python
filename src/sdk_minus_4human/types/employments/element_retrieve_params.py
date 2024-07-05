# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ElementRetrieveParams"]


class ElementRetrieveParams(TypedDict, total=False):
    external: bool
    """Param determines if id of employment is external (number) or internal (id)"""
