# Problem Statement
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


from trees import LinkedBinaryTree
from trees.build_tree import BuildLinkedBinaryTree
from trees.utils.traversals.diagonal_traversal import diagonal_traversal


def print_bfs(binary_tree=None, bt_node=None):
    current_node_level = 0
    assert binary_tree or bt_node, 'Neither of node or binary-tree is provided'

    for (node, node_level) in binary_tree.bfs(bt_node):
        if node_level > current_node_level:
            print('\n=============')
            current_node_level = node_level
        print(binary_tree.element(node), end=' ')
    print('\n')


class Traversal:
    def __init__(self, binary_tree: LinkedBinaryTree):
        self.binary_tree = binary_tree

    def print_inorder_traversal(self, bt_node=None):
        # In-order Traversal
        print('\nIn order Traversal: ')
        for node in self.binary_tree.in_order(bt_node):
            print(self.binary_tree.element(node), end=' ')
        print('\n')

    def print_preorder_traversal(self, bt_node=None):
        # Pre-order Traversal
        print('\nPre order Traversal: ')
        for node in self.binary_tree.pre_order(bt_node):
            print(self.binary_tree.element(node), end=' ')
        print('\n')

    def print_postorder_traversal(self, bt_node=None):
        # Post-order Traversal
        print('\nPost order Traversal: ')
        for node in self.binary_tree.post_order(bt_node):
            print(self.binary_tree.element(node), end=' ')
        print('\n')

    def print_level_order_traversal(self, bt_node=None):
        # Level-order Traversal
        print('\nBreadth First Traversal: ')
        print_bfs(self.binary_tree, bt_node)

    def print_diagonal_traversal(self, bt_node=None):
        # Diagonal Traversal (top-left to lower right diagonal)
        print('\nDiagonal Traversal: ')
        for diagonal_nodes_list in diagonal_traversal(self.binary_tree, bt_node):
            print([node.data for node in diagonal_nodes_list])
        print('\n')

    # def print_pictorial_repr(self):
    #     from collections import deque
    #
    #     left_child = 'l'
    #     right_child = 'r'
    #     root = 'b'
    #
    #     node_type_mapping = {
    #         'left_child': left_child,
    #         'right_child': right_child,
    #         'root': root
    #     }
    #
    #     def extreme_left_nodes_count(bst, node):
    #         extreme_nodes_count = 0
    #         while bst.left(node):
    #             extreme_nodes_count += 1
    #             node = bst.left(node)
    #         return extreme_nodes_count
    #
    #     def extreme_right_nodes_count(bst, node):
    #         extreme_nodes_count = 0
    #         while bst.right(node):
    #             extreme_nodes_count += 1
    #             node = bst.right(node)
    #         return extreme_nodes_count
    #
    #     @set_default_node
    #     def bfs(bst, node):
    #         nonlocal node_type_mapping
    #
    #         if node is None:
    #             raise Exception('Tree is empty!')
    #
    #         bfs_queue = deque()
    #         bfs_queue.append((node, 0, node_type_mapping['root'], None))
    #
    #         while bfs_queue:
    #             node, node_level, node_type, parent_node = bfs_queue.popleft()
    #             yield node, node_level, node_type, parent_node
    #
    #             left_child = bst.left(node)
    #             right_child = bst.right(node)
    #
    #             if left_child is not None:
    #                 bfs_queue.append((left_child, node_level + 1, node_type_mapping['left_child'], node))
    #             if right_child is not None:
    #                 bfs_queue.append((right_child, node_level + 1, node_type_mapping['right_child'], node))
    #
    #     current_node_level = 0
    #     # left_padding = 9
    #     node_space_value_mapping = {}
    #     node_spaces_in_level_so_far = {}
    #
    #     for (node, node_level, node_type, parent_node) in bfs(self.binary_tree):
    #         if node_level > current_node_level:
    #             print('\n')
    #             # left_padding -= 3 + 1
    #             current_node_level = node_level
    #         # print(self.binary_tree.element(node), end=' ')
    #
    #         if node_type == root:
    #             # left_padding += 2
    #             node_space_value = extreme_right_nodes_count(self.binary_tree, self.binary_tree.left(node)) + extreme_left_nodes_count(self.binary_tree, self.binary_tree.left(node)) + 1
    #             node_space_value = 20
    #             print(' ' * node_space_value, self.binary_tree.element(node), end='', sep='')
    #
    #         elif node_type == left_child:
    #
    #
    #
    #             # print(extreme_right_nodes_count(self.binary_tree, node))
    #             node_space_value = node_space_value_mapping[parent_node] - 2*extreme_right_nodes_count(self.binary_tree, node)
    #             print(' ' * (node_space_value - node_spaces_in_level_so_far.get(node_level, 0)), self.binary_tree.element(node), end='', sep='')
    #             node_spaces_in_level_so_far[node_level] = node_spaces_in_level_so_far.get(node_level, 0) + node_space_value
    #         else:
    #             node_space_value = node_space_value_mapping[parent_node] + extreme_left_nodes_count(self.binary_tree, node) + 1
    #             print(' ' * (node_space_value - node_spaces_in_level_so_far.get(node_level, 0)), self.binary_tree.element(node), end='', sep='')
    #             node_spaces_in_level_so_far[node_level] = node_spaces_in_level_so_far.get(node_level, 0) + extreme_left_nodes_count(self.binary_tree, node)
    #
    #         node_space_value_mapping[node] = node_space_value
    #
    #     print('\n')


# driver code
def run():
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[1, 2, 3, 4, 5, ]).get_tree()

    ###############
    # Build Tree
    root = binary_tree.root()
    # root_left = binary_tree.left(root)
    # root_right = binary_tree.right(root)
    #
    # root_right_right = binary_tree.add_right_child(root_right, 14)
    # root_right_left = binary_tree.add_left_child(root_right, 6)
    #
    # binary_tree.add_left_child(root_right_left, 4)
    # binary_tree.add_right_child(root_right_left, 7)
    #
    # binary_tree.add_left_child(root_right_right, 13)
    # binary_tree.add_left_child(root_left, 1)

    root._right._right = binary_tree.get_new_node(6)
    ###############
    # binary_tree = BuildLinkedBinaryTree(list_of_nodes=['60', '70', ], auto_populate=True).get_tree()
    # binary_tree = BuildLinkedBinaryTree(list_of_nodes=[10, 20, 30, 40, 50, 60, 70], auto_populate=True).get_tree()

    bt_traversal = Traversal(binary_tree)
    bt_traversal.print_preorder_traversal()
    bt_traversal.print_inorder_traversal()
    bt_traversal.print_postorder_traversal()
    bt_traversal.print_level_order_traversal()
    bt_traversal.print_diagonal_traversal()
    # bt_traversal.print_pictorial_repr()


if __name__ == '__main__':
    run()
