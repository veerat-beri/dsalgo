# Problem Statement
# https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/


from trees import LinkedBinaryTree


def diagonal_traversal(binary_tree: LinkedBinaryTree = None, bt_node: LinkedBinaryTree.BinaryTreeNode = None) -> list:
    diagonal_nodes = {}
    diagonal_level = 0

    def _diagonal_traversal(node: LinkedBinaryTree.BinaryTreeNode, diagonal_level):
        if node is None:
            return None

        diagonal_nodes_list = diagonal_nodes.get(diagonal_level, [])
        diagonal_nodes_list.append(node)
        diagonal_nodes[diagonal_level] = diagonal_nodes_list

        _diagonal_traversal(binary_tree.left(node), diagonal_level + 1)
        _diagonal_traversal(binary_tree.right(node), diagonal_level)

    assert binary_tree or bt_node, 'Neither of node or binary-tree is provided'

    _diagonal_traversal(bt_node or binary_tree.root(), diagonal_level)

    for diagonal_level, level_nodes_list in diagonal_nodes.items():
        yield level_nodes_list
