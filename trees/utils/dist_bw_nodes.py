# Problem Statement
# https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/

from trees import LinkedBinaryTree, BuildLinkedBinaryTree
from trees.utils import get_LCA_in_BT, Traversal


# Time Complexity: O(3N)
def get_dist_bw_nodes(tree: LinkedBinaryTree, node_1_data, node_2_data):
    lca_node = get_LCA_in_BT(tree, node_1_data, node_2_data)

    if not lca_node:
        return

    lca_rooted_tree = LinkedBinaryTree(root=lca_node)
    node_1_lca_dist = 0
    node_2_lca_dist = 0

    for node, node_level in lca_rooted_tree.bfs():
        if node.data == node_1_data:
            node_1_lca_dist = node_level
            break
    for node, node_level in lca_rooted_tree.bfs():
        if node.data == node_2_data:
            node_2_lca_dist = node_level
            break

    return node_1_lca_dist + node_2_lca_dist


# driver code
def run():
    node_1 = 40
    node_2 = 60
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[60, 70, 80, 90, 100, ], auto_populate=True).get_tree()

    Traversal(binary_tree).print_inorder_traversal()
    distance = get_dist_bw_nodes(binary_tree, node_1, node_2)

    if distance:
        print(f'Distance b/w nodes {node_2} and {node_1} is: {distance}')
    else:
        print(f'One of given or both nodes {node_1} and {node_2}, do not exists in given tree')


if __name__ == '__main__':
    run()
