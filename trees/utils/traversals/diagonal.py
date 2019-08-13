# Problem Statement
# https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/


from trees import LinkedBinaryTree, BuildLinkedBinaryTree


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


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[8, 3, 10, ]).get_tree()
    root = binary_tree.root()
    root._left._left = LinkedBinaryTree.get_new_node(1)
    root._right._right = LinkedBinaryTree.get_new_node(14)
    root._right._right._left = LinkedBinaryTree.get_new_node(13)
    root._right._left = LinkedBinaryTree.get_new_node(6)
    root._right._left._left = LinkedBinaryTree.get_new_node(4)
    root._right._left._right = LinkedBinaryTree.get_new_node(7)

    for diagonal_nodes_list in diagonal_traversal(binary_tree):
        print([node.data for node in diagonal_nodes_list])


if __name__ == '__main__':
    run()
