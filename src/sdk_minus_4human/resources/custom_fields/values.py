# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.custom_fields import (
    value_create_params,
    value_update_params,
    value_change_status_params,
    value_update_partial_params,
)
from ...types.custom_fields.value_create_response import ValueCreateResponse
from ...types.custom_fields.value_update_response import ValueUpdateResponse
from ...types.custom_fields.value_change_status_response import ValueChangeStatusResponse
from ...types.custom_fields.value_update_partial_response import ValueUpdatePartialResponse

__all__ = ["ValuesResource", "AsyncValuesResource"]


class ValuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self)

    def create(
        self,
        value_id: str,
        *,
        external_id: str,
        external_name: str,
        internal_id: str,
        name: str,
        return_single_item: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueCreateResponse:
        """This endpoint applies to creation of predefinied values for custom fields.

        Each
        predefined value may be treated as:

        - single value (in case of select fields)
        - tree structure value (in case of structural fields)

        Args:
          external_id: Can be treated as "Id of value from external system" used to find values in hr
              master by their own known id.

          external_name: Can be treated as "Name of value from external system" used to find values in hr
              master by their own known name.

          name: Field contains name of custom field value or custom value provided by user (i.e.
              text, number, date)

          return_single_item: Param determines whether a single item or the entire tree structure will be
              returned in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not value_id:
            raise ValueError(f"Expected a non-empty value for `value_id` but received {value_id!r}")
        return cast(
            ValueCreateResponse,
            self._post(
                f"/personnel/custom-fields/values/{value_id}",
                body=maybe_transform(
                    {
                        "external_id": external_id,
                        "external_name": external_name,
                        "internal_id": internal_id,
                        "name": name,
                    },
                    value_create_params.ValueCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"return_single_item": return_single_item}, value_create_params.ValueCreateParams
                    ),
                ),
                cast_to=cast(
                    Any, ValueCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        value_id: str,
        *,
        external_id: str,
        external_name: str,
        internal_id: Optional[str],
        name: Optional[str],
        return_single_item: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueUpdateResponse:
        """
        This endpoint allows to edit custom fields value identified by UUID.

        Args:
          external_id: Can be treated as "Id of value from external system" used to find values in hr
              master by their own known id.

          external_name: Can be treated as "Id of value from external system" used to find values in hr
              master by their own known id.

          name: Field contains name of custom field value or custom value provided by user (i.e.
              text, number, date)

          return_single_item: Param determines whether a single item or the entire tree structure will be
              returned in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not value_id:
            raise ValueError(f"Expected a non-empty value for `value_id` but received {value_id!r}")
        return cast(
            ValueUpdateResponse,
            self._put(
                f"/personnel/custom-fields/values/{value_id}",
                body=maybe_transform(
                    {
                        "external_id": external_id,
                        "external_name": external_name,
                        "internal_id": internal_id,
                        "name": name,
                    },
                    value_update_params.ValueUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"return_single_item": return_single_item}, value_update_params.ValueUpdateParams
                    ),
                ),
                cast_to=cast(
                    Any, ValueUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def change_status(
        self,
        value_id: str,
        *,
        return_single_item: bool | NotGiven = NOT_GIVEN,
        id: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueChangeStatusResponse:
        """
        Enable or disable custom field value with given id is possible only if given
        custom field value is not in use.

        Args:
          return_single_item: Param determines whether a single item or the entire tree structure will be
              returned in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not value_id:
            raise ValueError(f"Expected a non-empty value for `value_id` but received {value_id!r}")
        return cast(
            ValueChangeStatusResponse,
            self._patch(
                f"/personnel/custom-fields/values/change-status/{value_id}",
                body=maybe_transform({"id": id}, value_change_status_params.ValueChangeStatusParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"return_single_item": return_single_item}, value_change_status_params.ValueChangeStatusParams
                    ),
                ),
                cast_to=cast(
                    Any, ValueChangeStatusResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update_partial(
        self,
        value_id: str,
        *,
        return_single_item: bool | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        external_name: str | NotGiven = NOT_GIVEN,
        internal_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueUpdatePartialResponse:
        """
        Use this endpoint to modify a single field of a custom field value.

        Args:
          return_single_item: Param determines whether a single item or the entire tree structure will be
              returned in the response

          external_id: Can be treated as "Id of value from external system" used to find values in hr
              master by their own known id.

          external_name: Can be treated as "Name of value from external system" used to find values in hr
              master by their own known name.

          name: Field contains name of custom field value or custom value provided by user (i.e.
              text, number, date)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not value_id:
            raise ValueError(f"Expected a non-empty value for `value_id` but received {value_id!r}")
        return cast(
            ValueUpdatePartialResponse,
            self._patch(
                f"/personnel/custom-fields/values/{value_id}",
                body=maybe_transform(
                    {
                        "external_id": external_id,
                        "external_name": external_name,
                        "internal_id": internal_id,
                        "name": name,
                    },
                    value_update_partial_params.ValueUpdatePartialParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"return_single_item": return_single_item}, value_update_partial_params.ValueUpdatePartialParams
                    ),
                ),
                cast_to=cast(
                    Any, ValueUpdatePartialResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncValuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self)

    async def create(
        self,
        value_id: str,
        *,
        external_id: str,
        external_name: str,
        internal_id: str,
        name: str,
        return_single_item: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueCreateResponse:
        """This endpoint applies to creation of predefinied values for custom fields.

        Each
        predefined value may be treated as:

        - single value (in case of select fields)
        - tree structure value (in case of structural fields)

        Args:
          external_id: Can be treated as "Id of value from external system" used to find values in hr
              master by their own known id.

          external_name: Can be treated as "Name of value from external system" used to find values in hr
              master by their own known name.

          name: Field contains name of custom field value or custom value provided by user (i.e.
              text, number, date)

          return_single_item: Param determines whether a single item or the entire tree structure will be
              returned in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not value_id:
            raise ValueError(f"Expected a non-empty value for `value_id` but received {value_id!r}")
        return cast(
            ValueCreateResponse,
            await self._post(
                f"/personnel/custom-fields/values/{value_id}",
                body=await async_maybe_transform(
                    {
                        "external_id": external_id,
                        "external_name": external_name,
                        "internal_id": internal_id,
                        "name": name,
                    },
                    value_create_params.ValueCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"return_single_item": return_single_item}, value_create_params.ValueCreateParams
                    ),
                ),
                cast_to=cast(
                    Any, ValueCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        value_id: str,
        *,
        external_id: str,
        external_name: str,
        internal_id: Optional[str],
        name: Optional[str],
        return_single_item: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueUpdateResponse:
        """
        This endpoint allows to edit custom fields value identified by UUID.

        Args:
          external_id: Can be treated as "Id of value from external system" used to find values in hr
              master by their own known id.

          external_name: Can be treated as "Id of value from external system" used to find values in hr
              master by their own known id.

          name: Field contains name of custom field value or custom value provided by user (i.e.
              text, number, date)

          return_single_item: Param determines whether a single item or the entire tree structure will be
              returned in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not value_id:
            raise ValueError(f"Expected a non-empty value for `value_id` but received {value_id!r}")
        return cast(
            ValueUpdateResponse,
            await self._put(
                f"/personnel/custom-fields/values/{value_id}",
                body=await async_maybe_transform(
                    {
                        "external_id": external_id,
                        "external_name": external_name,
                        "internal_id": internal_id,
                        "name": name,
                    },
                    value_update_params.ValueUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"return_single_item": return_single_item}, value_update_params.ValueUpdateParams
                    ),
                ),
                cast_to=cast(
                    Any, ValueUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def change_status(
        self,
        value_id: str,
        *,
        return_single_item: bool | NotGiven = NOT_GIVEN,
        id: Literal["ACTIVE", "INACTIVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueChangeStatusResponse:
        """
        Enable or disable custom field value with given id is possible only if given
        custom field value is not in use.

        Args:
          return_single_item: Param determines whether a single item or the entire tree structure will be
              returned in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not value_id:
            raise ValueError(f"Expected a non-empty value for `value_id` but received {value_id!r}")
        return cast(
            ValueChangeStatusResponse,
            await self._patch(
                f"/personnel/custom-fields/values/change-status/{value_id}",
                body=await async_maybe_transform({"id": id}, value_change_status_params.ValueChangeStatusParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"return_single_item": return_single_item}, value_change_status_params.ValueChangeStatusParams
                    ),
                ),
                cast_to=cast(
                    Any, ValueChangeStatusResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update_partial(
        self,
        value_id: str,
        *,
        return_single_item: bool | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        external_name: str | NotGiven = NOT_GIVEN,
        internal_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueUpdatePartialResponse:
        """
        Use this endpoint to modify a single field of a custom field value.

        Args:
          return_single_item: Param determines whether a single item or the entire tree structure will be
              returned in the response

          external_id: Can be treated as "Id of value from external system" used to find values in hr
              master by their own known id.

          external_name: Can be treated as "Name of value from external system" used to find values in hr
              master by their own known name.

          name: Field contains name of custom field value or custom value provided by user (i.e.
              text, number, date)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not value_id:
            raise ValueError(f"Expected a non-empty value for `value_id` but received {value_id!r}")
        return cast(
            ValueUpdatePartialResponse,
            await self._patch(
                f"/personnel/custom-fields/values/{value_id}",
                body=await async_maybe_transform(
                    {
                        "external_id": external_id,
                        "external_name": external_name,
                        "internal_id": internal_id,
                        "name": name,
                    },
                    value_update_partial_params.ValueUpdatePartialParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"return_single_item": return_single_item}, value_update_partial_params.ValueUpdatePartialParams
                    ),
                ),
                cast_to=cast(
                    Any, ValueUpdatePartialResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ValuesResourceWithRawResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.create = to_raw_response_wrapper(
            values.create,
        )
        self.update = to_raw_response_wrapper(
            values.update,
        )
        self.change_status = to_raw_response_wrapper(
            values.change_status,
        )
        self.update_partial = to_raw_response_wrapper(
            values.update_partial,
        )


class AsyncValuesResourceWithRawResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.create = async_to_raw_response_wrapper(
            values.create,
        )
        self.update = async_to_raw_response_wrapper(
            values.update,
        )
        self.change_status = async_to_raw_response_wrapper(
            values.change_status,
        )
        self.update_partial = async_to_raw_response_wrapper(
            values.update_partial,
        )


class ValuesResourceWithStreamingResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.create = to_streamed_response_wrapper(
            values.create,
        )
        self.update = to_streamed_response_wrapper(
            values.update,
        )
        self.change_status = to_streamed_response_wrapper(
            values.change_status,
        )
        self.update_partial = to_streamed_response_wrapper(
            values.update_partial,
        )


class AsyncValuesResourceWithStreamingResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.create = async_to_streamed_response_wrapper(
            values.create,
        )
        self.update = async_to_streamed_response_wrapper(
            values.update,
        )
        self.change_status = async_to_streamed_response_wrapper(
            values.change_status,
        )
        self.update_partial = async_to_streamed_response_wrapper(
            values.update_partial,
        )
