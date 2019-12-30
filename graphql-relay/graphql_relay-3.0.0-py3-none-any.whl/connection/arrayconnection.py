import binascii
import warnings
from typing import Any, Optional, Sequence

from ..utils.base64 import base64, unbase64
from .connectiontypes import (
    Connection,
    ConnectionArguments,
    ConnectionCursor,
    Edge,
    PageInfo,
)

__all__ = [
    "connection_from_array",
    "connection_from_array_slice",
    "cursor_for_object_in_connection",
    "cursor_to_offset",
    "get_offset_with_default",
    "offset_to_cursor",
]


def connection_from_array(
    data: Sequence,
    args: ConnectionArguments = None,
    connection_type: Any = Connection,
    edge_type: Any = Edge,
    page_info_type: Any = PageInfo,
) -> Connection:
    """Create a connection object from a sequence of objects.

    Note that different from its JavaScript counterpart which expects an array,
    this function accepts any kind of sliceable object with a length.

    Given this `data` object representing the result set, and connection arguments,
    this simple function returns a connection object for use in GraphQL. It uses
    offsets as pagination, so pagination will only work if the data is static.

    The result will use the default types provided in the `connectiontypes` module
    if you don't pass custom types as arguments.
    """
    return connection_from_array_slice(
        data,
        args,
        slice_start=0,
        array_length=len(data),
        connection_type=connection_type,
        edge_type=edge_type,
        page_info_type=page_info_type,
    )


def connection_from_list(
    data: Sequence,
    args: ConnectionArguments = None,
    connection_type: Any = Connection,
    edge_type: Any = Edge,
    pageinfo_type: Any = PageInfo,
) -> Connection:
    """Deprecated alias for connection_from_array.

    We're now using the JavaScript terminology in Python as well, since list
    is too narrow a type and there is no other really appropriate type name.
    """
    warnings.warn(
        "connection_from_list() has been deprecated."
        " Please use connection_from_array() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return connection_from_array_slice(
        data,
        args,
        connection_type=connection_type,
        edge_type=edge_type,
        page_info_type=pageinfo_type,
    )


def connection_from_array_slice(
    array_slice: Sequence,
    args: ConnectionArguments = None,
    slice_start: int = 0,
    array_length: int = None,
    array_slice_length: int = None,
    connection_type: Any = Connection,
    edge_type: Any = Edge,
    page_info_type: Any = PageInfo,
) -> Connection:
    """Create a connection object from a slice of the result set.

    Note that different from its JavaScript counterpart which expects an array,
    this function accepts any kind of sliceable object. This object represents
    a slice of the full result set. You need to pass the start position of the
    slice as `slice start` and the length of the full result set as `array_length`.
    If the `array_slice` does not have a length, you need to provide it separately
    in `array_slice_length` as well.

    This function is similar to `connection_from_array`, but is intended for use
    cases where you know the cardinality of the connection, consider it too large
    to materialize the entire result set, and instead wish to pass in only a slice
    of the total result large enough to cover the range specified in `args`.

    If you do not provide a `slice_start`, we assume that the slice starts at
    the beginning of the result set, and if you do not provide an `array_length`,
    we assume that the slice ends at the end of the result set.
    """
    args = args or {}
    before = args.get("before")
    after = args.get("after")
    first = args.get("first")
    last = args.get("last")
    if array_slice_length is None:
        array_slice_length = len(array_slice)
    slice_end = slice_start + array_slice_length
    if array_length is None:
        array_length = slice_end
    before_offset = get_offset_with_default(before, array_length)
    after_offset = get_offset_with_default(after, -1)

    start_offset = max(slice_start - 1, after_offset, -1) + 1
    end_offset = min(slice_end, before_offset, array_length)

    if isinstance(first, int):
        if first < 0:
            raise ValueError("Argument 'first' must be a non-negative integer.")

        end_offset = min(end_offset, start_offset + first)
    if isinstance(last, int):
        if last < 0:
            raise ValueError("Argument 'last' must be a non-negative integer.")

        start_offset = max(start_offset, end_offset - last)

    # If supplied slice is too large, trim it down before mapping over it.
    trimmed_slice = array_slice[
        start_offset - slice_start : array_slice_length - (slice_end - end_offset)
    ]

    edges = [
        edge_type(node=value, cursor=offset_to_cursor(start_offset + index))
        for index, value in enumerate(trimmed_slice)
    ]

    first_edge_cursor = edges[0].cursor if edges else None
    last_edge_cursor = edges[-1].cursor if edges else None
    lower_bound = after_offset + 1 if after else 0
    upper_bound = before_offset if before else array_length

    return connection_type(
        edges=edges,
        pageInfo=page_info_type(
            startCursor=first_edge_cursor,
            endCursor=last_edge_cursor,
            hasPreviousPage=isinstance(last, int) and start_offset > lower_bound,
            hasNextPage=isinstance(first, int) and end_offset < upper_bound,
        ),
    )


def connection_from_list_slice(
    list_slice: Sequence,
    args: ConnectionArguments = None,
    connection_type: Any = Connection,
    edge_type: Any = Edge,
    pageinfo_type: Any = PageInfo,
    slice_start=0,
    list_length=0,
    list_slice_length=None,
) -> Connection:
    """Deprecated alias for connection_from_array_slice.

    We're now using the JavaScript terminology in Python as well, since list
    is too narrow a type and there is no other really appropriate type name.
    """
    warnings.warn(
        "connection_from_list_slice() has been deprecated."
        " Please use connection_from_array_slice() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return connection_from_array_slice(
        list_slice,
        args,
        slice_start=slice_start,
        array_length=list_length,
        array_slice_length=list_slice_length,
        connection_type=connection_type,
        edge_type=edge_type,
        page_info_type=pageinfo_type,
    )


PREFIX = "arrayconnection:"


def offset_to_cursor(offset: int) -> ConnectionCursor:
    """Create the cursor string from an offset."""
    return base64(f"{PREFIX}{offset}")


def cursor_to_offset(cursor: ConnectionCursor) -> Optional[int]:
    """Rederive the offset from the cursor string."""
    try:
        return int(unbase64(cursor)[len(PREFIX) :])
    except binascii.Error:
        return None


def cursor_for_object_in_connection(
    data: Sequence, obj: Any
) -> Optional[ConnectionCursor]:
    """Return the cursor associated with an object in a sequence.

    This function uses the `index` method of the sequence if it exists,
    otherwise searches the object by iterating via the `__getitem__` method.
    """
    try:
        offset = data.index(obj)
    except AttributeError:
        # data does not have an index method
        offset = 0
        try:
            while True:
                if data[offset] == obj:
                    break
                offset += 1
        except IndexError:
            return None
        else:
            return offset_to_cursor(offset)
    except ValueError:
        return None
    else:
        return offset_to_cursor(offset)


def get_offset_with_default(cursor: ConnectionCursor = None, default_offset=0) -> int:
    """Get offset from a given cursor and a default.

    Given an optional cursor and a default offset, return the offset to use;
    if the cursor contains a valid offset, that will be used,
    otherwise it will be the default.
    """
    if not isinstance(cursor, str):
        return default_offset

    offset = cursor_to_offset(cursor)
    return default_offset if offset is None else offset
