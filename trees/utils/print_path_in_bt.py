# Problem Statement
# https://www.geeksforgeeks.org/print-path-root-given-node-binary-tree/
from trees import BuildLinkedBinaryTree
from trees.tree import BinaryTree
from trees.utils import print_bfs


def get_path(tree: BinaryTree, searched_node_data):
    ###############
    # 1st Approach
    nodes_in_path = []

    def _custom_pre_order(node):
        if node is None:
            return False

        nodes_in_path.append(node)

        if tree.element(node) == searched_node_data:
            return True

        if _custom_pre_order(tree.left(node)) or _custom_pre_order(tree.right(node)):
            return True

        nodes_in_path.remove(node)
        return False

    _custom_pre_order(tree.root())
    for node in nodes_in_path:
        yield node


def run():
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[60, 70, 80, 90, 100, ], auto_populate=True).get_tree()
    searched_node = 100
    print('Tree Level order traversal: ')
    print_bfs(binary_tree)
    print(f'Path to node ({searched_node}): ')

    for node in get_path(binary_tree, searched_node):
        print(binary_tree.element(node), end=' ')


if __name__ == '__main__':
    run()
