#!/usr/bin/python3
"""
0-pascal_triangle
"""
from math import factorial


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for r in range(i + 1):
            element = factorial(i) // (factorial(r) * factorial(i - r))
            row.append(element)
        triangle.append(row)

    return triangle
