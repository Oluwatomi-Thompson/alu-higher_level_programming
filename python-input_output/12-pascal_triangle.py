#!/usr/bin/python3
"""
Module that provides Pascal's triangle generation functionality.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle
              or empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                # First and last elements of each row are always 1
                row.append(1)
            else:
                # Each element is the sum of the two elements above it
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
