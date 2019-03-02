# Problem Statement
# https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/


from trees.bst.bst import LinkedBinarySearchTree
from trees.bst.build_bst import BuildLinkedBinarySearchTree


def get_bst_inorder_successor(bst: LinkedBinarySearchTree, node: LinkedBinarySearchTree.BinaryTreeNode = None, node_data=None):
    def get_minimum_right_subtree_node(current_node):
        while bst.left(current_node):
            current_node = bst.left(current_node)
        return current_node

    def _get_bst_inorder_successor(given_node):
        current_node = bst.root()
        given_node_data = given_node.data
        given_node_left_parent = None

        while current_node:
            if given_node_data > current_node.data:
                current_node = bst.left(current_node)

            elif given_node_data < current_node.data:
                given_node_left_parent = current_node.left
                current_node = current_node.left

            else:
                break

        return given_node_left_parent

    given_node = node
    assert given_node or node_data, 'Either of Node or Node-data must be provided'

    if not given_node:
        given_node = bst.get_node(node_data)
        assert given_node, 'Node with given data is not found'

    if bst.right(given_node):
        return get_minimum_right_subtree_node(bst.right(given_node))

    return _get_bst_inorder_successor(given_node)


# driver code
def run():
    bst = BuildLinkedBinarySearchTree(auto_populate=True).get_tree()
    node_data = 14
    inorder_successor_node = get_bst_inorder_successor(bst, node_data=node_data)

    if inorder_successor_node:
        print(f'In-order successor of the node({node_data}): ', inorder_successor_node.data)
    else:
        print(f'In order successor of given node({node_data}) doesn\'t exists')


if __name__ == '__main__':
    run()
