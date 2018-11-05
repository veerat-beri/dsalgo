# Problem Statement
# https://www.geeksforgeeks.org/print-left-view-binary-tree/

from collections import deque, OrderedDict

from trees.build_tree import BuildLinkedBinaryTree
from trees.tree import LinkedBinaryTree, BinaryTree


# Standard Solution
# def left_view(tree: LinkedBinaryTree):
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
#             # if left_child is not None:
#             #     bfs_queue.append((left_child, node_level + 1))
#             # if right_child is not None:
#             #     bfs_queue.append((right_child, node_level + 1))
#             ###############
#             # 2nd Approach
#             for child in tree.children(node):
#                 bfs_queue.append((child, node_level + 1))
#             ###############
#
#     for node in _left_view(tree.root(), 0):
#         yield node
#
#     ###############
#     # 2nd Approach: DFS

# Full-proof Solution
def left_view(tree: LinkedBinaryTree):
    if tree.is_empty():
        raise ValueError('Tree is Empty')
    level_first_node = OrderedDict()
    ###############
    # 1st Approach: BFS
    def _left_view(node: BinaryTree.BinaryTreeNode, traversal_level, horizontal_distance):
        bfs_queue = deque()
        bfs_queue.append((node, traversal_level, horizontal_distance))
        # yield node
        level_first_node[traversal_level] = node, horizontal_distance
        while bfs_queue:
            node, node_level, node_hd = bfs_queue.popleft()
            if node_level > traversal_level:
                traversal_level = node_level
                # yield node
                level_first_node[traversal_level] = node, node_hd

            first_node_in_level = level_first_node.get(node_level)
            if first_node_in_level:
                if first_node_in_level[1] > node_hd:
                    level_first_node[traversal_level] = node, node_hd

            ###############
            # 1st Approach
            left_child = tree.left(node)
            right_child = tree.right(node)
            if left_child is not None:
                bfs_queue.append((left_child, node_level + 1, node_hd - 1))
            if right_child is not None:
                bfs_queue.append((right_child, node_level + 1, node_hd + 1))
            ###############
            # 2nd Approach
            # for child in tree.children(node):
            #     bfs_queue.append((child, node_level + 1))
            ###############

    _left_view(tree.root(), 0, 0)
    for node, node_hd in level_first_node.values():
        yield node
    ###############
    # 2nd Approach: DFS


# driver code
def run():
    # tree = BuildLinkedBinaryTree(auto_populate=True).build()
    root = LinkedBinaryTree.BinaryTreeNode(1)
    root._left = LinkedBinaryTree.BinaryTreeNode(2)
    root._right = LinkedBinaryTree.BinaryTreeNode(3)
    root._left._right = LinkedBinaryTree.BinaryTreeNode(4)
    root._right._left = LinkedBinaryTree.BinaryTreeNode(5)
    root._left._right._right = LinkedBinaryTree.BinaryTreeNode(6)
    root._right._left._left = LinkedBinaryTree.BinaryTreeNode(7)

    tree = BuildLinkedBinaryTree(root=root).build()
    print('Left-view: ')
    for node in left_view(tree):
        print(tree.element(node), end=' ')

    print('BFS: ')
    for node in tree.bfs():
        print(tree.element(node), end=' ')


if __name__ == '__main__':
    run()

