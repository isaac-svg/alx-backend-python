#!/usr/bin/env python3
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of elements in a list containing a mixture of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing a mixture of integers and floats.

    Returns:
        float: The sum of all elements in the list.
    """
    return sum(mxd_lst)
