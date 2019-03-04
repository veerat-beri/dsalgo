# Problem Statement
# https://www.geeksforgeeks.org/replace-node-binary-tree-sum-inorder-predecessor-successor/
from trees.bst import LinkedBinarySearchTree


def get_tree_with_replaced_nodes(bst: LinkedBinarySearchTree):
    def _replace_tree_nodes():
        pass

    initial_inorder = [0] + list(bst.in_order()) + [0]
    new_inorder = [initial_inorder[index - 1] + initial_inorder[index + 1] for index in range(1, len(initial_inorder) - 1)]
    


