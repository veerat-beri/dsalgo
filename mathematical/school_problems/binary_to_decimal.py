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
import sys
from typing import Union

from mathematical.bit_manipulations.services import get_binary_repr


class DecimalToBinary:
    def __init__(self, bin_num: Union[str, int]):
        self.bin_num = bin_num

    # For small range numbers
    def _get_decimal_from_binary(self):
        digit_index = 0
        decimal_num = 0
        while self.bin_num:
            rem = self.bin_num % 10
            self.bin_num //= 10
            decimal_num += (1 << digit_index) * rem
            digit_index += 1
        return decimal_num

    def _get_decimal_from_binary_in_str(self):
        bin_num_len = len(self.bin_num)
        for str_index in range(bin_num_len - 1, -1, -1):
            self.bin_num[str_index] * (1 << (bin_num_len - 1 - str_index))
            pass

    def get_decimal_from_binary(self):
        # return self._get_decimal_from_binary() if len(self.bin_num) <= len(get_binary_repr(sys.maxsize)) else self._get_decimal_from_binary_in_str()
        return self._get_decimal_from_binary_in_str()


# driver code
def run():
    total_test_cases = int(input())
    for _ in range(total_test_cases):
        # Method 1
        ###############
        print(DecimalToBinary(int(input())).get_decimal_from_binary())
        ###############
        # Method 2
        ###############
        # print(int('{:b}'.format(int(input()))))
        ###############


if __name__ == '__main__':
    run()
