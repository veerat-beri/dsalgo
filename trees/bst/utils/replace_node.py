# Problem Statement
# https://www.geeksforgeeks.org/replace-node-binary-tree-sum-inorder-predecessor-successor/


from trees.bst import LinkedBinarySearchTree, BuildLinkedBinarySearchTree
from trees.utils import Traversal


def get_tree_with_replaced_nodes(bst: LinkedBinarySearchTree):
    def _replace_tree_nodes(new_inorder: []):
        index = 0
        for node in bst.in_order():
            node.data = new_inorder[index]
            index += 1

    initial_inorder = [0] + [node.data for node in bst.in_order()] + [0]
    new_inorder = [initial_inorder[index - 1] + initial_inorder[index + 1] for index in range(1, len(initial_inorder) - 1)]

    _replace_tree_nodes(new_inorder)

    return bst


# driver code
def run():
    bst = BuildLinkedBinarySearchTree(auto_populate=True).get_tree()

    print('Before replacement: ')
    Traversal(bst).print_inorder_traversal()

    get_tree_with_replaced_nodes(bst)

    print('After replacement: ')
    Traversal(bst).print_inorder_traversal()


if __name__ == '__main__':
    run()
