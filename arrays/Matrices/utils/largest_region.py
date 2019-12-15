# Problem Statement
# https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/


class BinaryMatrixRegion:
    def __init__(self, matrix, no_of_rows, no_of_cols):
        self.matrix = matrix
        self.no_of_rows = no_of_rows
        self.no_of_cols = no_of_cols

    def __get_next_valid_cells(self, row_index, col_index):
        possible_row_indexes = {row_index, }
        possible_col_indexes = {col_index, }

        if row_index + 1 < self.no_of_rows:
            possible_row_indexes.add(row_index + 1)
        if row_index - 1 >= 0:
            possible_row_indexes.add(row_index - 1)

        if col_index + 1 < self.no_of_cols:
            possible_col_indexes.add(col_index + 1)
        if col_index - 1 >= 0:
            possible_col_indexes.add(col_index - 1)

        for possible_row_index in possible_row_indexes:
            for possible_col_index in possible_col_indexes:
                if self.matrix[possible_row_index][possible_col_index] == 1 and (possible_row_index, possible_col_index) != (row_index, col_index):
                    yield possible_row_index, possible_col_index

    def __get_region_length(self, row_index, col_index, visited_cells, region_length: list):
        visited_cells.add((row_index, col_index))
        for valid_row_index, valid_col_index in self.__get_next_valid_cells(row_index, col_index):
            if (valid_row_index, valid_col_index) in visited_cells:
                continue

            region_length[0] += 1
            self.__get_region_length(valid_row_index, valid_col_index, visited_cells, region_length)

    def get_largest_region_len(self):
        max_region_length = 0
        visited_cells = set()
        for row_index in range(self.no_of_rows):
            for col_index in range(self.no_of_cols):
                if (row_index, col_index) in visited_cells or not self.matrix[row_index][col_index]:
                    continue

                cell_region_length = [1, ]
                self.__get_region_length(row_index, col_index, visited_cells, cell_region_length)
                max_region_length = max(max_region_length, cell_region_length[0])

        return max_region_length


# driver code
def run():
    no_of_rows = 4
    no_of_cols = 5

    input_matrix = [
        [0, 0, 1, 1, 0, ],
        [1, 0, 1, 1, 0, ],
        [0, 1, 1, 0, 0, ],
        [0, 0, 0, 1, 1, ],
    ]

    largest_region_length = BinaryMatrixRegion(input_matrix, no_of_rows, no_of_cols).get_largest_region_len()
    print(f'Largest region length for given binary matrix: {largest_region_length}')


if __name__ == '__main__':
    run()
