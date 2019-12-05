def swap_arr_elem(index1: int, index2: int, arr: list):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def print_matrix(board):
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()


def create_matrix(no_of_rows=4, no_of_cols=4):
    return [[0] * no_of_cols for _ in range(no_of_rows)]
