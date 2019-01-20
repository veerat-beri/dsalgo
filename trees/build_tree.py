from trees.tree import LinkedBinaryTree, BinaryTree
from collections import deque


class BuildLinkedBinaryTree:
    def __init__(self, root: BinaryTree.BinaryTreeNode=None, list_of_nodes: [int]=None, auto_populate=False, **kwargs):
        self.list_of_nodes = self._get_list_of_nodes(list_of_nodes, auto_populate)
        self._tree = self._get_tree_instance(root)

    def _get_list_of_nodes(self, list_of_nodes, auto_populate):
        if list_of_nodes is None:
            list_of_nodes = []
        return ([10, 20, 30, 40, 50, ] if auto_populate else []) + list_of_nodes

    def _get_tree_instance(self, root_node):
        if root_node is None:
            return LinkedBinaryTree()
        return LinkedBinaryTree(root=root_node)

    def _build_tree(self):
        if self.list_of_nodes:
            if self._tree.is_empty():
                root_node = self._tree.add_root(self.list_of_nodes[0])
                index = 1
                bfs_queue = deque()
                bfs_queue.append(root_node)
                while index <= len(self.list_of_nodes) - 1:
                    root_node = bfs_queue.popleft()
                    self._tree.add_left_child(root_node, self.list_of_nodes[index])
                    index += 1
                    bfs_queue.append(self._tree.left(root_node))

                    if index == len(self.list_of_nodes):
                        break

                    self._tree.add_right_child(root_node, self.list_of_nodes[index])
                    index += 1
                    bfs_queue.append(self._tree.right(root_node))

    def get_tree(self):
        ###############
        # Make a simple test-tree
        #                                      10
        #                                     /  \
        #                                    20   30
        #                                   /  \
        #                                  40  50
        self._build_tree()
        return self._tree

    def get_diamond_tree(self):
        ###############
        # Make a complex test-tree
        #                                      1
        #                                     / \
        #                                    2   3
        #                                    \   /
        #                                     4 5
        #                                      \
        #                                     / 6
        #                                    7
        #
        self._tree.add_root(1)
        root_left = self._tree.add_left_child(self._tree.root(), 2)
        root_right = self._tree.add_right_child(self._tree.root(), 3)
        root_left_right = self._tree.add_right_child(root_left, 4)
        root_right_left = self._tree.add_left_child(root_right, 5)
        self._tree.add_right_child(root_left_right, 6)
        self._tree.add_left_child(root_right_left, 7)
        ###############
        return self._tree


