# Problem Statement
# https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

import sys


def check_zero_sum_subarray_exists(arr):
    prefix_sum = set()
    arr_sum_till_point = 0

    prefix_sum.add(0)
    for elem in arr:
        arr_sum_till_point += elem


        print(arr_sum_till_point, end=' ')
        if arr_sum_till_point in prefix_sum:
            return True
        prefix_sum.add(arr_sum_till_point)
    return False


# driver code
def run():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    do_zero_sum_subarray_exists = check_zero_sum_subarray_exists(arr)
    message = 'Sub-array with zero sum ' + ('exists' if do_zero_sum_subarray_exists else 'do not exists')
    print(message)


if __name__ == '__main__':
    run()