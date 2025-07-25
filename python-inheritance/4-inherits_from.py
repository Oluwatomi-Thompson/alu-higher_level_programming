#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check
        a_class: The class to check inheritance from

    Returns:
        bool: True if obj's class inherits from a_class, False otherwise
              (excludes exact same class)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
