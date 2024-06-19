#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates 90 degrees clockwise a matrix in place.
    Args:
        n x n matrix.
    """

    n = len(matrix)

    """Step 1: Transpose the matrix."""
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    """Reverse each row manually."""
    for i in range(n):
        row_length = len(matrix[i])
        for j in range(row_length // 2):
            left = matrix[i][j]
            right = matrix[i][row_length - 1 - j]
            matrix[i][j], matrix[i][row_length - 1 - j] = right, left
