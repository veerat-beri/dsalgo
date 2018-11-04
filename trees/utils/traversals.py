# Problem Statement
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

from trees.build_tree import BuildLinkedBinaryTree


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(auto_populate=True).build()

    # Pre-order Traversal
    print('\nPre order Traversal: ')
    for node in binary_tree.pre_order():
        print(binary_tree.element(node), end=' ')

    # In-order Traversal
    print('\nIn order Traversal: ')
    for node in binary_tree.in_order():
        print(binary_tree.element(node), end=' ')

    # Post-order Traversal
    print('\nPost order Traversal: ')
    for node in binary_tree.post_order():
        print(binary_tree.element(node), end=' ')

    # Post-order Traversal
    print('\nBreadth First Traversal: ')
    for node in binary_tree.bfs():
        print(binary_tree.element(node), end=' ')


if __name__ == '__main__':
    run()


