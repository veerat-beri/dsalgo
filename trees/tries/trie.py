# Problem Statement
# https://www.geeksforgeeks.org/trie-insert-and-search/

from trees.tree import BinaryTree


class Trie(BinaryTree):
    # either small or large Alphabet set
    DEFAULT_TRIE_NODE_CHILDREN_COUNT = 26

    class TrieNode(BinaryTree.BinaryTreeNode):
        def __init__(self, node_data, **kwargs):
            self.child_nodes = [None] * Trie.DEFAULT_TRIE_NODE_CHILDREN_COUNT
            self.is_end_node = True
            self.data = node_data

    def __init__(self, node_children_count: int = None, **kwargs):
        self.TRIE_NODE_CHILDREN_COUNT = node_children_count or self.DEFAULT_TRIE_NODE_CHILDREN_COUNT
        self._root = self.TrieNode(None)

    def _get_new_node(self, node_data):
        return self.TrieNode(node_data)

    # def root(self):
    #     return self._root
    #
    # def insert_node(self, node_data, parent_node):
    #     self._get_new_node(node_data)
