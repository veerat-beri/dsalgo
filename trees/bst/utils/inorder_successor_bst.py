# Problem Statement
# https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/


from base.services import assert_only_one_arg_is_present
from trees.bst import LinkedBinarySearchTree, BuildLinkedBinarySearchTree
from trees.utils import Traversal


def get_bst_inorder_successor(bst: LinkedBinarySearchTree, node: LinkedBinarySearchTree.BinaryTreeNode = None, node_data=None):
    def get_min_right_subtree_node(current_node):
        while bst.left(current_node):
            current_node = bst.left(current_node)
        return current_node

    def _get_bst_inorder_successor(given_node):
        current_node = bst.root()
        given_node_data = given_node.data
        given_node_right_ancestor = None

        while current_node:
            if given_node_data > current_node.data:
                current_node = bst.right(current_node)

            elif given_node_data < current_node.data:
                given_node_right_ancestor = current_node
                current_node = bst.left(current_node)

            else:
                break

        return given_node_right_ancestor

    given_node = node
    assert_only_one_arg_is_present('Either of Data or node must be provided', node, node_data)

    if not given_node:
        given_node = bst.get_node(node_data)
        assert given_node, 'Node with given data is not found'

    if bst.right(given_node):
        return get_min_right_subtree_node(bst.right(given_node))

    return _get_bst_inorder_successor(given_node)


# driver code
def run():
    bst = BuildLinkedBinarySearchTree(auto_populate=True).get_tree()
    node_data = 4
    # node_data = 7
    inorder_successor_node = get_bst_inorder_successor(bst, node_data=node_data)

    Traversal(bst).print_inorder_traversal()
    if inorder_successor_node:
        print(f'In-order successor of the node({node_data}): ', inorder_successor_node.data)
    else:
        print(f'In order successor of given node({node_data}) doesn\'t exists')


if __name__ == '__main__':
    run()
