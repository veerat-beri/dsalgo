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


def get_reverse_of_num(num: int):
    # dup_num = num
    # sum = 0
    # while dup_num:
    #     rem = dup_num % 10
    #     dup_num = dup_num // 10
    #     sum = sum + rem
    # return sum
    pass


def is_num_pallindrome(num: int):
    # Method 1
    str_repr_of_num = str(num)
    len_str_repr_of_num = len(str_repr_of_num)
    index = 0
    while index < len_str_repr_of_num:
        if str_repr_of_num[index] == str_repr_of_num[len_str_repr_of_num - index - 1]:
            index += 1
            continue
        break
    if index == len_str_repr_of_num:
        return True
    return False
    ###############
    # Method 2

    ###############


def is_sum_of_digits_pallindrome(num: int):
    digits_sum = get_sum_of_digits(num)
    return is_num_pallindrome(digits_sum)


# driver code
def run():
    t = int(input())
    for _ in range(t):
        num = int(input())
        print('Yes' if is_sum_of_digits_pallindrome(num) else 'No')


if __name__ == '__main__':
    run()
    