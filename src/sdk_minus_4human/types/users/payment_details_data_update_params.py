# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PaymentDetailsDataUpdateParams"]


class PaymentDetailsDataUpdateParams(TypedDict, total=False):
    account_number: Required[Annotated[str, PropertyInfo(alias="accountNumber")]]

    country_of_bank: Required[Annotated[str, PropertyInfo(alias="countryOfBank")]]

    iban: Required[Optional[str]]

    force_no_approval_policy: Annotated[bool, PropertyInfo(alias="forceNoApprovalPolicy")]
    """
    Determines if changes should be made without approval (no confirmation snapshots
    will be created).
    """
