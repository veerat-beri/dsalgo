# Problem Statement
# https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

import sys


# Time Complexity: O(4N)
# Space Complexity: O(2N)
def get_max_index_diff(arr: []):
    arr_len = len(arr)

    max_on_right = [0] * arr_len
    max_on_right[-1] = arr[arr_len - 1]
    max_on_right_so_far = arr[arr_len - 1]

    for arr_index in range(arr_len - 2, -1, -1):
        if max_on_right_so_far < arr[arr_index]:
            max_on_right_so_far = arr[arr_index]
        max_on_right[arr_index] = max_on_right_so_far

    min_on_left = [0] * arr_len
    min_on_left[0] = arr[0]
    min_on_left_so_far = arr[0]

    for arr_index in range(1, arr_len):
        if min_on_left_so_far > arr[arr_index]:
            min_on_left_so_far = arr[arr_index]
        min_on_left[arr_index] = min_on_left_so_far

    index_i, index_j = 0, 0
    max_index_diff = -sys.maxsize

    while index_i < arr_len and index_j < arr_len:
        if min_on_left[index_i] < max_on_right[index_j]:
            if max_index_diff < index_j - index_i:
                max_index_diff = index_j - index_i
            index_j += 1
        else:
            index_i += 1

    return max_index_diff


# driver code
def run():
    arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    # arr.sort(reverse=True)
    print(f'Given array: {arr}')
    result = get_max_index_diff(arr)
    if result > 0:
        print(f'Max j-i where arr[j] > arr[i] is: {result}')
    else:
        print('No such indexes exists')


if __name__ == '__main__':
    run()
