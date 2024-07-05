# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .benefits import (
    BenefitsResource,
    AsyncBenefitsResource,
    BenefitsResourceWithRawResponse,
    AsyncBenefitsResourceWithRawResponse,
    BenefitsResourceWithStreamingResponse,
    AsyncBenefitsResourceWithStreamingResponse,
)
from .deductions import (
    DeductionsResource,
    AsyncDeductionsResource,
    DeductionsResourceWithRawResponse,
    AsyncDeductionsResourceWithRawResponse,
    DeductionsResourceWithStreamingResponse,
    AsyncDeductionsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .additional_salaries import (
    AdditionalSalariesResource,
    AsyncAdditionalSalariesResource,
    AdditionalSalariesResourceWithRawResponse,
    AsyncAdditionalSalariesResourceWithRawResponse,
    AdditionalSalariesResourceWithStreamingResponse,
    AsyncAdditionalSalariesResourceWithStreamingResponse,
)

__all__ = ["ElementsResource", "AsyncElementsResource"]


class ElementsResource(SyncAPIResource):
    @cached_property
    def additional_salaries(self) -> AdditionalSalariesResource:
        return AdditionalSalariesResource(self._client)

    @cached_property
    def benefits(self) -> BenefitsResource:
        return BenefitsResource(self._client)

    @cached_property
    def deductions(self) -> DeductionsResource:
        return DeductionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ElementsResourceWithRawResponse:
        return ElementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ElementsResourceWithStreamingResponse:
        return ElementsResourceWithStreamingResponse(self)


class AsyncElementsResource(AsyncAPIResource):
    @cached_property
    def additional_salaries(self) -> AsyncAdditionalSalariesResource:
        return AsyncAdditionalSalariesResource(self._client)

    @cached_property
    def benefits(self) -> AsyncBenefitsResource:
        return AsyncBenefitsResource(self._client)

    @cached_property
    def deductions(self) -> AsyncDeductionsResource:
        return AsyncDeductionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncElementsResourceWithRawResponse:
        return AsyncElementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncElementsResourceWithStreamingResponse:
        return AsyncElementsResourceWithStreamingResponse(self)


class ElementsResourceWithRawResponse:
    def __init__(self, elements: ElementsResource) -> None:
        self._elements = elements

    @cached_property
    def additional_salaries(self) -> AdditionalSalariesResourceWithRawResponse:
        return AdditionalSalariesResourceWithRawResponse(self._elements.additional_salaries)

    @cached_property
    def benefits(self) -> BenefitsResourceWithRawResponse:
        return BenefitsResourceWithRawResponse(self._elements.benefits)

    @cached_property
    def deductions(self) -> DeductionsResourceWithRawResponse:
        return DeductionsResourceWithRawResponse(self._elements.deductions)


class AsyncElementsResourceWithRawResponse:
    def __init__(self, elements: AsyncElementsResource) -> None:
        self._elements = elements

    @cached_property
    def additional_salaries(self) -> AsyncAdditionalSalariesResourceWithRawResponse:
        return AsyncAdditionalSalariesResourceWithRawResponse(self._elements.additional_salaries)

    @cached_property
    def benefits(self) -> AsyncBenefitsResourceWithRawResponse:
        return AsyncBenefitsResourceWithRawResponse(self._elements.benefits)

    @cached_property
    def deductions(self) -> AsyncDeductionsResourceWithRawResponse:
        return AsyncDeductionsResourceWithRawResponse(self._elements.deductions)


class ElementsResourceWithStreamingResponse:
    def __init__(self, elements: ElementsResource) -> None:
        self._elements = elements

    @cached_property
    def additional_salaries(self) -> AdditionalSalariesResourceWithStreamingResponse:
        return AdditionalSalariesResourceWithStreamingResponse(self._elements.additional_salaries)

    @cached_property
    def benefits(self) -> BenefitsResourceWithStreamingResponse:
        return BenefitsResourceWithStreamingResponse(self._elements.benefits)

    @cached_property
    def deductions(self) -> DeductionsResourceWithStreamingResponse:
        return DeductionsResourceWithStreamingResponse(self._elements.deductions)


class AsyncElementsResourceWithStreamingResponse:
    def __init__(self, elements: AsyncElementsResource) -> None:
        self._elements = elements

    @cached_property
    def additional_salaries(self) -> AsyncAdditionalSalariesResourceWithStreamingResponse:
        return AsyncAdditionalSalariesResourceWithStreamingResponse(self._elements.additional_salaries)

    @cached_property
    def benefits(self) -> AsyncBenefitsResourceWithStreamingResponse:
        return AsyncBenefitsResourceWithStreamingResponse(self._elements.benefits)

    @cached_property
    def deductions(self) -> AsyncDeductionsResourceWithStreamingResponse:
        return AsyncDeductionsResourceWithStreamingResponse(self._elements.deductions)
