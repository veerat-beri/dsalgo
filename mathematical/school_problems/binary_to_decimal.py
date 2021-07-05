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

# OR https://www.geeksforgeeks.org/program-binary-decimal-conversion/
#############################################################################################################
# SOLUTION
#############################################################################################################
from typing import Union


class BinaryDecimalConversion:
    # For small range numbers
    def _get_decimal_from_binary(self, bin_num: int):
        assert type(bin_num), int
        print('Using input as int')
        digit_index = 0
        decimal_num = 0
        while bin_num:
            rem = bin_num % 10
            bin_num //= 10
            decimal_num += (1 << digit_index) * rem
            digit_index += 1
        return decimal_num

    def _get_decimal_from_binary_in_str(self, bin_num: str):
        assert type(bin_num), str
        print('Using input as string')
        decimal_num = 0
        bin_num_len = len(bin_num)
        for str_index in range(bin_num_len - 1, -1, -1):
            decimal_num += int(bin_num[str_index]) * (1 << (bin_num_len - 1 - str_index))
        return decimal_num

    def get_decimal_from_binary(self, num: Union[str, int]):
        return self._get_decimal_from_binary_in_str(num) if type(num) == str else self._get_decimal_from_binary(num)


# driver code
def run():
    total_test_cases = int(input())
    for _ in range(total_test_cases):
        bin_num = input()
        # Method 1
        ###############
        print(BinaryDecimalConversion().get_decimal_from_binary(int(bin_num)))
        ###############
        # Method 2
        ###############
        # print(int('{:b}'.format(int(input()))))
        ###############
        # Method 3
        ###############
        # print(int(bin_num, 2))
        ###############


if __name__ == '__main__':
    run()
