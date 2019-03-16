# Problem Statement
# https://www.geeksforgeeks.org/inorder-succesor-node-binary-tree/


from trees import LinkedBinaryTree, BuildLinkedBinaryTree
from trees.utils import Traversal


def get_bt_inorder_successor(binary_tree: LinkedBinaryTree, node: LinkedBinaryTree.BinaryTreeNode = None, node_data=None):
    def get_min_right_subtree_node(current_node):
        while binary_tree.left(current_node):
            current_node = binary_tree.left(current_node)
        return current_node

    def get_bt_inorder_successor(given_node):
        given_node_data = given_node.data
        given_node_right_ancestor = None

        def _get_bt_inorder_successor(current_node)-> bool:
            nonlocal given_node_right_ancestor
            if current_node is None:
                return False

            if given_node_data == current_node.data:
                return True

            if _get_bt_inorder_successor(binary_tree.left(current_node)):
                if given_node_right_ancestor is None:
                    given_node_right_ancestor = current_node
                return True

            if _get_bt_inorder_successor(binary_tree.right(current_node)):
                return True
            return False

        _get_bt_inorder_successor(binary_tree.root())
        return given_node_right_ancestor

    given_node = node
    assert given_node or node_data, 'Either of Node or Node-data must be provided'

    if not given_node:
        given_node = binary_tree.get_node(node_data)
        assert given_node, 'Node with given data is not found'

    if binary_tree.right(given_node):
        return get_min_right_subtree_node(binary_tree.right(given_node))

    return get_bt_inorder_successor(given_node)


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(auto_populate=True, list_of_nodes=[60, 70, 80, 90, 100]).get_tree()
    node_data = 60
    inorder_successor_node = get_bt_inorder_successor(binary_tree, node_data=node_data)

    Traversal(binary_tree).print_inorder_traversal()
    if inorder_successor_node:
        print(f'In-order successor of the node({node_data}): ', inorder_successor_node.data)
    else:
        print(f'In order successor of given node({node_data}) doesn\'t exists')


if __name__ == '__main__':
    run()
