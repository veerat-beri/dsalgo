# Problem Statement
# https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/


from collections import namedtuple

from heaps.heap import ManualMinHeap, CustomNodeMinHeap


def get_kth_smallest_in_sorted_2d_arr(arr: [], k: int, total_rows: int, total_cols: int):
    assert arr, 'Array can not be empty'
    assert k <= total_cols * total_rows, 'K should be in range of total array elements'

    heap_node = namedtuple('heap_node', ['data', 'arr_row', 'arr_col'])

    def _get_new_node(data: int, arr_row: int, arr_col: int):
        return heap_node(data, arr_row, arr_col)

    def _get_processed_row():
        heap_arr = [_get_new_node(arr[0][col_index], 0, col_index) for col_index in range(len(arr[0]))]
        return heap_arr

    heap = CustomNodeMinHeap(_get_processed_row())

    for _ in range(k - 1):
        smallest_node = heap.pop()
        try:
            pushing_elem_row = smallest_node.arr_row + 1
            pushing_elem_col = smallest_node.arr_col
            heap.push(_get_new_node(arr[pushing_elem_row][pushing_elem_col], pushing_elem_row, pushing_elem_col))
        except IndexError:
            continue

    return heap.pop().data


# driver code
def run():
    arr = [
        [10, 20, 30, 40, ],
        [15, 25, 35, 45, ],
        [24, 29, 37, 48, ],
        [32, 33, 39, 50, ],
    ]
    k = 7
    kth_smallest_node = get_kth_smallest_in_sorted_2d_arr(arr, k)
    if kth_smallest_node:
        print(f'Kth({k}) smallest elem in given sorted 2D arr is: {kth_smallest_node[0]}')
    else:
        print('No Kth({k}) smallest elem exists')


if __name__ == '__main__':
    run()
