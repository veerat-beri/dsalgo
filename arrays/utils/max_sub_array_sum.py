# Problem statement
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

import sys


def find_max_sub_array_sum(arr):
    max_sum_globally = -sys.maxsize - 1
    max_sum_till_point = -sys.maxsize - 1

    start_index, global_end_index, global_start_index = 0, 0, 0
    for index in range(len(arr)):
        if max_sum_till_point < 0:
            max_sum_till_point = arr[index]
            start_index = index

        else:
            max_sum_till_point += arr[index]

        if max_sum_globally < max_sum_till_point:
            max_sum_globally = max_sum_till_point
            global_start_index = start_index
            global_end_index = index

        # max_sum_globally = max(max_sum_globally, max_sum_till_point)

    return global_start_index, global_end_index, max_sum_globally


# driver code
def run():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    start_index, end_index, max_sum = find_max_sub_array_sum(arr)
    print(f'Sub-array with maximum sum({max_sum}): \n{arr[start_index: end_index + 1]}')


if __name__ == '__main__':
    run()