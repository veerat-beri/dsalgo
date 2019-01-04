# Problem Statement
# Given a Binary Number B, Print its decimal equivalent.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T
# test cases follow. Each test case contains a single Binary number B.
#
# Output:
# For each testcase, in a new line, print each Decimal number in new line.
#
# Constraints:
# 1 < T < 100
# 1 <= Digits in Binary <= 16
#
# Example:
# Input:
# 2
# 10001000
# 101100
# Output:
# 136
# 44

#############################################################################################################
# SOLUTION
#############################################################################################################


def get_decimal_from_binary(num: int):
    # Method 1 (for)
    dup_num = num
    digit_index = 0
    decimal_num = 0
    while dup_num:
        rem = dup_num % 10
        dup_num = dup_num // 10
        decimal_num += (1 << digit_index) * rem
        digit_index += 1
    return decimal_num


# driver code
def run():
    total_test_cases = int(input())
    for _ in range(total_test_cases):
        print(get_decimal_from_binary(int(input())))


if __name__ == '__main__':
    run()

