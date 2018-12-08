# Problem Statement
#


def print_board(board):
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=" ")
        print(end="\n")


def pos_feasible(row, col, board_status):
    for pos in range(col):
        if board_status[row][pos] == 1:
            return False
    for (rowNo, colNo) in zip(range(row,-1,-1), range(col,-1,-1)):
        if board_status[rowNo][colNo]:
            return False
    for (rowNo, colNo) in zip(range(row, board_size), range(col,-1,-1)):
        if board_status[rowNo][colNo]:
            return False
    return True


def backtrack(col, board_status):
    if col >= board_size:
        return True
    for row in range(board_size):
        if pos_feasible(row, col, board_status):
            board_status[row][col] = 1
            if backtrack(col+1, board_status):
                return True
            board_status[row][col] = 0
    return False

def driver():
    rows = cols = board_size
    board_status = [[0]*cols for row in range(rows)]
    #printSolution(board_status)
    solExist = backtrack(0, board_status)
    if solExist:
        printSolution(board_status)
    else:
        print("Solution doesn't exist")

board_size = int(input("enter value of N, for N-Queen prob. = "))
driver()
















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
