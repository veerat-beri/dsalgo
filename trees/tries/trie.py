# Problem Statement
# https://www.geeksforgeeks.org/trie-insert-and-search/


from strings.service import get_relative_ascii
from trees.tree import BinaryTree


class Trie:
    # either small or large Alphabet set
    DEFAULT_TRIE_NODE_CHILDREN_COUNT = 26

    class TrieNode(BinaryTree.BinaryTreeNode):
        def __init__(self, **kwargs):
            self.child_nodes = [None] * Trie.DEFAULT_TRIE_NODE_CHILDREN_COUNT
            self.is_end_node = False

    def __init__(self, node_children_count: int = None, **kwargs):
        self.TRIE_NODE_CHILDREN_COUNT = node_children_count or self.DEFAULT_TRIE_NODE_CHILDREN_COUNT
        self._root = self.TrieNode()

    def get_new_node(self):
        return self.TrieNode()

    def insert(self, word: str):
        # Recursive Approach
        def _insert(trie_node: Trie.TrieNode, alphabet: chr):
            if not trie_node.child_nodes[get_relative_ascii(alphabet)]:
                trie_node.child_nodes[get_relative_ascii(alphabet)] = self.get_new_node()
        ##############################
        # Iterative Approach

        ##############################
        _insert()

    def root(self):
        return self._root
    #
    # def insert_node(self, node_data, parent_node):
    #     self._get_new_node(node_data)
