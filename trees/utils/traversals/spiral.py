from collections import deque
from trees import LinkedBinaryTree, BuildLinkedBinaryTree


class SpiralTraversalMixin:
    ############################################################
    # Using 2 stacks
    def _using_stacks(self, root_node: LinkedBinaryTree.BinaryTreeNode):
        print('Using Stacks..')

        current_level_nodes = []
        next_level_nodes = []

        current_level_nodes.append(root_node)
        flag = self.append_right_first

        while current_level_nodes:
            current_node = current_level_nodes.pop(-1)
            yield current_node, flag

            for child_node in self.binary_tree.children(current_node, reverse_iter=True if flag else False):
                next_level_nodes.append(child_node)

            if not current_level_nodes:
                flag = not flag
                current_level_nodes, next_level_nodes = next_level_nodes, current_level_nodes

    ############################################################
    # Using 1 Deque
    def _using_deque(self, root_node: LinkedBinaryTree.BinaryTreeNode):
        print('Using Deque..')

        flag = self.append_right_first
        bfs_queue = deque([root_node, None] if not flag else [None, root_node])

        while len(bfs_queue) > 1:
            if flag:
                current_node = bfs_queue.pop()
                if current_node is None:
                    bfs_queue.append(None)
                    flag = not flag
                    continue

                for child_node in self.binary_tree.children(current_node, reverse_iter=True):
                    bfs_queue.appendleft(child_node)
            else:
                current_node = bfs_queue.popleft()
                if current_node is None:
                    bfs_queue.appendleft(None)
                    flag = not flag
                    continue

                for child_node in self.binary_tree.children(current_node):
                    bfs_queue.append(child_node)

            yield current_node, flag
    ############################################################


# Problem Statement
# https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/
# https://www.geeksforgeeks.org/zigzag-tree-traversal/
class SpiralTraversal(SpiralTraversalMixin):
    def __init__(self, binary_tree: LinkedBinaryTree, append_right_first=False, use_stacks=False):
        self.binary_tree = binary_tree
        self.append_right_first = append_right_first
        self.use_stacks = use_stacks

    def traverse_nodes(self):
        executing_func = self._using_stacks if self.use_stacks else self._using_deque
        for node in executing_func(self.binary_tree.root()):
            yield node


# driver code
def run():
    from trees.utils import Traversal
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[60, 70, 80, 90, 100, ], auto_populate=True).get_tree()
    Traversal(binary_tree).print_level_order_traversal()

    print('ZigZag Traversal of above tree is: ')
    append_right_first = False
    for node, level_bool in SpiralTraversal(binary_tree=binary_tree, append_right_first=append_right_first).traverse_nodes():
        if level_bool != append_right_first:
            print('\n', '=' * 15, sep='')
            append_right_first = level_bool
        print(node.data, end=' ')

    print('\n\nSpiral Traversal of above tree is: ')
    append_right_first = True
    for node, level_bool in SpiralTraversal(binary_tree=binary_tree,
                                            append_right_first=append_right_first).traverse_nodes():
        if level_bool != append_right_first:
            print('\n', '=' * 15, sep='')
            append_right_first = level_bool
        print(node.data, end=' ')


if __name__ == '__main__':
    run()
