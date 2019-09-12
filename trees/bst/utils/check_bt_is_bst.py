# Problem Statement
# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

from trees import LinkedBinaryTree, BuildLinkedBinaryTree

import sys

from trees.bst import BuildLinkedBinarySearchTree
from trees.utils import Traversal


def is_bt_bst(bt: LinkedBinaryTree, use_inorder=True):
    ###########################################################################
    # Using min, max values
    # Time complexity: O(N)
    # Space complexity: O(1)
    def _use_max_min(node, MAX_VALUE = sys.maxsize, MIN_VALUE = -sys.maxsize) -> bool:
        if node is None:
            return True

        if node.data > MAX_VALUE or node.data < MIN_VALUE:
            return False

        return _use_max_min(bt.left(node), node.data - 1, MIN_VALUE) and _use_max_min(bt.right(node), MAX_VALUE, node.data + 1)

    ###########################################################################
    # Using Inorder traversal
    # Time complexity: O(N)

    previous_node_data = None

    def _use_inorder(node):
        nonlocal previous_node_data
        if node is None:
            return True

        if not _use_inorder(bt.left(node)):
            return False

        if previous_node_data and previous_node_data > node.data:
            return False

        previous_node_data = node.data

        return _use_inorder(bt.right(node))
    ###########################################################################

    executing_func = _use_inorder if use_inorder else _use_max_min
    return executing_func(bt.root())


# driver code
def run():
    # binary_tree = BuildLinkedBinaryTree(auto_populate=True).get_tree()
    binary_tree = BuildLinkedBinarySearchTree(auto_populate=True).get_tree()
    print('Given tree ', end='')

    Traversal(binary_tree).print_inorder_traversal()
    print('Given binary-tree is {}bst'.format('' if is_bt_bst(binary_tree) else 'not '))


if __name__ == '__main__':
    run()
