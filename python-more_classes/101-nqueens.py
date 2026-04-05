#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def solve_nqueens(n):
    """Finds all solutions for the N queens problem."""
    col = set()
    pos_diag = set()  # (row + col)
    neg_diag = set()  # (row - col)
    res = []
    board = []

    def backtrack(r):
        """Backtracking function to place queens row by row."""
        if r == n:
            res.append(board[:])
            return

        for c in range(n):
            # Kraliçanın təhlükədə olub-olmadığını yoxlayır
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # Kraliçanı yerləşdir
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board.append([r, c])

            # Növbəti sətirə keç
            backtrack(r + 1)

            # Geri çəkil (Backtrack) - başqa ehtimalları yoxlamaq üçün
            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board.pop()

    backtrack(0)
    for sol in res:
        print(sol)


if __name__ == "__main__":
    # Arqumentlərin yoxlanılması
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Proqramı başlat
    solve_nqueens(N)
