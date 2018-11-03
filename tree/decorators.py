from tree.tree import BinaryTree


def set_default_node(func):
    def assign_default(self, node: BinaryTree.BinaryTreeNode):
        if node is None:
            node = self.root()
        func(self, node)

    return assign_default

