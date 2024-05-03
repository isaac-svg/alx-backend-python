#!/usr/bin/env python3
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely retrieves a value from a dictionary.

    This function retrieves the value associated with the specified key from the given dictionary. If the key is present
    in the dictionary, its corresponding value is returned. Otherwise, the default value (if provided) is returned.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key whose associated value should be retrieved.
        default (Union[T, None], optional): The default value to return if the key is not present in the dictionary.
            Defaults to None.

    Returns:
        Union[T, None]: The value associated with the specified key, or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
