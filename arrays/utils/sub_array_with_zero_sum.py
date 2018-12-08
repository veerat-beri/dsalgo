

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
    max_length_zero_sum_subarray = ()
    for index in range(len(arr)):
        arr_sum_till_point += arr[index]
        if arr_sum_till_point in indexed_prefix_sum:
            zero_subarray_indexes = indexed_prefix_sum[arr_sum_till_point]
            zero_subarray_indexes.append(index)
            if not max_length_zero_sum_subarray or (max_length_zero_sum_subarray[1] - max_length_zero_sum_subarray[0] <
                                                    zero_subarray_indexes[-1] - zero_subarray_indexes[0]):
                max_length_zero_sum_subarray = (zero_subarray_indexes[0], zero_subarray_indexes[-1])

        indexed_prefix_sum[arr_sum_till_point] = [index]
    return max_length_zero_sum_subarray


# driver code
def run():
    # arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    # arr = [4, -2, -1, -1, -1]
    arr = [15, -2, 2, -1, 1, 20, 10, -5, -3, -1, -1, 0, ]

    ###############
    # Check whether zero sum sub-array exists or not

    # do_zero_sum_subarray_exists = check_zero_sum_subarray_exists(arr)
    # message = 'Sub-array with zero sum ' + ('exists' if do_zero_sum_subarray_exists else 'do not exists')
    # print(message)
    ###############

    subarray_indexes = get_zero_sum_subarray(arr)
    if subarray_indexes:
        print(f'Max Length({subarray_indexes[1] - subarray_indexes[0]}) Sub-array with zero sum: ', arr[subarray_indexes[0] + 1: subarray_indexes[1] + 1], sep='\n')
    else:
        print('Sub-array with zero sum do not exists!')


if __name__ == '__main__':
    run()