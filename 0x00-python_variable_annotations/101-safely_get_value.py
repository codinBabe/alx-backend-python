#!/usr/bin/env python3
"""Safely get value"""


from typing import TypeVar, Union, Mapping, Any

T = TypeVar('T')
D = Union[T, None]
R = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> R:
    """
    Return the value of a key in a dictionary, or a default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
