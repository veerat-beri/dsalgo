# Problem Statement
# https://www.geeksforgeeks.org/selection-sort/

from arrays.services import swap_arr_elem


# Not Stable: Example = [2, 2, 1]
def get_sorted_arr(arr: []):
    arr_len = len(arr)
    for arr_index in range(arr_len - 1):
        min_elem_so_far_index = arr_index
        for successor_arr_index in range(arr_index + 1, arr_len):
            if arr[successor_arr_index] < arr[min_elem_so_far_index]:
                min_elem_so_far_index = successor_arr_index

        swap_arr_elem(min_elem_so_far_index, arr_index, arr)


def run():
    arr = [64, 25, 12, 22, 11, ]
    print(f'Array before sort: {arr}')
    get_sorted_arr(arr)
    print(f'Array after sort: {arr}')


if __name__ == '__main__':
    run()
