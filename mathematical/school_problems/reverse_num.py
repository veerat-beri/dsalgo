# Problem Statement
# Write a program to reverse digits of a number N.
#
# Input:
# The first line of input contains an integer T, denoting the number of test cases. T testcases follow.
# Each test case contains an integer N.
#
# Output:
# For each test case, print the reverse digits of number N .
#
# Constraints:
# 1 ≤ T ≤ 104
# 1 ≤ N ≤ 1015
#
# Example:
# Input:
# 2
# 200
# 122
# Output:
# 2
# 221

#############################################################################################################
# SOLUTION
#############################################################################################################


def get_reverse_of_num(num: int):
    ###############
    # Method 1
    dup_num = num
    reverse_num = 0
    while dup_num:
        rem = dup_num % 10
        dup_num = dup_num // 10
        reverse_num = 10 * reverse_num + rem
    return reverse_num
    ###############
    # Method 2
    # str_repr_of_num = str(num)
    # return int(str_repr_of_num[::-1])
    ###############


# driver code
def run():
    total_test_cases = int(input())
    for _ in range(total_test_cases):
        num = int(input())
        print(get_reverse_of_num(num))


if __name__ == '__main__':
    run()

