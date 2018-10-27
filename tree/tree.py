

class Tree:
    class Position:
        def element(self):
            pass

    def root(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def parent(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def number_of_children(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def children(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def __len__(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def _height(self, node):
        #############
        # 1st Approach
        # if not node:
        #     return 0
        # left_subtree_height = self.height(node.left)
        # right_subtree_height = self.height(node.right)
        # return 1 + max(left_subtree_height, right_subtree_height)
        ###############
        # 2nd Approach
        if self.is_leaf(node):
            return 0
        return 1 + max(self._height(node) for node in self.children(node))
        ###############

    def is_root(self, node):
        return self.root() == node

    def is_leaf(self, node):
        return self.number_of_children(node) == 0

    def is_empty(self):
        return len(self) == 0

    def height(self, node=None):
        if not node:
            node = self.root()
        return self._height(node)


class BinaryTree(Tree):
    def left(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def right(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def sibling(self, node):
        parent_node = self.parent(node)
        if not parent_node:
            return None
        if node == self.left(parent_node):
            return self.right(parent_node)
        return self.left(parent_node)


class LinkedBinaryTree(BinaryTree):

    class BinaryTreeNode:
        def __init__(self, data, parent=None, left=None, right=None, **kwargs):
            __slots__ = '_data', '_left', '_right', '_parent'
            self._data = data
            self._left = left
            self._right = right
            self._parent = parent

    def __init__(self, *args, **kwargs):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._root

