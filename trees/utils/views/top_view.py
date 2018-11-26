# Problem Statement
# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/

from collections import OrderedDict, deque
from trees import BuildLinkedBinaryTree, LinkedBinaryTree

# Standard Solution
# def top_view(tree: LinkedBinaryTree):
#     if tree.is_empty():
#         raise ValueError('Tree is Empty')
#
#     ###############
#     # 1st Approach: BFS
#     def _left_view(node: BinaryTree.BinaryTreeNode, traversal_level):
#         bfs_queue = deque()
#         bfs_queue.append((node, 0))
#         yield node
#
#         while bfs_queue:
#             node, node_level = bfs_queue.popleft()
#             if node_level > traversal_level:
#                 traversal_level = node_level
#                 yield node
#             ###############
#             # 1st Approach
#             # left_child = self.left(node)
#             # right_child = self.right(node)
#             # if right_child is not None:
#             #     bfs_queue.append((right_child, node_level + 1))
#             # if left_child is not None:
#             #     bfs_queue.append((left_child, node_level + 1))
#             ###############
#             # 2nd Approach
#             for child in tree.children(node):
#                 bfs_queue.append((child, node_level + 1))
#             ###############
#
#     for node in _left_view(tree.root(), 0):
#         yield node
#


# Full-proof Solution
def top_view(tree: LinkedBinaryTree, traversal_choice=LinkedBinaryTree.BFS):
    if tree.is_empty():
        raise ValueError('Tree is Empty')
    horizontal_distance_first_node = dict()

    ##############
    # 1st Approach: BFS
    def _top_view_bfs(node: LinkedBinaryTree.BinaryTreeNode, traversal_level, horizontal_distance):
        bfs_queue = deque()
        bfs_queue.append((node, traversal_level, horizontal_distance))
        horizontal_distance_first_node[horizontal_distance] = node
        while bfs_queue:
            node, node_level, node_hd = bfs_queue.popleft()

            ###############
            # First Node selection Logic
            # if node_level > traversal_level:
            #     traversal_level = node_level
            #     horizontal_distance_first_node[traversal_level] = node, node_hd

            if not horizontal_distance_first_node.get(node_hd, None):
                horizontal_distance_first_node[node_hd] = node

            ###############
            # Queue Append Logic
            left_child = tree.left(node)
            right_child = tree.right(node)
            if left_child is not None:
                bfs_queue.append((left_child, node_level + 1, node_hd - 1))
            if right_child is not None:
                bfs_queue.append((right_child, node_level + 1, node_hd + 1))
            ###############

    #############
    # 2nd Approach: DFS
    def _top_view_dfs(node: LinkedBinaryTree.BinaryTreeNode, node_level, node_hd):
        if node is None:
            return

        last_node_in_level = horizontal_distance_first_node.get(node_level)
        if last_node_in_level:
            if last_node_in_level[1] < node_hd:
                horizontal_distance_first_node[node_level] = node, node_hd
        else:
            horizontal_distance_first_node[node_level] = node, node_hd
        _top_view_dfs(tree.right(node), node_level + 1, node_hd + 1)
        _top_view_dfs(tree.left(node), node_level + 1, node_hd - 1)

    #############
    implementation_func = _top_view_bfs if traversal_choice == LinkedBinaryTree.BFS else _top_view_dfs
    implementation_func(tree.root(), 0, 0)
    for node, node_hd in horizontal_distance_first_node.values():
        yield node


# driver code
def run():
    # tree = BuildLinkedBinaryTree(auto_populate=True).build()
    # tree = BuildLinkedBinaryTree(root=root).build()
    tree = BuildLinkedBinaryTree().get_diamond_tree()

    print('Top-view: ')
    for node in top_view(tree):
        print(tree.element(node), end=' ')

    # print('\n\nBFS: ')
    # for node in tree.bfs():
    #     print(tree.element(node), end=' ')


if __name__ == '__main__':
    run()
