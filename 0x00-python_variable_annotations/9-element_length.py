#!/usr/bin/env python3
from typing import List, Tuple

def element_length(lst: List[float]) -> List[Tuple[float, int]]:
    """
    Returns a list of tuples containing each element of the input list and its length.

    Args:
        lst (List[float]): The list of floats.

    Returns:
        List[Tuple[float, int]]: A list of tuples where each tuple contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
