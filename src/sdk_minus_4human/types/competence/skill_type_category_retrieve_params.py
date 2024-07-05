# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SkillTypeCategoryRetrieveParams"]


class SkillTypeCategoryRetrieveParams(TypedDict, total=False):
    external: bool
    """Param determines if `id` is external (`number`) or internal (`id`)"""