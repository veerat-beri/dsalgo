# Problem Statement
# https://leetcode.com/problems/unique-paths/

########################################
# BACKTRACKING APPROACH 1
########################################
def possible_directions(m, n, row, col):
    if row < m - 1:
        yield row + 1, col

    if col < n - 1:
        yield row, col + 1


def unique_paths(m: int, n: int) -> int:
    paths = 0

    def backtrack(curr_row, curr_col, ):
        nonlocal paths
        if (curr_col == n - 1) and (curr_row == m - 1):
            paths += 1
            return

        for path in possible_directions(m, n, curr_row, curr_col):
            backtrack(path[0], path[1])

    backtrack(0, 0)
    return paths


########################################
# BACKTRACKING APPROACH 2
########################################
def unique_paths_short(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    return unique_paths(m, n - 1) + unique_paths(m - 1, n)
########################################


########################################
# DP
########################################
def unique_paths_dp(m: int, n: int) -> int:
    matrix = [[1]*n for _ in range(m)]
    # for col in range(n):
    #     matrix[0][col] = 1
    # for row in range(m):
    #     matrix[row][0] = 1
    
    for row in range(1, m):
        for col in range(1, n):
            matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]

    return matrix[m - 1][n - 1]
########################################


# driver code
def run():
    total_rows = 3
    total_cols = 3

    executing_func = unique_paths_short
    executing_func = unique_paths
    executing_func = unique_paths_dp
    print(f"Unique paths count for matrix of size {total_rows}x{total_cols}: \n{executing_func(total_rows, total_cols)}")


if __name__ == '__main__':
    run()
