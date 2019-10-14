# Problem statement
# https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/

from collections import defaultdict


# Time Complexity: O(N)
# Space Complexity: O(window-size)
def get_each_subarray_distinct_count(arr, subarray_window_size):
    current_subarray_elem_count = defaultdict(int)
    arr_len = len(arr)
    current_subarray_distinct_count = 0

    if arr_len < subarray_window_size:
        raise Exception('Array size is less than window size!')

    def is_current_subarray_elem_count_is_1(arr_index):
        elem = arr[arr_index]
        current_subarray_elem_count[elem] += 1
        return current_subarray_elem_count[elem] == 1

    for index in range(subarray_window_size):
        if is_current_subarray_elem_count_is_1(index):
            current_subarray_distinct_count += 1

    yield current_subarray_distinct_count

    for index in range(subarray_window_size, arr_len):
        current_subarray_elem_count[arr[index - subarray_window_size]] -= 1

        if current_subarray_elem_count[arr[index - subarray_window_size]] == 0:
            current_subarray_distinct_count -= 1

        if is_current_subarray_elem_count_is_1(index):
            current_subarray_distinct_count += 1

        yield current_subarray_distinct_count


# driver code
def run():
    window_size = 3 or 4
    arr = [1, 2, 1, 1, 4, 2, 3]
    # arr = [1, 2, 1, 3, 4, 2, 3]

    print('Given Array: ', arr)
    print(f'Distinct elements count in each sub-array of size-{window_size}, is: ')

    for dist_count in get_each_subarray_distinct_count(arr, window_size):
        print(dist_count)


if __name__ == '__main__':
    run()
