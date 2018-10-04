# Problem Statement
# https://www.geeksforgeeks.org/chocolate-distribution-problem/

import sys
min_diff = sys.maxsize


def find_min_diff_sub_array(arr, no_of_students: int):
    global min_diff

    if len(arr) < no_of_students:
        return -1

    if len(arr) == 0 or no_of_students == 0:
        return 0

    arr.sort()
    index = 0
    while index < len(arr) - no_of_students:
        extreme_indexes_diff = arr[index + no_of_students - 1] - arr[index]
        if extreme_indexes_diff < min_diff:
            min_diff = extreme_indexes_diff
        index += 1

    return min_diff


# driver code
packets_arr = [7, 3, 2, 4, 9, 12, 56]
students_count = 3
min_diff_in_chocolates_count = find_min_diff_sub_array(packets_arr, students_count)
print('Minimum difference is: ', min_diff_in_chocolates_count)
