# Problem Statement
# https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/
from trees import LinkedBinaryTree
from trees.utils import get_LCA_in_BT


# Time Complexity: O(N)
def get_dist_bw_nodes(tree: LinkedBinaryTree, node_1, node_2):
    lca_node = get_LCA_in_BT(tree, node_1, node_2)
    LinkedBinaryTree(tree)

# driver code
def run():
    pass


if __name__ == '__main__':
    run()
