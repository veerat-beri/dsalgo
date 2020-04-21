# Problem Statement
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/
# https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/

from collections import defaultdict
from trees import LinkedBinaryTree, BuildLinkedBinaryTree


class VerticalTraversal:
    def __init__(self, binary_tree: LinkedBinaryTree, in_same_order=True):
        self.in_same_order = in_same_order
        self.binary_tree = binary_tree

    def _using_dfs(self, hd_nodes_mapping):
        def __update_hd_nodes_mapping(node, node_hd):
            if not node:
                return

            hd_nodes_mapping[node_hd].append(node.data)

            __update_hd_nodes_mapping(self.binary_tree.left(node), node_hd - 1)
            __update_hd_nodes_mapping(self.binary_tree.right(node), node_hd + 1)

        __update_hd_nodes_mapping(self.binary_tree.root(), 0)

    def _using_bfs(self, hd_nodes_mapping):
        for (node, _, node_hd) in self.binary_tree.bfs():
            hd_nodes_mapping[node_hd].append(node.data)

    def traverse_tree(self):
        hd_nodes_mapping = defaultdict(list)
        self._using_bfs(hd_nodes_mapping) if self.in_same_order else self._using_dfs(hd_nodes_mapping)

        for node_hd in sorted(hd_nodes_mapping):
            print(*hd_nodes_mapping[node_hd], end='\n' + '=' * 15 + '\n')


# driver code
def run():
    from trees.utils import Traversal

    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[60, 70, ], auto_populate=True).get_tree()
    Traversal(binary_tree).print_level_order_traversal()

    print(f'Vertical Order Traversal of given tree is: \n')
    VerticalTraversal(binary_tree).traverse_tree()


if __name__ == '__main__':
    run()
