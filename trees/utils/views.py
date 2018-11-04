


# Problem Statement
# https://www.geeksforgeeks.org/print-left-view-binary-tree/
from collections import deque

from trees.tree import LinkedBinaryTree, BinaryTree


def left_view(tree: LinkedBinaryTree):
    root_node = tree.root()
    ###############
    # 1st Approach: BFS

    def _left_view(node: BinaryTree.BinaryTreeNode, traversal_level):
        bfs_queue = deque()
        bfs_queue.append((node, 0))
        yield node

        while bfs_queue:
            node, node_level = bfs_queue.popleft()
            if node_level > traversal_level:
                traversal_level = node_level
                yield node
            ###############
            # 1st Approach
            # left_child = self.left(node)
            # right_child = self.right(node)
            # if left_child is not None:
            #     bfs_queue.append(left_child)
            # if right_child is not None:
            #     bfs_queue.append(right_child)
            ###############
            # 2nd Approach
            for child in tree.children(node):
                bfs_queue.append((child, node_level + 1))
            ###############
    for node in _left_view(root_node, 0):
        yield node


def run():
    print('Left-view: ')
