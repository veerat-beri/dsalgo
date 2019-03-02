# Problem Statement
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/


from trees import LinkedBinaryTree
from trees.utils.traversals import Traversal


class LinkedBinarySearchTree(LinkedBinaryTree):
    def insert_node(self, node_data):
        def _insert_node(current_node):
            if node_data > current_node.data:
                if self.right(current_node) is None:
                    self.add_right_child(current_node, node_data)
                    return
                _insert_node(self.right(current_node))
            else:
                if self.left(current_node) is None:
                    self.add_left_child(current_node, node_data)
                    return
                _insert_node(self.left(current_node))

        if self.is_empty():
            self.add_root(node_data)
            return

        _insert_node(self.root())


# driver code
def run():
    from trees.bst.build_bst import BuildLinkedBinarySearchTree
    bst = BuildLinkedBinarySearchTree(auto_populate=True).get_tree()

    Traversal(bst).print_level_order_traversal()
    Traversal(bst).print_inorder_traversal()


if __name__ == '__main__':
    run()
