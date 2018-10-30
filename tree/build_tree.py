from tree.tree import LinkedBinaryTree


class BuildLinkedBinaryTree:
    def __init(self, tree: LinkedBinaryTree=None, list_of_nodes: [LinkedBinaryTree.BinaryTreeNode]=[], auto_populate=False, **kwargs):
        self.auto_populate = auto_populate
        self.list_of_nodes = list_of_nodes
        self._tree = tree

        self._create_tree()
        self._create_list_of_nodes()

    def _create_list_of_nodes(self):
        self.list_of_nodes = ([10, 20, 30, 40, 50, ] if self.auto_populate else []) + self.list_of_nodes

    def _create_tree(self):
        if not self._tree:
            self._tree = LinkedBinaryTree()

    def build(self):
        if self.list_of_nodes:
            root_node = self._tree.add_root(self.list_of_nodes[0])
            index = 1
            while index <= len(self.list_of_nodes) - 1:
                root_node.add_left_child(self.list_of_nodes[index])
                index += 1
                root_node.add_left_child(node_data)


        return self._tree