# Problem Statement

# Given the first 2 terms A and B of an Arithmetic Series, tell the Nth term of the series.
#
# Input:
# First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case in
# its first line should contain two positive integer A and B(First 2 terms of AP). In the second line of
# every test case it contains of an integer N.
#
# Output:
# For each testcase, in a new line, print the Nth term of the Arithmetic Progression.
#
# Constraints:
# 1 <= T <= 30
# -100 <= A <= 100
# -100 <= B <= 100
# 1 <= N <= 100
#
# Example:
# Input:
# 2
# 2 3
# 4
# 1 2
# 10
# Output:
# 5
# 10

#############################################################################################################
# SOLUTION
#############################################################################################################


def find_nth_term(a1, a2, n: int):
    d = a2 - a1
    return a1 + (n - 1) * d


# driver code
def run():
    total_test_cases = int(input())
    for test_case in range(total_test_cases):
        a1, a2 = map(int, input().strip().split())
        n = int(input())
        print(find_nth_term(a1, a2, n))


if __name__ == '__main__':
    run()