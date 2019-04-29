# Problem statement
# https://www.geeksforgeeks.org/smallest-sum-contiguous-subarray/

import sys


def get_min_sub_array_sum(arr):
    """
    Function to find the smallest sum contiguous sub-array
    :param arr: input array
    :return: start and end indexes of smallest sum sub-array.
    """
    # to store the minimum value that is ending up to the current index
    min_sum_till_point = sys.maxsize

    # to store the minimum value encountered so far
    min_sum_globally = sys.maxsize

    global_start_index, start_index, global_end_index = 0, 0, 0

    # traverse the array elements
    for index in range(len(arr)):
        # if min_sum_till_point > 0, then it could not possibly
        # contribute to the minimum sum further
        if min_sum_till_point > 0:
            min_sum_till_point = arr[index]
            start_index = index

        # else add the value sorted_arrays[index] to min_sum_till_point
        else:
            min_sum_till_point += arr[index]

        # update min_sum_globally and min sub-array indexes
        if min_sum_globally > min_sum_till_point:
            min_sum_globally = min_sum_till_point
            global_start_index = start_index
            global_end_index = index

    return global_start_index, global_end_index, min_sum_globally


# Driver code
def run():
    arr = [3, -4, 2, -3, -1, 7, -4, -3, -1, -5]
    # sorted_arrays = [2, 6, -5, 4, 1, 9]
    # sorted_arrays = [4, -1, -1, -1, -1, -1]

    start_index, end_index, min_sum = get_min_sub_array_sum(arr)
    print(f'Sub-array with minimum sum({min_sum}): \n{arr[start_index: end_index + 1]}')


if __name__ == '__main__':
    run()
