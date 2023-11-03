#!/usr/bin/python3
"""
NQueens: Alx interview

The N queens puzzle is the challenge of placing N non-attacking queens on
an NxN chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1
The program should print every possible solution to the problem
One solution per line
You don't have to print the solutions in a specific order
"""
import sys


args = sys.argv
if not len(args) == 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n = int(args[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n < 4:
    print('N must be at least 4')
    exit(1)


class ChessBoard:
    def __init__(self, n) -> None:
        """
        Chess Board class for inserting n non attacking queens
        n: size of board
        """
        self._board = [['_'] * n for _ in range(n)]
        self.POSITIONS = [[i, j] for i in range(n) for j in range(n)]
        self.PATH = []
        self.n = n
        self.solutions = []

    def display(self):
        """Display ChessBoard"""
        for row in self._board:
            print(row, end='\n\n')

    def insert(self, pos):
        """
        Insert queen into ChessBoard
        pos: tuple of (row, col)
        """
        row, col = pos
        self._board[row][col] = 'Q'

    def remove(self, pos):
        """
        Remove queen from ChessBoard
        pos: tuple of (row, col)
        """
        row, col = pos
        self._board[row][col] = '_'

    def is_safe(self, row, col):
        """
        Check if queen can be placed at (row, col)
        """
        for i in range(row):
            if self._board[i][col] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self._board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self._board[i][j] == 'Q':
                return False

        return True

    def _solve(self, row):
        """
        Solve NQueens problem
        """
        if row == self.n:
            self.solutions.append(self.PATH.copy())
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.insert([row, col])
                self.PATH.append([row, col])
                self._solve(row + 1)
                self.remove([row, col])
                self.PATH.pop()

    def solve(self):
        """Solve NQueens problem and return the PATH"""
        self._solve(0)
        return self.solutions

    def print_paths(self):
        """Print PATH with direction"""
        for path in self.solutions:
            for pos in path:
                print(pos, end=' -> ')
            print('End')

    def print_solutions(self):
        """Print all solutions"""
        for solution in self.solutions:
            print(solution)


if __name__ == '__main__':
    cb = ChessBoard(n)
    cb.solve()
    # cb.display()
    # cb.print_paths()
    cb.print_solutions()
    # print()
    # print()

# def solve(row, column):
#     solver = [[]]
#     for q in range(row):
#         solver = place_queen(q, column, solver)
#     return solver


# def place_queen(q, column, prev_solver):
#     solver_queen = []
#     for array in prev_solver:
#         for x in range(column):
#             if is_safe(q, x, array):
#                 solver_queen.append(array + [x])
#     return solver_queen


# def is_safe(q, x, array):
#     if x in array:
#         return (False)
#     else:
#         return all(abs(array[column] - x) != q - column
#                    for column in range(q))


# def n_queens():

#     the_queen = n
#     solver = solve(the_queen, the_queen)
#     for array in solver:
#         clean = []
#         for q, x in enumerate(array):
#             clean.append([q, x])
#         print(clean)


# if __name__ == '__main__':
#     n_queens()
