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

    def __constuct_tree(self, low, high, tree_arr_index):
        tree = self._tree
        tree.list_of_nodes[tree_arr_index] = tree.create_node(low, high, sum(self.input_arr))


    def _build_tree(self):
        self.__constuct_tree()


    def get_tree(self):
        self._build_tree()
        return self._tree


