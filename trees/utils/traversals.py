# Problem Statement
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

from trees.build_tree import BuildLinkedBinaryTree
from trees.tree import BinaryTree


def print_bfs(binary_tree):
    current_node_level = 0
    for (node, node_level) in binary_tree.bfs():
        if node_level > current_node_level:
            print('\n=============')
            current_node_level = node_level
        print(binary_tree.element(node), end=' ')
    print('\n')


##########################################################################################
# Problem Statement
# https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/

def diagonal_traversal(binary_tree: BinaryTree) -> list:
    diagonal_nodes = {}
    diagonal_level = 0

    def _diagonal_traversal(node: BinaryTree.BinaryTreeNode, diagonal_level):
        if node is None:
            return None

        diagonal_nodes_list = diagonal_nodes.get(diagonal_level, [])
        diagonal_nodes_list.append(node)
        diagonal_nodes[diagonal_level] = diagonal_nodes_list

        _diagonal_traversal(binary_tree.left(node), diagonal_level + 1)
        _diagonal_traversal(binary_tree.right(node), diagonal_level)

    _diagonal_traversal(binary_tree.root(), diagonal_level)

    for diagonal_level, level_nodes_list in diagonal_nodes.items():
        yield level_nodes_list

##########################################################################################


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[8, 3, 10, ]).get_tree()

    ###############
    # Build Tree
    root = binary_tree.root()
    root_left = binary_tree.left(root)
    root_right = binary_tree.right(root)

    root_right_right = binary_tree.add_right_child(root_right, 14)
    root_right_left = binary_tree.add_left_child(root_right, 6)

    binary_tree.add_left_child(root_right_left, 4)
    binary_tree.add_right_child(root_right_left, 7)

    binary_tree.add_left_child(root_right_right, 13)
    binary_tree.add_left_child(root_left, 1)

    ###############
    # binary_tree = BuildLinkedBinaryTree(list_of_nodes=['60', '70', ], auto_populate=True).get_tree()

    # Pre-order Traversal
    print('\n\nPre order Traversal: ')
    for node in binary_tree.pre_order():
        print(binary_tree.element(node), end=' ')

    # In-order Traversal
    print('\n\nIn order Traversal: ')
    for node in binary_tree.in_order():
        print(binary_tree.element(node), end=' ')

    # Post-order Traversal
    print('\n\nPost order Traversal: ')
    for node in binary_tree.post_order():
        print(binary_tree.element(node), end=' ')

    # Level-order Traversal
    print('\n\nBreadth First Traversal: ')
    print_bfs(binary_tree)

    # Diagonal Traversal
    print('Diagonal Traversal: ')
    for diagonal_nodes_list in diagonal_traversal(binary_tree):
        print([node.data for node in diagonal_nodes_list])


if __name__ == '__main__':
    run()


