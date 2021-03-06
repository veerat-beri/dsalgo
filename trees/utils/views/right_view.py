# Problem Statement
# https://www.geeksforgeeks.org/print-left-view-binary-tree/

from collections import deque, OrderedDict
from trees import BuildLinkedBinaryTree, LinkedBinaryTree

# Standard Solution
# def right_view(tree: LinkedBinaryTree):
#     if tree.is_empty():
#         raise ValueError('Tree is Empty')
#
#     ###############
#     # 1st Approach: BFS
#     def _right_view(node: LinkedBinaryTree.BinaryTreeNode, traversal_level):
#         bfs_queue = deque()
#         bfs_queue.append((node, 0))
#         yield node
#
#         while bfs_queue:
#             node, node_level = bfs_queue.popleft()
#             if node_level > traversal_level:
#                 traversal_level = node_level
#                 yield node
#             # left_child = self.left(node)
#             # right_child = self.right(node)
#             # if right_child is not None:
#             #     bfs_queue.append((right_child, node_level + 1))
#             # if left_child is not None:
#             #     bfs_queue.append((left_child, node_level + 1))
#
#     for node in _right_view(tree.root(), 0):
#         yield node
#


# Full-proof Solution
def right_view(tree: LinkedBinaryTree, traversal_choice=LinkedBinaryTree.BFS):
    if tree.is_empty():
        raise ValueError('Tree is Empty')
    level_last_node = OrderedDict()

    ##############
    # 1st Approach: BFS
    def _right_view_bfs(node: LinkedBinaryTree.BinaryTreeNode, node_level, horizontal_distance):
        bfs_queue = deque()
        bfs_queue.append((node, node_level, horizontal_distance))
        level_last_node[node_level] = node, horizontal_distance
        while bfs_queue:
            node, node_level, node_hd = bfs_queue.popleft()

            ###############
            # Last Node selection Logic
            last_node_in_level = level_last_node.get(node_level)

            if last_node_in_level:
                if last_node_in_level[1] < node_hd:
                    level_last_node[node_level] = node, node_hd
            else:
                level_last_node[node_level] = node, node_hd
            ###############
            # Queue Append Logic
            left_child = tree.left(node)
            right_child = tree.right(node)
            if right_child is not None:
                bfs_queue.append((right_child, node_level + 1, node_hd + 1))
            if left_child is not None:
                bfs_queue.append((left_child, node_level + 1, node_hd - 1))
            ###############

    #############
    # 2nd Approach: DFS
    def _right_view_dfs(node: LinkedBinaryTree.BinaryTreeNode, node_level, node_hd):
        if node is None:
            return

        last_node_in_level = level_last_node.get(node_level)
        if last_node_in_level:
            if last_node_in_level[1] < node_hd:
                level_last_node[node_level] = node, node_hd
        else:
            level_last_node[node_level] = node, node_hd
        _right_view_dfs(tree.right(node), node_level + 1, node_hd + 1)
        _right_view_dfs(tree.left(node), node_level + 1, node_hd - 1)

    #############
    implementation_func = _right_view_bfs if traversal_choice == LinkedBinaryTree.BFS else _right_view_dfs
    implementation_func(tree.root(), 0, 0)
    for node, node_hd in level_last_node.values():
        yield node


# driver code
def run():
    # tree = BuildLinkedBinaryTree(auto_populate=True).get_tree()
    tree = BuildLinkedBinaryTree().get_diamond_tree()

    print('Right-view: ')
    for node in right_view(tree):
        print(tree.element(node), end=' ')

    # print('\n\nBFS: ')
    # for node in tree.bfs():
    #     print(tree.element(node), end=' ')


if __name__ == '__main__':
    run()

