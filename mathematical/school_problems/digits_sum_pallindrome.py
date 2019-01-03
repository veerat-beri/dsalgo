# Problem Statement

# Write a program to check if the sum of digits of a given number N is a palindrome number or not.

# Input:
# The first line of the input contains T denoting the number of testcases. T testcases follow.
# Then each of the T lines contains single positive integer N denoting the value of number.
#
# Output:
# For each testcase, in a new line, output "YES" if pallindrome else "NO". (without the quotes)
#
# Constraints:
# 1 <= T <= 200
# 1 <= N <= 1000
#
# Example:
# Input:
# 2
# 56
# 98
# Output:
# YES
# NO

#############################################################################################################
# SOLUTION
#############################################################################################################


def get_sum_of_digits(num: int):
    dup_num = num
    sum = 0
    while dup_num:
        rem = dup_num % 10
        dup_num = dup_num // 10
        sum = sum + rem
    return sum

def is_sum_of_digits_pallindrome(num: int):
    pass
