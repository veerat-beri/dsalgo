# Problem Statement
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

from trees.build_tree import BuildLinkedBinaryTree


def print_bfs(binary_tree):
    current_node_level = 0
    for (node, node_level) in binary_tree.bfs():
        if node_level > current_node_level:
            print('\n=============')
            current_node_level = node_level
        print(binary_tree.element(node), end=' ')
    print('\n')


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(auto_populate=True).get_tree()

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


if __name__ == '__main__':
    run()


