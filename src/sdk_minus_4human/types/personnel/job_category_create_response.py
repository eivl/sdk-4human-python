# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JobCategoryCreateResponse"]


class JobCategoryCreateResponse(BaseModel):
    id: str
    """Not editable, unique internal 4human's ID, not visible in system interface"""

    description: Optional[str] = None
    """Job category additional description"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    Editable, not unique external ID, allowing to store the ID of the client's
    system
    """

    internal_id: str = FieldInfo(alias="internalId")
    """Editable, unique internal ID provided by application user"""

    name: str
    """Unique job category name"""

    status: Literal["active", "inactive", "archived"]
    """Job category status"""
