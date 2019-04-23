# Problem Statement
# https://www.geeksforgeeks.org/merge-k-sorted-arrays/

from collections import namedtuple
from math import ceil

from heaps.heap import CustomNodeMinHeap


class MergeKSortedArrays:
    def __init__(self, arr: [], k: int):
        self.arr = arr
        self.k = k
        self.heap_node = namedtuple('heap_node', ['data', 'arr_row', 'arr_col'])

    def _get_new_node(self, data: int, arr_row: int, arr_col: int):
        return self.heap_node(data, arr_row, arr_col)

    def get_heap_inst(self):
        return CustomNodeMinHeap(self._get_processed_row())

    def _get_processed_row(self):
        heap_arr = [self._get_new_node(self.arr[row_index][0], row_index, 0) for row_index in range(self.k)]
        return heap_arr

    def get_pushing_node(self, popped_node):
        pushing_elem_row = popped_node.arr_row
        pushing_elem_col = popped_node.arr_col + 1
        return self._get_new_node(self.arr[pushing_elem_row][pushing_elem_col], pushing_elem_row, pushing_elem_col)

    def get_merged_arr_using_heap(self):
        heap = self.get_heap_inst()

        while not heap.is_empty():
            popped_node = heap.pop()
            yield popped_node.data
            try:
                heap.push(self.get_pushing_node(popped_node))
            except IndexError:
                continue

    def get_merged_arr_using_sort(self):
        for arr in range(ceil(self.k)):

    # Using MinBinaryHeap
    # def __get_merged_arr_using_heap(self):
    #     for node in self.get_smallest_in_sorted_2d_arr():
    #         yield node

    # Using Sorting
    # def __get_merged_arr_using_sort(self):
    #     for node in self.get_smallest_in_merged_arr():
    #         yield node

    def get_merged_array(self, use_min_heap=True):
        # executing_func = self.__get_merged_arr_using_heap if use_min_heap else self.__get_merged_arr_using_sort
        # return executing_func()
        executing_func = self.get_merged_arr_using_heap if use_min_heap else self.get_merged_arr_using_sort
        for node in executing_func():
            yield node


# driver code
def run():
    arr = [
        [1, 3, 5, 7, ],
        [2, 4, 6, 8, ],
        [0, 9, 10, 11, ],
    ]
    print('Sorted Merged array is: ')
    for arr_elem in MergeKSortedArrays(arr, 3).get_merged_array():
        print(arr_elem, end=' ')


if __name__ == '__main__':
    run()
