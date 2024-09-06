#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter an island
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    assert 1 <= num_rows and num_cols <= 100

    perimeter = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:  # Only consider land cells
                if i == 0 or grid[i - 1][j] == 0:  # Check upper neighbor
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check left neighbor
                    perimeter += 1
                # Check lower neighbor
                if i == num_rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check right neighbor
                if j == num_cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
