# Problem Statement
# https://www.geeksforgeeks.org/zigzag-tree-traversal/

from collections import deque

from trees import BuildLinkedBinaryTree, LinkedBinaryTree


def zigzag_traversal(binary_tree: LinkedBinaryTree, append_right_first=False, use_stacks=False):
    ############################################################
    # Using 2 stacks
    def _zigzag_traversal(root_node: LinkedBinaryTree.BinaryTreeNode):
        print('Using Stacks..')

        current_level_nodes = []
        next_level_nodes = []

        current_level_nodes.append(root_node)
        flag = append_right_first

        while current_level_nodes:
            current_node = current_level_nodes.pop(-1)
            yield current_node, flag

            for child_node in binary_tree.children(current_node, reverse_iter=True if flag else False):
                next_level_nodes.append(child_node)

            if not current_level_nodes:
                flag = not flag
                current_level_nodes, next_level_nodes = next_level_nodes, current_level_nodes

    ############################################################
    # Using 1 Deque
    def _zig_zag_traversal(root_node: LinkedBinaryTree.BinaryTreeNode):
        print('Using Deque..')

        flag = append_right_first
        bfs_queue = deque([root_node, None] if not flag else [None, root_node])

        while len(bfs_queue) > 1:
            if flag:
                current_node = bfs_queue.pop()
                if current_node is None:
                    bfs_queue.append(None)
                    flag = not flag
                    continue

                for child_node in binary_tree.children(current_node, reverse_iter=True):
                    bfs_queue.appendleft(child_node)
            else:
                current_node = bfs_queue.popleft()
                if current_node is None:
                    bfs_queue.appendleft(None)
                    flag = not flag
                    continue

                for child_node in binary_tree.children(current_node):
                    bfs_queue.append(child_node)

            yield current_node, flag
    ############################################################

    executing_func = _zigzag_traversal if use_stacks else _zig_zag_traversal
    for node in executing_func(binary_tree.root()):
        yield node


# driver code
def run():
    from trees.utils import Traversal
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[60, 70, 80, 90, 100, ], auto_populate=True).get_tree()
    Traversal(binary_tree).print_level_order_traversal()

    print('ZigZag Traversal of above tree is: ')
    append_right_first = False
    for node, level_bool in zigzag_traversal(binary_tree=binary_tree, append_right_first=append_right_first):
        if level_bool != append_right_first:
            print('\n', '=' * 15, sep='')
            append_right_first = level_bool
        print(node.data, end=' ')


if __name__ == '__main__':
    run()
