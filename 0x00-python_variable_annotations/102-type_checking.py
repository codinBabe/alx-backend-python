#!/usr/bin/env python3
"""Zoom array"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom array by a specified factor.

    Args:
        lst (Tuple): The original array to be zoomed.
        factor (int, optional): The factor by which to zoom the array.
        Defaults to 2.

    Returns:
        Tuple: The zoomed array.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)