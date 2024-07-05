# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SkillTypeCategoryRetrieveResponse", "Icon"]


class Icon(BaseModel):
    icon_name: Literal[
        "award",
        "book-medical",
        "crutches",
        "file-certificate",
        "file-check",
        "fire-alt",
        "globe-africa",
        "guitar",
        "heartbeat",
        "industry",
        "life-ring",
        "medal",
        "police-box",
        "shield-check",
        "star'",
        "thumbs-up",
        "tools",
        "trophy",
        "truck",
        "user-graduate",
        "user-hard-hat",
        "users-class",
        "user-shiel",
    ] = FieldInfo(alias="iconName")
    """Name of the icon"""

    prefix: Literal["fas", "fab", "far", "fal", "fad"]
    """Prefix that determines the style of icon"""


class SkillTypeCategoryRetrieveResponse(BaseModel):
    id: str
    """ID of skill type category"""

    color: Optional[
        Literal[
            "#191970",
            "#4169E1",
            "#4682B4",
            "#52BFFF",
            "#4ED1CC",
            "#008080",
            "#298652",
            "#5E8115",
            "#4B0082",
            "#800080",
            "#C71585",
            "#8562CD",
            "#AF4AC8",
            "#F084F0",
            "#E0330D",
            "#FF8B6F",
            "#C35252",
            "#696969",
            "#A52A2A",
            "#EA977B",
            "#DAA51F",
            "#F4A503",
        ]
    ] = None
    """Color of icon skill type category (hexadecimal color value)"""

    description: str
    """Description of skill type category"""

    icon: Optional[Icon] = None

    name: str
    """Name of skill type category"""

    number: str
    """Number of skill type category"""

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)
    """ID of parent skill type category"""