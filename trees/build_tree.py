from trees.tree import LinkedBinaryTree, BinaryTree
from collections import deque


class BuildLinkedBinaryTree:
    def __init__(self, root: BinaryTree.BinaryTreeNode=None, list_of_nodes: [LinkedBinaryTree.BinaryTreeNode]=[], auto_populate=False, **kwargs):
        self.auto_populate = auto_populate
        self.list_of_nodes = list_of_nodes

        self._tree = self._create_tree(root)
        self._create_list_of_nodes()

    def _create_list_of_nodes(self):
        self.list_of_nodes = ([10, 20, 30, 40, 50, ] if self.auto_populate else []) + self.list_of_nodes

    def _create_tree(self, root_node):
        if root_node is None:
            return LinkedBinaryTree()
        return LinkedBinaryTree(root=root_node)

    def build(self):
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
                    self._tree.add_right_child(root_node, self.list_of_nodes[index])
                    index += 1
                    bfs_queue.append(self._tree.left(root_node))

        return self._tree

