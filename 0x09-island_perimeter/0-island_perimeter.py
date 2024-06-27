#!/usr/bin/python3
"""Defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                """Check all the sides of the current cell."""
                if r == 0 or grid[r-1][c] == 0:
                    """the top."""
                    perimeter += 1

                if r == rows - 1 or grid[r+1][c] == 0:
                    """the bottom."""
                    perimeter += 1

                if c == 0 or grid[r][c-1] == 0:
                    """the left."""
                    perimeter += 1

                if c == cols - 1 or grid[r][c+1] == 0:
                    """the right."""
                    perimeter += 1

    return perimeter
