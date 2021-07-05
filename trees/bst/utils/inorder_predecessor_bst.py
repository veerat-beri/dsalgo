# Problem Statement
# https://www.geeksforgeeks.org/inorder-predecessor-successor-given-key-bst/


from trees.bst import LinkedBinarySearchTree, BuildLinkedBinarySearchTree
from trees.utils import Traversal


def get_bst_inorder_predecessor(bst: LinkedBinarySearchTree, node: LinkedBinarySearchTree.BinaryTreeNode = None, node_data=None):
    def get_max_left_subtree_node(current_node):
        while bst.right(current_node):
            current_node = bst.right(current_node)
        return current_node

    def _get_bst_inorder_predecessor(given_node):
        current_node = bst.root()
        given_node_data = given_node.data
        given_node_left_ancestor = None

        while current_node:
            if given_node_data > current_node.data:
                given_node_left_ancestor = current_node
                current_node = bst.right(current_node)

            elif given_node_data < current_node.data:
                current_node = bst.left(current_node)

            else:
                break

        return given_node_left_ancestor

    # Ref: https://algorithmsandme.com/inorder-predecessor-in-binary-search-tree/
    def get_bst_inorder_predecessor_from_key():
        possible_inorder_predecessor = None

        def _get_bst_inorder_predecessor_from_key(current_node):
            nonlocal possible_inorder_predecessor
            if current_node is None:
                return

            if current_node.data == node_data:
                if bst.left(current_node):
                    return get_max_left_subtree_node(bst.left(current_node))
                return possible_inorder_predecessor

            if node_data > current_node.data:
                possible_inorder_predecessor = current_node
                return _get_bst_inorder_predecessor_from_key(bst.right(current_node))

            return _get_bst_inorder_predecessor_from_key(bst.left(current_node))

        return _get_bst_inorder_predecessor_from_key(bst.root())

    given_node = node
    assert given_node or node_data, 'Either of Node or Node-data must be provided'

    if not given_node:
        # given_node = bst.get_node(node_data)
        # assert given_node, 'Node with given data is not found'
        return get_bst_inorder_predecessor_from_key()

    if bst.left(given_node):
        return get_max_left_subtree_node(bst.left(given_node))

    return _get_bst_inorder_predecessor(given_node)


# driver code
def run():
    bst = BuildLinkedBinarySearchTree(auto_populate=True).get_tree()
    # node_data = 4
    # node_data = 7
    node_data = 14
    inorder_predecessor_node = get_bst_inorder_predecessor(bst, node_data=node_data)

    Traversal(bst).print_inorder_traversal()
    if inorder_predecessor_node:
        print(f'In-order predecessor of the node({node_data}): ', inorder_predecessor_node.data)
    else:
        print(f'In order predecessor of given node({node_data}) doesn\'t exists')


if __name__ == '__main__':
    run()
