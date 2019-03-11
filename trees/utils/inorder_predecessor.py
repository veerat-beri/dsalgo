# Problem Statement
#


from trees import LinkedBinaryTree, BuildLinkedBinaryTree
from trees.utils import Traversal


def get_bt_inorder_predecessor(binary_tree: LinkedBinaryTree, node: LinkedBinaryTree.BinaryTreeNode = None, node_data=None):
    def get_max_left_subtree_node(current_node):
        while binary_tree.right(current_node):
            current_node = binary_tree.right(current_node)
        return current_node

    def get_bt_inorder_predecessor_from_key():
        given_node_right_ancestor = None

        def _get_bt_inorder_predecessor_from_key(current_node):
            nonlocal given_node_right_ancestor

            if node_data == current_node.data:
                if binary_tree.left(current_node):
                    return get_max_left_subtree_node(current_node)
                return given_node_right_ancestor

            if binary_tree.right(current_node):
                given_node_right_ancestor = current_node
                possible_predecessor_node = _get_bt_inorder_predecessor_from_key(binary_tree.right(current_node))
                if possible_predecessor_node:
                    return possible_predecessor_node

            if binary_tree.left(current_node):
                possible_predecessor_node = _get_bt_inorder_predecessor_from_key(binary_tree.left(current_node))
                if possible_predecessor_node:
                    return possible_predecessor_node

        return _get_bt_inorder_predecessor_from_key(binary_tree.root())

    given_node = node
    assert given_node or node_data, 'Either of Node or Node-data must be provided'

    if given_node and binary_tree.right(given_node):
        return get_max_left_subtree_node(binary_tree.right(given_node))

    return get_bt_inorder_predecessor_from_key()


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(auto_populate=True, list_of_nodes=[60, 70, 80, 90, 100]).get_tree()
    node_data = 60
    inorder_predecessor_node = get_bt_inorder_predecessor(binary_tree, node_data=node_data)

    Traversal(binary_tree).print_inorder_traversal()
    Traversal(binary_tree).print_level_order_traversal()
    if inorder_predecessor_node:
        print(f'In-order predecessor of the node({node_data}): ', inorder_predecessor_node.data)
    else:
        print(f'In order predecessor of given node({node_data}) doesn\'t exists')


if __name__ == '__main__':
    run()
