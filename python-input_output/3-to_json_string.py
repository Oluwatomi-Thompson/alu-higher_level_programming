#!/usr/bin/python3
"""
Module that provides JSON string conversion functionality.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
