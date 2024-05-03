#!/usr/bin/env python3
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key-value pair into a tuple, where the value is squared.

    Args:
        k (str): The key.
        v (Union[int, float]): The value, which can be either an integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the square of the value.
    """
    return (k, v * v)
