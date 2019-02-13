# Problem Statement
# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/


from trees import LinkedBinaryTree, BuildLinkedBinaryTree
from trees.utils import print_bfs


def get_tree_from_inorder_and_preorder(inorder_path: [], preorder_path: [])-> LinkedBinaryTree:
    preorder_traversal_index = 0

    def _get_tree_from_inorder_and_preorder(inorder_path, preorder_path):
        global preorder_traversal_index
        if inorder_path:
            inorder_path_index = inorder_path.index(preorder_path[preorder_traversal_index])
            preorder_traversal_index += 1

            node = LinkedBinaryTree.get_new_node(inorder_path[inorder_path_index])
            node._left = _get_tree_from_inorder_and_preorder(inorder_path[:inorder_path_index], preorder_path)
            node._right = get_tree_from_inorder_and_preorder(inorder_path[inorder_path_index + 1:], preorder_path)
            return node

    root_node = _get_tree_from_inorder_and_preorder(inorder_path, preorder_path)
    return LinkedBinaryTree(root=root_node)


# driver code
def run():
    inorder_path = ['D', 'B', 'E', 'A', 'F', 'C', ]
    preorder_path = ['A', 'B', 'D', 'E', 'C', 'F', ]
    # binary_tree = get_tree_from_inorder_and_preorder(inorder_path, preorder_path)
    sample_bt = BuildLinkedBinaryTree(list_of_nodes=['a', 'b', 'c', 'd', 'e', 'f']).get_tree()

    for node in sample_bt.pre_order():
        print(sample_bt.element(node), end=' ')


if __name__ == '__main__':
    run()
