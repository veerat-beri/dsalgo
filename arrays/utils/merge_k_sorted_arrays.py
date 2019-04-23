# Problem Statement
# https://www.geeksforgeeks.org/merge-k-sorted-arrays/

from arrays.utils.kth_smallest_row_col_sorted_2d_arr import KthSmallestUsingCustomHeap


class MergeKSortedArrays(KthSmallestUsingCustomHeap):
    def __init__(self):
    def get_pushing_node(self, popped_node):
        pushing_elem_row = popped_node.arr_row
        pushing_elem_col = popped_node.arr_col + 1
        return self._get_new_node(self.arr[pushing_elem_row][pushing_elem_col], pushing_elem_row, pushing_elem_col)

    # Using MinBinaryHeap
    def __get_merged_arr_using_heap(self):
        return self.get_kth_smallest_in_sorted_2d_arr()

    def __get_merged_arr_using_sort(self):
        pass

    def get_merged_array(self, use_min_heap=True):
        executing_func = self.__get_merged_arr_using_heap if use_min_heap else self.__get_merged_arr_using_sort
        return executing_func()


# driver code
def run():
    arr = [
        [1, 3, 5, 7, ],
        [2, 4, 6, 8, ],
        [0, 9, 10, 11, ],
    ]
    k = 3
    MergeKSortedArrays(arr, k).get_merged_array()


if __name__ == '__main__':
    run()
