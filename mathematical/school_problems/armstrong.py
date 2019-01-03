# Problem Statement

# For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three
# digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example,
# 371 is an Armstrong number since 33 + 73 + 13 = 371
#
# Input:
# First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case contains
# a positive integer N.
#
# Output:
# For each testcase, in a new line, print "Yes" if it is a armstrong number else print "No".
#
# Constraints:
# 1 <= T <= 31
# 100 <= N < 1000
#
# Example:
# Input:
# 1
# 371
# Output:
# Yes

#############################################################################################################
# SOLUTION
#############################################################################################################


def is_armstrong(num: int):
    sum_of_digits_cubes = 0
    dup_num = num
    while dup_num:
        rem = dup_num % 10
        dup_num = dup_num // 10
        sum_of_digits_cubes = sum_of_digits_cubes + pow(rem, 3)

        if sum_of_digits_cubes > num:
            break

    if sum_of_digits_cubes == num:
        return True
    return False


# driver code
def run():
    t = int(input())
    for _ in range(t):
        if is_armstrong(int(input())):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    run()

