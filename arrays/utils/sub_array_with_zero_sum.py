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


def find_zero_sum_subarray(arr):
    indexed_prefix_sum = {}
    arr_sum_till_point = 0

    for index in range(len(arr)):
        arr_sum_till_point += arr[index]
        if arr_sum_till_point in indexed_prefix_sum:
            return indexed_prefix_sum[arr_sum_till_point] + 1, index
        indexed_prefix_sum[arr_sum_till_point] = index


# driver code
def run():
    # arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    arr = [4, -2, -1, -1, -1]

    ###############
    # Check whether zero sum sub-array exists or not

    # do_zero_sum_subarray_exists = check_zero_sum_subarray_exists(arr)
    # message = 'Sub-array with zero sum ' + ('exists' if do_zero_sum_subarray_exists else 'do not exists')
    # print(message)
    ###############

    subarray_indexes = find_zero_sum_subarray(arr)
    if subarray_indexes:
        print('Sub-array with zero sum: ', arr[subarray_indexes[0]: subarray_indexes[1] + 1], sep='\n')
    else:
        print('Sub-array with zero sum do not exists!')


if __name__ == '__main__':
    run()