# Problem Statement
# https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

import sys


def max_index_diff(arr: []):
    max_on_right_so_far = -sys.maxsize
    arr_len = len(arr)

    max_on_right = [0] * arr_len

    for arr_index in range(arr_len - 1, -1, -1):
        if max_on_right_so_far < arr[arr_index]:
            max_on_right_so_far = arr[arr_index]

        max_on_right[arr_index] = max_on_right_so_far

    global_min_i = None
    global_max_j = None

    for index in range(arr_len):
        if max_on_right[index] > arr[index]:
            # while arr[index]
            pass


# driver code
def run():
    arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    max_index_diff(arr)


if __name__ == '__main__':
    run()
