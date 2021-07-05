# Problem Statement
# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


########################################
# APPROACH 1
# Time Complexity: O(5*NxM) ~= O(NxM)
# Space Complexity: O(1)
########################################
from arrays.services import print_matrix


def set_zeroes(matrix: List[List[int]]) -> None:
    total_rows = len(matrix)
    total_cols = len(matrix[0])
    for col in range(total_cols):
        col_contains_0 = False

        for row in range(total_rows):
            if matrix[row][col] == 0:
                col_contains_0 = True
                break

        if col_contains_0:
            for row in range(total_rows):
                if matrix[row][col] != 0:
                    matrix[row][col] = None

    for row in range(total_rows):
        row_contains_0 = False

        for col in range(total_cols):
            if matrix[row][col] == 0:
                row_contains_0 = True
                break

        if row_contains_0:
            for col in range(total_cols):
                if matrix[row][col] != 0:
                    matrix[row][col] = None

    for row in range(total_rows):
        for col in range(total_cols):
            if matrix[row][col] is None:
                matrix[row][col] = 0


########################################
# APPROACH 2
# Time Complexity: O(2*NxM) ~= O(NxM)
# Space Complexity: O(1)
########################################
def set_zeroes_optimised(matrix: List[List[int]]) -> None:
    total_rows = len(matrix)
    total_cols = len(matrix[0])
    first_row_contains_0 = False
    first_col_contains_0 = False

    for row in range(1, total_rows):
        for col in range(1, total_cols):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    for row in range(total_rows):
        if matrix[row][0] == 0:
            first_col_contains_0 = True
            break

    for col in range(total_cols):
        if matrix[0][col] == 0:
            first_row_contains_0 = True
            break

    for row in range(1, total_rows):
        for col in range(1, total_cols):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if first_row_contains_0:
        for col in range(total_cols):
            matrix[0][col] = 0

    if first_col_contains_0:
        for row in range(total_rows):
            matrix[row][0] = 0


# driver code
def run():
    given_matrix = []

    print("Given matrix: ")
    print_matrix(given_matrix)

    exec_func = set_zeroes_optimised
    exec_func = set_zeroes_optimised
    exec_func(given_matrix)

    print("Matrix after setting 0s: ")
    print_matrix(given_matrix)


if __name__ == '__main__':
    run()
