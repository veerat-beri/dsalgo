# Problem Statement
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

from trees.build_tree import BuildLinkedBinaryTree


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(auto_populate=True).build()

    for node in binary_tree.pre_order():
        print(binary_tree.element(node), end=' ')


if __name__ == '__main__':
    run()


