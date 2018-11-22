# Problem statement
# https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/


def get_every_subarray_distinct_count(arr, subarray_window_size):
    current_subarray_elem_count = {}
    if len(arr) < subarray_window_size:
        raise Exception('Array size is less than window size!')

    current_subarray_distinct_count = 0
    for index in range(subarray_window_size):
        if current_subarray_elem_count.get(arr[index]):
            current_subarray_elem_count[arr[index]] += 1
        else:
            current_subarray_elem_count[arr[index]] = 1
            current_subarray_distinct_count += 1


        