# Problem Statement
#


def print_board(board):
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=" ")
        print(end="\n")


def is_pos_feasible(row, col, board):
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
            if is_pos_feasible(row, col, board):
                board[row][col] = 1
                if _backtrack(col + 1, board):
                    return True
                board[row][col] = 0
        return False
    return _backtrack(0, board), board


def run():
    board_size = int(input("enter value of N, for N-Queen prob. = "))

    are_queens_set, board = backtrack(board_size)
    if are_queens_set:
        print('Board status after setting N queens is: ')
        print_board(board)
    else:
        print("Solution doe not exists!")


if __name__ == '__main__':
    run()
















# z=[0]
#
# print(id(z))
# a=z*5
# print(id(a))
# print(id(a[1]),id(a[2]))
# b=[a]*5
# print(id(b))
# print(id(b[1]), id (b[2]))
# #b[1][0]=1
# b[1]=[1,2,3]
# a[1]=1
# print(id(b[1]), id(b[2]))
# print(id(a[1]))
