from collections import deque

from trees.decorators import set_default_node


class Tree:
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

    def root(self):
        raise NotImplementedError('Has to be Implemented by sub class')

    def num_children(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def children(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def element(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def is_root(self, node):
        return self.root() == node

    def is_leaf(self, node):
        ###############
        # 1st Approach
        return not (node._left is None or node._right is None)
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

    def _make_node(self, node_data):
        raise NotImplementedError('Has to be Implemented by sub class')


class BinaryTreeTraversalMixin:
    def _subtree_preorder(self, node):
        ###############
        # 1st Approach
        yield node
        for child in self.children(node):
            for other_node in self._subtree_preorder(child):
                yield other_node
        ###############
        # 2nd Approach
        # if node is None:
        #     return None
        #
        # yield node
        # self._subtree_preorder(self.left(node))
        # self._subtree_preorder(self.right(node))
        ###############

    def _subtree_postorder(self, node):
        ###############
        # 1st Approach
        for child in self.children(node):
            for other_node in self._subtree_preorder(child):
                yield other_node
        yield node
        ###############
        # 2nd Approach
        # if node is None:
        #     return None
        #
        # self._subtree_postorder(self.left(node))
        # self._subtree_postorder(self.right(node))
        # yield node
        ###############

    def _subtree_inorder(self, node):
        ###############
        # 1st Approach
        if self.left(node):
            for other_node in self._subtree_preorder(self.left(node)):
                yield other_node
        yield node
        if self.right(node):
            for other_node in self._subtree_preorder(self.right(node)):
                yield other_node
        ###############
        # 2nd Approach
        # if node is None:
        #     return None
        #
        # self._subtree_inorder(self.left(node))
        # yield node
        # self._subtree_inorder(self.right(node))
        ###############

    # @set_default_node
    def pre_order(self, node=None):
        if node is None:
            node = self.root()

        print(node._data)
        if node is not None:
            for node in self._subtree_preorder(node):
                yield node

    @set_default_node
    def in_order(self, node=None):
        if node is not None:
            for node in self._subtree_inorder(node):
                yield node

    @set_default_node
    def post_order(self, node=None):
        if node is not None:
            for node in self._subtree_postorder(node):
                yield node

    @set_default_node
    def bfs(self, node):
        bfs_queue = deque()
        bfs_queue.append(node)

        while bfs_queue:
            node = bfs_queue.popleft()
            yield node
            ###############
            # 1st Approach
            # left_child = self.left(node)
            # right_child = self.right(node)
            # if left_child is not None:
            #     bfs_queue.append(left_child)
            # if right_child is not None:
            #     bfs_queue.append(right_child)
            ###############
            # 2nd Approach
            for child in self.children(node):
                bfs_queue.append(child)
            ###############


class BinaryTree(BinaryTreeTraversalMixin, Tree):
    class BinaryTreeNode:
        def __init__(self):
            raise NotImplementedError('Has to be Implemented by sub class')

    def left(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def right(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def sibling(self, node):
        raise NotImplementedError('Has to be Implemented by sub class')

    def children(self, node):
        """Generates an iteration of Children of node"""
        if node._left is not None:
            yield self.left(node)
        if node._right is not None:
            yield self.right(node)


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
        self._root = self._make_node(node_data)
        return self._root

    def _add_left(self, node: BinaryTreeNode, new_node_data):
        if node._left is not None:
            raise ValueError('Left child exists')
        node._left = self._make_node(new_node_data)
        self._size += 1
        return node._left

    def _add_right(self, node: BinaryTreeNode, new_node_data):
        if node._right is not None:
            raise ValueError('Right child exists')
        node._right = self._make_node(new_node_data)
        self._size += 1
        return node._right

    def _replace(self, node: BinaryTreeNode, new_data):
        """Replace the element of node with new_data, and return old data."""
        old_data = node._data
        node._data = new_data
        return old_data

    # def _delete(self, node: BinaryTreeNode):
    #     if self.is_leaf(node)

    def _make_node(self, node_data):
        return self.BinaryTreeNode(node_data)

    def _num_descendants(self, node: BinaryTreeNode):
        if node is None:
            return 0

        left_subtree_nodes = self._num_descendants(self.left(node))
        right_subtree_nodes = self._num_descendants(self.right(node))

        return 1 + left_subtree_nodes + right_subtree_nodes

    def _sibling(self, root: BinaryTreeNode, sibling_node_data):
        if root is None:
            return
        if self.element(self.left(root)) == sibling_node_data:
            return self.right(root)
        if self.element(self.right(root)) == sibling_node_data:
            return self.left(root)
        return self._sibling(self.left(root), sibling_node_data) or self._sibling(self.right(root), sibling_node_data)

    def _is_sibling(self, root: BinaryTreeNode, node_1_data, node_2_data) -> bool:
        """Return True if node_1 is sibling of node_2"""
        if root is None:
            return False
        if (self.element(self.left(root)), self.element(self.right(root))) == (node_1_data, node_2_data) or \
                (self.element(self.left(root)), self.element(self.right(root))) == (node_2_data, node_1_data):
            return True
        return self._is_sibling(self.left(root), node_1_data, node_2_data) or \
            self._is_sibling(self.right(root), node_1_data, node_2_data)

    def root(self):
        return self._root

    def right(self, node):
        return node._right

    def left(self, node):
        return node._left

    def element(self, node: BinaryTreeNode):
        if node is not None:
            return node._data

    def num_children(self, node):
        no_of_children = 0
        ###############
        # 1st Approach
        # if node._left is not None:  # left child exists
        #     no_of_children += 1
        #
        # if node._right is not None:  # right child exists
        #     no_of_children += 1
        #
        ###############
        # 2nd Approach
        for _ in self.children(node):
            no_of_children += 1
        ###############
        return no_of_children

    @set_default_node
    def num_descendants(self, node=None):
        # if not node:
        #     node = self.root()
        return self._num_descendants(node)

    def is_sibling(self, node_1_data, node_2_data) -> bool:
        if self.root():
            if self.element(self.root()) == node_1_data or self.element(self.root()) == node_2_data:
                return False
        return self._is_sibling(self.root(), node_1_data, node_2_data)

    def sibling(self, sibling_node_data):
        if self.root():
            if self.element(self.root()) == sibling_node_data:
                return
        return self._sibling(self.root(), sibling_node_data)

    def add_root(self, node_data):
        return self._add_root(node_data)

    def add_left_child(self, parent_node: BinaryTreeNode, new_node_data):
        return self._add_left(parent_node, new_node_data)

    def add_right_child(self, parent_node: BinaryTreeNode, new_node_data):
        return self._add_right(parent_node, new_node_data)


class LinkedBinaryTreeWithParent(LinkedBinaryTree):

    class BinaryTreeNode(LinkedBinaryTree.BinaryTreeNode):
        def __init__(self, data, left=None, right=None, parent=None, **kwargs):
            super().__init__(data, left, right)
            __slots__ = '_parent'
            self._parent = parent

    def _add_left(self, node: BinaryTreeNode, new_node_data):
        raise NotImplementedError('Has to be Implemented by this class')

    def _add_right(self, node: BinaryTreeNode, new_node_data):
        raise NotImplementedError('Has to be Implemented by this class')

    def _delete(self, node: BinaryTreeNode):
        raise NotImplementedError('Has to be Implemented by this class')

    def parent(self, node: BinaryTreeNode):
        return node._parent

    def sibling(self, node):
        parent_node = self.parent(node)
        if not parent_node:
            return None
        if node == self.left(parent_node):
            return self.right(parent_node)
        return self.left(parent_node)
