from pprint import pprint


def find_next_empty(sudoku):
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == -1:
                return r, c

    return None, None


def is_valid(sudoku, guess, row, col):
    row_vals = sudoku[row]
    if guess in row_vals:
        return False

    col_vals = [sudoku[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Calculates the starting indices of the row and column of the 3x3 matrix we want to look at.
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start +3):
            if sudoku[r][c] == guess:
                return False

    return True


def solve_sudoku(sudoku):
    row, col = find_next_empty(sudoku)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(sudoku, guess, row, col):
            sudoku[row][col] = guess

            if solve_sudoku(sudoku):
                return True

        # Backtracking:
        # Resets the value at our index to empty in case our guess is not valid, or didn't solve the Sudoku.
        sudoku[row][col] = -1

    return False


if __name__ == '__main__':

    sudoku_example = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(solve_sudoku(sudoku_example))
    pprint(sudoku_example)
