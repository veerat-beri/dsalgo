# Problem Statement
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/


from trees import LinkedBinaryTree


class BinarySearchTree(LinkedBinaryTree):
    def insert_node(self, node_data):
        def _insert_node(node_data):

                current_node = self.root()
                next_node = None
                while next_node:
                    current_node = next_node
                    if node_data > current_node.data:
                        next_node = self.right(current_node)

        if self.is_empty():
            inserted_node = self.add_root(node_data)

        return inserted_node

