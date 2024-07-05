# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .skill_types import (
    SkillTypesResource,
    AsyncSkillTypesResource,
    SkillTypesResourceWithRawResponse,
    AsyncSkillTypesResourceWithRawResponse,
    SkillTypesResourceWithStreamingResponse,
    AsyncSkillTypesResourceWithStreamingResponse,
)
from .skill_type_categories import (
    SkillTypeCategoriesResource,
    AsyncSkillTypeCategoriesResource,
    SkillTypeCategoriesResourceWithRawResponse,
    AsyncSkillTypeCategoriesResourceWithRawResponse,
    SkillTypeCategoriesResourceWithStreamingResponse,
    AsyncSkillTypeCategoriesResourceWithStreamingResponse,
)
from .skill_types.skill_types import SkillTypesResource, AsyncSkillTypesResource

__all__ = ["CompetenceResource", "AsyncCompetenceResource"]


class CompetenceResource(SyncAPIResource):
    @cached_property
    def skill_type_categories(self) -> SkillTypeCategoriesResource:
        return SkillTypeCategoriesResource(self._client)

    @cached_property
    def skill_types(self) -> SkillTypesResource:
        return SkillTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompetenceResourceWithRawResponse:
        return CompetenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompetenceResourceWithStreamingResponse:
        return CompetenceResourceWithStreamingResponse(self)


class AsyncCompetenceResource(AsyncAPIResource):
    @cached_property
    def skill_type_categories(self) -> AsyncSkillTypeCategoriesResource:
        return AsyncSkillTypeCategoriesResource(self._client)

    @cached_property
    def skill_types(self) -> AsyncSkillTypesResource:
        return AsyncSkillTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompetenceResourceWithRawResponse:
        return AsyncCompetenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompetenceResourceWithStreamingResponse:
        return AsyncCompetenceResourceWithStreamingResponse(self)


class CompetenceResourceWithRawResponse:
    def __init__(self, competence: CompetenceResource) -> None:
        self._competence = competence

    @cached_property
    def skill_type_categories(self) -> SkillTypeCategoriesResourceWithRawResponse:
        return SkillTypeCategoriesResourceWithRawResponse(self._competence.skill_type_categories)

    @cached_property
    def skill_types(self) -> SkillTypesResourceWithRawResponse:
        return SkillTypesResourceWithRawResponse(self._competence.skill_types)


class AsyncCompetenceResourceWithRawResponse:
    def __init__(self, competence: AsyncCompetenceResource) -> None:
        self._competence = competence

    @cached_property
    def skill_type_categories(self) -> AsyncSkillTypeCategoriesResourceWithRawResponse:
        return AsyncSkillTypeCategoriesResourceWithRawResponse(self._competence.skill_type_categories)

    @cached_property
    def skill_types(self) -> AsyncSkillTypesResourceWithRawResponse:
        return AsyncSkillTypesResourceWithRawResponse(self._competence.skill_types)


class CompetenceResourceWithStreamingResponse:
    def __init__(self, competence: CompetenceResource) -> None:
        self._competence = competence

    @cached_property
    def skill_type_categories(self) -> SkillTypeCategoriesResourceWithStreamingResponse:
        return SkillTypeCategoriesResourceWithStreamingResponse(self._competence.skill_type_categories)

    @cached_property
    def skill_types(self) -> SkillTypesResourceWithStreamingResponse:
        return SkillTypesResourceWithStreamingResponse(self._competence.skill_types)


class AsyncCompetenceResourceWithStreamingResponse:
    def __init__(self, competence: AsyncCompetenceResource) -> None:
        self._competence = competence

    @cached_property
    def skill_type_categories(self) -> AsyncSkillTypeCategoriesResourceWithStreamingResponse:
        return AsyncSkillTypeCategoriesResourceWithStreamingResponse(self._competence.skill_type_categories)

    @cached_property
    def skill_types(self) -> AsyncSkillTypesResourceWithStreamingResponse:
        return AsyncSkillTypesResourceWithStreamingResponse(self._competence.skill_types)
