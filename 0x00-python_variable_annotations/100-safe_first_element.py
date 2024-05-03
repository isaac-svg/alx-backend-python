#!/usr/bin/env python3
from typing import Any, Union, Sequence

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element from a sequence.

    This function retrieves the first element from the given sequence. If the sequence is not empty,
    the first element is returned. Otherwise, None is returned.

    Args:
        lst (Sequence[Any]): The sequence from which to retrieve the first element.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
