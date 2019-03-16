# Problem Statement
# https://www.geeksforgeeks.org/check-if-the-given-binary-tree-have-a-subtree-with-equal-no-of-1s-and-0s/

from trees import LinkedBinaryTree, BuildLinkedBinaryTree
from trees.utils import Traversal


def get_equal_0_1_subtrees(binary_tree: LinkedBinaryTree):
    equal_01_subtrees = set()

    def _post_order(current_node):
        if current_node is None:
            return 0, 0

        left_subtree_node_1_count, left_subtree_node_0_count = _post_order(binary_tree.left(current_node))
        right_subtree_node_1_count, right_subtree_node_0_count = _post_order(binary_tree.right(current_node))

        total_node_1_count = left_subtree_node_1_count + right_subtree_node_1_count
        total_node_0_count = left_subtree_node_0_count + right_subtree_node_0_count

        if current_node.data:
            total_node_1_count += 1
        else:
            total_node_0_count += 1

        if total_node_0_count == total_node_1_count:
            equal_01_subtrees.add(current_node)

        return total_node_1_count, total_node_0_count

    _post_order(binary_tree.root())
    return equal_01_subtrees


# driver code
def run():
    # Make Tree
    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[1, 0, 0, 1, 0]).get_tree()

    root_right = binary_tree.right(binary_tree.root())
    binary_tree.add_right_child(root_right, 1)
    binary_tree.add_right_child(binary_tree.right(root_right), 1)
    root_left = binary_tree.left(binary_tree.root())
    binary_tree.add_left_child(binary_tree.left(root_left), 1)
    root_left_right = binary_tree.right(root_left)
    binary_tree.add_right_child(root_left_right, 0)
    binary_tree.add_left_child(root_left_right, 1)
    binary_tree.add_left_child(binary_tree.left(root_left_right), 1)
    binary_tree.add_left_child(binary_tree.right(root_left_right), 0)
    binary_tree.add_left_child(binary_tree.left(binary_tree.right(root_left_right)), 1)

    # Traversal(binary_tree).print_level_order_traversal()
    #############################################

    equal_01_subtrees = get_equal_0_1_subtrees(binary_tree)
    if equal_01_subtrees:
        print(f'Yes, {len(equal_01_subtrees)} subtrees having equal 0s and 1s nodes are present')
        for subtree in equal_01_subtrees:
            Traversal(binary_tree).print_level_order_traversal(subtree)
    else:
        print('No subtree having equal 0s 1s is present')


if __name__ == '__main__':
    run()
