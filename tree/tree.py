

class Tree:
    class Position:
        def element(self):
            pass

    def root(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def number_of_children(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def children(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def __len__(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def _height(self, node):
        ###############
        # 1st Approach
        if not node:
            return 0
        left_subtree_height = self.height(node.left)
        right_subtree_height = self.height(node.right)
        return 1 + max(left_subtree_height, right_subtree_height)
        ###############
        # 2nd Approach
        # if self.is_leaf(node):
        #     return 0
        # return 1 + max(self._height(node) for node in self.children(node))
        ###############

    def is_root(self, node):
        return self.root() == node

    def is_leaf(self, node):
        ###############
        # 1st Approach
        return not (node._left is None or node._right)
        ###############
        # 2nd Approach
        # return self.number_of_children(node) == 0
        ###############

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
        def __init__(self, data, left=None, right=None, **kwargs):
            __slots__ = '_data', '_left', '_right'
            self._data = data
            self._left = left
            self._right = right

    def __init__(self, *args, **kwargs):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def _add_root(self, node_data):
        if self._root is not None:
            raise ValueError('Root Exists')
        self._size += 1
        return self.BinaryTreeNode(node_data)

    def _add_left(self, node, new_node_data):
        if node._left is not None:
            raise ValueError('Left child exists')
        node._left = self.BinaryTreeNode(new_node_data)
        self._size += 1
        return node._left

    def _add_right(self, node, new_node_data):
        if node._right is not None:
            raise ValueError('Right child exists')
        node._right = self.BinaryTreeNode(new_node_data)
        self._size += 1
        return node._right

    def _replace(self, node: BinaryTreeNode, new_data):
        """Replace the element of node with new_data, and return old data."""
        old_data = node._data
        node._data = new_data
        return old_data

    def _delete(self, node: BinaryTreeNode):
        if self.is_leaf(node)

    def _all_children(self, node):
        if not node:
            return 0
        left_subtree_nodes = self._all_children(node._left)
        right_subtree_nodes = self._all_children(node._right)
        return 1 + left_subtree_nodes + right_subtree_nodes

    def root(self):
        return self._root

    def right(self, node):
        return node._right

    def left(self, node):
        return node._left

    def number_of_children(self, node):
        # TODO: had to cross-check this method implementation with book reference
        return self._number_of_children(node)


class LinkedBinaryTreeWithParent(LinkedBinaryTree):

    class BinaryTreeNode(LinkedBinaryTree.BinaryTreeNode):
        def __init__(self, data, left=None, right=None, parent=None, **kwargs):
            __slots__ = '_data', '_left', '_right', '_parent'
            super().__init__(data, left, right)
            self._parent = parent

    def parent(self, node: BinaryTreeNode):
        return node._parent

    def _add_left(self, node, new_node_data):
        raise NotImplementedError('Has to be Implemented by this class')

    def _add_right(self, node, new_node_data):
        raise NotImplementedError('Has to be Implemented by this class')

    def _delete(self, node):
        raise NotImplementedError('Has to be Implemented by this class')