#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that takes a float as input and returns the result of multiplying
            that float by the specified multiplier.
    """
    def multiplier_function(num: float) -> float:
        return num * multiplier
    return multiplier_function
