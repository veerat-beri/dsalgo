# Problem Statement
# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
from trees.tree import BinaryTree
from trees.utils import print_bfs


def get_tree_from_inorder_and_preorder(inorder_path: [], preorder_path: [])-> BinaryTree:
    def _get_tree_from_inorder_and_preorder():
        for node_data in preorder_path:
            inorder_path_index = inorder_path.index(node_data)
            node =

    root_node = _get_tree_from_inorder_and_preorder()


# driver code
def run():
    inorder_path = ['D', 'B', 'E', 'A', 'F', 'C', ]
    preorder_path = ['A', 'B', 'D', 'E', 'C', 'F', ]
    binary_tree = get_tree_from_inorder_and_preorder(inorder_path, preorder_path)
    print_bfs(binary_tree)


if __name__ == '__main__':
    run()
