# Problem Statement
# https://leetcode.com/problems/battleships-in-a-board/

from typing import List


def should_inc_count(board, elem, current_row, current_col):
    return elem == 'X' and (current_row == 0 or board[current_row - 1][current_col] == '.') and (
            current_col == 0 or board[current_row][current_col - 1] == '.')


def count_battleships(board: List[List[str]]) -> int:
    total_battleships = 0
    current_row = 0

    if not board:
        return total_battleships

    for row in board:
        current_col = 0
        for elem in row:
            if should_inc_count(board, elem, current_row, current_col):
                total_battleships += 1
            current_col += 1
        current_row += 1

    return total_battleships


# driver code
def run():
    board = [
        ['X', '.', '.', 'X', ],
        ['.', '.', '.', 'X', ],
        ['.', '.', '.', 'X', ],
    ]

    print(f"total battleships: {count_battleships(board)}")


if __name__ == '__main__':
    run()

