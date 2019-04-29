# Problem Statement
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

from arrays import binary_search


############################################################
# O(2(log2 N)) Approach
def get_arr_elem(arr: [], key: int):
    arr_len = len(arr)

    def find_pivot(low, high):
        if low > high:
            return

        mid = (low + high) // 2

        if mid > low and arr[mid] < arr[mid - 1]:  # mid > low is required to avoid error, if low=high=0
            return mid - 1
        if mid < high and arr[mid] > arr[mid + 1]:  # mid < high is required to avoid error, if low=high=len(sorted_arrays) - 1
            return mid

        if arr[mid] <= arr[low]:
            return find_pivot(low, mid - 1)

        return find_pivot(mid + 1, high)

    pivoted_index = find_pivot(0, arr_len - 1)
    if pivoted_index:
        if arr[pivoted_index] == key:
            return pivoted_index
        if key > arr[0]:
            return binary_search(arr, 0, pivoted_index - 1, key)
        return binary_search(arr, pivoted_index + 1, arr_len - 1, key)

    return binary_search(arr, 0, arr_len - 1, key)
############################################################


# O(log2 N) Approach
def get_arr_elem_optimised(arr: [], key: int):
    def _get_arr_elem(low, high):
        if high < low:
            return

        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        # if sorted_arrays[low:mid + 1] is sorted
        if arr[mid] >= arr[low]:
            if arr[mid] > key and arr[low] <= key:
                return binary_search(arr, low, mid - 1, key)

            return _get_arr_elem(mid + 1, high)

        # sorted_arrays[mid + 1:] is sorted
        else:
            if arr[mid + 1] <= key and arr[high] >= key:
                return binary_search(arr, mid + 1, high, key)
            return _get_arr_elem(low, mid - 1)

    return _get_arr_elem(0, len(arr) - 1)
############################################################


# driver code
def run():
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    elem_index = get_arr_elem_optimised(arr, key)
    print(f'Given array: {arr}')

    if elem_index:
        print(f'Given element({key}) is found at index: {elem_index}')
    else:
        print(f'Element({key}) not found in arr')


if __name__ == '__main__':
    run()
