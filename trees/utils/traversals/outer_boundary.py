# Problem Statement
# https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/

from trees import LinkedBinaryTree, BuildLinkedBinaryTree
from trees.utils import Traversal
from trees.utils.views import left_view, right_view
from trees.utils.views.bottom_view import bottom_view


class BoundaryTraversal:
    def __init__(self, binary_tree: LinkedBinaryTree = None, bt_node: LinkedBinaryTree.BinaryTreeNode = None):
        assert binary_tree or bt_node, 'Neither of node or binary-tree is provided'
        self.binary_tree = binary_tree or LinkedBinaryTree(root=bt_node)

    ############################################################
    # Method 1
    # 1. Print left-view of the tree
    # 2. Print all leaf nodes, except the first one from left. (Bottom-view will not work)
    # 3. Print right-view in reverse order and skip first node in order.

    # Time-Complexity: O (N + N + N) and code complexity is also high, as both left-view and right-view traversal codes
    # need to be implemented first.
    ############################################################
    # Method 2
    ############################################################
    def left_boundary_traversal(self, node: LinkedBinaryTree.BinaryTreeNode):
        if node is None or self.binary_tree.is_leaf(node):
            return
        yield node
        for node in self.left_boundary_traversal(self.binary_tree.left(node) or self.binary_tree.left(node)):
            yield node

    def right_boundary_reverse_traversal(self, node: LinkedBinaryTree.BinaryTreeNode):
        if node is None or self.binary_tree.is_leaf(node):
            return
        for boundary_node in self.right_boundary_reverse_traversal(self.binary_tree.right(node) or self.binary_tree.left(node)):
            yield boundary_node
        yield node

    def leaf_nodes_traversal(self, node: LinkedBinaryTree.BinaryTreeNode):
        if node is None:
            return

        for boundary_node in self.leaf_nodes_traversal(self.binary_tree.left(node)):
            yield boundary_node

        if self.binary_tree.is_leaf(node):
            yield node

        for boundary_node in self.leaf_nodes_traversal(self.binary_tree.right(node)):
            yield boundary_node

    def boundary_traversal(self):
        root_node = self.binary_tree.root()
        for node in self.left_boundary_traversal(root_node):
            yield node
        for node in self.leaf_nodes_traversal(root_node):
            yield node
        for node in self.right_boundary_reverse_traversal(self.binary_tree.right(root_node)):
            yield node


# driver code
def run():
    # -------------------- Create Tree -------------------- #
    # binary_tree = BuildLinkedBinaryTree(auto_populate=True).get_tree()

    binary_tree = BuildLinkedBinaryTree(list_of_nodes=[20, 8, 22, 4, 12, ]).get_tree()
    binary_tree._root._right._right = binary_tree.get_new_node(25)
    binary_tree._root._left._right._right = binary_tree.get_new_node(14)
    binary_tree._root._left._right._left = binary_tree.get_new_node(10)

    # -------------------- -------------------- #
    Traversal(binary_tree).print_preorder_traversal()
    print('Boundary Nodes traversal: ')
    for boundary_node in BoundaryTraversal(binary_tree).boundary_traversal():
        print(boundary_node.data, end=' ')


if __name__ == '__main__':
    run()
