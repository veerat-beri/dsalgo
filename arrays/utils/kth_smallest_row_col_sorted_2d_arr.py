# Problem Statement
# https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/


from collections import namedtuple
from heaps.heap import CustomNodeMinHeap


class KthSmallestUsingCustomHeap:
    def _validate_input(self, arr: [], k: int, total_rows: int, total_cols: int):
        # Input Validations
        assert arr, 'Array can not be empty'
        assert k <= total_cols * total_rows, 'K should be in range of total array elements'

    def __init__(self, arr: [], k: int, total_rows: int, total_cols: int):
        self._validate_input(arr, k, total_rows, total_cols)

        self.arr = arr
        self.k = k
        self.heap_node = namedtuple('heap_node', ['data', 'arr_row', 'arr_col'])

    def _get_new_node(self, data: int, arr_row: int, arr_col: int):
        return self.heap_node(data, arr_row, arr_col)

    def _get_processed_row(self):
        heap_arr = [self._get_new_node(self.arr[0][col_index], 0, col_index) for col_index in range(len(self.arr[0]))]
        return heap_arr

    def get_heap_inst(self):
        return CustomNodeMinHeap(self._get_processed_row())

    def get_pushing_node(self, popped_node):
        pushing_elem_row = popped_node.arr_row + 1
        pushing_elem_col = popped_node.arr_col
        return self._get_new_node(self.arr[pushing_elem_row][pushing_elem_col], pushing_elem_row, pushing_elem_col)

    def get_kth_smallest_in_sorted_2d_arr(self):
        heap = self.get_heap_inst()

        for _ in range(self.k - 1):
            popped_node = heap.pop()
            try:
                heap.push(self.get_pushing_node(popped_node))
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
    kth_smallest_node = KthSmallestUsingCustomHeap(arr, k, 4, 4).get_kth_smallest_in_sorted_2d_arr()

    # if kth_smallest_node:
    print(f'Kth({k}) smallest elem in given sorted 2D arr is: {kth_smallest_node}')
    # else:
    #     print('No Kth({k}) smallest elem exists')


if __name__ == '__main__':
    run()
