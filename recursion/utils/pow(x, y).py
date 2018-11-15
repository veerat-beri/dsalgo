# Problem Statement
# https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/


def cal_pow(x, y):
    if y == 1:
        return x

    if y%2 == 0:
        return cal_pow()
