# Problem statement
#
import sys


def find_max_sub_array_sum(arr):
    max_sum_globally = - sys.maxsize - 1
    max_sum_till_point = - sys.maxsize - 1

    for elem in arr:
        if max_sum_till_point < 0:
            max_sum_till_point = elem
        else:
            max_sum_till_point += elem

        max_sum_globally = max(max_sum_globally, max_sum_till_point)

    return max_sum_globally


# driver code
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sub_array_sum = find_max_sub_array_sum(arr)
print('max sub-array sum: ', max_sub_array_sum)
