from trees import BinaryTree


class ArraySegmentTree(BinaryTree):
    class ArraySegmentTreeNode(BinaryTree.BinaryTreeNode):
        def __init__(self, low, high, data):
            __slots__ = '_low', '_high', '_data'
            self._low = low
            self._high = high
            self._data = data

        @property
        def data(self):
            return self._data

        @property
        def low(self):
            return self._low

        @property
        def high(self):
            return self._high

    @staticmethod
    def get_size_from_tree_height(tree_height: int):
        return pow(2, tree_height + 1) - 1

    def create_node(self, low, high, data):
        return self.ArraySegmentTreeNode(low, high, data)

    def __len__(self):
        return self._size

    def __init__(self, **kwargs):
        self._size = kwargs.get('size', 1)
        self.list_of_nodes = [None] * len(self)





