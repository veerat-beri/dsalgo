# Problem Statement
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

from arrays.services import print_matrix, create_matrix


def is_pos_feasible(row, col, board, board_size):
    for pos in range(col):
        if board[row][pos] == 1:
            return False
    for (row_no, col_no) in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[row_no][col_no]:
            return False
    for (row_no, col_no) in zip(range(row, board_size), range(col, -1, -1)):
        if board[row_no][col_no]:
            return False
    return True


def backtrack(board_size):
    board = create_matrix(board_size, board_size)

    def _backtrack(col, board):
        if col >= board_size:
            return True
        for row in range(board_size):
            if is_pos_feasible(row, col, board, board_size):
                board[row][col] = 1
                if _backtrack(col + 1, board):
                    return True
                board[row][col] = 0
        return False
    return _backtrack(0, board), board


def run():
    board_size = int(input('enter value of N, for N-Queen prob: '))

    are_queens_set, board = backtrack(board_size)
    if are_queens_set:
        print('Board status after setting N queens is: ')
        print_matrix(board)
    else:
        print('Solution doe not exists!')


if __name__ == '__main__':
    run()
