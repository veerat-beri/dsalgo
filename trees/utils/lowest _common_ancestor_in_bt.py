# Problem Statement
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
from trees import BuildLinkedBinaryTree, LinkedBinaryTree
from trees.utils import print_bfs


def get_LCA_in_BT(tree: LinkedBinaryTree, node_1_data, node_2_data):
    ###############
    # 1st Approach
    """
    Assuming both nodes are present
    :param tree: Binary Tree
    :param node_1_data: node_1
    :param node_2_data: node_2
    :return: LCA node
    """
    assert node_1_data != node_2_data, 'both nodes should be distinct'

    def _get_LCA_in_BT(node: LinkedBinaryTree.BinaryTreeNode):
        if node is None:
            return None

        if tree.element(node) == node_1_data or tree.element(node) == node_2_data:
            return node

        left_subtree = _get_LCA_in_BT(tree.left(node))
        right_subtree = _get_LCA_in_BT(tree.right(node))

        if left_subtree and right_subtree:
            return node

        return left_subtree if left_subtree else right_subtree

    return _get_LCA_in_BT(tree.root())


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[60, 70, 80, 90, 100, ], auto_populate=True).get_tree()
    node_1 = 70
    node_2 = 100
    print('Tree Level order traversal: ')
    print_bfs(binary_tree)
    print(f'LCA of {node_1} and {node_2} is: ')
    lca_node = get_LCA_in_BT(binary_tree, node_1, node_2)
    if lca_node:
        print(binary_tree.element(lca_node))
    else:
        print('No LCA exists!')


if __name__ == '__main__':
    run()
