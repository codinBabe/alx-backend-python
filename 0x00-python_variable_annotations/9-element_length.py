#!/usr/bin/env python3
"""Iterate over a list"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, where each tuple contains an element
    from the input list and its length.

    Parameters:
        lst (Iterable[Sequence]): A list of strings.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing
        each element and its length.
    """
    return [(i, len(i)) for i in lst]
