from math import factorial


def pascal_triangle(n):
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
