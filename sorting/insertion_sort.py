# Problem Statement
#

from arrays.services import swap_arr_elem


def get_sorted_arr(arr: []):
    arr_len = len(arr)

    for arr_index in range(1, arr_len):
        # More Swaps
        # test_elem_index = arr_index
        # while test_elem_index and arr[test_elem_index - 1] > arr[test_elem_index]:
        #     swap_arr_elem(test_elem_index - 1, test_elem_index, arr)
        #     test_elem_index -= 1
        ##############################
        # Less Swaps
        comparator_elem = arr[arr_index]
        test_elem_index = arr_index - 1
        while test_elem_index >= 0 and arr[test_elem_index] > comparator_elem:
            arr[test_elem_index + 1] = arr[test_elem_index]
            test_elem_index -= 1
        arr[test_elem_index + 1] = comparator_elem
        ##############################


# driver code
def run():
    arr = [64, 25, 12, 22, 11, ]
    print(f'Array before sort: {arr}')
    get_sorted_arr(arr)
    print(f'Array after sort: {arr}')


if __name__ == '__main__':
    run()
