from trees import LinkedBinaryTree
from trees.utils import print_bfs

###########################################################################
# Problem Statement
# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/


def get_bt_from_inorder_and_preorder(inorder_path: [], preorder_path: [])-> LinkedBinaryTree:
    preorder_traversal_index = 0

    def _get_bt_root_from_inorder_and_preorder(inorder_path):
        nonlocal preorder_traversal_index

        if inorder_path:
            inorder_path_index = inorder_path.index(preorder_path[preorder_traversal_index])
            preorder_traversal_index += 1

            node = LinkedBinaryTree.get_new_node(inorder_path[inorder_path_index])
            node._left = _get_bt_root_from_inorder_and_preorder(inorder_path[:inorder_path_index])
            node._right = _get_bt_root_from_inorder_and_preorder(inorder_path[inorder_path_index + 1:])
            return node

    root_node = _get_bt_root_from_inorder_and_preorder(inorder_path)
    return LinkedBinaryTree(root=root_node)

###########################################################################

# Problem Statement
# https://www.geeksforgeeks.org/full-and-complete-binary-tree-from-given-preorder-and-postorder-traversals/


def get_full_bt_from_preorder_and_postorder(preorder_path: [], postorder_path: [])-> LinkedBinaryTree:
    preorder_traversal_index = 0

    def _get_bt_root_from_preorder_and_postorder(postorder_path):
        nonlocal preorder_traversal_index
        if postorder_path:
            node = LinkedBinaryTree.get_new_node(preorder_path[preorder_traversal_index])
            preorder_traversal_index += 1

            if len(postorder_path) > 1:
                postorder_path_index = postorder_path.index(preorder_path[preorder_traversal_index])
                node._left = _get_bt_root_from_preorder_and_postorder(postorder_path[:postorder_path_index + 1])
                node._right = _get_bt_root_from_preorder_and_postorder(postorder_path[postorder_path_index + 1: -1])

            return node

    root_node = _get_bt_root_from_preorder_and_postorder(postorder_path)
    return LinkedBinaryTree(root=root_node)

###########################################################################
# Problem Statement
# https://www.geeksforgeeks.org/construct-tree-inorder-level-order-traversals/


def get_bt_from_inorder_and_levelorder(inorder_path: [], level_order_path: [])-> LinkedBinaryTree:
    def _get_bt_from_inorder_and_levelorder(inorder_path):
        pass

    root_node = _get_bt_from_inorder_and_levelorder(inorder_path)
    return LinkedBinaryTree(root=root_node)


###########################################################################

# driver code
def run():
    inorder_path = ['D', 'B', 'E', 'A', 'F', 'C', ]
    preorder_path = ['A', 'B', 'D', 'E', 'C', 'F', ]

    binary_tree = get_bt_from_inorder_and_preorder(inorder_path, preorder_path)

    print('Constructing new tree from preorder and inorder....')
    print('Preorder of new Tree constructed is:')
    for node in binary_tree.pre_order():
        print(binary_tree.element(node), end=' ')

    print('\n\nLevel order traversal of new tree is: ')
    print_bfs(binary_tree)

    ###########################################################################
    preorder_path = [1, 2, 4, 8, 9, 5, 3, 6, 7]
    postorder_path = [8, 9, 4, 5, 2, 6, 7, 3, 1]
    print('###########################################################################\nConstructing new full tree from preorder and postorder....')
    binary_tree = get_full_bt_from_preorder_and_postorder(preorder_path, postorder_path)

    print('Preorder of new Tree constructed is:')
    for node in binary_tree.pre_order():
        print(binary_tree.element(node), end=' ')

    print('\n\nLevel order traversal of new tree is: ')
    print_bfs(binary_tree)


if __name__ == '__main__':
    run()
