# Problem Statement
#

from arrays.services import swap_arr_elem


def get_sorted_arr(arr: []):
    arr_len = len(arr)

    for arr_index in range(1, arr_len):
        test_elem_index = arr_index


        print(test_elem_index)
        while test_elem_index and arr[test_elem_index - 1] < arr[test_elem_index]:
            swap_arr_elem(arr_index, test_elem_index, arr)
            test_elem_index -= 1


# driver code
def run():
    arr = [64, 25, 12, 22, 11, ]
    print(f'Array before sort: {arr}')
    get_sorted_arr(arr)
    print(f'Array after sort: {arr}')


if __name__ == '__main__':
    run()
