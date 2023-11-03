#!/usr/bin/python3
"""
NQueens: Alx interview

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
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
        self.POSITIONS = [(i, j) for i in range(n) for j in range(n)]
        self.PATH = []

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

    def is_safe(self, pos):
        """
        Check if queen can be placed at pos
        pos: tuple of (row, col)
        """
        row, col = pos
        for r, c in self.PATH:
            if r == row or c == col:
                return False
            if abs(r - row) == abs(c - col):
                return False
        return True
    
    def _solve(self):
        """
        Solve NQueens problem
        """
        if len(self.PATH) == n:
            return True
        for pos in self.POSITIONS:
            if self.is_safe(pos):
                self.insert(pos)
                self.PATH.append(pos)
                if self._solve():
                    return True
                self.remove(pos)
                self.PATH.remove(pos)
        return False

    def solve(self):
        """Solve NQueens problem and return the PATH"""
        self._solve()
        return self.PATH
    
    def print_path(self):
        """Print PATH with direction"""
        for pos in self.PATH:
            print(pos, end=' -> ')
        print('End')

    def list_path(self):
        """Return PATH"""
        print([list(s) for s in self.PATH])

cb = ChessBoard(n)
cb.solve()
# cb.display()
# cb.print_path()
cb.list_path()
