#!/usr/bin/env python3
"""Iterate over a list"""

from typing import List, Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a non-empty list,
    or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
