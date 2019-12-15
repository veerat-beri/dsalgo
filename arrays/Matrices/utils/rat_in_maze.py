# Problem Statement
# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

from arrays.services import print_matrix


class MatrixTrajectory:
    def __init__(self, matrix, no_of_rows, no_of_cols):
        self.matrix = matrix
        self.no_of_rows = no_of_rows
        self.no_of_cols = no_of_cols

    def get_next_steps(self, row_no, col_no):
        if row_no + 1 < self.no_of_rows and self.matrix[row_no + 1][col_no] == 1:
            yield row_no + 1, col_no

        if col_no + 1 < self.no_of_cols and self.matrix[row_no][col_no + 1] == 1:
            yield row_no, col_no + 1

    def get_rat_trajectory(self, row, col, result_matrix):
        if not self.matrix[row][col]:
            return 0

        # Final cell is reached
        if row == self.no_of_rows - 1 and col == self.no_of_cols - 1:
            result_matrix[row][col] = 1
            return 1

        for next_row, next_col in self.get_next_steps(row, col):
            is_path_of_part = self.get_rat_trajectory(next_row, next_col, result_matrix)
            result_matrix[row][col] = is_path_of_part
            if is_path_of_part:
                return is_path_of_part


# driver code
def run():
    no_of_rows = 4
    no_of_cols = 4
    input_matrix = [
        [1, 0, 1, 0, ],
        [1, 1, 0, 1, ],
        [0, 1, 1, 1, ],
        [1, 1, 0, 1, ],
    ]
    result_matrix = [[0] * no_of_rows for _ in range(no_of_cols)]

    print(f'Input Matrix is:')
    print_matrix(input_matrix)

    MatrixTrajectory(input_matrix, no_of_rows, no_of_cols).get_rat_trajectory(0, 0, result_matrix)

    if not result_matrix[0][0]:
        print('\nSolution does not exists')
        return

    print(f'\nSolution Matrix is:')
    print_matrix(result_matrix)


if __name__ == '__main__':
    run()
