from math import factorial


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for space in range(1, n - i):
            row.append(0)  # Add placeholder 0s for formatting
        for r in range(i + 1):
            ncr = factorial(i) // (factorial(r) * factorial(i - r))
            row.append(ncr)
        triangle.append(row)

    return triangle
