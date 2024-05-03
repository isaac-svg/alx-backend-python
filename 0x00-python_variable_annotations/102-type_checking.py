#!/usr/bin/env python3
from typing import Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on the elements of the input tuple by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): The tuple containing the elements to be zoomed in on.
        factor (int, optional): The factor by which to zoom in on the elements. Defaults to 2.

    Returns:
        Tuple[int, ...]: A new tuple containing the zoomed-in elements.
    """
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_array.__annotations__)
