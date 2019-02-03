from math import log2, ceil

from trees.segment_trees.segment_tree import ArraySegmentTree


class _BuildSegmentTree:
    pass


class BuildArraySegmentTree(_BuildSegmentTree):
    def __init__(self, arr: []=None, auto_populate=False):
        self.input_arr = self._get_input_array(arr, auto_populate)
        if len(self.input_arr) == 0:
            raise ValueError('Input Array can not be empty!')
        if not all([isinstance(arr_item, int) for arr_item in arr]):
            raise ValueError('Array Item should be Integer')

        tree_height = ceil(log2(len(self.input_arr)))
        tree_size = ArraySegmentTree.get_size_from_tree_height(tree_height)

        self._tree = ArraySegmentTree(size=tree_size)

    def _get_input_array(self, arr, auto_populate):
        if arr is None:
            arr = []
        return ([1, 2, 3, 4, 5, ] if auto_populate else []) + arr

    def _build_tree(self, low, high, tree_arr_index):
        if low >= high:
            self._tree.add_node(tree_arr_index, low, low, self.input_arr[low])
            return self.input_arr[low]

        lower_half_range_arr_sum = self._build_tree(low, ArraySegmentTree.get_range_mid(low, high), self._tree.get_left_node_index(tree_arr_index))
        upper_half_range_arr_sum = self._build_tree(ArraySegmentTree.get_range_mid(low, high) + 1, high, self._tree.get_right_node_index(tree_arr_index))

        self._tree.add_node(tree_arr_index, low, high, lower_half_range_arr_sum + upper_half_range_arr_sum)
        return lower_half_range_arr_sum + upper_half_range_arr_sum

    def get_tree(self):
        self._build_tree(0, len(self.input_arr) - 1, 0)
        return self._tree



