#!/usr/bin/env python3
"""Sum of a list of mixed floats and integers"""


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list of mixed integers and floats.
    >>> sum_mixed_list([1, 2, 3, 4.5, 5.5])
    16.0
    """
    return sum(mxd_lst)
