from collections import deque

from trees.decorators import set_default_node


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
            for other_node in self._subtree_postorder(child):
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
            for other_node in self._subtree_inorder(self.left(node)):
                yield other_node
        yield node
        if self.right(node):
            for other_node in self._subtree_inorder(self.right(node)):
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

    @set_default_node
    def pre_order(self, node=None):
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
