# Problem Statement
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/


def print_board(board, board_size):
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=" ")
        print(end="\n")


def is_pos_feasible(row, col, board, board_size):
    for pos in range(col):
        if board[row][pos] == 1:
            return False
    for (rowNo, colNo) in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[rowNo][colNo]:
            return False
    for (rowNo, colNo) in zip(range(row, board_size), range(col, -1, -1)):
        if board[rowNo][colNo]:
            return False
    return True


def get_empty_board(board_size):
    return [[0] * board_size for row in range(board_size)]


def backtrack(board_size):
    board = get_empty_board(board_size)

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
    board_size = int(input("enter value of N, for N-Queen prob: "))

    are_queens_set, board = backtrack(board_size)
    if are_queens_set:
        print('Board status after setting N queens is: ')
        print_board(board, board_size)
    else:
        print("Solution doe not exists!")


if __name__ == '__main__':
    run()