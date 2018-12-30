from trees.tree import BinaryTree


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

    @property
    def root(self):
        return self.list_of_nodes[0]

    def __len__(self):
        return self._size

    def __init__(self, **kwargs):
        self._size = kwargs.get('size', 1)
        self.list_of_nodes = [None] * len(self)

    @staticmethod
    def get_size_from_tree_height(tree_height: int):
        return pow(2, tree_height + 1) - 1

    def create_node(self, low, high, data):
        return self.ArraySegmentTreeNode(low, high, data)

    def get_left_node_index(self, node_index: int):
        left_node_index = 2 * node_index + 1
        if not left_node_index < len(self):
            raise IndexError('Left of node do not exists!')
        return left_node_index

    def get_right_node_index(self, node_index: int):
        right_node_index = 2 * node_index + 2
        if not right_node_index <= len(self):
            raise IndexError('Left of node do not exists!')
        return right_node_index

    def get_mid(self, low, high):
        return (high - low) // 2 + low
