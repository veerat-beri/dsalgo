# Problem Statement
# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/

from collections import deque, namedtuple
from trees import BuildLinkedBinaryTree, LinkedBinaryTree


def bottom_view(tree: LinkedBinaryTree, traversal_choice=LinkedBinaryTree.BFS):
    if tree.is_empty():
        raise ValueError('Tree is Empty')

    horizontal_distance_last_node = dict()
    Node = namedtuple('Node', ['node', 'level'])

    def get_named_node_tuple(node, node_level=None):
        return Node(node, node_level)

    ##############
    # 1st Approach: BFS
    def _bottom_view_bfs(node: LinkedBinaryTree.BinaryTreeNode, traversal_level, horizontal_distance):
        bfs_queue = deque()
        bfs_queue.append((node, traversal_level, horizontal_distance))
        horizontal_distance_last_node[horizontal_distance] = get_named_node_tuple(node)
        while bfs_queue:
            node, node_level, node_hd = bfs_queue.popleft()

            # save last node of each HD
            horizontal_distance_last_node[node_hd] = get_named_node_tuple(node)

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
    def _bottom_view_dfs(node: LinkedBinaryTree.BinaryTreeNode, node_level, node_hd):
        if node is None:
            return

        first_node_in_hd = horizontal_distance_last_node.get(node_hd)
        if not first_node_in_hd or first_node_in_hd.level < node_level:
            horizontal_distance_last_node[node_hd] = get_named_node_tuple(node, node_level)

        _bottom_view_dfs(tree.right(node), node_level + 1, node_hd + 1)
        _bottom_view_dfs(tree.left(node), node_level + 1, node_hd - 1)

    #############
    implementation_func = _bottom_view_bfs if traversal_choice == LinkedBinaryTree.BFS else _bottom_view_dfs
    implementation_func(tree.root(), 0, 0)
    for node_hd, node in sorted(horizontal_distance_last_node.items(), key=lambda item: item[0]):
        yield node.node


# driver code
def run():
    # tree = BuildLinkedBinaryTree(auto_populate=True).get_tree()
    tree = BuildLinkedBinaryTree().get_diamond_tree()

    print('Bottom-view: ')
    for node in bottom_view(tree, LinkedBinaryTree.DFS):
        print(tree.element(node), end=' ')

    # print('\n\nBFS: ')
    # for node in tree.bfs():
    #     print(tree.element(node), end=' ')


if __name__ == '__main__':
    run()
