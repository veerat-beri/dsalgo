

# Problem Statement
# https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
def check_zero_sum_subarray_exists(arr):
    prefix_sum = set()
    arr_sum_till_point = 0

    # To handle case like: [4, -2, -1, -1, -1], where prefix sum is itself zero.
    prefix_sum.add(0)

    for elem in arr:
        arr_sum_till_point += elem
        if arr_sum_till_point in prefix_sum:
            return True
        prefix_sum.add(arr_sum_till_point)
    return False


# Problem Statement
# https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/
def get_zero_sum_subarray(arr):
    indexed_prefix_sum = {}
    arr_sum_till_point = 0
    max_length_zero_sum_subarray_indexes = ()
    zero_sum_subarray_max_length = 0
    for index in range(len(arr)):
        arr_sum_till_point += arr[index]
        if arr_sum_till_point == 0:
            zero_sum_subarray_max_length = index + 1
            max_length_zero_sum_subarray_indexes = (0, index)

        if arr_sum_till_point in indexed_prefix_sum:
            if zero_sum_subarray_max_length < index - indexed_prefix_sum[arr_sum_till_point]:
                zero_sum_subarray_max_length = index - indexed_prefix_sum[arr_sum_till_point]
                max_length_zero_sum_subarray_indexes = (indexed_prefix_sum[arr_sum_till_point] + 1, index)

        elif arr_sum_till_point != 0:
            indexed_prefix_sum[arr_sum_till_point] = index
    return zero_sum_subarray_max_length, max_length_zero_sum_subarray_indexes


# driver code
def run():
    # arr = [1, 1, 0, 0, ]
    # arr = [4, -2, -1, -1, -1, 1]
    arr = [15, -2, 2, -1, 1, 10, -5, -3, -1, -1, 0, ]
    # arr = [15, -2, 2, -1, 1, 20, 10, -5, -3, -1, -1, 0, ]

    ###############
    # Check whether zero sum sub-array exists or not

    # do_zero_sum_subarray_exists = check_zero_sum_subarray_exists(arr)
    # message = 'Sub-array with zero sum ' + ('exists' if do_zero_sum_subarray_exists else 'do not exists')
    # print(message)
    ###############

    subarray_length, subarray_indexes = get_zero_sum_subarray(arr)
    if subarray_length:
        print(f'Max Length({subarray_length}) Sub-array with zero sum: ', arr[subarray_indexes[0]: subarray_indexes[1] + 1], sep='\n')
    else:
        print('Sub-array with zero sum do not exists!')


if __name__ == '__main__':
    run()