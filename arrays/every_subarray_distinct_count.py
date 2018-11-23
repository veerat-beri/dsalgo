# Problem statement
# https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/


def get_every_subarray_distinct_count(arr, subarray_window_size):
    current_subarray_elem_count = {}
    arr_len = len(arr)
    if arr_len < subarray_window_size:
        raise Exception('Array size is less than window size!')

    current_subarray_distinct_count = 0
    for index in range(subarray_window_size):
        if current_subarray_elem_count.get(arr[index]):
            current_subarray_elem_count[arr[index]] += 1
        else:
            current_subarray_elem_count[arr[index]] = 1
            current_subarray_distinct_count += 1

    yield current_subarray_distinct_count

    for index in range(subarray_window_size, arr_len):
        current_subarray_distinct_count -= 1
        current_subarray_elem_count[arr[index - subarray_window_size]] -= 1

        if current_subarray_elem_count[arr[index - subarray_window_size]] == 1:
            current_subarray_distinct_count += 1

        if current_subarray_elem_count.get(arr[index]):
            current_subarray_elem_count[arr[index]] += 1
        else:
            current_subarray_elem_count[arr[index]] = 1

        if current_subarray_elem_count[arr[index]] == 1:
            current_subarray_distinct_count += 1

        yield current_subarray_distinct_count


# driver code
def run():
    window_size = 4
    arr = [1, 2, 1, 3, 4, 2, 3]
    print(f'Distinct elements count in each sub-array if size-{window_size}, is: ')
    for dist_count in get_every_subarray_distinct_count(arr, window_size):
        print('\n', dist_count)


if __name__ =='__main__':
    run()
        