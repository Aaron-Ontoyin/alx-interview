#!/usr/bin/python3
"""
Problem
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn't have “lakes”
(water inside that isn't connected to the water surrounding the island).
"""


def get_num_neigbors(grid, idx):
    """Get the number of neighbors of the current cell"""
    num_neighbors = 0
    row, col = idx
    if row - 1 >= 0 and grid[row - 1][col] == 1:
        num_neighbors += 1
    if row + 1 < len(grid) and grid[row + 1][col] == 1:
        num_neighbors += 1
    if col - 1 >= 0 and grid[row][col - 1] == 1:
        num_neighbors += 1
    if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
        num_neighbors += 1
    return num_neighbors


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter += (4 - get_num_neigbors(grid, (row, col)))
    return perimeter
