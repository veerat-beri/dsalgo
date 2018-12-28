# Problem Statement
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/


from trees import BuildLinkedBinaryTree, LinkedBinaryTree
from trees.utils import print_bfs


def get_LCA_in_BT(tree: LinkedBinaryTree, node_1_data, node_2_data):
    """
    Also works when any of queried nodes are not present in tree.
    One tree traversal if both nodes are present in tree, or both nodes are not present in tree.
    Two traversals if one node is present and other is either not present, or the child of another queried node.

    Time Complexity: O(2N)
    Space Complexity: O(1)

    :param tree: Binary Tree
    :param node_1_data: node_1
    :param node_2_data: node_2
    :return: LCA node
    """
    assert node_1_data != node_2_data, 'both nodes should be distinct'

    is_node_1_found, is_node_2_found = False, False

    def _get_LCA_in_BT(node: LinkedBinaryTree.BinaryTreeNode):
        nonlocal is_node_1_found, is_node_2_found

        if node is None:
            return None

        if tree.element(node) == node_1_data:
            is_node_1_found = True
            return node

        if tree.element(node) == node_2_data:
            is_node_2_found = True
            return node

        left_subtree = _get_LCA_in_BT(tree.left(node))
        right_subtree = _get_LCA_in_BT(tree.right(node))

        if left_subtree and right_subtree:
            return node

        return left_subtree if left_subtree else right_subtree

    lca_node = _get_LCA_in_BT(tree.root())

    # check if both nodes exists in tree or not
    if is_node_1_found and is_node_2_found or is_node_1_found and tree.do_node_exists_in_tree(node_2_data) or is_node_2_found and tree.do_node_exists_in_tree(node_1_data):
        return lca_node

    return None


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[60, 70, 80, 90, 100, ], auto_populate=True).get_tree()
    node_1 = 30
    node_2 = 70
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
