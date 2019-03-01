from trees import BuildLinkedBinaryTree
from trees.bst.bst import LinkedBinarySearchTree


class BuildLinkedBinarySearchTree(BuildLinkedBinaryTree):
    def _get_tree_instance(self, root_node):
        if root_node is None:
            return LinkedBinarySearchTree()
        return LinkedBinarySearchTree(root=root_node)

    def _get_list_of_nodes(self, list_of_nodes, auto_populate):
        if list_of_nodes is None:
            list_of_nodes = []
        return ([8, 3, 10, 1, 6, 14, 4, 7, 13, ] if auto_populate else []) + list_of_nodes

    def _build_tree(self):
        if self.list_of_nodes:
            for node_data in self.list_of_nodes:
                self._tree.insert_node(node_data)