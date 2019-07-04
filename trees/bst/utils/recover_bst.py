# Problem Statement
# https://leetcode.com/articles/recover-binary-search-tree/


from trees import BuildLinkedBinaryTree
from trees.bst import LinkedBinarySearchTree
from trees.utils import Traversal


class RecoverBST:
    def __init__(self, incorrect_bst: LinkedBinarySearchTree):
        self.incorrect_bst = incorrect_bst

    def _set_swap_nodes(self, node):
        previous_node = None
        swap_node_1 = None
        swap_node_2 = None

        def _using_recursive(node):
            if node is None:
                return

            _using_recursive(self.incorrect_bst.left(node))

            if previous_node:
                is_not_bst = previous_node.data > node.data
                if is_not_bst:
                    if not swap_node_1:
                        swap_node_1 = previous_node
                    elif not swap_node_2:
                        swap_node_2 = node

            self.previous_node = node
            _using_recursive(self.incorrect_bst.right(node))

    def get_swapped_nodes(self):
        self._set_swap_nodes(self.incorrect_bst.root())
        self.swap_node_2.data, self.swap_node_1.data = self.swap_node_1.data, self.swap_node_2.data


# driver code
def run():
    bst = BuildLinkedBinaryTree().get_tree()
    bst._root = bst.get_new_node(1)
    bst._root._left = bst.get_new_node(3)
    bst._root._left._right = bst.get_new_node(2)

    print('Initial', end=' ')
    Traversal(bst).print_inorder_traversal()
    RecoverBST(bst).get_swapped_nodes()
    print('After swapping incorrect nodes', end=' ')
    Traversal(bst).print_inorder_traversal()


if __name__ == '__main__':
    run()
