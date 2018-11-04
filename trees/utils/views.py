from collections import deque

from trees.build_tree import BuildLinkedBinaryTree
from trees.tree import LinkedBinaryTree, BinaryTree


# Problem Statement
# https://www.geeksforgeeks.org/print-left-view-binary-tree/
def left_view(tree: LinkedBinaryTree):
    if tree.is_empty():
        raise ValueError('Tree is Empty')

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
            #     bfs_queue.append((left_child, node_level + 1))
            # if right_child is not None:
            #     bfs_queue.append((right_child, node_level + 1))
            ###############
            # 2nd Approach
            for child in tree.children(node):
                bfs_queue.append((child, node_level + 1))
            ###############

    for node in _left_view(tree.root(), 0):
        yield node

    ###############
    # 2nd Approach: DFS


def right_view(tree: LinkedBinaryTree):
    pass


# driver code
def run():
    tree = BuildLinkedBinaryTree(auto_populate=True).build()
    # tree = BuildLinkedBinaryTree(root=root).build()
    print('Left-view: ')
    for node in left_view(tree):
        print(tree.element(node), end=' ')

    # print('Right-view: ')
    # for node in right_view(tree):
    #     print(tree.element(node), end=' ')


if __name__ == '__main__':
    run()

